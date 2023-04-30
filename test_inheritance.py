import unittest
from Inheritance import Paladin, OathOfGlory


class TestPaladin(unittest.TestCase):

    def test_paladin_attack(self):
        # Create a Paladin instance and call the attack method
        p = Paladin('René', 7, 74)
        # Assert that the Paladin's attack method returns the expected output
        self.assertEqual(p.attack(), 'René attacks with his melee weapon!')

class TestOathOfGlory(unittest.TestCase):

    def test_oath_of_glory_attack(self):
        og = OathOfGlory('Radko', 7, 70)
        self.assertEqual(og.attack(), 'Radko attacks with his melee weapon!')

    def test_oath_of_glory_spell(self):
        og = OathOfGlory('Radko', 7, 70)
        self.assertEqual(og.use_spell(), 'Radko casts Cure Wounds!')

if __name__ == '__main__':
    unittest.main()