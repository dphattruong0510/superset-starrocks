FROM apache/superset:4.1.3

WORKDIR /app

USER root

RUN apt-get update && apt-get install -y \ 
    procps \
    nano \ 
    gcc \
    pkg-config \
    && apt-get clean

RUN pip install psycopg2-binary Pillow mysqlclient redis


COPY superset/superset-init.sh /superset-init.sh

# Change permissions to make superset-init.sh executable
RUN chmod +x /superset-init.sh

# Make superset user an owner of the superset_config.py
COPY --chown=superset superset/superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py

# Create a folder for custom logos
RUN mkdir -p /app/superset/static/assets/images/custom_logos/
# Copy custom images
COPY superset/src/img/ /app/superset/static/assets/images/custom_logos/

USER superset
ENTRYPOINT [ "/superset-init.sh" ]