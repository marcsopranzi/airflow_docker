sudo docker build -t build_linux_airflow .

sudo docker run -it -p 8080:8080 build_linux_airflow /bin/bash

sudo docker run -it --rm -d -p 8080:8080 build_linux_airflow

sudo docker ps
sudo docker kill bd45e9bdd437

sudo docker images
sudo docker rmi -f c5ac86982355

sudo docker exec -it 9c3e356fbbae /bin/bash