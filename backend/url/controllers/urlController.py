from flask import jsonify
from ..model.url import Url
from ..database.db import db 
import random
import string

def url(request):
    allUrls = Url.query.all()
    outputs = map(lambda p: {
        'id': p.id, 
        'original_url': p.original_url, 
        'short_url': p.short_url, 
        'clicks': p.clicks}, allUrls)
    usable_outputs = list(outputs)
    return usable_outputs, 200

def get_url_by_long_url(url):
    print("************** ", url, " **************")
    long_url = Url.query.filter_by(original_url=url).first()
    print("**************",  long_url, " **************")
    output = {
        "original_url": long_url.original_url, 
        "short_url": long_url.short_url, 
        "click": long_url.clicks
        }
    return output, 200

def create(request):
    data = request.json
    # Create short url
    generated_url = short_url_Generator()
    new_url = Url(original_url=data["original_url"], short_url=generated_url)
    try:
        db.session.add(new_url)
        db.session.commit()
    except:
        # Fetch existing url
        exists = get_url_by_long_url(data["original_url"])
        print(exists)

        return "Already Exists", 404
    # Check if original_url exists
    return "URL Added", 201

def short_url_Generator():
    base = 'http://127.0.0.1:5000/'
    # Generate random id
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(5))
    return base + id
