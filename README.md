# Minimal Docker Compose Example

Basic working example that links a flask webserver to a mongo database instance.

## First, Get Docker

If you don't already have it, download [Docker](https://www.docker.com/get-docker).

## Build the Docker image

Once that's installed and running, navigate to this directory and run the following:

```unix
docker-compose build
```

## Run the Docker image

The following command will boot up the Docker image. 

```unix
docker-compose up
```

You should be able to browse over to `127.0.0.1:3000` to see the output of the
webserver. Note that beyond linking to the mongo container and opening a
connection, we do nothing with the Mongo database. 

The MongoDB is stored on your local machine in the `data/db` directory. This location is
specified in the `docker-compose.yml` file. Note the MongoDB is running on its default 
address. If you have another Mongo instance running on your machine, there will be a 
conflict and things will go badly.
