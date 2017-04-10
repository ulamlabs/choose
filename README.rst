choose
========

Choices on steroids

.. image:: https://img.shields.io/pypi/v/choose.svg
        :target: https://pypi.python.org/pypi/choose

.. image:: https://img.shields.io/travis/ulamlabs/choose.svg
        :target: https://travis-ci.org/ulamlabs/choose

.. image:: https://codecov.io/gh/ulamlabs/choose/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/ulamlabs/choose


Supported versions
================

- Python 2 and 3 support


How to install
==========

    .. code-block:: bash
    
        pip install choose


Basic usage:
===========

    .. code-block:: python

        >>> class Types(choose.Choices):
        >>>     BAR = choose.Choice('foo_bar', 'Foo Bar')
        >>>     BAZ = choose.Choice('foo_baz', 'Foo Baz')
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

Extended usage:
===============

    .. code-block:: python

        >>> class Types2(choose.Choices):
        >>>     BAR = choose.Choice('foo_bar', 'Foo Bar', default=False)
        >>>     BAZ = choose.Choice('foo_baz', 'Foo Baz', default=False)
        >>>     FOO = choose.Choice('foo_foo', 'Foo Foo', default=True)
        >>>
        >>>     @classmethod
        >>>     def get_default(cls):
        >>>         return next(
        >>>             (item for item in cls.keys() if item.opts.default is True),
        >>>             None,
        >>>         )
        >>>
        >>> Types2.BAR.opts.default
        False
        >>> Types2.BAR.opts.not_existing_attr is None
        True
        >>> 'foo_bar' == Types2.get_default()
        False
        >>> Types2.BAR == Types2.get_default()
        False
        >>> 'foo_foo' == Types2.get_default()
        True
        >>> Types2.FOO == Types2.get_default()
        True

Usage in Django:
================

    .. code-block:: python

        class AModel(models.Model):
            class AChoices(choose.Choices):
                X = choose.Choice('x', 'X')
                Y = choose.Choice('y', 'Y')

            choice = models.CharField(max_length=63, choices=AChoices.items())
