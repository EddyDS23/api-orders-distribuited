
class DomainException(Exception):
    pass


class ItemExistingInOrder(DomainException):
    pass


class ItemNotExistingInOrder(DomainException):
    pass