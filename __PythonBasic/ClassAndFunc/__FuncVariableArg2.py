### Example_1 #################################################
def kw_dict(**kwargs):
    print(kwargs)
    return kwargs
print(kw_dict(a=1,b=2,c=3) == {'a':1, 'b':2, 'c':3})



params = {"username":"testname", "passwd":"123"}

print('----------------------------- 1 ')
kw_dict(**params)
print('----------------------------- 2 ')
print(params.items())

