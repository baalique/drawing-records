class ServiceLayerException(Exception):
    pass


class AlreadyExistsError(ServiceLayerException):
    pass


class NotFoundError(ServiceLayerException):
    pass


ex = NotFoundError()
