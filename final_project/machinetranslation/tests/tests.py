#Create a new file called tests.py in the machinetranslation directory.
#Write at least 2 tests in tests.py for each method
#Test for null input for frenchToEnglish
#Test for null input for englishToFrench.
#Test for the translation of the world 'Hello' and 'Bonjour'.
#Test for the translation of the world 'Bonjour' and 'Hello'.
#Take a screenshot of your unit tests and save it as a .jpg or .png with the filename translation_unittests.


import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    def test_english_to_french_first(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_second(self):
        self.assertEqual(english_to_french(None), None)

    def test_french_to_english_first(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_french_to_english_second(self):
        self.assertEqual(french_to_english(None), None)

if __name__ == '__main__':
    unittest.main()
