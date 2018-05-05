class A:
    def __init__(self):
        self.name = 'leewen'

    # self.age='24'
    def method(self): {
        print("method print")
    }



Instance = A()
print(getattr(Instance , 'name', 'not find')) #如果Instance 对象中有属性name则打印self.name的值，否则打印'not find'
print(getattr(Instance , 'age', 'not find')) #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'
print(getattr(Instance, 'method', 'no func')) #如果有方法method，否则打印其地址，否则打印no func
print(getattr(Instance, 'method', 'no func')())#如果有方法method，运行函数并打印None否则打印no func

# https://www.cnblogs.com/vipchenwei/p/6991209.html
# 2. hasattr(object, name)
#     说明：判断对象object是否包含名为name的特性（hasattr是通过调用getattr(ojbect, name)是否抛出异常来实现的）
#
# 3. setattr(object, name, value)
#     这是相对应的getattr()。参数是一个对象,一个字符串和一个任意值。字符串可能会列出一个现有的属性或一个新的属性。这个函数将值赋给属性的。该对象允许它提供。例如,setattr(x,“foobar”,123)相当于x.foobar = 123。
#
# 4. delattr(object, name)
#     与setattr()相关的一组函数。参数是由一个对象(记住python中一切皆是对象)和一个字符串组成的。string参数必须是对象属性名之一。该函数删除该obj的一个由string指定的属性。delattr(x, 'foobar')=del x.foobar

# 判断某个函数或者变量是否存在
r = hasattr(Instance,'name')
print( r)

# 给commons模块增加一个全局变量age = 18，创建成功返回none
setattr(Instance,'age',18)
print(getattr(Instance , 'age', 'not find')) #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'

#  给模块添加一个函数
setattr(Instance,'age',lambda  a:a+1)

#  删除模块中某个变量或者函数
delattr(Instance,'age')