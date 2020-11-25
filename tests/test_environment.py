import os


def test_env_vars():
    assert os.getenv('TRELLO_API_KEY')
    assert os.getenv('TRELLO_API_TOKEN')
