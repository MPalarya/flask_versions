from flask import Blueprint
from ..common import bdb as common


api = Blueprint(__name__, __name__)


@api.route('/common')
def get_common():
    return "'get_common' from v2 -> " + common.get_common()


@api.route('/unique')
def get_unique():
    return "'get_unique' from v2."
