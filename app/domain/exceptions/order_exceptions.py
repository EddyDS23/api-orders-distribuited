
class DomainError(Exception):
    pass


class EmptyOrderError(DomainError):
    pass


class InvalidOperationOrderError(DomainError):
    pass

class OrderNotFoundException(DomainError):
    pass

