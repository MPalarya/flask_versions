from typing import List

from common import DEPRECATED_ATTRIBUTE

import v1
import v2

SUPPORTED_VERSIONS = [v1, v2]  # type: List
DEFAULT_VERSION = v2  # default is None
VERSION_FALLBACK = {
    'v2': 'v1'
}


def register_versions(application, versions, default_version=None):

    def _register_blueprint(blueprint, url_prefix):
        print('registering - {}'.format(url_prefix))
        application.register_blueprint(blueprint, url_prefix=url_prefix)

    def _register_version(version_module, is_default=False):
        # (Module) api.v1 -> (String) v1
        version_str = version_module.__name__.split('.')[1]

        # List of sub-apis in the specific api version
        sub_apis = [sub_api for sub_api in version_module.__dict__ if not sub_api.startswith('_')]
        for sub_api in sub_apis:
            api_blueprint = version_module.__dict__[sub_api].__dict__['api']
            prefix = '/{}'.format(sub_api) if is_default else '/{}/{}'.format(version_str, sub_api)
            _register_blueprint(blueprint=api_blueprint, url_prefix=prefix)

    if default_version:
        _register_version(version_module=default_version, is_default=True)

    for api_version in versions:
        _register_version(version_module=api_version)
