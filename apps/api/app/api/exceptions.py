class NotFoundException(RuntimeError):
    """Raise when the resource is not found"""

    pass


class InvalidInputException(RuntimeError):
    """Raise when the input is invalid"""

    pass
