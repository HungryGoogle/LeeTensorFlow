### Example_1 #################################################
def fun1(a, b):
    """
    :param a:
    :param b:
    :return: return sum (a, b)
    """
    return a + b


print("a + b = %d" % (fun1(2, 3)))


### Example_2 #################################################
def fun2(a):
    """
    :param a: 输入整数或long类型
    """
    a += 1
    return a


print("a = 2; a += 1,result = %d" % (fun2(2)))


