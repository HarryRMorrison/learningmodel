# Topic 1 – Multilayer Perceptrons (MLPs)

## Huber Loss

Huber loss is a regression loss function that combines the strengths of **Mean Squared Error (MSE)** and **Mean Absolute Error (MAE)**.

- For **small errors**, Huber loss behaves like **MSE**.
  - This makes it sensitive to small differences and encourages precise predictions.
- For **large errors**, Huber loss behaves like **MAE**.
  - This makes it more robust to outliers than MSE.

In other words, Huber loss is useful when the dataset may contain outliers, because it does not punish large errors as harshly as MSE.

---

## Overfitting

Overfitting occurs when a model learns the training data too well, including noise or random patterns that do not generalise to unseen data.

### Signs of Overfitting

A common sign of overfitting is:

- Training accuracy is high
- Validation accuracy is much lower
- Training loss continues decreasing while validation loss stops improving or increases

This means the model performs well on the training set but poorly on new data.

### How to Reduce Overfitting

Overfitting can be reduced by:

- Reducing model complexity
  - Use fewer layers or fewer neurons.
- Adding regularisation
  - For example, L1 or L2 regularisation.
- Using dropout
  - Randomly disables some neurons during training.
- Using early stopping
  - Stop training when validation performance stops improving.
- Using data augmentation
  - Create varied versions of the training data.
- Collecting more training data
  - More data can help the model generalise better.
- Using a smaller learning rate
  - This may help the model converge more smoothly, although it can increase training time.
- Adjusting batch size
  - Smaller batch sizes can add noise to training, which sometimes improves generalisation.

---

## Underfitting

Underfitting occurs when a model is too simple to capture the underlying patterns in the data.

### Signs of Underfitting

A common sign of underfitting is:

- Training accuracy is low
- Validation accuracy is also low
- Both training and validation loss remain high

This means the model has not learned the training data well enough.

### How to Reduce Underfitting

Underfitting can be reduced by:

- Increasing model complexity
  - Add more layers or more neurons.
- Training for longer
  - The model may not have had enough time to learn.
- Reducing excessive regularisation
  - Too much regularisation can prevent the model from learning.
- Tuning the learning rate
  - If the learning rate is too high, the model may fail to converge.
  - If the learning rate is too low, training may be extremely slow.
- Trying a different optimiser
  - For example, Adam may converge faster than basic gradient descent.
- Trying different activation functions
  - For example, ReLU or Leaky ReLU may work better than sigmoid in deeper networks.
- Improving the input features
  - Feature engineering or better preprocessing may help the model learn useful patterns.

---

## Quick Comparison

| Issue | What Happens | Common Signs | Possible Fixes |
|---|---|---|---|
| Overfitting | Model learns noise in the training data | High training accuracy, lower validation accuracy | Regularisation, dropout, early stopping, data augmentation, reduce complexity |
| Underfitting | Model is too simple or poorly trained | Low training accuracy and low validation accuracy | Increase complexity, train longer, tune learning rate, improve features |
