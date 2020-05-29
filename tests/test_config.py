import os
from unittest.mock import Mock, patch

from flaskr import create_app


@patch("flaskr.MongoEngine")
@patch("flaskr.Flask")
def test_app_is_configured_correctly_for_non_test_environments(patched_app, patched_mongo_engine):
    os.environ["FLASK_ENV"] = "production"
    mocked_db = Mock(name="db")
    mocked_config = Mock(name="config")
    mocked_app = Mock(name="app")
    patched_app.return_value = mocked_app
    mocked_app.config = mocked_config
    mocked_app.instance_path = "/fake/path"
    patched_mongo_engine.return_value = mocked_db

    create_app()

    mocked_db.init_app.assert_called_once_with(mocked_app)
    mocked_config.from_pyfile.assert_called_once_with("config.py", silent=True)
