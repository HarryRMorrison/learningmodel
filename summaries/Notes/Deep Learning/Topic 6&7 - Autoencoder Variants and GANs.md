# Topic 6 & 7 – Convolutional Autoencoders, Denoising Autoencoders, Variational Autoencoders, and GANs

## Convolutional Autoencoders

A **convolutional autoencoder** is an autoencoder designed for image data.

Instead of using only fully connected layers, it uses convolutional layers in the encoder and decoder.

This makes convolutional autoencoders especially useful for images because they preserve spatial structure.

---

## Why Use Convolutional Autoencoders for Images?

Images contain spatial relationships between nearby pixels.

Convolutional autoencoders are useful because they:

- Preserve spatial information.
- Learn local image patterns.
- Use fewer parameters than fully connected autoencoders.
- Learn hierarchical visual features.
- Are better suited to image reconstruction tasks.

---

## Convolutional Autoencoder Structure

A convolutional autoencoder has two main parts:

1. **Encoder**
2. **Decoder**

The encoder compresses the image into a latent representation.

The decoder reconstructs the image from the latent representation.

---

## Encoder

The encoder is usually a regular CNN.

It may contain:

- Convolutional layers
- Activation functions, such as ReLU
- Pooling layers or strided convolutions

The encoder gradually reduces the spatial dimensions of the image while increasing the depth of the feature maps.

For example:

$$
64 \times 64 \times 3 \rightarrow 32 \times 32 \times 32 \rightarrow 16 \times 16 \times 64 \rightarrow z
$$

where $z$ is the latent representation.

---

## Decoder

The decoder reverses the process of the encoder.

It takes the compressed latent representation and reconstructs the original image.

The decoder may use:

- Transposed convolutional layers
- Upsampling layers
- Convolutional layers
- Activation functions

The goal is to upscale the latent representation back to the original image dimensions.

For example:

$$
z \rightarrow 16 \times 16 \times 64 \rightarrow 32 \times 32 \times 32 \rightarrow 64 \times 64 \times 3
$$

---

## Transposed Convolutions

A **transposed convolution** is often used in the decoder to increase the spatial size of feature maps.

It is sometimes called a **deconvolution**, although this term is not technically precise.

Transposed convolutions learn how to upsample feature maps during training.

They are commonly used in:

- Convolutional autoencoders
- Image generation
- Semantic segmentation
- GAN generators

---

## Convolutional Autoencoder Pipeline

A convolutional autoencoder can be represented as:

$$
\text{Image} \rightarrow \text{Convolutional Encoder} \rightarrow \text{Latent Representation} \rightarrow \text{Convolutional Decoder} \rightarrow \text{Reconstructed Image}
$$

---

## Denoising Autoencoders

A **denoising autoencoder** is trained to reconstruct a clean input from a corrupted or noisy version of that input.

The model receives a noisy input, but the target output is the original noise-free input.

---

## Key Idea

Instead of training the autoencoder to simply copy the input, we deliberately add noise to the input.

The model must learn useful features that allow it to recover the original data.

This forces the autoencoder to learn more robust representations.

---

## Denoising Autoencoder Pipeline

A denoising autoencoder works as follows:

$$
\text{Original Input} \rightarrow \text{Add Noise} \rightarrow \text{Noisy Input} \rightarrow \text{Autoencoder} \rightarrow \text{Reconstructed Clean Input}
$$

or:

$$
x \rightarrow \tilde{x} \rightarrow \hat{x}
$$

where:

- $x$ is the original clean input.
- $\tilde{x}$ is the noisy input.
- $\hat{x}$ is the reconstructed output.

---

## Types of Noise

Common types of noise include:

### Gaussian Noise

Gaussian noise adds random values sampled from a normal distribution.

$$
\tilde{x} = x + \epsilon
$$

where:

$$
\epsilon \sim N(0, \sigma^2)
$$

### Dropout Noise

Dropout noise randomly sets some input values to zero.

This forces the model to reconstruct missing information from the remaining features.

### Masking Noise

Masking noise hides or removes parts of the input.

For images, this might mean blacking out some pixels or patches.

---

## Why Denoising Autoencoders Are Useful

Denoising autoencoders are useful because they:

- Learn robust features.
- Reduce overfitting.
- Can remove noise from images or signals.
- Avoid learning a simple identity function.
- Improve the quality of learned latent representations.

---

## Variational Autoencoders

A **Variational Autoencoder**, or **VAE**, is a probabilistic generative model.

Unlike a standard autoencoder, which maps an input to a fixed latent vector, a VAE maps an input to a probability distribution in latent space.

The model then samples from this distribution to generate or reconstruct data.

---

## Key Idea of VAEs

A VAE learns a structured latent space.

Instead of encoding an input as a single point $z$, the encoder outputs parameters of a probability distribution.

Usually, this distribution is a Gaussian distribution.

The encoder outputs:

- A mean vector, $\mu$
- A log variance vector, $\log(\sigma^2)$

A latent vector $z$ is then sampled from this distribution.

---

## VAE Encoder

The VAE encoder takes an input $x$ and outputs:

$$
\mu
$$

and

$$
\log(\sigma^2)
$$

These define the approximate latent distribution:

$$
q(z|x)
$$

Usually:

$$
q(z|x) = N(\mu, \sigma^2)
$$

---

## Sampling in a VAE

The VAE samples a latent vector $z$ from the learned distribution.

However, direct random sampling makes gradient-based training difficult.

To solve this, VAEs use the **reparameterisation trick**.

---

## Reparameterisation Trick

The reparameterisation trick rewrites the sampling operation as:

$$
z = \mu + \sigma \odot \epsilon
$$

where:

- $z$ is the sampled latent vector.
- $\mu$ is the mean vector.
- $\sigma$ is the standard deviation vector.
- $\epsilon$ is random noise sampled from a standard normal distribution.
- $\odot$ means element-wise multiplication.

The noise term is sampled as:

$$
\epsilon \sim N(0, I)
$$

This allows gradients to flow through $\mu$ and $\sigma$ during backpropagation.

---

## VAE Decoder

The decoder takes the sampled latent vector $z$ and reconstructs the input.

$$
z \rightarrow \hat{x}
$$

where:

- $z$ is the latent vector.
- $\hat{x}$ is the reconstructed output.

The decoder learns to generate data samples from points in the latent space.

---

## VAE Loss Function

The VAE loss has two main parts:

1. **Reconstruction loss**
2. **KL divergence loss**

The total loss is:

$$
\text{VAE Loss} = \text{Reconstruction Loss} + \text{KL Divergence}
$$

---

## Reconstruction Loss

The reconstruction loss measures how close the reconstructed output is to the original input.

It encourages the decoder to reconstruct the input accurately.

Common reconstruction losses include:

- Mean squared error
- Binary cross-entropy

---

## KL Divergence

**Kullback-Leibler divergence**, or **KL divergence**, measures how different the learned latent distribution is from a standard normal distribution.

The standard normal distribution is usually:

$$
p(z) = N(0, I)
$$

The KL divergence term encourages the latent space to be smooth and well-structured.

This makes it easier to sample new data from the latent space.

---

## Why VAEs Are Generative

VAEs are generative because once training is complete, we can sample a random latent vector:

$$
z \sim N(0, I)
$$

and pass it through the decoder to generate a new sample:

$$
z \rightarrow \hat{x}
$$

For example, a VAE trained on images of faces can generate new face-like images by sampling from its latent space.

---

## Standard Autoencoder vs Variational Autoencoder

| Feature | Standard Autoencoder | Variational Autoencoder |
|---|---|---|
| Latent representation | Fixed vector | Probability distribution |
| Encoder output | Latent code $z$ | Mean $\mu$ and log variance $\log(\sigma^2)$ |
| Sampling | Usually no sampling | Samples from learned distribution |
| Latent space | May be irregular | Smooth and structured |
| Generative ability | Limited | Stronger |
| Loss | Reconstruction loss | Reconstruction loss + KL divergence |

---

## Generative Adversarial Networks, or GANs

A **Generative Adversarial Network**, or **GAN**, is a generative model made of two competing neural networks:

1. **Generator**
2. **Discriminator**

The generator tries to create realistic fake data.

The discriminator tries to distinguish real data from fake data.

---

## Generator

The **generator** takes random noise as input and produces fake data.

For example, in an image GAN:

$$
\text{Random Noise} \rightarrow \text{Generator} \rightarrow \text{Fake Image}
$$

The generator learns to create outputs that look like the real training data.

Its goal is to fool the discriminator.

---

## Discriminator

The **discriminator** takes a data sample and predicts whether it is real or fake.

The input may be:

- A real sample from the training set.
- A fake sample produced by the generator.

The discriminator outputs a probability that the sample is real.

---

## GAN Training

GAN training alternates between two steps:

1. Train the discriminator.
2. Train the generator.

---

## Step 1: Train the Discriminator

The discriminator is trained on a mixture of real and fake samples.

It learns to classify:

- Real samples as real.
- Fake samples as fake.

During this step:

- The discriminator's weights are updated.
- The generator's weights are frozen.

The discriminator is commonly trained using binary cross-entropy loss.

---

## Step 2: Train the Generator

The generator creates fake samples and tries to make the discriminator classify them as real.

During this step:

- The discriminator's weights are frozen.
- The generator's weights are updated.

The generator improves by learning how to produce more realistic samples.

---

## GAN Objective

GANs are adversarial because the generator and discriminator have opposing goals.

| Component | Goal |
|---|---|
| Generator | Create fake samples that look real |
| Discriminator | Correctly classify real and fake samples |

Ideally, the generator becomes so good that the discriminator cannot reliably tell whether a sample is real or fake.

---

## GAN Difficulties

GANs can be difficult to train because the generator and discriminator continuously adapt to each other.

This creates unstable training dynamics.

---

## Nash Equilibrium

In theory, GAN training should reach a **Nash equilibrium**.

A Nash equilibrium occurs when neither network can improve without the other changing.

In the ideal GAN case:

- The generator produces highly realistic samples.
- The discriminator cannot do better than random guessing.

However, in practice, reaching this equilibrium is difficult.

---

## Mode Collapse

**Mode collapse** occurs when the generator produces only a limited variety of outputs.

For example, if a GAN is trained on handwritten digits, it may learn to generate only one or two digit types instead of all digits.

This is a problem because the generator loses diversity and does not fully represent the training distribution.

---

## Instability

GANs can be unstable because both networks are constantly changing.

The generator improves to fool the discriminator.

The discriminator improves to catch the generator.

This can cause:

- Oscillating parameters
- Unstable losses
- Failure to converge
- Poor sample quality

---

## VAE vs GAN

| Feature | VAE | GAN |
|---|---|---|
| Type | Probabilistic generative model | Adversarial generative model |
| Main components | Encoder and decoder | Generator and discriminator |
| Latent space | Smooth and structured | Often less directly structured |
| Training | Usually more stable | Often unstable |
| Output quality | Can be blurrier | Often sharper and more realistic |
| Loss | Reconstruction + KL divergence | Adversarial loss |
| Sampling | Sample from latent distribution | Sample noise into generator |

---

## Topic Summary

Key ideas from Topic 6 and 7 include:

- Convolutional autoencoders are best suited for image reconstruction.
- The encoder is usually a CNN.
- The decoder reverses the encoder using upsampling or transposed convolutions.
- Denoising autoencoders learn to reconstruct clean inputs from noisy inputs.
- Denoising helps force the model to learn robust and useful features.
- Variational autoencoders are probabilistic and generative.
- VAEs encode inputs as distributions using $\mu$ and $\log(\sigma^2)$.
- VAEs use the reparameterisation trick: $z = \mu + \sigma \odot \epsilon$.
- VAE loss combines reconstruction loss and KL divergence.
- GANs use a generator and discriminator that compete against each other.
- GAN training can be difficult due to Nash equilibrium issues, mode collapse, and instability.