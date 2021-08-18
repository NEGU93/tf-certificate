import tensorflow as tf
import tensorflow_datasets as tfds
from pdb import set_trace

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0


def _get_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    model.add(tf.keras.layers.Dense(300, activation="relu"))
    model.add(tf.keras.layers.Dense(100, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))

    model.compile(loss=tf.losses.sparse_categorical_crossentropy, optimizer=tf.optimizers.SGD(), metrics=["accuracy"])

    return model


def get_model_and_history_example():
    model = _get_model()
    history = model.fit(x=x_train, y=y_train, epochs=30, validation_data=(x_test, y_test), verbose=0)
    return model, history

