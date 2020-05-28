DEPRECATED_ATTRIBUTE = '_deprecated'


def deprecated(func):
    setattr(func, DEPRECATED_ATTRIBUTE, True)
    return func
