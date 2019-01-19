import tensorflow as tf

state=tf.Variable(0,name='counter')
# print(state.name)
# 变量+常量=变量
one=tf.constant(1)
new_value=tf.add(state,one)
#将state用new_value代替
updata=tf.assign(state,new_value)

#变量必须要激活
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(updata)
        print(sess.run(state))