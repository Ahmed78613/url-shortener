from flask import Blueprint, request, jsonify, redirect
from ..controllers import urlController

main_route = Blueprint("main", __name__)

@main_route.route("/",  methods=['GET', 'POST'])
def url():
    fns = {
        'GET': urlController.url,
        'POST': urlController.create,
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@main_route.route("/url/<string:url>")
def getSpecificUrl(url):
    resp, code = urlController.get_url_by_long_url(url)
    return jsonify(resp), code


@main_route.route("/<string:url>")
def redirectUser(url):
    resp = urlController.redirect_to_url(url)
    return resp

