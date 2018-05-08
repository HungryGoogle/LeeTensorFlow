

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