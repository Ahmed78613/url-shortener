from flask import Blueprint, request, jsonify
from ..controllers import urlController

main_route = Blueprint("main", __name__)

@main_route.route("/url",  methods=['GET', 'POST'])
def url():
    fns = {
        'GET': urlController.url,
        'POST': urlController.create,
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

