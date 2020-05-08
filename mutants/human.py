from dataclasses import dataclass
from itertools import chain
from typing import Generator, List


ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'
DNA_NUCLEOBASES = frozenset([ADENINE, CYTOSINE, GUANINE, THYMINE])


@dataclass
class Human:
    dna: List[str]

    def is_mutant(self) -> bool:
        four_equal_nucleobases_sequences: int = 0

        result = False
        for sequence in chain(rows(self.dna), columns(self.dna)):
            for base in DNA_NUCLEOBASES:
                if base * 4 in sequence:
                    four_equal_nucleobases_sequences += 1
                    if four_equal_nucleobases_sequences == 2:
                        return True
        return False


def rows(matrix: List[str]) -> Generator[str, None, None]:
    yield from matrix


def columns(matrix: List[str]) -> Generator[str, None, None]:
    yield from rows(transpose(matrix))


def transpose(matrix: List[str]) -> List[str]:
    return [''.join(row) for row in zip(*matrix)]
