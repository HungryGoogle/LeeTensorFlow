import os


# if os.path.isfile('autojump.png'):
try:
    print('os.remove file')
    os.remove('autojump.png')
except Exception:
    print('Exception 1')
    pass

# print('Exception 2')
print('after Exception 3')
