import copy

import choose


class TestChoices(choose.Choices):
    ONE = choose.Choice(
        'one', 'One',
        opt=1, onlyone='onlyone', onlythree=None,
    )
    TWO = choose.Choice(
        'two', 'Two',
        opt=2, onlyone=None, onlythree=None,
    )
    THREE = choose.Choice(
        'three', 'Three',
        opt=3, onlythree='onlythree', onlyone=None,
    )


class TestChoices2(choose.Choices):
    ONE = choose.Choice('one', foo=1)
    TWO = choose.Choice('two', bar=2)
    THREE = choose.Choice('three', baz=3)


def test_items():
    expected = (('one', 'One'), ('two', 'Two'), ('three', 'Three'))
    assert TestChoices.items() == expected


def test_keys():
    expected = ('one', 'two', 'three')
    assert TestChoices.keys() == expected


def test_values():
    expected = ('One', 'Two', 'Three')
    assert TestChoices.values() == expected


def test_choice():
    assert TestChoices.ONE == 'one'
    assert TestChoices.TWO == 'two'
    assert TestChoices.THREE == 'three'

    assert TestChoices.ONE.text == 'One'
    assert TestChoices.TWO.text == 'Two'
    assert TestChoices.THREE.text == 'Three'


def test_opts():
    assert TestChoices.ONE.opt == 1
    assert TestChoices.TWO.opt == 2
    assert TestChoices.THREE.opt == 3

    assert TestChoices.ONE.onlyone == 'onlyone'
    assert TestChoices.TWO.onlyone is None
    assert TestChoices.THREE.onlyone is None

    assert TestChoices.ONE.onlythree is None
    assert TestChoices.TWO.onlythree is None
    assert TestChoices.THREE.onlythree == 'onlythree'


def test_no_text():
    expected = (('one', None), ('two', None), ('three', None))
    assert TestChoices2.items() == expected

    expected = ('one', 'two', 'three')
    assert TestChoices2.keys() == expected

    expected = (None, None, None)
    assert TestChoices2.values() == expected

    assert TestChoices2.ONE.foo == 1
    assert TestChoices2.TWO.bar == 2
    assert TestChoices2.THREE.baz == 3


def test_in():
    assert 'one' in TestChoices
    assert 'one2' not in TestChoices


def test_copy():
    ONE_copied = copy.copy(TestChoices.ONE)
    assert ONE_copied == TestChoices.ONE
    assert ONE_copied.opt == 1

    TWO_copied = copy.deepcopy(TestChoices.TWO)
    assert TWO_copied == TestChoices.TWO
    assert TWO_copied.opt == 2


def test_get():
    assert TestChoices.get('one') == TestChoices.ONE
    assert TestChoices.get('two') == TestChoices.TWO
    assert TestChoices.get('three').opt == 3
