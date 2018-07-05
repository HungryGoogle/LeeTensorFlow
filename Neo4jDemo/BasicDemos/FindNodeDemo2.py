from py2neo import Graph, Node, Relationship, NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

graph.delete_all()


a = Node('Person', name='Alice', age=21, location='广州')
b = Node('Person', name='Bob', age=22, location='上海')
c = Node('Person', name='Mike', age=21, location='北京')

a.setdefault('time','---2018---')
a['time1'] = '---2018_1---'
print(a)

r1 = Relationship(a, 'KNOWS', b)
r2 = Relationship(b, 'KNOWS', c)
r2.setdefault("time","198708")
r1['time']='2018'
graph.create(a)
graph.create(r1)
graph.create(r2)

r1.update()

# graph.delete(a)


print("------------> r2 ------------>")
print(r2)

selector = NodeSelector(graph)

print("------------> selector.select( age=21)")
persons = selector.select( age=21)
print(list(persons))

print("------------> selector.select('Person', age=21)")
persons = selector.select('Person', age=21)
print(list(persons))



print("------------> selector.select('Person', age=21).limit(1)")
persons = selector.select('Person', age=21).limit(1)
print(list(persons))

print("------------> selector.select('Person')")
persons = selector.select('Person')
print(list(persons))

# 错误
print("----------*****--> selector.select('Person').where('_.name =~ \"A.*\"').first()")
persons2 = selector.select('Person').where('_.name =~\'A.*\'').first()
print(persons2)


print("------------> KNOWS")
# persons2 = selector.select().where(rel_type='KNOWS')
# print(persons2)
relationship = graph.match_one(rel_type='KNOWS')
print(relationship)

relationship = graph.match_one(a, rel_type='KNOWS')
print(relationship)

relationship = graph.match_one(a, 'KNOWS',b)
print(relationship)

for rel in graph.match(start_node=a, rel_type="KNOWS"):
    print(rel.end_node()["name"])

for rel in graph.match(rel_type="KNOWS", end_node=b):
    print('--------> start_node', rel.start_node()["name"])

for rel in graph.match(start_node=a, end_node=b):
    if rel['time'] == '201':
        print('-------=================================-> ', rel)

# relationship = graph.match(a, b)
# print(relationship)
#
# cond = ' AND '.join("p.{}={}".format(prop, value) for prop, value in d.items())
#
# query = "MATCH (p:Person) {condition} RETURN p"
# query = query.format(condition=cond)
# # "MATCH (p:Person) p.age=22 AND p.name='Alice' RETURN p"
# results = graph.cypher.execute(query)
# print(results)
