"""
File :
    ---------------------------
"""


class IMyMath:
    def bar(self):
        print("   IMyMath bar() func ")
        return

    def bar2(self):
        print("   IMyMath bar2() func ")
        return

if __name__ == '__main__':
    # main()
    IMyMath().bar()
    IMyMath().bar2()
