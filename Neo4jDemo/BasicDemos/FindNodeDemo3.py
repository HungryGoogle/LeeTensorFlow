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
d = Node('Person', name='Jim', age=21, location='杭州')

a.setdefault('time','---2018---')
a['time1'] = '---2018_1---'
print(a)
print(a['time1'] )


r1 = Relationship(a, 'KNOWS', b)
r2 = Relationship(b, 'KNOWS', c)
r3 = Relationship(b, 'KNOWS', d)

r2.setdefault("time","198708")
r1['time']='2018'
graph.create(a)
graph.create(r1)
graph.create(r2)
graph.create(r3)


# 参考 https://blog.csdn.net/free8666/article/details/52909523
# result = graph.run('Match (p:Person) RETURN p ')
# print(list(result))

result = graph.run('Match (start:Person{name:\'Alice\'})-[:KNOWS*1..1]->(end:Person) return end')
print(list(result))

result = graph.run('Match (start:Person{name:\'Alice\'})-[:KNOWS*2..2]->(end:Person) return end')
print(list(result))
