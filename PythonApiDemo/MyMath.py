"""
File :
    ---------------------------
"""
from PythonApiDemo.IMyMath import IMyMath


class MyMath(IMyMath):
    def bar(self):
        return IMyMath.bar(MyMath)


    def bar2(self):
        return IMyMath.bar2(MyMath)


if __name__ == '__main__':
    MyMath().bar()
    MyMath().bar2()
