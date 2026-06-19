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

## Understanding or Memorising 
- Analyse internal weights as it is computing to see if there are internal thoughts or images.
- Ask an LLM to make a sentence that has never been said before
