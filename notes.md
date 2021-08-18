# Task objective

## Classification

**Binary classification:**
   - Can have several values to one.
   - Example: if a mail is spam or not AND if is urgent or not.
   - Output layer: Logistic (ex. sigmoid)

**Multi-class classification**
   - Can have only one value, classes are exclusive
   - Output layer: Softmax


### Loss functions

| Labels   |      Example      | function |
|----------|:-------------:|------:|
| sparse |  3 | sparse_categorical_crossentropy |
| one-hot encoded vectors |    [0, 0, 1, 0, 0]  | categorical_crossentropy |
| binary classification | [1, 1, 0] | binary_crossentropy |

- To convert sparse into one-hot: [`tf.keras.utils.to_categorical()`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical)
- To convert one-hot to sparse: `np.argmax(axis=-1)`

## Regression

| Hyperparameter   |      Typical value      |
|----------|:-------------:|
| Hidden act |  ReLU (or SeLU) |
| Output act |  None, ReLU/Softplus (if positive outputs), tanh/logistic (if bounded outputs) |
| Loss function |  MSE or MAE (if outliers) |

# APIs

- Sequential API
- Functional API
   - Good for using multiple input/outputs or *skip connections*
- Subclassing API
   - Good for doing if/loops inside `call()` method

# Optimizing result

- Input Normalization
- BN (almost compulsory)

Initialization:

| Initializaiton   |      Activation Function      |
|----------|:-------------:|
| Glorot |  None, tanh, logistic, softmax |
| He |  ReLU and variants |
| LeCun | SeLU |

Choosing hyper-parameters tips:
- In general, make deeper and not bigger
- Learning rate: Use the swipe of learning rates
- Try changing ReLU to LeakyReLU or ELU

Overfitting:
- EarlyStopping
- Dropout
- BN

Exploding Gradient:
- Glorot/He init
- BN

