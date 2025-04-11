from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    first_node = TextNode("Some text", TextType.BOLD, "https://example.com")
    second_node = TextNode("Some text", TextType.BOLD, "https://example.com")
    print(first_node)
    html_node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank",})
    print(html_node.props_to_html())
    print(html_node)
main()
