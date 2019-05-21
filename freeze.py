from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

@freezer.register_generator
def projects():
    yield {'page_name': 'j1'}
    yield {'page_name': 'j2'}
    yield {'page_name': 'w1'}
    yield {'page_name': 'w2'}
    yield {'page_name': 'w3'}

if __name__ == '__main__':
    freezer.freeze()