import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
        
    def test_repr(self):
        node = HTMLNode("a", "Link to something", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual('HTMLNode: (\ntag: a\nvalue: Link to something\nchildren: None\nprops: {\'href\': \'https://www.google.com\', \'target\': \'_blank\'}\n)', repr(node))        

    def test_props_to_html(self):
        node = HTMLNode("a", "Link to something", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(' href="https://www.google.com" target="_blank"',node.props_to_html())

    def test_props_to_html_not_eq(self):
        node = HTMLNode("a", "Link to something", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual('href="https://www.google.com" target="_blank"',node.props_to_html())

if __name__ == "__main__":
    unittest.main()