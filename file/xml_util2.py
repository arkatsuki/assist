import xml.etree.ElementTree as ET

"""

"""


class XmlUtil(object):
    def __init__(self, file_path, namespace = [], content_dict = {}):
        self.content_dict = content_dict
        self.file_path = file_path
        self.namespace = namespace
        pass

    def set_tag_content(self, node):
        for k, v in self.content_dict.items():
            search_str = './'
            namespace = '{http://maven.apache.org/POM/4.0.0}'
            if k.find('$') < 0:
                search_str = search_str + namespace + k
                pass
            else:
                tag_li = k.split('$')
                for i in range(0, len(tag_li)):
                    search_str = search_str + namespace + tag_li[i]
                    search_str = search_str + '/'
                    pass
                search_str = search_str[:len(search_str) - 1]
                print('search_str:', search_str)
                pass
            for groupIdNode in node.findall(search_str):
                groupIdNode.text = v
                pass
            pass
        pass



    pass
