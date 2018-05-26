from py2neo import Node, Relationship
from py2neo import Graph

global graph

def init():
    global graph
    graph = Graph("http://localhost:7474", username="neo4j", password="123456")
def clearAll():
    graph.delete_all()

def addNode(tag, **keyValues):
    """
    :param tag: 标签，比如Person
    :param keyValues: 标签值<key, value>格式
    :return: 插入到图数据库结果
              0 成功
              1 失败
    eg.
        addNode("Person", name="Jim")
    """
    # print(tag)
    # print(keyValues)
    tempNode = Node(tag)
    for first_part, second_part in keyValues.items():
        tempNode[first_part] = second_part
    graph.create(tempNode)
    return tempNode
    pass


def addRelationship(nodeA, relationship, nodeB, **properties):
    """
    :param nodeA: 节点A
    :param nodeB: 节点B
    :param relationship: 关系
    :return: 插入到图数据库结果
              0 成功
              1 失败
    eg.
        (bob)-[:KNOWS {time:"198708"}]->(mike)
    """

    relationship = Relationship(nodeA, relationship, nodeB)
    for first_part, second_part in properties.items():
        relationship[first_part] = second_part
    graph.create(relationship)
    return relationship
    pass

def delRefence(relationship):
    """
    :param relationship: 关系 Relationship
    :return: 插入到图数据库结果
              0 成功
              1 失败
    eg.
        (bob)-[:KNOWS {time:"198708"}]->(mike)
        person.knows.remove(target)
    """
    graph.delete(relationship)
    pass

def delRefence(nodeA, relationship, nodeB):
    """
    :param nodeA: 节点A
    :param nodeB: 节点B
    :param relationship: 关系
    :return: 插入到图数据库结果
              0 成功
              1 失败
    eg.
        (bob)-[:KNOWS {time:"198708"}]->(mike)
        person.knows.remove(target)
    """

    pass

def selectBeginNode(relationship, nodeB):
    """
    :param
    :param nodeB: 节点B
    :param relationship: 关系
    :return: 插入到图数据库结果
              成功 nodeA: 节点A
              失败 null
    eg.
        selectEndNode(bob, r)
        (bob)-[:KNOWS {time:"198708"}]->(mike)
    """
    selector = NodeSelector(graph)

    pass

def selectEndNode(nodeA, relationship):
    """
    :param nodeA: 节点A
    :param
    :param relationship: 关系
    :return: 插入到图数据库结果
              成功 nodeB: 节点B
              失败 null
    eg.
        (bob)-[:KNOWS {time:"198708"}]->(mike)
    """
    pass

def selectRelationship(nodeA, nodeB):
    """
    :param nodeA: 节点A
    :param nodeB: 节点B
    :param
    :return: 插入到图数据库结果
              成功 relationship: 关系
              失败 null
    eg.
        (bob)-[:KNOWS {time:"198708"}]->(mike)
    """
    pass