# Method
class FooParent:
    def bar(self, message):
        print("Parent method: " + message)
FooParent().bar("Hello, World.")

# Method
class FooChild1(FooParent):
    def bar(self, message):
        print("Child  method: " + message)
FooChild1().bar("Hello, child 1.")

# Method
class FooChild2(FooParent):
    def bar(self, message):
        super(FooChild2, self).bar("child2 call parent : " + message)
FooChild2().bar("Hello, World.")