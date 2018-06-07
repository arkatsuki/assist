import xml.etree.ElementTree as ET

"""

"""

def recur_trav_node(node, content_dict):
    """
    recursion traversal node
    :param node:
    :return:
    """
    # length equals the number of sub tag, if length==0, indicate that there is no sub tag
    if len(node)<1:
        for k, v in content_dict.items():
            if node.tag.endswith(k):
                # print('find groupId')
                node.text = v
                pass
            pass
        pass
    else:
        for child in node:
            recur_trav_node(child, content_dict)
            pass
        pass

    pass

def set_tag_content(file_path, content_dict):
    """
    设置标签体的内容
    :param file_path:
    :param content_dict:  a dict, key is tag_name, value is tag_content
    :return:
    """
    tree = get_tree(file_path)
    # root = ET.fromstring(country_string) #从字符串传递xml
    root = tree.getroot()
    # help(root)
    recur_trav_node(root, content_dict)
    tree.write(file_path)
    pass


def trav_te(file_path):
    """
    test traversal
    :param file_path:
    :return:
    """
    tree = get_tree(file_path)
    # root = ET.fromstring(country_string) #从字符串传递xml
    root = tree.getroot()
    # help(root)
    for child in root:
        print(child.tag, 'len:' ,len(child))
        # child.tag.find('')
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
    ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    return ET.parse(file_path)
    pass


if __name__ == "__main__":
    file_path = r'D:\workspace\eclipse-oxygen\p_web2\pom.xml'
    # content_dict = {}
    # content_dict['groupId'] = 'groupId111'
    # content_dict['artifactId'] = 'artifactId111'
    # content_dict['source'] = 'source333'
    # content_dict['target'] = 'target333'
    # set_tag_content(file_path, content_dict)
    # test_trav(file_path)
    tree = get_tree(file_path)
    root = tree.getroot()
    print(root.tag)
    # only direct children
    # node_list = root.findall('./[{http://maven.apache.org/POM/4.0.0}groupId]')
    # node_list = root.findall('{http://maven.apache.org/POM/4.0.0}groupId')
    # all children, include direct and indirect
    node_list = root.findall('.//{http://maven.apache.org/POM/4.0.0}groupId')
    # node_list = root.findall("./[@name='{http://maven.apache.org/POM/4.0.0}groupId']")
    print(len(node_list))
    for groupIdNode in node_list:
        print('find:', groupIdNode.tag)
        groupIdNode.text = 'groupId222'
        pass

    # also work, get all direct and indirect
    # for groupIdNode in root.iter('{http://maven.apache.org/POM/4.0.0}groupId'):
    #     print('find2:', groupIdNode.tag)
    #     pass

    pass

