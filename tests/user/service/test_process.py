from faker import Faker
from faker.providers import profile
from faker.providers import color
import requests
import json
from tests.commons.logger import get_logger

logger = get_logger('test_api.py')
fake = Faker()
fake.add_provider(profile)
fake.add_provider(color)

def test_signup():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
        "name" : simple['name'],
        "username" : simple['username'],
        "password" : fake.color_name(),
        "enabled": True
    }
    logger.info(user)
    response = requests.post("http://127.0.0.1:8002/signup", data=json.dumps(user))
    logger.info(response.json())
    assert response.status_code == 200