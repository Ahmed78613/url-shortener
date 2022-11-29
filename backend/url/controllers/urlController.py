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
    print(usable_outputs)
    return usable_outputs, 200

def create(request):
    data = request.json
    # Create short url
    generated_url = short_url_Generator()
    print(generated_url)
    new_url = Url(original_url=data["original_url"], short_url=generated_url)
    try:
        db.session.add(new_url)
        db.session.commit()
    except:
        return "Already Exists", 404
    # Check if original_url exists
    return "URL Added", 201

def short_url_Generator():
    base = 'http://127.0.0.1:5000/'
    # Generate random id
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(5))
    return base + id
