from abc import ABC

from manager import Manager


class BaseClass(ABC):
    id = 0
    manager = None
    object_list = None

    def __init__(self, *args, **kwargs):
        self._id = self.generate_id()
        self.store(self)
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)
