from celery import Celery

from flaskr import create_app


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config.get("CELERY_RESULT_BACKEND"),
        broker=app.config.get("CELERY_BROKER_URL"),
        include=["flaskr.tasks"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(create_app())
if celery.conf['result_backend'] is not None:
    celery.control.rate_limit("flaskr.tasks.save_human", "6000/m")
