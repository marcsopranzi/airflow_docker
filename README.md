# Airflow ETL: Airflow and Postgres with docker images.

This is an ETL running mostly out of the box with docker files. This ETL will load data from [NYC open data](https://opendata.cityofnewyork.us/data/#datasetscategory) and insert into a Postgres DB. To run it you need an .env file with the configuration for db name, login details and the folders dags, logs and plugins.

## Setup
1. Crete an .env file with your own details:
`echo -e "AIRFLOW_UI=$(id -u)
AIRFLOW_GID=0
POSTGRES_DB=ecology
POSTGRES_USER=<>
POSTGRES_PASSWORD=<>
POSTGRES_HOST=database
POSTGRES_PORT=5432" > .env
`

    If you change the details of the `.env` file, keep in mind you should check this file: `airflow_docker/docker/db_backend/init-db.sh`. You can change the file name too but you will have to update your docker-compose file plus the initiation.

2. Create folders:
- dags
- logs
- plugins

    To grant Airflow permission to write in the logs folder if you use debian you can run `sudo chmod u=rwx,g=rwx,o=rwx logs`
## Initialize Airflow and DB.
- `docker-compose up airflow-init`
- `docker-compose --env-file .env up`

    You can log in to the docker postgres image to check the result with `docker exec -it <image id> /bin/bash`
    and inside the image you can login to postgres with: `psql -U postgres -h localhost`

    If you decide to use this as the starting point for your own work don't forget to test your task and run them before the developemnt gets too complicated: `airflow tasks test <DAG name> <task id> <YYYY-MM-DD>`
