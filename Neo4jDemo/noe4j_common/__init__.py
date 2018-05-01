
print(" init noe4j_common ------------------------------------------")

# from py2neo import Graph,Node,Relationship
#
# test_graph = Graph(
#     "http://localhost:7474",
#     username="neo4j",
#     password="123456"
# )
#
# test_graph.delete_all()
#
# a = Node('Person', name='Alice')
# b = Node('Person', name='Bob')
# r = Relationship(a, 'KNOWS', b)
# print(a, b, r)
#
# a['age'] = 20
# b['age'] = 21
# r['time'] = '2017/08/31'
# print(a, b, r)
#
# a.setdefault('location', '北京')
# print(a)
#
# a['location'] = '上海'
# a.setdefault('location', '北京')
# print(a)
#
# data = {
#     'name': 'Amy',
#     'age': 21
# }
# a.update(data)
# print(a)
#
#
# print(" 取 Subgraph 的各个属性 1 ------------------------------------------")
# s = a | b | r
# print(s)
#
# print(" 取 Subgraph 的各个属性 2 ------------------------------------------")
# print(s.keys())
# print(s.labels())
# print(s.nodes())
# print(s.relationships())
# print(s.types())
#
# # 另外还可以利用 & 取 Subgraph 的交集，例如：
# print(" & 取 Subgraph 的交集 ------------------------------------------")
# s1 = a | b | r
# s2 = a | b
# print(s1 & s2)
#

