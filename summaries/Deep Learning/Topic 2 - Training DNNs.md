# Topic 2 – Training Deep Neural Networks

## Vanishing and Exploding Gradients

Deep neural networks can be difficult to train because gradients must be backpropagated through many layers.

### Vanishing Gradients

The **vanishing gradients problem** occurs when gradients become smaller and smaller as they are propagated backward through the network.

As a result:

- Lower layers receive extremely small weight updates.
- Early layers learn very slowly or almost not at all.
- Training may converge very slowly or fail to find a good solution.

This is especially common when using activation functions such as sigmoid or tanh in deep networks, because their derivatives can become very small when the activations saturate.

### Exploding Gradients

The **exploding gradients problem** occurs when gradients become larger and larger during backpropagation.

As a result:

- Weight updates become extremely large.
- Training becomes unstable.
- The loss may fluctuate heavily or become `NaN`.

Exploding gradients are especially common in recurrent neural networks and very deep networks.

---

## Why Vanishing Gradients Happen

A common historical cause of vanishing gradients was the combination of:

- Logistic sigmoid activation functions
- Poor weight initialisation, such as sampling from `Normal(0, 1)`

This caused several problems:

- The logistic sigmoid has a mean output around `0.5`, not `0`.
- The variance of outputs could become much larger than the variance of inputs.
- Large input values cause the sigmoid function to saturate.
- When sigmoid saturates, its derivative becomes close to `0`.
- During backpropagation, these tiny derivatives multiply together, causing gradients to vanish.

---

## Activation Function Issues

### Sigmoid

The sigmoid activation function is:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Sigmoid can cause vanishing gradients because it saturates for large positive or negative values.

When this happens, the derivative becomes very small.

### ReLU

ReLU is often better for deep networks because it does not saturate for positive values.

$$
ReLU(z) = \max(0, z)
$$

However, ReLU can suffer from the **dying ReLU problem**.

This occurs when a neuron only outputs `0` because its input is always negative. If this happens, the neuron may stop learning because the gradient is also `0`.

### Leaky ReLU

Leaky ReLU helps reduce the dying ReLU problem by allowing a small gradient when the input is negative.

$$
LeakyReLU(z) = \max(\alpha z, z)
$$

where `α` is a small positive value, such as `0.01`.

---

## Weight Initialisation

Good weight initialisation helps prevent gradients from vanishing or exploding.

The goal is to keep the variance of activations and gradients roughly stable across layers.

| Initialisation | Common Activation Functions | Purpose |
|---|---|---|
| Glorot / Xavier | Tanh, sigmoid, softmax | Keeps variance stable for symmetric activations |
| He | ReLU, Leaky ReLU, ELU | Designed for ReLU-like activations |
| LeCun | SELU | Designed for self-normalising networks |

### General Rule

- Use **Glorot/Xavier initialisation** for sigmoid or tanh.
- Use **He initialisation** for ReLU and its variants.
- Use **LeCun initialisation** for SELU.

---

## Batch Normalisation

**Batch Normalisation** normalises the inputs to a layer so that they have approximately:

$$
\mu = 0
$$

and

$$
\sigma^2 = 1
$$

This helps stabilise and speed up training.

Batch Normalisation can be inserted either:

- Before the activation function
- After the activation function

If Batch Normalisation is used **before** the activation function, the layer bias is usually unnecessary because Batch Normalisation already includes a shift parameter.

### Batch Normalisation Formula

$$
\hat{x} = \frac{x - \mu}{\sigma}
$$

$$
z = \gamma \hat{x} + \beta
$$

where:

- `x` is the input.
- `μ` is the batch mean.
- `σ` is the batch standard deviation.
- `x̂` is the normalised input.
- `γ` is a trainable scaling parameter.
- `β` is a trainable shifting parameter.

### Benefits of Batch Normalisation

Batch Normalisation can:

- Reduce sensitivity to weight initialisation.
- Allow larger learning rates.
- Speed up convergence.
- Provide some regularisation effect.
- Reduce internal covariate shift.

---

## Momentum Optimisation

Momentum improves gradient descent by keeping track of previous gradients.

Instead of updating weights using only the current gradient, momentum uses a moving average of past gradients.

This helps the optimiser build speed in consistent directions and reduce oscillations.

### Momentum Update

$$
m = \beta m - \eta \nabla_\theta J(\theta)
$$

$$
\theta = \theta + m
$$

where:

- `m` is the momentum vector.
- `β` controls how much past momentum is retained.
- `η` is the learning rate.
- `∇θ J(θ)` is the gradient of the loss function.
- `θ` represents the model parameters.

A common value for `β` is `0.9`.

---

## Nesterov Accelerated Gradient

**Nesterov Accelerated Gradient**, or **NAG**, is a variant of momentum.

Standard momentum calculates the gradient at the current parameter position.

Nesterov momentum calculates the gradient slightly ahead in the direction of the current momentum.

Instead of calculating the gradient at:

$$
\theta
$$

Nesterov calculates it at:

$$
\theta + \beta m
$$

This gives the optimiser a "look-ahead" ability.

### Benefit

Nesterov momentum often converges faster and more accurately than standard momentum because it can correct its direction earlier.

---

## AdaGrad

**AdaGrad** is an adaptive learning rate optimisation algorithm.

It gives each parameter its own learning rate based on the history of its gradients.

### Key Idea

Parameters with large gradients get smaller learning rates, while parameters with small gradients get relatively larger learning rates.

This is useful when features have very different scales or when dealing with sparse data.

### Disadvantage

AdaGrad can reduce the learning rate too aggressively.

Over time, the accumulated squared gradients become very large, causing the learning rate to become extremely small.

As a result, training may stop too early, especially in neural networks.

---

## RMSProp

**RMSProp** improves AdaGrad by preventing the learning rate from shrinking too quickly.

Instead of accumulating all past squared gradients, RMSProp only keeps an exponentially decaying average of recent squared gradients.

### Key Idea

RMSProp remembers recent gradients more strongly than older gradients.

This allows the optimiser to keep learning for longer.

A common decay rate is:

$$
\rho = 0.9
$$

### Benefit

RMSProp works well for training neural networks because it avoids AdaGrad's problem of stopping too early.

---

## Adam

**Adam** stands for **Adaptive Moment Estimation**.

It combines ideas from:

- Momentum
- RMSProp

Adam keeps track of:

- The exponentially decaying average of past gradients.
- The exponentially decaying average of past squared gradients.

### Key Idea

Adam estimates both the mean and variance of the gradients.

It uses:

- `m` for the first moment, similar to momentum.
- `s` for the second moment, similar to RMSProp.

### Adam Parameters

Adam commonly uses:

$$
\beta_1 = 0.9
$$

$$
\beta_2 = 0.999
$$

where:

- `β₁` controls the decay rate for the moving average of gradients.
- `β₂` controls the decay rate for the moving average of squared gradients.

### Bias Correction

Adam applies bias correction because `m` and `s` are initialised at zero.

$$
\hat{m} = \frac{m}{1 - \beta_1^t}
$$

$$
\hat{s} = \frac{s}{1 - \beta_2^t}
$$

where `t` is the current training step.

### Benefit

Adam is often a strong default optimiser because it is fast, adaptive, and usually works well without much tuning.

---

## Adam Variants

### AdaMax

AdaMax is a variant of Adam based on the infinity norm.

It can be more stable in some cases.

### Nadam

Nadam combines Adam with Nesterov momentum.

It adds the look-ahead behaviour of Nesterov Accelerated Gradient to Adam.

### AdamW

AdamW modifies Adam by decoupling weight decay from the gradient update.

This usually gives better regularisation than standard Adam with L2 regularisation.

AdamW reduces model weights during each training iteration, helping prevent overfitting.

---

## Learning Rate Scheduling

The learning rate controls how large each weight update is during training.

Choosing a good learning rate is important because:

- If the learning rate is too high, training may diverge or fail to converge.
- If the learning rate is too low, training may be very slow.
- If the learning rate is adjusted during training, the model may converge faster and reach a better solution.

Learning rate scheduling changes the learning rate as training progresses.

---

## Common Learning Rate Schedules

### Piecewise Constant Scheduling

The learning rate is kept constant for a period of time, then reduced at set steps.

Example:

```text
Epochs 1–10:   learning rate = 0.1
Epochs 11–20:  learning rate = 0.01
Epochs 21–30:  learning rate = 0.001
```
### Power Scheduling

Power scheduling gradually decreases the learning rate over time.

A common form is:

$$
\eta(t) = \frac{\eta_0}{(1 + t/s)^c}
$$

where:

- `η(t)` is the learning rate at step `t`.
- `η₀` is the initial learning rate.
- `s` controls how quickly the learning rate decays.
- `c` is the power value.

---

## Regularisation

Regularisation is used to reduce overfitting by limiting how complex the model can become.

Regularisation methods add constraints or penalties during training so the model does not rely too heavily on specific weights or features.

---

## L1 and L2 Regularisation

L1 and L2 regularisation constrain neural network weights during training.

### L1 Regularisation

L1 regularisation adds a penalty based on the absolute value of the weights.

$$
L1 = \lambda \sum_i |w_i|
$$

L1 regularisation can encourage **sparsity**, meaning some weights may become exactly zero.

This can be useful when you want the model to ignore less important features.

### L2 Regularisation

L2 regularisation adds a penalty based on the squared value of the weights.

$$
L2 = \lambda \sum_i w_i^2
$$

L2 discourages very large weights and usually produces smoother models.

It is also commonly referred to as **weight decay**, although in optimisers like AdamW, weight decay is implemented slightly differently from standard L2 regularisation.

---

## Dropout

Dropout is a regularisation technique where some neurons are randomly ignored during training.

Each neuron has a probability of being temporarily dropped.

### Key Idea

During each training step:

- A random subset of neurons is turned off.
- The network cannot rely too heavily on any one neuron.
- This encourages the network to learn more robust features.
- The model behaves like an ensemble of many smaller neural networks.

### Benefit

Dropout helps reduce overfitting and improves generalisation.

At inference time, dropout is turned off and all neurons are used.

---

## Quick Optimiser Comparison

| Optimiser | Main Idea | Strength | Weakness |
|---|---|---|---|
| Gradient Descent | Uses current gradient only | Simple and stable | Can be slow |
| Momentum | Uses moving average of gradients | Speeds up training and reduces oscillation | Requires tuning momentum parameter |
| Nesterov Momentum | Looks ahead before calculating gradient | Often more accurate than standard momentum | Slightly more complex |
| AdaGrad | Adaptive learning rate per parameter | Good for sparse data | Learning rate may shrink too much |
| RMSProp | Uses recent squared gradients | Avoids AdaGrad stopping too early | Requires decay rate tuning |
| Adam | Combines Momentum and RMSProp | Strong default optimiser | Can sometimes generalise worse than SGD |
| AdamW | Adam with decoupled weight decay | Better regularisation than Adam | Still requires tuning weight decay |

---
