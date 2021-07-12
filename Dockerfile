FROM python:3.8

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system

# Set some default env variables for things like ECS
ENV BINANCE_CRYPTO_PAIRS="BTCUSDT"
ENV MONGO_URL="mongodb://<your host>"

COPY src ./src

CMD ["python", "./src/main.py"]


