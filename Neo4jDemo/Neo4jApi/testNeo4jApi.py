from py2neo import Graph, Node, Relationship, NodeSelector

from Neo4jDemo.Neo4jApi import neo4jApi

if __name__ == '__main__':
    neo4jApi.init()
    neo4jApi.clearAll()
    nodeA = neo4jApi.addNode('person', name='alice')
    nodeB = neo4jApi.addNode('person', name='bob')
    relationship = neo4jApi.addRelationship(nodeA, 'knows', nodeB, time='20180505')

    listBeginsNodes = neo4jApi.selectBeginNode('knows', nodeB)

    print('nodeA : ', nodeA)
    print('nodeB : ', nodeB)
    print('relationship : ', relationship)
    print('listBeginsNodes : ', listBeginsNodes)



