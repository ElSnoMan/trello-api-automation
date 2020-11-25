import os
import requests

BASE_URL = 'https://api.trello.com/1'
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')

def test_get_me():
    url = f'{BASE_URL}/members/me/boards?key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'
    response = requests.get(url)
    assert response.ok


def test_get_automation_board():
    board_id = '5f74c7fd2c07b40aa7722682'
    url = f'{BASE_URL}/boards/{board_id}?key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'
    response = requests.get(url)
    assert response.ok
    body = response.json()
    assert body['name'] == 'Automation'
