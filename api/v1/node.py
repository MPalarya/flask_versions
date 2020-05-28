from flask import Blueprint


api = Blueprint(__name__, __name__)


@api.route('/')
def stupid():
    return __name__
