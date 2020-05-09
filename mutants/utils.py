from dataclasses import dataclass
from typing import Generator, List, Tuple


@dataclass
class Matrix:
    # Podemos limitar la matriz a trabajar con List[str], siempre
    # asumiendo que es una verdadera matriz porque `str` es una
    # lista de caracteres, cosa que es técnicamente falsa en Python
    # pero, dado nuestro input, es una asumpción suficientemente buena.
    # Podemos generalizarlo en el futuro si necesitácemos.
    data: List[str]

    def __post_init__(self) -> None:
        self.matrix_size = len(self.data)

    def get_rows(self) -> Generator[str, None, None]:
        """Returns a generator with the rows of the matrix."""
        yield from self.data

    def get_columns(self) -> Generator[str, None, None]:
        """Returns a generator with the columns of the matrix.

        It does so in a way that the columns are reversed, because
        it is convenient for us to reuse this function when we calculate
        counter-clockwise diagonals.

        So, given the following matrix

        | 'a', 'b', 'c' |
        |               |
        | 'd', 'e', 'f' |
        |               |
        | 'g', 'h', 'i' |

        Instead of returning

        > Generator['adg', 'beh', 'cfi']

        it returns

        > Generator['cfi', 'beh', 'adg']

        """
        yield from self._transpose()

    def get_all_diagonals(self) -> Generator[str, None, None]:
        """Returns a generator with the diagonals –clockwise and counter-clockwise– of the matrix.

        Note that this is not just the main diagonal for the matrix, which is
        the first thought that might pop into your head whilst talking about
        matrices and diagonals, but _every_ diagonal for the matrix.

        So, in case you have a matrix like this one

        | 'a', 'b', 'c' |
        |               |
        | 'd', 'e', 'f' |
        |               |
        | 'g', 'h', 'i' |

        we end up with this function generating both

         clockwise diagonals        and   counter-clockwise diagonals

        |    ,    , 'a',    ,     |      |    ,    , 'c',    ,     |
        |    , 'd',    , 'b',     |      |    , 'b',    , 'f',     |
        | 'g',    , 'e',    , 'c' |      | 'a',    , 'e',    , 'i' |
        |    , 'h',    , 'f',     |      |    , 'd',    , 'h',     |
        |    ,    , 'i',    ,     |      |    ,    , 'g',    ,     |

        """
        for idx in range((self.matrix_size - 1) * 2 + 1):
            yield from self._get_diagonals(idx, self.get_rows())
            yield from self._get_diagonals(idx, self.get_columns())

    def _get_diagonals(self, idx: int, matrix: Generator[str, None, None]) -> Generator[str, None, None]:
        yield ''.join([x[2] for x in self._rotate_45_degrees(matrix) if x[0] == idx])

    def _transpose(self) -> Generator[str, None, None]:
        for row in reversed(list(zip(*self.data))):
            yield ''.join(row)

    def _get_indexes_with_values(
        self,
        matrix: Generator[str, None, None],
    ) -> Generator[Tuple[int, int, str], None, None]:
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                yield (row_idx, col_idx, val)

    def _rotate_45_degrees(self, matrix: Generator[str, None, None]) -> Generator[Tuple[int, int, str], None, None]:
        for i, j, v in self._get_indexes_with_values(matrix):
            yield (i + j, self.matrix_size - 1 - i + j, v)
