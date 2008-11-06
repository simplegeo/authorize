import inspect

def add_method(kls, name, func):
    """
    Add a method 'func' to the class 'kls' in an attribute named 'name'
    """
    f = lambda self, **kw: self.request(func(self.login, self.key, **kw))
    f.__name__ = name
    setattr(kls, name, f)

def populate(k, from_, prefix, async=False):
    # get all the function objects from xml module and filter out those
    # that don't start with 'cim_' and add them to Api class.
    for name, func in inspect.getmembers(from_, inspect.isfunction):
        if name.startswith(prefix):
            # warning add_method function is required to bind func, otherwise
            # doing this inline would use the last value of the name 'func'
            add_method(k, name[len(prefix):], func)
