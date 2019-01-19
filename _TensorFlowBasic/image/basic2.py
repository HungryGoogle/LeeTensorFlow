import tensorflow as tf
import matplotlib.pyplot as plt

# https://blog.csdn.net/White_Idiot/article/details/78825341


# 读取图像的原始数据
image_raw_data = tf.gfile.FastGFile('pic/lena512_512.jpg', 'rb').read()


# 使用pyplot显示图像
def show(img_data):
    plt.imshow(img_data.eval())
    plt.show()


with tf.Session() as sess:
    # 将原始数据解码成多维矩阵
    img_data = tf.image.decode_jpeg(image_raw_data)
    # print(img_data.eval())
    show(img_data)

    resized = tf.image.resize_images(img_data, [300, 300], method=1)
    print(resized.get_shape())  # 图像深度没有显式指定则为问号
    show(resized)

    # 将图像的矩阵编码成图像并存入文件
    encoded_image = tf.image.encode_jpeg(resized)
    with tf.gfile.GFile('pic/output.jpg', 'wb') as f:
        f.write(encoded_image.eval())

    # 将图像数据的类型转为实数类型，便于对图像进行处理
    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)
