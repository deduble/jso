class JSO:
    def __new__(cls, item):
        if isinstance(item, dict):
            obj = object.__new__(cls)
            obj.__init__(item)
        elif isinstance(item, list):
            obj = []
            for el in item:
                el_obj = JSO.__new__(cls, el)
                el_obj.__init__(el)
                obj.append(el_obj)
        else:
            obj = item
        return obj

    def __init__(self, item):
        if isinstance(item, dict):
            for key in item.keys():
                self.__setattr__(key, JSO(item[key]))

    def __repr__(self):
        return self.__dict__.__repr__()