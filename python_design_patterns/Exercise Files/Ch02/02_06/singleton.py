class Borg:

    """The Borg design pattern"""
    _shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class Singleton(Borg):

    """The singleton class"""

    def __init__(self, **kwargs) -> None:
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP="Hyper Text Transfer Protocol")

print(x)

y = Singleton(SMTP='Simple Mail Transfer Protocol')

print(y)
