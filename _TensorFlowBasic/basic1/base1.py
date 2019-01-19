import tensorflow as tf


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.constant(6.0)
d = tf.multiply(a, b)
y = tf.multiply(d, c)

with tf.Session() as sess:
    print(sess.run(y, feed_dict={a: 3.0, b: 3.0}))

    A = [[1.1, 2.3], [3.4, 4.1]]
    Y = tf.matrix_inverse(A)
    print(sess.run(Y))

    sess.close()