import unittest

import choose


class TestChoices(choose.Choices):
    ONE = choose.Choice('one', 'One', opt=1, onlyone='onlyone')
    TWO = choose.Choice('two', 'Two', opt=2)
    THREE = choose.Choice('three', 'Three', opt=3, onlythree='onlythree')


class ChooseTestCase(unittest.TestCase):
    def test_items(self):
        self.assertEqual(
            TestChoices.items(),
            (('one', 'One'), ('two', 'Two'), ('three', 'Three'))
        )

    def test_keys(self):
        self.assertEqual(
            TestChoices.keys(),
            ('one', 'two', 'three')
        )


    def test_values(self):
        self.assertEqual(
            TestChoices.values(),
            ('One', 'Two', 'Three'),
        )

    def test_choice(self):
        self.assertEqual(TestChoices.ONE, 'one')
        self.assertEqual(TestChoices.TWO, 'two')
        self.assertEqual(TestChoices.THREE, 'three')

        self.assertEqual(TestChoices.ONE.text, 'One')
        self.assertEqual(TestChoices.TWO.text, 'Two')
        self.assertEqual(TestChoices.THREE.text, 'Three')

    def test_opts(self):
        self.assertEqual(TestChoices.ONE.opts.opt, 1)
        self.assertEqual(TestChoices.TWO.opts.opt, 2)
        self.assertEqual(TestChoices.THREE.opts.opt, 3)

        self.assertEqual(TestChoices.ONE.opts.onlyone, 'onlyone')
        self.assertEqual(TestChoices.TWO.opts.onlyone, None)
        self.assertEqual(TestChoices.THREE.opts.onlyone, None)

        self.assertEqual(TestChoices.ONE.opts.onlythree, None)
        self.assertEqual(TestChoices.TWO.opts.onlythree, None)
        self.assertEqual(TestChoices.THREE.opts.onlythree, 'onlythree')

        self.assertEqual(TestChoices.ONE.opts.otheropt, None)
        self.assertEqual(TestChoices.TWO.opts.otheropt, None)
        self.assertEqual(TestChoices.THREE.opts.otheropt, None)

