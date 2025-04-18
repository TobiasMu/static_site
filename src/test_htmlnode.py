import unittest


from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com",
                                                     "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=https://www.google.com target=_blank")

    def test_notequal(self):
        node = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com",
                                                     "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), "href=https://www.google.comtarget=_blank")

    def test_moretest(self):
        self.assertEqual(0,0)

if __name__ == "__main__":
    unittest.main()
