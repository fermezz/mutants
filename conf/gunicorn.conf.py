import logging
import multiprocessing
import os

import beeline


bind = "0.0.0.0:5000"

# Vamos a usar la cantidad de workers recomendada por Gunicorn.
# Podremos optimizarlo luego si es necesario.
# https://docs.gunicorn.org/en/stable/design.html#how-many-workers
workers = multiprocessing.cpu_count() * 2 + 1


def post_worker_init(worker):
    logging.info(f"beeline initialization in process pid {os.getpid()}")
    beeline.init(writekey=os.environ["HONEYCOMB_API_KEY"], dataset="mutants-api", debug=True)
