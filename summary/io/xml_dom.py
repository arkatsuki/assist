from xml.dom.minidom import parse
import xml.dom.minidom


def recur_trav_node_print(node):
    # length equals the number of sub tag, if length==0, indicate that there is no sub tag
    # print(node.nodeName)
    # print('len(node.childNodes):',len(node.childNodes))
    if len(node.childNodes)==1:
        if node.nodeType == node.ELEMENT_NODE:
            # print(node.nodeName)
            # print(node.toxml())
            # this could get text data
            print(node.childNodes[0].data)
            # print(node.childNodes[0].nodeType)
            # print(node.childNodes[0].nodeName)
            # node.replaceChild(node.childNodes[0], 'ttt')
            # node.removeChild(node.childNodes[0])
            # node.appendChild('ttt')
            pass
        pass
    elif len(node.childNodes)==0:
        if node.nodeType == node.TEXT_NODE:
            # print(node.nodeName)
            # print(node.toxml())
            # cannot get text data in this way, use node.childNodes[0].data instead
            # print(node.data)
            # print(node.nodeValue)
            # print(node.nodeType)
            pass
        pass
    else:
        for child in node.childNodes:
            recur_trav_node_print(child)
            pass
        pass

    pass

file_path = r'D:\workspace\eclipse-oxygen\p_web2\pom1.xml'
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(file_path)
collection = DOMTree.documentElement
# help(collection)

# recur_trav_node_print(collection)
