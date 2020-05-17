from mongoengine import Document, ListField


class Mutant(Document):
    dna = ListField()


class NonMutant(Document):
    dna = ListField()
