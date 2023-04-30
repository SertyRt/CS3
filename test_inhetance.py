import unittest
from io import StringIO
from contextlib import redirect_stdout

from Inheritance import Paladin, OathOfTheAncients


class TestPaladin(unittest.TestCase):

    def test_paladin_attack(self):
        # Create a Paladin instance and call the attack method
        p = Paladin('Arthur', 5, 50)
        with redirect_stdout(StringIO()) as f:
            p.attack()
        # Assert that the Paladin's attack method returns the expected output
        self.assertEqual(f.getvalue().strip(), 'Arthur attacks with his melee weapon!')

class TestOathOfTheAncients(unittest.TestCase):

    def test_oath_of_ancients_attack(self):
        # Create an OathOfTheAncients instance and call the attack method
        oa = OathOfTheAncients('Galahad', 7, 70)
        with redirect_stdout(StringIO()) as f:
            oa.attack()
        # Assert that the OathOfTheAncients' attack method returns the expected output
        self.assertEqual(f.getvalue().strip(), 'Galahad attacks with his melee weapon!')

    def test_oath_of_ancients_spell(self):
        # Create an OathOfTheAncients instance and call the use_spell method
        oa = OathOfTheAncients('Galahad', 7, 70)
        with redirect_stdout(StringIO()) as f:
            oa.use_spell()
        # Assert that the OathOfTheAncients' use_spell method returns the expected output
        self.assertEqual(f.getvalue().strip(), 'Galahad casts Cure Wounds!')

if __name__ == '__main__':
    unittest.main()