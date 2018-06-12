import xml.etree.ElementTree as ET

"""

"""


def set_tag_content(node, data_dict):
    for k, v in data_dict.items():
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
            search_str = search_str[:len(search_str)-1]
            print('search_str:', search_str)
            pass
        node_list = node.findall(search_str)
        print('len(node_list):', len(node_list))
        for groupIdNode in node_list:
            print(groupIdNode.tag)
            print(groupIdNode.text)
            groupIdNode.text = v
            pass
        pass
    pass


def get_tree(file_path):
    """
    parse xml file and return the result
    :param file_path:
    :return:
    """
    # if not register_namespace, a namespace prefix will be added right before every tag.
    ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')
    # ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    return ET.parse(file_path)
    pass


if __name__ == "__main__":
    file_path = r'D:\workspace\eclipse-oxygen\p_web2\pom.xml'
    tree = get_tree(file_path)
    root = tree.getroot()
    content_dict = {}
    content_dict['groupId'] = 'groupId111'
    content_dict['artifactId'] = 'artifactId111'
    content_dict['build$plugins$plugin$configuration$source'] = 'source333'
    content_dict['build$plugins$plugin$configuration$target'] = 'target333'
    set_tag_content(root, content_dict)
    tree.write(file_path)
    pass

