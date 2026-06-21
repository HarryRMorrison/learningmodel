# FINCHAIN: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning
URL: https://arxiv.org/pdf/2506.02515

## Abstract
FINCHAIN addresses gaps by introducing a symbolic, executable benchmark with explicit intermediate supervision and automatic alignmentbased evaluation, spanning 58 topics across 12 financial domains.

## Introduction
- Effective analysis often requires synthesizing large volumes of textual information from
reports, news, and social media, which reflect and influence financial phenomena such as investor sentiment, risk perceptions, and expected market trends.
- Previous models produce short outputs and do not test whether they can perform transparent, multi-step financial reasoning that justify each intermediate step.
- Inspired by the symbolic-template paradigm introduced in mathematical reasoning (Mirzadeh et al., 2025)

### Main Contributions
- We introduce the first from-scratch symbolic benchmark for financial reasoning, grounded in a fine-grained taxonomy spanning 12 domains and 58 topics.
- We propose CHAINEVAL, a verifiable reasoning measure that evaluates both step-level consistency and final-answer correctness, and shows the strongest correlation with expert human judgments.
- We benchmark 26 leading proprietary and open-weight LLMs, and find that even state of-the-art LLMs struggle with verifiable multistep financial reasoning, particularly on advanced symbolic templates

## Related Studies
### Financial NLP
- Driven by modeling and benchmarking
- Early work focused on extraction and classification with model such as:
    - FinBERT  (Liu et al., 2020)
    - Personal finance (Hean et al., 2025)
    - Credit scoring (Feng et al., 2023)
    - Risk-awareness benchmarking (Yuan et al., 2024)
    - Datasets like FiNER-ORD, REFinD, FinARG, and ECTSum support tasks in NER, relation extraction, argument mining, and summarization
- Large financial language models have further advanced the field.
- BloombergGPT (Wu et al., 2023) achieved broad in-domain performance, FinGPT (Liu et al., 2023) emphasized open-source adaptability, and FinMA (Xie et al., 2023a) delivered competitive results with a compact architecture.
- Benchmarks for broad evaluation and diverse tasks; FLANG, FinBen, FinMTEB.
- Benchmarks for quantitative and multimodal reasoning; BizBench, PIXIU.
- Limitations in multi-step reasoning, long-context understanding, and cross market generalization (shows the need for this gap to be filled).

### Financial Reasoning
- Real-world problems require precise numerical reasoning.
- **FinQA** (2021) and **ConvFinQA** (2022) were developed before Chain-of-Thought reasoning became a standard evaluation target.
    - As result they supervise arithmetic program generation but offer only weak step-level signals, yielding traces that are neither explicit nor verifiable.
- **FinTextQA** (2024) introduces long form financial questions from textbooks and regulatory sources.
    - Focus on explanatory retrieval rather than traceable computation.
- Bridging text and numerical reasoning:
    - **TAT-QA** (2021) and **MultiHiertt** (2022), combine textual and tabular evidence.
    - **DocMath-Eval** (2024) and FinanceMath(2024) move toward interpretable symbolic evaluation.
- Afformentioned datasets remain largely domain-agnostic and lack explicit step-level supervision grounded in financial formulae.
- **FinancialReasoning** (2025) improves answer level numerical reliability by introducing executable python solutions.
    - However, does not systematic verification of step-level reasoning alignment.

## ChainEval
- An evaluation framework that jointly assesses reasoning-step alignment (via step-answer matching) and final-answer correctness.
- Builds on prior work on reasoning consistency (Lyu et al., 2023; Golovneva et al., 2023)
- Defines $S^*$ as gold solution and $\hat{S}$ as predicted solution with $m$ and $n$ reasoning steps.
$$S^*=(s^{*}_{1},...,s^{*}_{m}), \space \hat{S}=(\hat{s}_{1},...,\hat{s}_{m})$$
- Each step produces an intermediate result representing the numerical or symbolic value compute at each step.
$$\text{StepRes}(s_i)=a_i$$
- To evaluate the reasoning faithfulness, they compare these sequences both semantically and numerically.
- They apply Dynamic Time Warping (DTW) to capture the global structural alignment between step sequences.
    - Provides flexible order-preserving alignment.

### Reasoning Step Alignment
- Consistency between gold and predicted reasoning traces is assessed on *semantic similarity* and *answer level agreement*, combined within a *DTW-based alignment framework*.
- **Semantic Similarity**: each step in encoded using a sentence encoder $\text{Enc}(\dot)$ and the pairwise semantic similarity between the gold and the predicted steps is computed with *cosine similarity* as:
$$SS(s^{*}_{i},\hat{s}_{j})=\text{cos}(\text{Enc}(s^{*}_{i}), \text{Enc}(\hat{s}_{j}))$$
- **Answer Match**: evaluate numeric or symbolic consistency at each step. $\mathbb{I}$ denotes the indicator function (doesn't say what). $\epsilon=0.05$ which permits up to a 5% relative numerical deviation to account for rounding or error propagation (design choice inline financial auditing standards):
$$
\mathrm{AM}(s_i^*, \hat{s}_j) =
\begin{cases}
\mathbb{I}\left(\dfrac{|\hat{a}_j - a_i^*|}{|a_i^*|} \le \epsilon\right), & \text{if both are numeric,} \\
\mathbb{I}(\hat{a}_j = a_i^*), & \text{otherwise.}
\end{cases}
$$
- **Gated Step-Level Similarity**: Ensures that a pair of steps is considered consistent only when semantics and results agree, they define a gated score (forms basis of DTW alignment):
$$\text{Score}_{\text{gate}}(i,j)=SS(s^{*}_{i},\hat{s}_{j}) \times \mathrm{AM}(s_i^*, \hat{s}_j)$$
- **Dynamic Sequence Alignment** : The minimal DTW cost is transformed into a normalised similarity measure. $\text{Cost}_{DTW}$ denotes the total alignment cost and $L_{\text{path}}$ is the length of the optimal alignment path. Scores lie with [0,1] with higher value showing stronger alignment:
$$\text{DTWGate}(S^*,\hat{S})=1-\frac{\text{Cost}_{DTW}}{L_{\text{path}}}$$
- **Final Answer Correctness**: Asess the final output.
$$
\mathrm{FAC}(s_i^*, \hat{s}_j) =
\begin{cases}
\mathbb{I}\left(\dfrac{|\hat{a}_n - a_m^*|}{|a_m^*|} \le \epsilon\right), & \text{if both are numeric,} \\
\mathbb{I}(\hat{a}_n = a_m^*), & \text{otherwise.}
\end{cases}
$$
- **Final Formulae**: Where $\alpha=0.1$ which was set via maximising correlation with human evaluations.
$$\text{ChainEval}=(1-\alpha) \cdot \text{DTWGate} + \alpha \cdot \text{FAC}$$

## Experiments and Results
### Validation
- Before large scale experiments they sampled 20 questions and asked 5 models to answer them. With financial experts and the gold reasoning trace, two ratings were given across 2 dimensions; reasoning process quality and final answer accuracy. A 0.94 correlation was observed between them. Showing that coherent reasoning often leads to accurate final answers.
### Results
- Frontier proprietary models achieved the highest scores.
- Scructured supervision helps models with reasoning.
- Models exhibit a clear degradation on advanced instances, highlighting the challenge of solving complex, multi-step financial reasoning problems to completion.
    - open-weight and fine-tuned models show substantially steeper declines as difficulty increases
- Bigger frontier models showed better performance across financial topics. Finetuned models had areas it did better and worse in.
- GPT-5-mini and Finance-Qwen were compared on what the errors were. GPT-5-mini mainly suffered from computational and conceptual errors, while Finance-Qwen suffered from way more; computational, conceptual, parsing\format, hallucination.