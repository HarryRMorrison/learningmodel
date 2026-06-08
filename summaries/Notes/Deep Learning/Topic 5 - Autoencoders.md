# Topic 5 – Autoencoders

## Autoencoders

An **autoencoder** is a neural network trained to reconstruct its input.

It learns a compressed or useful representation of the input data without needing labelled examples.

This makes autoencoders a form of **unsupervised learning**.

---

## Key Idea

An autoencoder tries to learn a function that maps an input back to itself:

$$
x \rightarrow \hat{x}
$$

where:

- $x$ is the original input.
- $\hat{x}$ is the reconstructed output.

The goal is for $\hat{x}$ to be as close as possible to $x$.

---

## Autoencoder Structure

An autoencoder has two main parts:

1. **Encoder**
2. **Decoder**

The encoder compresses the input into a smaller representation.

The decoder uses that representation to reconstruct the original input.

---

## Encoder

The **encoder** maps the input data into a latent representation, also called a coding.

$$
x \rightarrow z
$$

where:

- $x$ is the input.
- $z$ is the latent representation.

The latent representation captures the most important information from the input.

---

## Latent Representation

The **latent representation** is the compressed internal representation learned by the autoencoder.

It is also called:

- A coding
- A bottleneck representation
- A feature representation
- An embedding

This representation is usually lower-dimensional than the original input.

For example, an image with thousands of pixels may be compressed into a much smaller vector.

---

## Decoder

The **decoder** maps the latent representation back to the original input space.

$$
z \rightarrow \hat{x}
$$

where:

- $z$ is the latent representation.
- $\hat{x}$ is the reconstructed output.

The decoder tries to reconstruct the original input as accurately as possible.

---

## Autoencoder Pipeline

A basic autoencoder can be represented as:

$$
\text{Input} \rightarrow \text{Encoder} \rightarrow \text{Latent Representation} \rightarrow \text{Decoder} \rightarrow \text{Reconstruction}
$$

or:

$$
x \rightarrow z \rightarrow \hat{x}
$$

---

## Training Objective

The autoencoder is trained to minimise the difference between the input and the reconstructed output.

This difference is called the **reconstruction loss**.

Common reconstruction losses include:

### Mean Squared Error

Used when the input values are continuous, such as normalised pixel values.

$$
L = ||x - \hat{x}||^2
$$

### Binary Cross-Entropy

Used when the input values are binary or represent probabilities.

---

## Why Autoencoders Are Useful

Autoencoders are useful because they can:

- Learn efficient representations of data.
- Reduce dimensionality.
- Detect important features.
- Remove noise from data.
- Compress data.
- Generate new data in some cases.
- Support unsupervised pretraining.

---

## Autoencoders as Feature Detectors

Autoencoders can act as **feature detectors**.

Because the model must reconstruct the input, it needs to learn the most useful patterns in the data.

For example, an autoencoder trained on images may learn features such as:

- Edges
- Corners
- Shapes
- Textures
- Object parts

These learned features can then be useful for other tasks.

---

## Undercomplete Autoencoders

An **undercomplete autoencoder** has a latent representation with lower dimensionality than the input.

This creates a bottleneck.

For example:

$$
\text{Input dimension} = 1000
$$

$$
\text{Latent dimension} = 50
$$

Because the latent representation is smaller, the model cannot simply copy the input.

Instead, it must learn the most important features.

### Benefit

Undercomplete autoencoders are useful for:

- Dimensionality reduction
- Compression
- Feature learning

---

## Overcomplete Autoencoders

An **overcomplete autoencoder** has a latent representation with equal or higher dimensionality than the input.

For example:

$$
\text{Input dimension} = 100
$$

$$
\text{Latent dimension} = 200
$$

This can be risky because the model may simply learn to copy the input without learning useful features.

To make overcomplete autoencoders useful, extra constraints are usually needed.

Examples include:

- Sparsity constraints
- Denoising
- Dropout
- Regularisation

---

## Autoencoders Are Usually Nonlinear

Autoencoders are usually **nonlinear** because they use activation functions in the encoder and decoder.

This means they can learn more complex representations than linear methods such as PCA.

For example, using activation functions such as ReLU, sigmoid, or tanh allows the autoencoder to learn nonlinear mappings.

---

## Relationship Between Autoencoders and PCA

**Principal Component Analysis**, or **PCA**, is a linear dimensionality reduction method.

A simple autoencoder with:

- One hidden layer
- Linear activations
- Mean squared error loss

can learn a similar subspace to PCA.

However, standard neural network autoencoders are usually more flexible than PCA because they can use nonlinear activation functions.

---

## PCA

PCA reduces dimensionality by finding directions of maximum variance in the data.

It does not use nonlinear activation functions.

### Key Point

PCA is a **linear** dimensionality reduction method.

This means it works well when the important structure in the data is approximately linear.

---

## t-SNE

**t-SNE**, or **t-distributed Stochastic Neighbor Embedding**, is a nonlinear dimensionality reduction method.

It is commonly used to visualise high-dimensional data in two or three dimensions.

For example, t-SNE can map high-dimensional image embeddings into a 2D plot where similar images appear close together.

### Key Point

t-SNE is mainly used for **visualisation**, not usually for general-purpose compression or reconstruction.

---

## Stacked Autoencoders

A **stacked autoencoder** is a deep autoencoder with multiple layers in the encoder and decoder.

Instead of having only one hidden layer, it has several hidden layers.

This allows the model to learn more complex hierarchical representations.

---

## Stacked Autoencoder Structure

A stacked autoencoder may look like:

$$
\text{Input} \rightarrow h_1 \rightarrow h_2 \rightarrow z \rightarrow h_3 \rightarrow h_4 \rightarrow \text{Output}
$$

where:

- $h_1$ and $h_2$ are encoder hidden layers.
- $z$ is the latent representation.
- $h_3$ and $h_4$ are decoder hidden layers.

---

## Unsupervised Pretraining Using Stacked Autoencoders

Stacked autoencoders can be used for **unsupervised pretraining**.

The general process is:

1. Train an autoencoder on unlabelled data.
2. Keep the encoder part.
3. Add a supervised output layer on top.
4. Fine-tune the full model on labelled data.

This can be useful when labelled data is limited but unlabelled data is available.

---

## Tying Weights

**Tying weights** means using the same weights for the encoder and decoder, but transposed.

If the encoder uses weight matrix $W$, then the decoder uses:

$$
W^T
$$

This reduces the number of trainable parameters.

---

## Benefits of Tying Weights

Tying weights can:

- Halve the number of weights.
- Reduce the risk of overfitting.
- Speed up training.
- Encourage symmetry between the encoder and decoder.

---

## Autoencoders as Generative Models

Some autoencoders can be used as **generative models**.

A generative model can create new data samples that resemble the training data.

However, basic autoencoders are not always strong generative models because their latent space may not be smooth or well-structured.

Variational autoencoders are better suited for generation because they learn a probabilistic latent space.

---

## Topic Summary

Autoencoders are neural networks trained to reconstruct their inputs.

Key ideas include:

- Autoencoders learn latent representations without labels.
- The encoder compresses the input into a coding.
- The decoder reconstructs the input from the coding.
- Undercomplete autoencoders use a smaller latent space.
- Overcomplete autoencoders use a larger latent space and need extra constraints.
- Autoencoders are usually nonlinear because they use activation functions.
- PCA is a linear dimensionality reduction method.
- t-SNE is mainly used for visualising high-dimensional data.
- Stacked autoencoders are deep autoencoders.
- Stacked autoencoders can be used for unsupervised pretraining.
- Tying weights reduces parameters by sharing encoder and decoder weights.