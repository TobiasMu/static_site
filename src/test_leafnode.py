
import unittest


from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="a", value="click this", props={"href": "https://www.google.com",
                                                     "target": "_blank"})
        print(node)
        self.assertEqual(node.to_html(), "<a href=https://www.google.com target=_blank>click this</a>")

    def test_notequal(self):
        node = LeafNode(tag="p", value="??", props={"href": "https://www.google.com",
                                                     "target": "_blank"})
        self.assertNotEqual(node.to_html(), "href=https://www.google.comtarget=_blank")

    def test_moretest(self):
        self.assertEqual(0,0)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
if __name__ == "__main__":
    unittest.main()
