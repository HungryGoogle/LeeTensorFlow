import pickle


dic = {'age': 23, 'job': 'student'}
byte_data = pickle.dumps(dic)
# out -> b'\x80\x03}q\x00(X\x03\x00\x00\...'
print(byte_data)



obj = pickle.loads(byte_data)
print(obj)