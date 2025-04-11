class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""   
        props_string = ""
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'
        return props_string
    
    def __repr__(self):
        return f"HTMLNode: (\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n)"