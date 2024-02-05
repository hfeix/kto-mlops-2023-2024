import unittest

"""
Count names with more than seven letters

	Args:
            prenoms(List[str]): liste des prénoms

        Returns:
            int: Number of names with more than seven letters
"""

def count_names_letters(prenoms: str) -> str:
    max_letters = 7	
    more_than_seven_count = 0
    for prenom in prenoms:
        if len(prenom) > max_letters :
            more_than_seven_count += 1
            print("Prenom supérieur à 7 lettres : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 lettres : " + prenom)
    return more_than_seven_count

class TestNamesMethod(unittest.TestCase):
     def test_count_names_letters(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven_count = count_names_letters(prenoms=prenoms)
        self.assertEqual(more_than_seven_count, 4)

if __name__ == '__main__':
    unittest.main()
