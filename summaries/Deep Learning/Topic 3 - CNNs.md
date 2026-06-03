# Topic 3 – Convolutional Neural Networks (CNNs)

## Key Idea

Convolutional Neural Networks, or **CNNs**, are neural networks designed to process data with a grid-like structure, especially images.

CNNs learn **hierarchical features**:

- **Low-level features**: edges, corners, simple patterns
- **Mid-level features**: textures, shapes, parts of objects
- **High-level features**: full objects or complex structures

For example, in an image classification model:

1. Early layers may detect edges.
2. Middle layers may detect shapes or textures.
3. Later layers may detect objects such as faces, cars, or animals.

---

## Why CNNs Are Useful for Images

Images have spatial structure. Nearby pixels are usually related to each other.

CNNs are useful because they:

- Preserve spatial information.
- Learn local patterns.
- Share weights across the image.
- Require fewer parameters than fully connected networks.
- Can detect the same feature in different parts of an image.

---

## Convolution Operation

A convolution applies a small matrix called a **filter** or **kernel** across an input image.

The filter slides over the image and computes weighted sums of local regions.

This produces a **feature map**, which highlights where a particular feature appears in the image.

---

## Convolution Formula

$$
I'(x, y) = \sum_i \sum_j I(x+i, y+j) f(i,j)
$$

where:

- $I(x+i, y+j)$ represents pixel values in the local input window.
- $f(i,j)$ represents the filter or kernel weights.
- $I'(x, y)$ represents the output value in the feature map.
- The filter acts like a feature detector.

---

## Filters / Kernels

A **filter** is a small matrix of trainable weights.

Each filter learns to detect a specific pattern, such as:

- Vertical edges
- Horizontal edges
- Corners
- Textures
- Curves
- Object parts

During training, the CNN learns the values of the filter weights automatically through backpropagation.

---

## Feature Maps

A **feature map** is the output produced by applying a filter to an input.

Each filter creates one feature map.

If a convolutional layer has multiple filters, it produces multiple feature maps.

For example:

- 1 filter produces 1 feature map.
- 32 filters produce 32 feature maps.
- 64 filters produce 64 feature maps.

Each feature map detects a different type of pattern.

---

## Weight Sharing

CNNs use **weight sharing**, meaning the same filter is applied across the entire image.

This is useful because the same feature may appear anywhere in the image.

For example, an edge detector should be able to detect an edge whether it appears in the top-left, centre, or bottom-right of the image.

### Benefits of Weight Sharing

Weight sharing:

- Reduces the number of parameters.
- Improves computational efficiency.
- Helps the model generalise better.
- Allows the model to detect features regardless of their location.

---

## Receptive Field

A **receptive field** is the region of the input image that a neuron looks at.

In early convolutional layers, receptive fields are small.

In deeper layers, neurons effectively see larger parts of the original image because information from earlier layers is combined.

This allows deeper layers to learn more complex and global patterns.

---

## Parameters in a Convolutional Layer

The number of parameters in one filter is:

$$
n_h \times n_w \times n_c + 1
$$

where:

- $n_h$ is the height of the filter.
- $n_w$ is the width of the filter.
- $n_c$ is the number of input channels.
- $+1$ represents the bias term.

For multiple filters:

$$
\text{Total parameters} = (n_h \times n_w \times n_c + 1) \times n_f
$$

where:

- $n_f$ is the number of filters.

---

## Example Parameter Calculation

Suppose a convolutional layer has:

- A $3 \times 3$ filter size
- 3 input channels, such as RGB
- 64 filters

Then the number of parameters is:

$$
(3 \times 3 \times 3 + 1) \times 64
$$

$$
= 28 \times 64
$$

$$
= 1792
$$

So the layer has **1,792 trainable parameters**.

---

## Stride

**Stride** is the step size the filter takes as it moves across the image.

A stride of 1 means the filter moves one pixel at a time.

A stride of 2 means the filter moves two pixels at a time.

### Effect of Stride

- Smaller stride produces a larger output feature map.
- Larger stride produces a smaller output feature map.
- Larger stride can be used for downsampling.

In general:

- **Stride = 1** keeps more spatial detail.
- **Stride > 1** reduces the spatial size of the output.

---

## Padding

**Padding** adds extra pixels around the border of an image.

Usually, these added pixels are zeros.

Padding is used to control the spatial size of the output feature map.

---

## Valid Padding

**Valid padding** means no padding is added.

As a result:

- The filter only moves over positions where it fully fits inside the image.
- The output feature map is smaller than the input.
- Border information may be lost.

---

## Same Padding

**Same padding** adds enough zeros around the image so that the output has the same spatial height and width as the input, assuming stride is 1.

As a result:

- The output feature map keeps the same spatial size.
- Border pixels are used more effectively.
- Spatial information is preserved across layers.

---

## Output Size Formula

The output size of a convolutional layer is:

$$
\text{Output size} = \left\lfloor \frac{n + 2p - f}{s} \right\rfloor + 1
$$

where:

- $n$ is the input size.
- $p$ is the amount of padding.
- $f$ is the filter size.
- $s$ is the stride.
- $\lfloor \cdot \rfloor$ means round down.

This formula applies separately to height and width.

---

## Pooling Layers

Pooling layers reduce the spatial size of feature maps.

They help make the network more efficient and can make the model more robust to small shifts in the input.

### Max Pooling

**Max pooling** takes the maximum value from each local region.

This keeps the strongest detected feature.

For example, if a small region contains values:

$$
[1, 3, 2, 5]
$$

max pooling outputs:

$$
5
$$

### Average Pooling

**Average pooling** takes the average value from each local region.

This gives a smoother summary of the region.

---

## CNN Architecture

A typical CNN architecture contains:

1. Convolutional layers
2. Activation functions, usually ReLU
3. Pooling layers
4. Flattening
5. Fully connected layers
6. Output layer

A simple CNN pipeline might look like:

$$
\text{Input Image} \rightarrow \text{Conv} \rightarrow \text{ReLU} \rightarrow \text{Pooling} \rightarrow \text{Conv} \rightarrow \text{ReLU} \rightarrow \text{Pooling} \rightarrow \text{Fully Connected} \rightarrow \text{Output}
$$

---

## Flattening

After convolution and pooling layers, the output is usually a 3D tensor.

Before passing it into a fully connected layer, it is often flattened into a 1D vector.

For example:

$$
7 \times 7 \times 64 = 3136
$$

This becomes a vector of length 3136.

---

## Fully Connected Layers

Fully connected layers use the features learned by the convolutional layers to make final predictions.

For example:

- In image classification, the final layer predicts the class label.
- In binary classification, the final layer may use sigmoid.
- In multi-class classification, the final layer may use softmax.

---

## CNNs Compared to MLPs

| Feature | MLP | CNN |
|---|---|---|
| Input structure | Treats input as flat vector | Preserves spatial structure |
| Parameters | Usually many | Fewer due to weight sharing |
| Spatial awareness | Weak | Strong |
| Best for images | Not ideal | Very effective |
| Feature learning | Learns global patterns directly | Learns local-to-global hierarchical features |

---

## Topic Summary

CNNs are powerful for image-based tasks because they use convolutional filters to learn spatial patterns.

Key ideas include:

- CNNs learn hierarchical features.
- Filters detect local patterns.
- Weight sharing reduces the number of parameters.
- Stride controls how far the filter moves.
- Padding controls the output size.
- Pooling reduces spatial dimensions.
- Fully connected layers use the learned features for prediction.