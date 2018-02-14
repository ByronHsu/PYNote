# Tensorflow

### 基本操作
[code](./tfcode/ex2.py)

```py
# 建模
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = Weights*x_data + biases
# 計算誤差
loss = tf.reduce_mean(tf.square(y-y_data))
# 傳播誤差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
# 初始化
init = tf.global_variables_initializer()
# 訓練
sess = tf.Session()
sess.run(init)
for step in range(201):
    sess.run(train)
```

### Session會話控制
[code](./tfcode/sess-control.py)

Session 是 Tensorflow 为了控制,和输出文件的执行的语句. 运行 session.run() 可以获得

1. 你要得知的运算结果 ``sess.run(Weights)``
2. 你所要运算的部分 ``sess.run(train)``

### Variable變量
[code](./tfcode/var.py)

```py
# 定义常量
state = tf.Variable(0, name='counter')
one = tf.constant(1)
# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)
# 将 State 更新成 new_value
update = tf.assign(state, new_value)
# 如果定义 Variable, 就一定要 initialize
init = tf.global_variables_initializer()
 
# 使用 Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
```

### Placeholder傳入值
[code](./tfcode/placeholder.py)

```py
import tensorflow as tf

#在 Tensorflow 中需要定义 placeholder 的 type ，一般为 float32 形式
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# mul = multiply 是将input1和input2 做乘法运算，并输出为 output 
ouput = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(ouput, feed_dict={input1: [7.], input2: [2.]}))
# [ 14.]

```