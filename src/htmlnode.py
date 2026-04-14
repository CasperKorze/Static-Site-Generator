


class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        #tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.) An HTMLNode without a tag will just render as raw text
        self.tag = tag 
        #value - A string representing the value of the HTML tag (e.g. the text inside a paragraph) An HTMLNode without a value will be assumed to have children
        self.value = value
        #children - A list of HTMLNode objects representing the children of this node. An HTMLNode without children will be assumed to have a value
        self.children = children
        #props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"} An HTMLNode without props simply won't have any attributes
        self.props = props


    def to_html(self):
        raise NotImplementedError("to_html method not implemented yet")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return " " + props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    

    