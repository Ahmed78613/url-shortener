from url import db
from url import app
from url.model.url import Url

data = [
    {'id': 1, 'original_url': "test1", 'short_url': "shorter1", 'clicks': 0},
    {'id': 2, 'original_url': "test2", 'short_url': "shorter2", 'clicks': 100},
    {'id': 3, 'original_url': "test3", 'short_url': "shorter3", 'clicks': 54}
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for url in data:
        db.session.add(Url(original_url=url['original_url'], short_url=url['short_url'], clicks=url['clicks']))
        db.session.commit()


