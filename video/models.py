
import tensorflow as tf

class ConvLSTM2D_a(tf.keras.Model):
    
    
    def __init__(self, input_shape):
        super(ConvLSTM2D_a, self).__init__(name="ConvLSTM2D_a")
        
        self.layer1 = tf.keras.layers.ConvLSTM2D(filters=32, kernel_size=[2,3], strides=(4,4), data_format="channels_last")
        self.layer2 = tf.keras.layers.Flatten()
        self.layer3 = tf.keras.layers.Dense(1024)
        self.layer4 = tf.keras.layers.Dense(256)
        self.layer5 = tf.keras.layers.Dense(6, activation="softmax")
        
    def call(self, inputs):
        x = self.layer1(inputs)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        return x
        
    def build_graph(self, input_shape):
        """use this function to initialize a graph and define the shapes when asking for summary()"""
        x = tf.keras.Input(shape=input_shape[1:], name="input")
        return tf.keras.Model(inputs=[x], outputs=self.call(x), name=self.name)