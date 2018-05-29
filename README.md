# Minimal Docker Compose Example

Basic working example that links a flask webserver to a mongo database instance.

To get this running, install Docker on your machine, and then run:

```unix
docker-compose build
```

To run the docker image, simply run:

```unix
docker-compose up
```

You should be able to browse over to `127.0.0.1:3000` to see the output of the
webserver. Note that beyond linking to the mongo container and opening a connection, we 
don't do anything with the mongo database.
