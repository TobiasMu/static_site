from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag==None:
            raise ValueError("no tag")
        if len(self.children)==0:
            raise ValueError("no children")

        start, end = self.get_tags()
        value=""
        for child in self.children:
            value += child.to_html()
        return start + value +end

