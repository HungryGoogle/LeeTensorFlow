from py2neo import Graph, Node, Relationship, NodeSelector

from Neo4jDemo.Neo4jApi import neo4jApi

if __name__ == '__main__':
    neo4jApi.init()
    neo4jApi.clearAll()
    nodeA = neo4jApi.addNode('person', name='alice')
    nodeB = neo4jApi.addNode('person', name='bob')
    relationship = neo4jApi.addRelationship(nodeA, 'knows', nodeB, time='20180505')

    listBeginsNodes1 = neo4jApi.selectBeginNode('knows', nodeB)
    listBeginsNodes2 = neo4jApi.selectEndNode(nodeA,'knows')



    print('nodeA : ', nodeA)
    print('nodeB : ', nodeB)
    print('relationship : ', relationship)
    print('listBeginsNodes1 : ', listBeginsNodes1)
    print('listBeginsNodes2 : ', listBeginsNodes2)



