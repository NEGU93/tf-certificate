# Classification

**Binary classification:**
   - Can have several values to one.
   - Example: if a mail is spam or not AND if is urgent or not.
   - Output layer: Logistic (ex. sigmoid)

**Multi-class classification**
   - Can have only one value, classes are exclusive
   - Output layer: Softmax


## Loss functions

| Labels   |      Example      | function |
|----------|:-------------:|------:|
| sparse |  3 | sparse_categorical_crossentropy |
| one-hot encoded vectors |    [0, 0, 1, 0, 0]  | categorical_crossentropy |
| binary classification | [1, 1, 0] | binary_crossentropy |

# Regression

| Hyperparameter   |      Typical value      |
|----------|:-------------:|
| Hidden act |  ReLU (or SeLU) |
| Output act |  None, ReLU/Softplus (if positive outputs), tanh/logistic (if bounded outputs) |
| Loss function |  MSE or MAE (if outliers) |