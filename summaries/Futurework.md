## Epistemic Awareness
**Gap 1: Step-level epistemic calibration**
- Can a model identify which reasoning step is uncertain, under-supported, contradicted, or speculative?

**Gap 2: Disentangling likelihood, confidence, and evidence**
- Current work treats confidence in a single dimension when in reality it is treated in seperate dimensions.
    - probability: “likely”, “unlikely”, “possible”;
    - confidence: “certain”, “not sure”, “confident”;
    - evidentiality: “according to”, “it seems”, “the evidence suggests”;
    - reasoning status: “assuming”, “therefore”, “this depends on”.

**Gap 3: Reasoning-trace uncertainty, not just answer uncertainty**
- Existing work measures whether final confidence is calibrated; this project measures whether uncertainty is correctly distributed across the reasoning trace.
- Looks at reasoning steps.

**Gap 4: Evidence-conditioned epistemic awareness in RAG**
- Does the model express uncertainty when the evidence is missing, conflicting, or insufficient, even if the answer sounds plausible?

**Ideas**
- Use contrastive learning to build a scale for epistemic measurement.
    - KV cache
    - All weights
    - Some weights
- Use philosophical argument trees to visualise it
    - Potenitally use a graph network

**MPhil Projects**
1. Can LLMs express uncertainty at the correct point in a reasoning chain, and can contrastive or ordinal learning improve the measurement of that behaviour?
2. A framework for evaluating whether LLMs place the right amount of uncertainty at the right reasoning step, conditioned on evidence quality and reasoning correctness.
3. Investigating whether divergent originality and convergent usefulness are encoded as distinct causal subspaces in LLMs.

## Understanding or Memorising 
**Gap 1: Perturbational VS Counterfactual**
- Whether perturbational and counterfactual memorization are mechanistically equivalent and, therefore, can be both mediated by LiReFs.

## LLMs creativity and Understanding 
- LLMs favour familiar, widely appealing, high-probability patterns
    - Kitsch paper and homogenising creativity

# MPhil Project Ideas
1. Is there a single or multiple sets of linear features that mediate the models ability to produce more creative or original text? Can pertubing these linear features cause the model to produce more unique creative text or generic text.
    - Creativity of reasoning steps?
    - **Papers:**
        - The Reasoning-Memorization Interplay in Language Models Is Mediated by a Single Direction

2. A framework for evaluating whether LLMs place the right amount of uncertainty at the right reasoning step, conditioned on evidence quality and reasoning correctness. (Could mean a step-level metric)
    - **Papers:**
        - Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?
        - FINCHAIN: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning

3. Alignment Whack-a-Mole suggests that semantic representations and exact textual memories may be linked inside the model. Can retrieval pathways be identified and regularised to reduce memorisation while increasing generalisation.
    - Could linear features influence a model to activate more generalisation pathways
    - **Papers:**
        - Alignment Whack-a-Mole: Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models
        - The Reasoning-Memorization Interplay in Language Models Is Mediated by a Single Direction
