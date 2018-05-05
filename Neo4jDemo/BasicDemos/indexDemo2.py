from py2neo import Graph, Node, Relationship, NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

graph.delete_all()
#
#
# a = Node('Person', name='Alice', age=21, location='广州')
# b = Node('Person', name='Bob', age=22, location='上海')
# c = Node('Person', name='Mike', age=21, location='北京')
# r1 = Relationship(a, 'KNOWS', b)
# r2 = Relationship(b, 'KNOWS', c)
# graph.create(a)
# graph.create(r1)
# graph.create(r2)
#
#
# selector = NodeSelector(graph)
# persons = selector.select('Person', age=21)
# print(list(persons))
#
# persons = selector.select('Person')
# print(list(persons))
#
#
#
# persons2 = selector.select('Person').where('_.name =~ "A.*"').first()
# print(persons2)
#

# 编译不过
# IndexManager index = graphDb.index();
# Index<Node> fulltextMovies = index.forNodes( "movies-fulltext", MapUtil.stringMap( IndexManager.PROVIDER, "lucene", "type", "fulltext"));
# fulltextMovies.add( theMatrix, "title", "The Matrix" );
# fulltextMovies.add( theMatrixReloaded, "title", "The Matrix Reloaded" );
# // search in the fulltext index
# Node found = fulltextMovies.query( "title", "reloAdEd" ).getSingle();