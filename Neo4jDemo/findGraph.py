from py2neo import Graph

from Neo4jDemo.noe4j_common.neo4j_base import connectNeo4j

graph = connectNeo4j()
node = graph.find_one(label='Person')
print(node)
relationship = graph.match_one(rel_type='KNOWS')
print(relationship)