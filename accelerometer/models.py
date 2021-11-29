
import tensorflow as tf


class ConvLSTM1D_a(tf.keras.Model):
    
    def __init__(self, input_shape):
        super(ConvLSTM1D_a, self).__init__(name="ConvLSTM1D_a")

        self.layer1 = tf.keras.layers.Bidirectional( tf.keras.layers.ConvLSTM1D(64, (3), dropout=0.4) )
        self.layer2 = tf.keras.layers.Flatten()
        self.layer3 = tf.keras.layers.Dense(1024, activation="relu")
        self.layer4 = tf.keras.layers.Dropout(0.2)
        self.layer5 = tf.keras.layers.Dense(512, activation="relu")
        self.layer6 = tf.keras.layers.Dropout(0.2)
        self.layer7 = tf.keras.layers.Dense(256, activation="relu")
        self.layer8 = tf.keras.layers.Dropout(0.2)
        self.layer9 = tf.keras.layers.Dense(20, activation="softmax")
        
    def call(self, inputs):
        x = self.layer1(inputs)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.layer6(x)
        x = self.layer7(x)
        x = self.layer8(x)
        x = self.layer9(x)
        return x
    
    def build_graph(self, input_shape):
        """use this function to initialize a graph and define the shapes when asking for summary()"""
        x = tf.keras.Input(shape=input_shape[1:], name="input")
        return tf.keras.Model(inputs=[x], outputs=self.call(x), name=self.name)