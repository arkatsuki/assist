import xml.sax


class PomHandler(xml.sax.ContentHandler):
    def __init__(self, content_dict = {}):
        self.current_data = ""
        self.content_dict = content_dict

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag in self.content_dict.keys():
            # print('find tag:',tag)
            # self.current_data = tag
            pass
        else:
            # print('tag not in:',tag)
            pass


    def endElement(self, tag):
        self.current_data = ''
        pass


    def characters(self, content):
        if self.current_data in self.content_dict.keys():
            print('self.current_data:', self.current_data)
            print('content:', content)
            pass
        # print('content:', content)
        pass


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    content_dict = {}
    # content_dict['year'] = '1111'
    content_dict['groupId'] = 'groupId333'
    content_dict['artifactId'] = 'artifactId333'
    content_dict['source'] = 'source333'
    content_dict['target'] = 'target333'
    # 重写 ContextHandler
    handler = PomHandler(content_dict)
    parser.setContentHandler(handler)
    file_path = r'D:\workspace\eclipse-oxygen\p_web2\pom.xml'

    parser.parse(file_path)
