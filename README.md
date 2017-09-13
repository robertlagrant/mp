Running the code 
================
*(tested on a recent Ubuntu with Docker 17.06.0-ce, Docker-Compose 1.16.1)*

    cd <checkout_directory>
    docker-compose up

Repo contents
=============
- **mp-app/** - folder containing app definition
  - **Dockerfile** - definition of robertlagrant/mp-app Docker image
  - **app.py** - the Python code
  - **requirements.txt** - the input to pip to install the relevant packages
- **mp-db/** - folder containing database definition
  - **Dockerfile** - definition of robertlagrant/mp-db Docker image
  - **10_create_product_table.sql** - SQL to create Product table - runs on container creation
  - **20_insert_seed_data.sql** - SQL to seed Product table - runs on container creation
- **README.md** - this file
- **api.swagger** - Swagger file describing the marketplace API
- **docker-compose.yml** - docker-compose file to pull and run the API and its database
- **tests.postman** - Postman tests

Docker repo URL
===============
https://hub.docker.com/r/robertlagrant/

Notes
=====
The Flask application has a `depends_on` parameter so it starts after the database starts, but it will probably be ready first. In real life a wait script or similar is necessary.

The Flask application is all in one file, because it's under 100 lines! This isn't okay as an app grows, but it seemed silly to add a lot of structure to such a small amount of source code. Hopefully everything's very clear.

The database image doesn't map to an external volume, which would be necessary if a Docker-based database were considered worth doing in production.
