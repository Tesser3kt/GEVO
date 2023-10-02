SYMBOLS = ["-", ".", "_"]


def polygon(symbols: list) -> dict:
    """ Create an encoding polygon. """
    return {
        index: symbol
        for index, symbol in enumerate(symbols)
    }


def rotate(polygon: dict, shift: int) -> dict:
    """ Rotate the polygon by the given shift. """
    return {
        (index + shift) % len(polygon): symbol
        for index, symbol in polygon.items()
    }


def reflect(polygon: dict) -> dict:
    """ Reflect the polygon. """
    return {
        len(polygon) - index - 1: symbol
        for index, symbol in polygon.items()
    }
