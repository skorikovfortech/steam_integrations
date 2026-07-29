from pytest import fixture

@fixture
def create_user_data():
    return {
    "email": "test1@email.com",
    "username": "max1uraye",
    "password": "qweQ1qwe",
    }
