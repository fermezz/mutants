from datetime import datetime, timedelta
from functools import lru_cache, wraps


# Un decorador que usa el ya decorador `lru_cache` y le agrega funcionalidad
# para poder limpiar la cache en un tiempo especificado.
# Implementación robada y adaptada de https://gist.github.com/Morreski/c1d08a3afa4040815eafd3891e16b945
def timed_cache(**timedelta_kwargs):
    """Wraps functools.lru_cache to have extra time-based functionality."""

    def _wrapper(f):
        update_delta = timedelta(**timedelta_kwargs)
        next_update = datetime.utcnow() + update_delta
        f = lru_cache(maxsize=1)(f)

        @wraps(f)
        def _wrapped(*args, **kwargs):
            nonlocal next_update
            now = datetime.utcnow()
            if now >= next_update:
                f.cache_clear()
                next_update = now + update_delta
            return f(*args, **kwargs)
        return _wrapped
    return _wrapper
