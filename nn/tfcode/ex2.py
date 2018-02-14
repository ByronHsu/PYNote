import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# create tf structure start #
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

# create tensorflow structure end #
sess = tf.Session()
sess.run(init) 

for step in range(201):
   sess.run(train)
   if step % 20 == 0:
      print(step, sess.run(Weights), sess.run(biases))

# result
# 0 [-0.3298871] [0.6988347]
# 20 [-0.04082211] [0.37214875]
# 40 [0.06052463] [0.32022482]
# 60 [0.08893425] [0.30566946]
# 80 [0.09689804] [0.30158928]
# 100 [0.09913047] [0.30044553]
# 120 [0.09975626] [0.30012488]
# 140 [0.09993168] [0.300035]
# 160 [0.09998084] [0.30000985]
# 180 [0.09999464] [0.30000275]
# 200 [0.09999852] [0.3000008]