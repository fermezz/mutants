FROM mongo:4.2.6

RUN chown -R mongodb:mongodb /var/log /data/
USER mongodb

COPY scripts/create-mutants-user.sh /docker-entrypoint-initdb.d/
