import logging
import multiprocessing
import os

import beeline


bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1


def post_worker_init(worker):
    logging.info(f"beeline initialization in process pid {os.getpid()}")
    beeline.init(writekey=os.environ["HONEYCOMB_API_KEY"], dataset="mutants-api", debug=True)
