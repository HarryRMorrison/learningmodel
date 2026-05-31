# Defining Creativity

Creativity is defined as:

> The ability to produce or use original and unusual ideas.

- Creativity is a complex and multifaceted concept. Creativity can be high in some aspect(s) but low in others. For example, a portrait of a person is not original, but the representation can be (i.e., Picasso).
- To "think outside of the box" requires knowledge of the box. Therefore, creativity requires a certain level of contextual knowledge and understanding. This is also dependent on what the norms are of the current time period.
- Creativity can exist without being quality or logical. For example, a child can be creative in their play, but it may not be logical or of high quality.

# Current Frameworks

## N-Gram Originality vs. Training Data

The absolute baseline of AI creativity is checking if the model is just memorizing text. Researchers measure this by calculating the fraction of unseen n-grams, sequences of $n$ words or characters, in the AI's output compared to its training corpus.

- If the AI writes a poem and uses 4-word phrases that never appeared anywhere on the internet or in its training data, its structural originality score spikes.
- The originality score can be calculated as:

$$
\text{Originality Score} = 1 - \frac{\text{Count of } n\text{-grams found in training data}}{\text{Total } n\text{-grams in output}}
$$

## The Creativity Frontier: The Harmonic Mean

To prevent rewarding nonsense, the state-of-the-art approach combines the unsupervised distance/originality score with a quality score, usually calculated via an automated task metric or an LLM-as-a-judge panel.

- The creativity score is calculated as the harmonic mean of originality and quality:

$$
\text{Creativity Score} = 2 \times \frac{\text{Originality} \times \text{Quality}}{\text{Originality} + \text{Quality}}
$$

- This way, if an output is highly original but of low quality, such as nonsense, it will not score well overall.

## Self-Similarity and "Intra-Model" Diversity

This looks at the model's internal variance. If you give an AI the same creative prompt 50 times with a high temperature, or randomness setting, does it keep repeating variations of the same idea, or can it explore entirely different regions of the embedding space?

- You can measure this by generating multiple outputs from the AI and calculating the average pairwise distance between its own answers:

$$
\text{Diversity} = \frac{2}{k(k-1)} \sum_{i < j} \text{Distance}(\text{Output}_i, \text{Output}_j)
$$

## SemDis: Semantic Distance Platform

SemDis is an open platform designed specifically to automate creativity tasks like the Alternate Uses Task (AUT), such as "Name 20 creative uses for a brick".

It passes the AI's answers through an unsupervised semantic space to see if the AI suggests typical uses, such as "building a wall", or highly distant, novel uses, such as "using it as crude sandpaper".

## RAG-Based Novelty Checkers

For high-level creative outputs, such as an AI generating a new scientific hypothesis or a movie plot, researchers use a Retrieval-Augmented Generation (RAG) loop.

- The AI generates an output, then a retrieval system checks whether similar ideas exist in the training data or the broader internet, such as the top 50 documents from a vector database.
- If the retrieval system finds close matches, the output is flagged as less creative.
- This can be formalized as:

$$
\text{Novelty Score} = 1 - \frac{\text{Similarity}(\text{Output}, \text{Retrieved Data})}{\text{Max Similarity}}
$$