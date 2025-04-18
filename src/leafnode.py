from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag,value,None,props)


    def to_html(self):
        if self.value==None:
            print(self)
            raise ValueError
        if self.tag==None:
            return self.value
        start_tag, end_tag = self.get_tags()
        return f"{start_tag}{self.value}{end_tag}"

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
