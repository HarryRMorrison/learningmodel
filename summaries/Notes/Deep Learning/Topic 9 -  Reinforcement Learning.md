# Topic 9 – Reinforcement Learning

## Reinforcement Learning

**Reinforcement Learning**, or **RL**, is a type of machine learning where an agent learns by interacting with an environment.

The agent makes observations, takes actions, and receives rewards.

The goal is to learn a strategy that maximises long-term rewards.

---

## Key Components

| Component | Meaning |
|---|---|
| Agent | The learner or decision-maker |
| Environment | The world the agent interacts with |
| Observation | Information the agent receives from the environment |
| Action | A choice made by the agent |
| Reward | Feedback received after taking an action |
| Policy | The strategy used by the agent to choose actions |

---

## Main Goal

The objective of reinforcement learning is to learn a policy that maximises total future reward.

The agent does not just try to maximise immediate reward.

Instead, it tries to maximise **long-term reward**.

For example, in a game, the best move may not give an immediate reward but may help win later.

---

## Policy

A **policy** is the rule or algorithm used by the agent to decide which action to take.

A policy can be:

- Rule-based
- Probabilistic
- Learned by a neural network

For example, a policy might say:

> If the pole is leaning left, move the cart left.

A neural network policy might instead take observations as input and output probabilities for each possible action.

---

## Exploration vs Exploitation

A major challenge in reinforcement learning is balancing **exploration** and **exploitation**.

### Exploration

Exploration means trying new actions to learn more about the environment.

This helps the agent discover better strategies.

### Exploitation

Exploitation means choosing the best-known action based on current knowledge.

This helps the agent gain rewards using what it already knows.

### Key Idea

The agent must explore enough to learn, but exploit enough to perform well.

---

## Brute Force Grid Search

One simple approach is to try many combinations of policy parameters.

This is called **brute force grid search**.

The agent tests different policies and keeps the best-performing one.

### Limitation

This becomes impractical when the number of possible policies is large.

Searching through a large policy space can be like finding a needle in a haystack.

---

## Genetic Algorithms

**Genetic algorithms** are inspired by natural selection.

They use the idea of survival of the fittest.

The general process is:

1. Generate many policies.
2. Evaluate their performance.
3. Keep the best policies.
4. Combine or mutate them to create new policies.
5. Repeat.

Good policies are more likely to produce offspring.

---

## Policy Gradients

**Policy gradient methods** directly optimise the policy.

Instead of learning the value of actions first, the model learns how to choose better actions.

The policy may be represented by a neural network.

The neural network takes observations as input and outputs action probabilities.

---

## Neural Network Policies

A neural network policy can output a probability distribution over actions.

For example:

| Action | Probability |
|---|---|
| Move left | 0.7 |
| Move right | 0.3 |

The agent can then sample an action from this distribution.

This allows the agent to explore while still favouring actions it currently believes are good.

---

## Policy Gradient Caveats

Neural network policies can be challenging when:

- Observations do not contain the full state of the environment.
- Observations are noisy.
- Rewards are sparse or delayed.
- The agent needs memory of past observations or actions.

If the current observation does not fully describe the environment, the agent may need to consider previous observations as well.

If observations are noisy, the agent may use several past observations to estimate the current state.

---

## Credit Assignment Problem

The **credit assignment problem** is the difficulty of knowing which actions caused a reward or penalty.

Rewards are often delayed.

For example, if a pole falls after 100 steps, it does not necessarily mean the final action was the only bad action.

Earlier actions may have contributed to the failure.

The challenge is deciding which actions deserve credit or blame.

---

## Discounted Rewards

A **discounted reward** reduces the value of rewards that happen further in the future.

Future rewards are multiplied by a discount factor.

The discount factor is usually written as:

$$
\gamma
$$

where:

- $\gamma$ is between 0 and 1.
- A value close to 0 makes the agent focus more on immediate rewards.
- A value close to 1 makes the agent care more about future rewards.

---

## Return

The total discounted reward from a time step is called the **return**.

It can be written as:

$$
G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \gamma^3 r_{t+3} + \cdots
$$

where:

- $G_t$ is the return from time step $t$.
- $r_t$ is the reward at time step $t$.
- $\gamma$ is the discount factor.

---

## Action Advantage

The **advantage** of an action measures how much better or worse it was compared to the average action.

A good action may still be followed by bad actions, causing it to receive a low total score.

To reduce this issue, action scores are often averaged and normalised.

A common normalisation is:

$$
\frac{x - \text{mean}}{\text{standard deviation}}
$$

This helps good actions receive better relative scores.

---

## REINFORCE Algorithm

**REINFORCE** is a policy gradient algorithm.

It updates the policy parameters in the direction that increases expected rewards.

### Steps

1. Let the neural network play several episodes.
2. At each step, compute the gradients that would make the chosen action more likely.
3. Do not apply the gradients immediately.
4. Compute each action's score using discounted rewards or action advantage.
5. Multiply each gradient by the corresponding action score.
6. Average the resulting gradients.
7. Use the averaged gradients to update the policy.

---

## Markov Decision Processes

A **Markov Decision Process**, or **MDP**, is a mathematical framework for reinforcement learning.

An MDP contains:

- States
- Actions
- Transition probabilities
- Rewards

The next state depends on:

- The current state
- The chosen action

This is called the **Markov property**.

The Markov property means the future depends only on the current state, not the full history of previous states.

---

## Bellman Optimality Equation

The **Bellman optimality equation** defines the value of a state recursively.

It estimates how good it is to be in a given state, assuming the agent acts optimally afterwards.

The value of a state depends on:

- The immediate reward
- The discounted value of future states

---

## Value Iteration

**Value iteration** is a dynamic programming algorithm used to solve MDPs when the transition probabilities and rewards are known.

It repeatedly updates estimates of state values until they converge.

The goal is to estimate the optimal value function.

---

## Q-Values

A **Q-value** estimates how good it is to take a specific action in a specific state.

It is written as:

$$
Q(s, a)
$$

where:

- $s$ is the state.
- $a$ is the action.

The optimal Q-value is written as:

$$
Q^*(s, a)
$$

It represents the expected sum of discounted future rewards after taking action $a$ in state $s$, assuming the agent acts optimally afterwards.

---

## Q-Value Iteration

**Q-value iteration** focuses on state-action pairs instead of only states.

It estimates the best long-term reward for each action in each state.

After obtaining the optimal Q-values, the optimal policy is:

$$
\pi^*(s) = \arg\max_a Q^*(s, a)
$$

This means the best action is the action with the highest Q-value in the current state.

---

## Temporal Difference Learning

**Temporal Difference Learning**, or **TD Learning**, is used when transition probabilities and rewards are not known in advance.

The agent learns from experience by observing transitions.

A transition contains:

$$
(s, a, r, s')
$$

where:

- $s$ is the current state.
- $a$ is the action.
- $r$ is the reward.
- $s'$ is the next state.

---

## TD Target

The **TD target** combines the immediate reward with the estimated value of the next state.

A simple TD target is:

$$
r + \gamma V(s')
$$

where:

- $r$ is the immediate reward.
- $\gamma$ is the discount factor.
- $V(s')$ is the estimated value of the next state.

---

## TD Error

The **TD error** measures the difference between the TD target and the current value estimate.

$$
\delta = r + \gamma V(s') - V(s)
$$

where:

- $\delta$ is the TD error.
- $V(s)$ is the current value estimate.
- $r + \gamma V(s')$ is the TD target.

TD learning updates value estimates using this error.

---

## Q-Learning

**Q-learning** is a reinforcement learning algorithm that learns Q-values from experience.

It does not require knowing the transition probabilities or reward function in advance.

Q-learning updates Q-values using observed transitions.

---

## Q-Learning Update

The Q-learning update is:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \left[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right]
$$

where:

- $\alpha$ is the learning rate.
- $r$ is the reward.
- $\gamma$ is the discount factor.
- $s'$ is the next state.
- $\max_{a'} Q(s',a')$ is the best estimated future value.

---

## Off-Policy Learning

Q-learning is an **off-policy** algorithm.

This means the policy being learned is not necessarily the same as the policy used to choose actions during training.

For example, the agent may explore using an epsilon-greedy policy, while learning the optimal greedy policy.

---

## Limitation of Q-Learning

Basic Q-learning does not scale well to large or continuous state spaces.

This is because it may require storing a Q-value for every possible state-action pair.

For large problems, this creates too many parameters.

---

## Epsilon-Greedy Policy

An **epsilon-greedy policy** balances exploration and exploitation.

It uses a parameter:

$$
\epsilon
$$

With probability $\epsilon$, the agent chooses a random action.

With probability $1 - \epsilon$, the agent chooses the best-known action.

---

## Epsilon Decay

Usually, $\epsilon$ decreases over time.

At the start of training:

- $\epsilon$ is high.
- The agent explores more.

Later in training:

- $\epsilon$ is lower.
- The agent exploits what it has learned.

This allows the agent to explore early and then focus on good actions later.

---

## Approximate Q-Learning

**Approximate Q-learning** uses a function approximator instead of a table of Q-values.

The function approximator estimates Q-values.

This allows Q-learning to scale to larger problems.

A neural network can be used as the function approximator.

---

## Deep Q-Learning

**Deep Q-Learning** uses a deep neural network to estimate Q-values.

The neural network is called a **Deep Q-Network**, or **DQN**.

The input is usually the current state.

The output is the estimated Q-value for each possible action.

---

## Deep Q-Network

A DQN estimates:

$$
Q(s, a)
$$

for each action.

For example, if there are three possible actions, the DQN may output:

| Action | Estimated Q-value |
|---|---|
| Left | 2.1 |
| Right | 4.8 |
| Stay | 1.3 |

The agent chooses the action with the highest Q-value, unless it is exploring.

---

## DQN Target Value

The target value in DQN combines:

- The immediate reward
- The best discounted estimate of future rewards

The target is:

$$
r + \gamma \max_{a'} Q(s', a')
$$

where:

- $r$ is the immediate reward.
- $\gamma$ is the discount factor.
- $s'$ is the next state.
- $a'$ is a possible next action.

---

## Catastrophic Forgetting

**Catastrophic forgetting** occurs when a neural network forgets previously learned information while learning new information.

In reinforcement learning, this can happen because training data is highly correlated and constantly changing.

For example, a DQN may learn a useful strategy early in training but later overwrite it while adapting to new experiences.

---

## Topic Summary

Key ideas from reinforcement learning include:

- An agent interacts with an environment.
- The agent observes states, takes actions, and receives rewards.
- The goal is to maximise long-term reward.
- A policy determines which action the agent takes.
- Exploration means trying new actions.
- Exploitation means using the best-known action.
- The credit assignment problem makes it difficult to know which actions caused rewards.
- Discounted rewards reduce the value of future rewards.
- REINFORCE is a policy gradient algorithm.
- MDPs formalise reinforcement learning problems.
- Value iteration estimates state values.
- Q-learning estimates state-action values.
- Epsilon-greedy policies balance exploration and exploitation.
- Deep Q-learning uses neural networks to estimate Q-values.
- Catastrophic forgetting occurs when new learning overwrites old learning.