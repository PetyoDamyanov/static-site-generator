from textnode import TextNode, TextType

def main():
    first_node = TextNode("Some text", TextType.BOLD, "https://example.com")
    second_node = TextNode("Some text", TextType.BOLD, "https://example.com")
    print(first_node)

main()
