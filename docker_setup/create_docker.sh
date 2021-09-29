sudo docker build -t build_linux_airflow .

sudo docker run -it -p 8080:8080 build_linux_airflow /bin/bash

sudo docker run -it --rm -d -p 8080:8080 build_linux_airflow

sudo docker ps