### Local testing

Tested using Python 3.8

1. If you don't already have a MongoDB instance running, you can start the provided Docker service with `docker-compose up -d mongodb`
1. Copy `example.env` to `.env` and fill out your own crypto pairs / MongoDB host url. 
1. From the root directory `pipenv install` in order to install dependencies.
1. You should now be able to run the main function in `main.py` in VS Code / IntelliJ

### Testing locally using Docker Compose

1. Copy `example.env` to `.env` and fill out your own credentials / crypto pairs / MongoDB host url.
1. From the root directory run `docker-compose up -d --build`

Both the Python script, and MongoDB should be running. You can make sure it's working by checking `docker ps` / `docker logs`, etc.

You should be able to use MongoDB Compass (or your favourite MongoDB viewer) to look at the `binance.ticker` table.

### Pushing to remote registry

1. `docker build -t binance-ticker .`
1. `docker push binance-ticker <your remote registry address>`
