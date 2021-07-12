import os
from datetime import datetime

from binance import ThreadedWebsocketManager
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import Set


def main():
    mongo = MongoClient(os.getenv('MONGO_URL'))
    db = mongo.binance
    collection = db.ticker

    ensure_table_indexes(collection)

    def handle(msg) -> None:
        """
        Handle ticker message

        :param msg: A dictionary received from binance ticker stream
        :return: None
        """
        # The bookTicker stream does not seem to include any timestamp; We have to inject one manually...
        # Not sure how this will affect training models. the other option is to use the '@ticker' stream, which only gives updates every 1 second.
        # Payload fields can be found: https://binance-docs.github.io/apidocs/spot/en/#individual-symbol-book-ticker-streams
        msg['time'] = datetime.utcnow()
        print(f'msg:{msg}')
        collection.insert_one(msg)

    socket = ThreadedWebsocketManager()
    socket.start()
    symbols = parse_symbols(os.getenv('BINANCE_CRYPTO_PAIRS'))
    streams = get_streams_from_symbols(symbols)
    socket.start_multiplex_socket(callback=handle, streams=list(streams))
    socket.join()


def get_streams_from_symbols(symbols: Set[str]) -> Set[str]:
    """
    Parse ticker symbols into a set of Binance websocket streams

    :param symbols: Raw set of symbol strings
    :return: A set of Binance websocket formatted ticker stream identifiers
    """
    return set(map(lambda x: x + '@bookTicker', symbols))


def parse_symbols(symbols: str) -> Set[str]:
    """
    Return parsed, and formatted ticker symbol names from a string

    :param symbols: As string of symbols
    :return: Set of formatted ticker symbols
    """
    return set(map(lambda x: x.lower().strip(), symbols.split(',')))


def ensure_table_indexes(collection) -> None:
    """
    Ensure that MongoDB indexes are set on some key document fields

    :param collection:
    :return:
    """
    # Unique ticker event ID
    collection.create_index('data.u', unique=True)
    # The symbol, e.g. BTCUSDT
    collection.create_index('data.s')
    # The time for sorting.
    collection.create_index('time')


if __name__ == '__main__':
    load_dotenv()
    main()
