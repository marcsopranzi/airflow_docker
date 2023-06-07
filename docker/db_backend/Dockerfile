FROM postgres:11.4-alpine
RUN echo 'Image loaded'


COPY init-db.sh /docker-entrypoint-initdb.d/init-db.sh
RUN echo 'init copied'

RUN chmod +x /docker-entrypoint-initdb.d/init-db.sh
RUN echo 'init executed'

EXPOSE 5440