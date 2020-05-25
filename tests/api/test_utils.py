from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from flaskr.api.utils import timed_cache


@patch('flaskr.api.utils.datetime')
def test_timed_cache(patched_datetime):
    myfunc = Mock(side_effect=[1, 2])

    utcnow = datetime.utcnow()
    patched_datetime.utcnow.return_value = utcnow
    timed_cache_myfunc = timed_cache(seconds=1)(myfunc)

    result = timed_cache_myfunc()
    assert result == 1

    # Medio segundo después, la caché todavía no se limpia,
    # por lo que el resultado de la función debería ser exactamente
    # el mismo que la primera vez.
    half_a_second_later = utcnow + timedelta(seconds=0.5)
    patched_datetime.utcnow.return_value = half_a_second_later

    result_half_a_second_later = timed_cache_myfunc()
    assert result_half_a_second_later == 1

    # Un segundo después es el límite que hemos seteado para
    # guardar los resultados anteriores, por lo tanto deberíamos
    # obtener un nuevo resultado ahora.
    a_whole_second_later = utcnow + timedelta(seconds=1)
    patched_datetime.utcnow.return_value = a_whole_second_later

    result_a_second_later = timed_cache_myfunc()
    assert result_a_second_later == 2
