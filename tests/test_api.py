# -*- coding: utf-8 -*-
import os

import requests
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = f"http://localhost:{os.environ.get('PORT', 8080)}"


def test_can_call_api():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
