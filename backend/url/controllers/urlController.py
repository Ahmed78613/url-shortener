from flask import redirect, url_for
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
    try:
        long_url = Url.query.filter_by(original_url=str(url)).first()
        output = {
            "original_url": long_url.original_url, 
            "short_url": long_url.short_url, 
            "clicks": long_url.clicks
            }
        return output, 200
    except:
        return "doesn't Exist", 404

def get_long_url_by__short_url(url):
    print("start*********************")
    try:
        long_url = Url.query.filter_by(short_url=str(url)).first()
        output = {
            "original_url": long_url.original_url, 
            "short_url": long_url.short_url, 
            "clicks": long_url.clicks
            }
        print("finish*********************")
        return output, 200
    except:
        print("fail*********************")
        return "doesn't Exist", 404

def create(request):
    data = request.json
    # Fetch existing url
    existing_url = check_if_url_exists(data["original_url"])
    if existing_url == False:
        # Create short url
        generated_url = short_url_Generator()
        new_url = Url(original_url=data["original_url"], short_url=generated_url)
        # Add to DB
        db.session.add(new_url)
        db.session.commit()
        # Get The data
        data = get_url_by_long_url(data["original_url"])
        return data, 201
    else:
        return existing_url, 200

def short_url_Generator():
    base = 'http://127.0.0.1:5000/'
    # Generate random id
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(5))
    return base + id

def check_if_url_exists(url):
    try:
        long_url = Url.query.filter_by(original_url=str(url)).first()
        output = {
            "original_url": long_url.original_url, 
            "short_url": long_url.short_url, 
            "click": long_url.clicks
        }
        return output
    except: 
        return False

def redirect_to_url(url):
    print('********* redirect url ********')
    base = 'http://127.0.0.1:5000/'
    print(url)
    data = get_long_url_by__short_url(base+url)
    original_url = data[0]['original_url']
    print('******** redirect url *********')
    print(original_url)
    return redirect(original_url)



        
