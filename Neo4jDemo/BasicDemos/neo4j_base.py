from py2neo import Graph


def connectNeo4j():

    neo4j_graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="123456"
    )
    return neo4j_graph;

# print("here connectNeo4j")