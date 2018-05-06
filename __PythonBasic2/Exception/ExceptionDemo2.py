



def func1():
    s = input("input your age:")
    if s == "":
        raise Exception("input must not be empty.")

    try:
        i = int(s)
    except Exception as err:
        print(err)
    finally:
        print("Goodbye func!")


try:
    func1()
except Exception as err:
    print(err)
finally:
    print("Goodbye main!")
