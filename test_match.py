import unittest

from main import match_height_in_inches


class TestMatch(unittest.TestCase):

    def test_match_height_in_inches(self):
        self.assertNotEqual(match_height_in_inches(0), "Brevin Knight")
        self.assertEqual(match_height_in_inches(0), [])
        self.assertEqual(match_height_in_inches(139),
                         ['Brevin Knight     Nate Robinson', 'Mike Wilks     Nate Robinson'])
        self.assertEqual(match_height_in_inches(139),
                         ['Brevin Knight     Nate Robinson', 'Mike Wilks     Nate Robinson'])
        self.assertEqual(match_height_in_inches(177),
                         ['Yao Ming     Zydrunas Ilgauskas'])


if __name__ == '__main__':
    unittest.main()
