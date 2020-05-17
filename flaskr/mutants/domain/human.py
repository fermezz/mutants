from dataclasses import dataclass
from itertools import chain
from typing import List

from flaskr.mutants.domain.utils import Matrix


ADENINE = "A"
CYTOSINE = "C"
GUANINE = "G"
THYMINE = "T"
DNA_NUCLEOBASES = frozenset([ADENINE, CYTOSINE, GUANINE, THYMINE])


@dataclass
class Human:
    dna: List[str]

    def is_mutant(self) -> bool:
        """Returns a boolean telling whether the current human is a mutant or not,
        based on the quantity of sequences with four equal nucleobases.

        If the human has more than one sequence with four equal nucleobases, we say it's a mutant.
        """
        four_equal_nucleobases_sequences: int = 0
        dna_matrix = Matrix(self.dna)

        for sequence in chain(
            dna_matrix.get_rows(),
            dna_matrix.get_columns(),
            dna_matrix.get_all_diagonals(),
        ):
            # Dado que las secuencias de ADN no tienen ningún tipo de orden
            # y no tiene sentido darle un orden, podemos hacer una búsqueda linear
            # de secuencias con cuatro nucleobases iguales sin sospechar, por ahora,
            # de que ese tipo de búsqueda va a ser mala en cuanto a la performance
            # a comparación de alguna otra técnica de búsqueda.

            # La línea `any(nucleobase * 4 in sequence for nucleobase in DNA_NUCLEOBASES)`
            # nos va a devolver `True` si existe en la secuencia alguna de las cuatro
            # nucleobases de manera consecutiva. Si no, `False`.
            # Tomando eso como referencia, simplemente podemos castear `True` o `False`
            # a entero, para que nos devuelva `1` o `0` respectivamente y nos hace más fácil
            # el conteo de cantidad de secuencias que tienen cuatro nucleobases consecutivas.
            # De otra manera, podríamos terminar con una serie de bloques if/for que es bastante
            # difícil de leer en mi opinión. Por ejemplo, lo siguiente funcionaría de la misma manera
            #
            # ```
            # for base in DNA_NUCLEOBASES:
            #    if base * 4 in sequence:
            #        four_equal_nucleobases_sequences += 1
            #        if four_equal_nucleobases_sequences == 2:
            #            return True
            # ```
            # pero es un poco más verborrágico.

            four_equal_nucleobases_sequences += int(any(nucleobase * 4 in sequence for nucleobase in DNA_NUCLEOBASES))
            if four_equal_nucleobases_sequences == 2:
                return True

        return False
