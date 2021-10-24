docker build -t airflow-basic .
docker run --rm -d -p 8080:8080 airflow-basic
sudo docker exec -ti c1693f77a0db /bin/bash
sudo docker exec c1693f77a0db /bin/bash

airflow tasks test spark_submit_airflow data_to_s3 202-10-01