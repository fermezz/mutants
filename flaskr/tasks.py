from flaskr.celery import celery
from flaskr.mutants.models.human import Mutant, NonMutant


@celery.task()
def save_human(dna, is_mutant):
    if is_mutant:
        Mutant(dna=dna).save()
    else:
        NonMutant(dna=dna).save()
