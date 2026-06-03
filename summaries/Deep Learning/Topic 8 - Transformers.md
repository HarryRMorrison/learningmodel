# Topic 8 – Transformers

## Key Idea

Transformers are neural networks designed to process sequences, such as text.

Unlike RNNs, transformers do not process tokens one at a time. Instead, they process the whole sequence in parallel.

This makes transformers faster to train and better at handling long-range dependencies.

---

## Why Transformers Are Useful

Transformers are useful because they:

- Handle long sequences better than basic RNNs.
- Process tokens in parallel.
- Learn relationships between words regardless of their distance.
- Use attention to focus on the most relevant parts of the input.

---

## Attention

The key idea behind transformers is **attention**.

Attention allows the model to decide which parts of the input sequence are most important for each token.

For example, in the sentence:

> The dog chased the ball because it was excited.

The model can use attention to understand that **it** likely refers to **the dog**.

---

## Self-Attention

**Self-attention** means that each token in a sequence looks at every other token in the same sequence.

Each word can gather information from the other words around it.

This helps the model understand context.

For example, the meaning of a word like **bank** depends on the surrounding words:

- "river bank"
- "bank account"

Self-attention helps the model distinguish between these meanings.

---

## Queries, Keys, and Values

Self-attention uses three learned vectors:

- **Query**
- **Key**
- **Value**

The query asks:  
"What am I looking for?"

The key says:  
"What information do I contain?"

The value says:  
"What information should I pass on?"

The model compares queries and keys to decide how much attention each token should pay to every other token.

---

## Multi-Head Attention

**Multi-head attention** means the transformer uses multiple attention mechanisms at the same time.

Each attention head can learn a different type of relationship.

For example, one head might focus on:

- Subject-verb relationships

Another might focus on:

- Pronoun references

Another might focus on:

- Nearby words

The outputs of the attention heads are combined together.

---

## Positional Encoding

Transformers process tokens in parallel, so they do not naturally know the order of words.

To solve this, transformers use **positional encoding**.

Positional encoding adds information about the position of each token in the sequence.

This helps the model understand word order.

For example:

> The dog bit the man.

has a different meaning from:

> The man bit the dog.

---

## Transformer Encoder

A transformer encoder reads an input sequence and produces contextual representations of each token.

An encoder layer usually contains:

1. Multi-head self-attention
2. Add and normalise
3. Feedforward neural network
4. Add and normalise

Encoders are useful for tasks such as:

- Text classification
- Named entity recognition
- Sentence embeddings
- Understanding input text

---

## Transformer Decoder

A transformer decoder generates an output sequence one token at a time.

A decoder layer usually contains:

1. Masked self-attention
2. Encoder-decoder attention
3. Feedforward neural network
4. Add and normalise steps

Decoders are useful for tasks such as:

- Text generation
- Translation
- Summarisation
- Chatbots

---

## Encoder-Decoder Transformer

An encoder-decoder transformer uses:

- An **encoder** to read the input sequence.
- A **decoder** to generate the output sequence.

This is commonly used for sequence-to-sequence tasks.

For example:

$$
\text{Input sentence} \rightarrow \text{Encoder} \rightarrow \text{Decoder} \rightarrow \text{Translated sentence}
$$

---

## Transformer Advantages

Transformers have several advantages:

- They train faster than RNNs because they process tokens in parallel.
- They handle long-range dependencies better.
- They are highly scalable.
- They perform well on many language tasks.
- They are the foundation of many modern large language models.

---

## Topic Summary

Key ideas from transformers include:

- Transformers process sequences in parallel.
- They use attention instead of recurrence.
- Self-attention lets each token look at every other token.
- Multi-head attention learns different types of relationships.
- Positional encoding gives the model information about word order.
- Encoders are mainly used for understanding input.
- Decoders are mainly used for generating output.
- Transformers are the foundation of many modern NLP models.