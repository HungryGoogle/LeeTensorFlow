from py2neo import Graph, Node, Relationship, NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

graph.delete_all()

test_node_1 = Node("Person", name="test_node_1")
test_node_2 = Node("Person", name="test_node_2")

graph.create(test_node_1)
graph.create(test_node_2)

# # 官方已废弃
# find_code_1 = graph.find_one(
#   label="Person",
#   property_key="name",
#   property_value="test_node_1"
# )
# print (find_code_1)

# # 官方已废弃
# node = graph.find(label='Person', property_key = 'name', property_value = 'test_node_1')
# print(node['name'])

selector = NodeSelector(graph)
persons = selector.select('Person')

print(list(persons))
print(persons)
