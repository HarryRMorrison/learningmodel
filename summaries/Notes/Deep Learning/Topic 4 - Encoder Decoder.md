# Topic 4 – Encoder-Decoder Models and Sequence Learning

## Recurrent Neural Networks, or RNNs

Recurrent Neural Networks, or **RNNs**, are neural networks designed to process sequential data.

They are commonly used for tasks involving:

- Text
- Speech
- Time series
- Sequences of events
- Language modelling
- Machine translation

Unlike standard feedforward neural networks, RNNs have connections that allow information from previous time steps to influence later time steps.

---

## Key Idea of RNNs

RNNs process input one step at a time.

At each time step, the model receives:

- The current input
- A hidden state from the previous time step

The hidden state acts like a memory of previous inputs.

This allows the RNN to use information from earlier in the sequence when making predictions later in the sequence.

---

## RNN Memory

RNNs have a form of memory because the hidden state is passed forward through time.

More recent time steps usually have a stronger influence on the hidden state than earlier time steps.

This means RNNs often remember recent information better than information from far earlier in the sequence.

---

## RNN Formula

A simple RNN update can be written as:

$$
h_t = f(W_x x_t + W_h h_{t-1} + b)
$$

where:

- $h_t$ is the hidden state at time step $t$.
- $x_t$ is the input at time step $t$.
- $h_{t-1}$ is the hidden state from the previous time step.
- $W_x$ is the input weight matrix.
- $W_h$ is the recurrent weight matrix.
- $b$ is the bias.
- $f$ is an activation function, often `tanh` or `ReLU`.

---

## Encoder-Decoder Models

An **encoder-decoder model** is a neural network architecture used to transform one sequence into another sequence.

It is commonly used in:

- Machine translation
- Text summarisation
- Image captioning
- Speech recognition
- Question answering

---

## Encoder

The **encoder** reads the input sequence and compresses it into a hidden representation.

This hidden representation is often called:

- A context vector
- A latent representation
- An encoded representation

The encoder attempts to capture the important information from the input sequence.

---

## Decoder

The **decoder** takes the encoded representation and generates an output sequence.

For example, in machine translation:

- The encoder reads a sentence in English.
- The decoder generates the translated sentence in French.

---

## Encoder-Decoder Pipeline

A simple encoder-decoder model can be represented as:

$$
\text{Input Sequence} \rightarrow \text{Encoder} \rightarrow \text{Context Vector} \rightarrow \text{Decoder} \rightarrow \text{Output Sequence}
$$

---

## Limitation of Basic Encoder-Decoder Models

A major limitation of basic encoder-decoder models is that the entire input sequence must be compressed into a single context vector.

This can be difficult for long sequences because important early information may be lost.

This limitation helped motivate the development of attention mechanisms and transformers.

---

## 1D Convolutional Layers for Sequences

A **1D convolutional layer** can be used to process sequence data.

Instead of applying a filter over height and width, as in image CNNs, a 1D convolution applies filters across one dimension, usually time or token position.

This creates feature maps over a sequence.

---

## Why Use 1D Convolutions for Sequences?

1D convolutional layers can detect local patterns in sequences, such as:

- Short phrases in text
- Local sound patterns in audio
- Short-term trends in time series

They are useful because they:

- Can be faster than RNNs.
- Can process multiple positions in parallel.
- Capture local dependencies well.
- Avoid some recurrent training issues.

However, standard 1D convolutions may struggle with long-range dependencies unless many layers or dilation are used.

---

## RNN Limitations

RNNs have several important limitations.

### 1. Difficulty with Long Sequences

RNNs often struggle with long sequences because information must be passed through many time steps.

As the sequence gets longer, early information may gradually be forgotten.

This makes it difficult for basic RNNs to learn long-term dependencies.

---

### 2. Vanishing and Exploding Gradients

RNNs are especially vulnerable to vanishing and exploding gradients.

This happens because the same recurrent weights are repeatedly applied across many time steps.

During backpropagation through time, gradients may:

- Shrink exponentially, causing vanishing gradients.
- Grow exponentially, causing exploding gradients.

---

### 3. Nonsaturating Activations May Not Fully Solve the Problem

Using nonsaturating activation functions such as ReLU may help with vanishing gradients, but it does not fully solve the issue.

Because the same weights are reused at every time step, gradients can still become unstable.

In some cases, ReLU-based RNNs may suffer from exploding gradients.

---

## Long Short-Term Memory, or LSTM

**Long Short-Term Memory**, or **LSTM**, is a type of RNN designed to learn long-term dependencies more effectively.

LSTMs use gates to control what information is:

- Remembered
- Forgotten
- Updated
- Output

This makes them better than simple RNNs at handling long sequences.

---

## Why LSTMs Are Useful

LSTMs are useful because they:

- Remember early inputs better than simple RNNs.
- Detect long-term dependencies in data.
- Reduce the vanishing gradient problem.
- Often converge faster than basic RNNs on sequence tasks.

---

## LSTM Cell

An LSTM cell contains:

- A **forget gate**
- An **input gate**
- A **candidate memory update**
- An **output gate**
- A **cell state**
- A **hidden state**

The cell state acts as a long-term memory pathway through the sequence.

---

## Forget Gate

The **forget gate** decides what information should be removed from the cell state.

It outputs values between 0 and 1.

- A value close to 0 means forget this information.
- A value close to 1 means keep this information.

---

## Input Gate

The **input gate** decides what new information should be added to the cell state.

It controls how much of the candidate memory update should be stored.

---

## Output Gate

The **output gate** decides what information should be passed to the hidden state.

The hidden state is then used for prediction and passed to the next time step.

---

## Gated Recurrent Unit, or GRU

A **Gated Recurrent Unit**, or **GRU**, is a simplified version of an LSTM.

GRUs are designed to capture long-term dependencies while using fewer parameters than LSTMs.

---

## GRU Key Idea

GRUs combine some of the LSTM gates into fewer components.

A GRU usually has:

- An **update gate**
- A **reset gate**

Unlike LSTMs, GRUs do not have a separate cell state.

Instead, they use the hidden state to store and pass information through time.

---

## LSTM vs GRU

| Feature | LSTM | GRU |
|---|---|---|
| Complexity | More complex | Simpler |
| Gates | Forget, input, output gates | Update and reset gates |
| Cell state | Has separate cell state | No separate cell state |
| Parameters | More parameters | Fewer parameters |
| Training speed | Often slower | Often faster |
| Long-term dependencies | Very strong | Strong |
| Best use | Complex sequence tasks | Faster sequence modelling |

---

## Topic Summary

Encoder-decoder models are used to transform one sequence into another sequence.

Key ideas include:

- RNNs process sequences one time step at a time.
- RNNs use hidden states as memory.
- Basic RNNs struggle with long sequences.
- RNNs can suffer from vanishing and exploding gradients.
- 1D convolutional layers can learn local sequence patterns.
- LSTMs improve RNNs by using gates and a cell state.
- GRUs are simplified LSTMs with fewer parameters.
- Encoder-decoder models are useful for sequence-to-sequence tasks.