"""File standard Model"""
from copy import deepcopy


class Model(object):
    """Standard model class"""

    def dump(self):
        """Dump all attributes to a dictionnary"""
        d = deepcopy(self.__dict__)
        try:
            del d["_sa_instance_state"]
        except:
            pass
        return d