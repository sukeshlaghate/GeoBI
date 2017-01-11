""" Provides metaclasses for implementing patterns. This creates a singleton pattern"""


# Meta class method of creating the singleton
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            try:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            except TypeError as exception:
                cls._instances[cls] = super(Singleton, cls).__call__()

        return cls._instances[cls]