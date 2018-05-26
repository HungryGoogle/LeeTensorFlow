### Example_1 #################################################

### Example_2 #################################################
def testArg(city,name,*,age = 10,job):
    print("city = " + city)
    print("name = " + name)
    print("city = " + city)
    print("age = " + age)
    print("job = " + job)


testArg('beijin', 'wfp', age='25', job='hoker')
### Example_3 #################################################
def total(a = 5, *numbers, **phonebook):
    print('a =', a)

    # 遍历元组中的所有项目
    print("\nsingle_item --------");
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    print("\nphonebook -------- phonebook = ", phonebook);
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
        # print ('Optional argument %s = %s' % (first_part, second_part))
        print('hello')


print("\n--------------------------------------------------------");
print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

#
# ### Example_4 #################################################
# # Use *args
# args = [1, 2, 3, 4, 5]
# def test_args(*args):
#     # print(args)
#     return
#
# kwargs = {
#     'first': 1,
#     'second': 2,
#     'third': 3,
#     'fourth': 4,
#     'fifth': 5
# }
#
# test_args(*kwargs)



# ### Example_5 #################################################
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字 参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print("\nf1 --------------------------------------------------------");
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    print("args.__len__()",args.__len__())
    print("kw.__len__()",kw.__len__())

def f2(a, b, c=0, *, d, **kw):
    print("\nf2 --------------------------------------------------------");
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print("\n--------------------------------------------------------");
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99, Y=99, Z=99)

f2(1, 2, d=99, ext=None)

print("\nkey value --------------------------------------------------------");
kw = {'Z': 99, 'x': 99, 'Y': 99}
print('kw =', kw)
print('kw.items =', kw.items())
