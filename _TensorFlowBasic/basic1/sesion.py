import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])
# matrix multiply
# np.dot(m1,m2)
product = tf.matmul(matrix1, matrix2)

# # method 1
# sess = tf.Session()  # Session是一个object，首字母要大写
# # 只有sess.run()之后，tensorflow才会执行一次
# result = sess.run(product)
# print(result)
# # close 不影响，会显得更整洁
# sess.close()

# method 2
# with 可以自己关闭会话
with tf.Session() as sess:

    result2 = sess.run(product)
    print(result2)
    sess.close()