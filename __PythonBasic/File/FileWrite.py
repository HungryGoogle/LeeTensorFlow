#
#  file_obj = open("文件路径", "模式")
#
# 打开文件模式有：
# r   以只读方式打开文件
# w   打开文件只用于写入。该文件存在将其覆盖，不存在创建新文件
# a   打开一个文件用于追加。该文件存在结尾进行追加，不存在创建写入
# w+  打开一个文件写读。文件存在覆盖，不存在创建

f = open(".\\log\\test.log", "w")
f.write("this is line1\n")
f.write("this is line2\n")
f.write("this is line3\n")
f.close()

print("Write succefully.")
