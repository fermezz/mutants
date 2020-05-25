import os
from typing import Any, Dict, Optional

from beeline.middleware.flask import HoneyMiddleware
from flask import Flask
from flask_mongoengine import MongoEngine


def create_db() -> MongoEngine:
    return MongoEngine()


def create_app(test_config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__, instance_path="/app/flaskr", instance_relative_config=True)
    HoneyMiddleware(app, db_events=False)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    db = create_db()
    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.api import views
    app.register_blueprint(views.bp)

    return app
