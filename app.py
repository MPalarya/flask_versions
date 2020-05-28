from flask import Flask
from flask import request
from werkzeug.routing import RequestRedirect
from werkzeug.exceptions import MethodNotAllowed, NotFound

import api


app = Flask(__name__)


@app.errorhandler(404)
def handle_fallback(_):
    version = filter(None, request.path.split('/'))[0]
    if version not in api.VERSION_FALLBACK:
        return "not found."

    fallback_url = request.path.replace(version, api.VERSION_FALLBACK[version])
    rules_adapter = app.url_map.bind('localhost')
    try:
        the_rule, the_args = rules_adapter.match(fallback_url)
    except RequestRedirect:
        return "we do not support recursive redirects yet."
    except (MethodNotAllowed, NotFound):
        return "this is a real 404. nothing found."

    the_func = app.view_functions.get(the_rule)

    if getattr(the_func, api.DEPRECATED_ATTRIBUTE, False):
        return "deprecated: {}.".format(the_rule)
    return the_func()


def run():
    api.register_versions(application=app, versions=api.SUPPORTED_VERSIONS, default_version=api.DEFAULT_VERSION)
    app.run()


if __name__ == '__main__':
    run()
