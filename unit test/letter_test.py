from letters import LetterCompiler
import unittest

class TestLetters(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_word(self):
        testcase = "awesome"
        expected = ['a']
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_unmatch(self):
        testcase = "go"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

if __name__ == "__main__":
	unittest.main()