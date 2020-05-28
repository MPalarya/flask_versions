from flask import Blueprint
from ..common import deprecated
from ..common import bdb as common


api = Blueprint(__name__, __name__)


@api.route('/common')
def get_common():
    return "'get_common' from v1 -> " + common.get_common()


@api.route('/unique')
def get_unique():
    return "'get_unique' from v1."


# defined only in v1:


@api.route('/not_deprecated')
def not_deprecated():
    return 'not_deprecated FROM v1'


@deprecated
@api.route('/deprecated')
def deprecated():
    return 'deprecated FROM v1'
