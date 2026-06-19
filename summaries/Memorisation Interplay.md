# The Reasoning-Memorization Interplay in Language Models Is Mediated by a Single Direction
Linear direction for creativity

We follow the linear feature hypothesis and postulate that the reasoning capability of LLMs is mediated by a single direction in the residual stream, and that by steering this direction, it is possible to control model interplay between reasoning and memorization. We compute the linear reasoning features (LiReFs) using the difference-in-means technique, which effectively disentangles key feature information as demonstrated by previous work (Marks
and Tegmark, 2023; Rimsky et al., 2024).

## Contributions
- We show that LLM reasoning capability is mediated by a set of linear features (LiReFs) in its activation space. Such features govern model
generalizability in solving various reasoning tasks including math, logical, and scientific questions (Section 3).
- We casually validate the functionality of our discovered reasoning features by showing that LLM reasoning generalizability can be enhanced by intervening LiReFs at inference time (Section 4.1).
- We show via case analyses that mediating LiReFs during inference time reduces LLM reasoning errors and misapplication of model reasoning or memorization ability. (Section 4.2).

## Related Work
- **Defintion**: In reasoning tasks, memorization is often seen as poor generalizability to questions outside the training data, as evidenced by studies on work sequence reversal (McCoy et al., 2023) and alphabet shifting (Prabhakar et al., 2024), which show degraded performance on infrequent patterns. Other studies observe performance degradation from controlled perturbations of input questions (Wu et al., 2024; Xie et al., 2024).

### Understanding LLM Reasoning
- Studies suggest LLMs undergo structure multi-step reasoning processes, transitioning though distinct reasoning stages that follow an ordered sequence of knowledge retrieval and rule-based processing.
- Similarly, extended training beyond over-fitting (grokking) has been shown to leas to the emergence of reasoning circuits, indicating reasoning in a learn and structured capability.
- Mathematical reasoning confirms LLMs compute neccessary information rather than memorising templates.
    - Reasoning computations leaving identifiable traces in model activations, particularly in the residual stream.
- Attention heads have been shown to play a key role in both knowledge recall and latent reasoning, suggest these processes are distinct yet interconnected.

### Linear Semantic Features
- Language models encode various semantic concepts as linear directions in their activation space.
- These linear semantic features have been discovered by contrasting inputs that differ in the target semantic dimensions.
- These linear features can be manipulated to control model behaviour.
    - This work extends this line of study by indentifying linear features that mediate the models ability to switch between genuine reasoning and memory recall.

## Linear Reasoning Features (LiReFs)
### Background
- A decoder-only transformer language model $\mathbf{M}$ maps input sequence of tokens $x=[x_1, ..., x_T]$ into a probability distribution over the vocabulary for next-token prediction.
- Within the transformer, the $i$-th token $x_i$ is represented as a series of hidden states $\mathbf{h}$.
- Within each layer $l \in [L]$, two modules compute updates that are added to the layer input $\mathbf{h}^{l-1}(x_i)$: (1) a multi-head self attention module outputs $\mathbf{a}^{(l)}(x_i)$, and (2) a multi-layer perceptron  (MLP) outputs $\mathbf{m}^{(l)}(x_i)$. Putting together, the hidden representation $\mathbf{h}^{(l)}(x_i)$ is computed as:
$$\mathbf{h}^{(l)}(x_i) = \mathbf{h}^{(l-1)}(x_i) +\mathbf{a}^{(l)}(x_i)+\mathbf{m}^{(l)}(x_i)$$
- They call $\mathbf{h}^{(l)}(x_i)$ the *residual stream activation* of $x_i$ at layer $l$.
- They focus on the last token's residual stream $x_T$ of the user turn as the point when the model is going to generate the first answer token, denoted as $\mathbf{H}(x)=\{\mathbf{h}^{(l)}(x_T)\}^{L}_{l=1}$

### Reasoning Feature Extraction
Given a collection of *reasoning-intensive questions* $x \in \mathbf{D}_{Reasoning}$ (e.g. “What is the answer of (5 + 2) ∗ 3?”) and antoher set of memory intensive questions $x \in \mathbf{D}_{Memory}$, calculate the difference between the model's mean last token residual stream activations when running on two categories of input questions (omit some details about positional encoding and layer normalisation):
$$\mathbf{r}^{(l)}=\frac{\sum_{x \in \mathbf{D}_{Reasoning}}\mathbf{h}^{(l)}(x)}{|{\mathbf{D}_{Reasoning}}|} - \frac{\sum_{x \in \mathbf{D}_{Memory}}\mathbf{h}^{(l)}(x)}{|{\mathbf{D}_{Memory}}|}$$

### Reasoning Feature Intervention
- Given $\mathbf{r}^{(l)}$ extracted from layer $l$, we can modulate the strength of the corresponding reasoning feature via simple linear interventions.
- Specifcally, we can perform *reasoning feature addition* by adding the difference-in-means vector to the activations of an input question to shift it closer to the mean activation of typical reasoning-intensive questions, thereby unlocking model reasoning capability:
$$\mathbf{h}'^{(l)}(x) \leftarrow \mathbf{h}^{(l)}(x) + \alpha * r^(l)$$
- Similarly, one can perform *reasoning feature ablation* by erasing the component along $\hat{r}^{(l)}$ for every residual stream activation $\mathbf{h}^{(l)}(x)$ ($\hat{r}$ is a unit vector):
$$\mathbf{h}'^{(l)}(x) \leftarrow \mathbf{h}^{(l)}(x) + \hat{r}\hat{r}\mathbf{h}^{(l)}(x)$$
    - $\mathbf{h}^{(l)}(x) + \hat{r}\hat{r}\mathbf{h}^{(l)}(x)$ zeros out the value along the reasoning direction.

### Datasets and Models
Employ LLM as a judge to determine which questions are Reasoning or Memory based on the following datasets:
- MMlu-Pro
- GSM-8K
- MGSM
- PopQA
- C-Eval Chinese Benchmark

Models:
- LLaMA3-8B Instruct base
- Gemma2-9B Instruct base
- Mistrial-7B-v0.3 Instruct base
- OLMo2-7B Instruct base

## Results

### PCA and Cosine Sim Plots
- Models show linearly seperate activations between memory based and reasoning based questions
    - Especially in the middle layers
    - Reasoning activations where mostly positive while memory wsa mostly negative.
- 3 out of the 4 LLMs have similary layerwise cosine similarity with LiReF profiles between the base and instruct fine tuned models. Suggests LLMs may have developed linear reasoning features to mediate its emergent reasoning capability during pre-training rather than post-training.

### Gradient Nature of Reasoning-Memorisation Interplay
- Due to the positive and negative activation tendencies of memory and reasoning questions, it raised the question: What types of questions fall near the boundary (i.e. those with near-zero LiReF activation values)? Do these problems require both memory and reasoning capabilities to solve?
- Relatively high spearmans correlation between LiReF and LLM-as-Judge memory reasoning question scores
- Coding examples are then used as they require both memory and reasoning. Found they cluster around the decision boundary line of the PCA of LiReF.

## Causal Validation of LiReFs
- Use positive values of $\alpha$ for $\mathbf{D}_{Memory}$ and negative values of $\alpha$ for $\mathbf{D}_{Reasoning}$
- Large improvements across both dataset questions

## Case Study
- Why some memory intensive questions where being activated as reasoning and vice versa.
- By switching the relevant activations for those cases it was found to increase performance.
- This suggests LLM reasoning errors might be due to incorrect activations and not lack of knowledge.

## Limitations
- This study focuses on small LLMs and Large LLMs have been known to increase reasoning capabilities
- While LiReFs can increase performance, but may change if using prompt engineering.
- Future work should investigate Whether perturbational and counterfactual memorization are mechanistically equivalent and, therefore, can be both mediated by LiReFs.