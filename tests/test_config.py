from flaskr import create_app

from unittest.mock import Mock, patch


@patch("flaskr.Flask")
def test_app_is_configured_correctly_for_non_test_environments(patched_app):
    mocked_config = Mock()
    patched_app().config = mocked_config

    create_app()

    mocked_config.from_pyfile.assert_called_once_with("config.py", silent=True)
