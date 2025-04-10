import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_text(self):
        node = TextNode("This is a text node ", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_type(self):
        node = TextNode("This is a text node ", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)        

    def test_noteq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)        
    
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
            node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
            self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))        

if __name__ == "__main__":
    unittest.main()