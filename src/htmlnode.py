
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError
    def get_tags(self):
        if self.tag ==None:
            return ""
        start = f"<{self.tag}{self.props_to_html()}>"
        end = f"</{self.tag}>"
        return start, end


    def props_to_html(self):
        property =""
        if self.props==None or len(self.props) == 0:
            return property
        for key in self.props:
            new_property = f" {key}={self.props[key]}"
            property+= new_property
        return property

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
