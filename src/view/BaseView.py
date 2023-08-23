from abc import ABC, abstractmethod

class BaseView(ABC):
    def __init__(self, request, *args, **kwargs):
        pass
    @abstractmethod
    def output(self, string):
        raise NotImplementedError

    @abstractmethod
    def input(self, string):
        raise NotImplementedError

