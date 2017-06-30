import itertools

import six


class _ChoicesMeta(type):
    def __new__(mcs, name, bases, attrs):
        obj = super(_ChoicesMeta, mcs).__new__(mcs, name, bases, attrs)
        obj._items = ()
        if bases != (object,):
            values = sorted([
                (val._order, val) for val in attrs.values()
                if isinstance(val, Choice)
            ])
            values = [value[1] for value in values]
            obj._items = tuple((val, val.text) for val in values)
        return obj

    def __iter__(self):
        """
        Provides 'in' ability
        """
        for x in self._items:
            yield x[0]


@six.add_metaclass(_ChoicesMeta)
class Choices(object):
    """
    >>> class Types(Choices):
    >>>     BAR = Choice('foo_bar', 'Foo Bar')
    >>>     BAZ = Choice('foo_baz', 'Foo Baz')
    >>> Types.BAR
    'foo_bar'
    >>> Types.BAR.text
    'Foo Bar'
    >>> Types.items()
    (('foo_bar', 'Foo Bar'), ('foo_baz', 'Foo Baz'))
    >>> Types.keys()
    ('foo_bar', 'foo_baz')
    >>> Types.values()
    ('Foo Bar', 'Foo Baz')
    >>> 'foo_bar' in Types
    True

    >>> class Types2(Choices):
    >>>     BAR = Choice('foo_bar', 'Foo Bar', extra_attr='x')
    >>>     BAZ = Choice('foo_baz', 'Foo Baz', extra_attr='y')
    >>> Types2.BAR.extra_attr
    'x'
    >>> Types2.BAR.not_existing_attr is None
    True
    """

    @classmethod
    def items(cls):
        return cls._items

    @classmethod
    def keys(cls):
        return tuple(item[0] for item in cls.items())

    @classmethod
    def values(cls):
        return tuple(item[1] for item in cls.items())

    @classmethod
    def get(cls, name):
        return next((key for key in cls.keys() if key == name), None)


class Choice(str):
    _counter = itertools.count()

    def __new__(cls, choice, text=None, **kwargs):
        obj = str.__new__(cls, choice)
        obj.text = text
        for k, v in six.iteritems(kwargs):
            setattr(obj, k, v)
        return obj

    def __init__(self, *args, **kwargs):
        self._order = next(Choice._counter)
        super(Choice, self).__init__()

    def __copy__(self):
        cls = self.__class__
        return cls(str(self), **self.__dict__)

    def __deepcopy__(self, _):
        return self.__copy__()
