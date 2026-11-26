<p align="center">
  <img src="assets/loop-banner.svg" alt="Awesome Loop Generative Models — a living reading map for models that revisit computation" width="100%">
</p>

<h1 align="center">Awesome Loop Generative Models</h1>

<p align="center">
  <b>A living reading map for generative models that revisit computation.</b><br>
  Companion paper collection for <i>Looping in Generative Models</i>.
</p>

<p align="center">
  <a href="#the-five-feedback-families">Taxonomy</a> ·
  <a href="#a-guided-reading-path">Reading path</a> ·
  <a href="#full-collection-by-reading-topic">Full collection</a> ·
  <a href="#contribute">Contribute</a>
</p>

<!-- LOOP-BOT:STATS:START -->
<p align="center">
  <img alt="listed works: 489" src="https://img.shields.io/badge/listed%20works-489-157f79?style=flat-square">
  <img alt="feedback families: 5" src="https://img.shields.io/badge/feedback%20families-5-6557a8?style=flat-square">
</p>

**489 research papers, model reports, and supporting references**, organized around five feedback families and related topics.
<!-- LOOP-BOT:STATS:END -->

## Why loops?

A model can spend more computation on a prediction by revisiting a learned
transformation. The important questions are **what state is updated, where it
returns, and which parameters are reused**. A deeper reasoning loop, another
denoising step, a longer memory, and an agent's next attempt spend computation
in different ways. This collection helps readers tell them apart.

Our main focus is **shared-parameter latent computation**. Sample refinement,
temporal memory, and agent feedback provide related views of recurrence.
The bibliography also includes foundations, comparisons, and evaluation tools;
it is a narrative selection, not an exhaustive census of the field.

## The five feedback families

<!-- LOOP-BOT:TAXONOMY:START -->
| Family | What returns to computation? | Question to ask |
| :-- | :-- | :-- |
| **[Recurrent depth](#1-recurrent-depth)** | Hidden state at a fixed prediction | How many times should a shared block refine the same prediction? |
| **[Latent feedback](#2-latent-feedback)** | Hidden representations passed across positions | Can a completed hidden representation become the next reasoning input? |
| **[Sample refinement](#3-sample-refinement)** | A sample and its auxiliary predictions | What information should survive between successive sample updates? |
| **[Temporal memory](#4-temporal-memory)** | Persistent state across inputs or observations | What should a model retain and update as new observations arrive? |
| **[Agent feedback](#5-agent-feedback)** | Feedback passed between model invocations | How can critique or experience improve the next model call? |
<!-- LOOP-BOT:TAXONOMY:END -->

## A guided reading path

Start with **Universal Transformers** and **Deep Equilibrium Models** for
shared computation and fixed-point views. Then follow recurrent-depth language
models into visual generation, or explore one of the other feedback interfaces.
The selections below are entry points rather than a ranking.

<!-- LOOP-BOT:READING:START -->
### 1. Recurrent depth

How many times should a shared block refine the same prediction?

- **2019** · [Universal Transformers](<https://arxiv.org/abs/1807.03819>)
- **2019** · [Deep Equilibrium Models](<https://arxiv.org/abs/1909.01377>)
- **2025** · [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](<https://arxiv.org/abs/2502.05171>)
- **2026** · [ELT: Elastic Looped Transformers for Visual Generation](<https://arxiv.org/abs/2604.09168>)

### 2. Latent feedback

Can a completed hidden representation become the next reasoning input?

- **2025** · [Training Large Language Models to Reason in a Continuous Latent Space](<https://arxiv.org/abs/2412.06769>)
- **2026** · [Pretraining Latent Information Feedback Transformers with Teacher Supervision](<https://arxiv.org/abs/2609.38149>)

### 3. Sample refinement

What information should survive between successive sample updates?

- **2022** · [Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning](<https://arxiv.org/abs/2208.04202>)
- **2022** · [Self-conditioned Embedding Diffusion for Text Generation](<https://arxiv.org/abs/2211.04236>)
- **2026** · [Few-Step Generation via Data-Space Iteration](<https://arxiv.org/abs/2610.12102>)

### 4. Temporal memory

What should a model retain and update as new observations arrive?

- **2022** · [Block-Recurrent Transformers](<https://arxiv.org/abs/2203.07852>)
- **2026** · [The Topological Trouble With Transformers](<https://arxiv.org/abs/2604.17121>)
- **2026** · [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](<https://arxiv.org/abs/2610.17434>)

### 5. Agent feedback

How can critique or experience improve the next model call?

- **2023** · [Reflexion: Language Agents with Verbal Reinforcement Learning](<https://arxiv.org/abs/2303.11366>)
- **2023** · [Self-Refine: Iterative Refinement with Self-Feedback](<https://papers.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html>)
<!-- LOOP-BOT:READING:END -->

## From research to model releases

Two provider reports give concrete examples of shared layers in released models.
These are architecture descriptions, not a controlled performance comparison.

| Model | Shared computation | Primary source |
| :-- | :-- | :-- |
| **Inkling 2 Mini** | Middle 12 layers run 3 times; 24 stored layers give 48 layer applications per token. | [Model card](https://thinkingmachines.ai/model-card/inkling-2-mini/) |
| **GLM-5.4** | A shared block of 28 layers runs for 2 iterations. | [Technical announcement](https://z.ai/blog/glm-5.4) |

## Recent additions

Dates below indicate when a work was added to this collection. Publication
years appear in the full reading list.

<!-- LOOP-BOT:RECENT:START -->
| Added | Paper | Reading topic |
| :-- | :-- | :-- |
| 2026-11-26 | [LoopDVR: Looped Transformer for Efficient Dense Visual Recognition](<https://arxiv.org/abs/2611.32067>) | Recurrent depth |
| 2026-11-24 | [NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation](<https://arxiv.org/abs/2611.06377>) | Training and execution |
| 2026-11-24 | [Hy-Nomas: Towards Free-form Interactive World Generation](<https://arxiv.org/abs/2610.36729>) | Temporal memory |
| 2026-11-24 | [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](<https://arxiv.org/abs/2610.17434>) | Temporal memory |
| 2026-11-24 | [Few-Step Generation via Data-Space Iteration](<https://arxiv.org/abs/2610.12102>) | Sample refinement |
| 2026-11-24 | [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](<https://arxiv.org/abs/2610.11756>) | Temporal memory |
| 2026-11-24 | [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](<https://arxiv.org/abs/2609.02886>) | Training and execution |
| 2026-11-24 | [Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models](<https://arxiv.org/abs/2605.18601>) | Temporal memory |
| 2026-11-24 | [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](<https://arxiv.org/abs/2605.16649>) | Foundations and related models |
| 2026-11-24 | [FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction](<https://arxiv.org/abs/2605.06509>) | Foundations and related models |

[Browse the complete bibliography →](PAPERS.md)
<!-- LOOP-BOT:RECENT:END -->

## Interpretability and oversight

Moving reasoning into hidden states can remove a readable chain of thought.
Keeping text does not, by itself, make that text a faithful explanation.
These papers provide a starting point for studying what a monitor can observe:

<!-- LOOP-BOT:OVERSIGHT:START -->
- **2025** · [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](<https://arxiv.org/abs/2507.11473>)
- **2025** · [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](<https://arxiv.org/abs/2503.11926>)
- **2025** · [Reasoning Models Don't Always Say What They Think](<https://arxiv.org/abs/2505.05410>)
- **2025** · [Monitoring Monitorability](<https://arxiv.org/abs/2512.18311>)
<!-- LOOP-BOT:OVERSIGHT:END -->

## Full collection by reading topic

Browse every reference in the topic groups below. Each work has one
primary reading topic. The five feedback families are complemented by sections
on foundations, training, and evaluation, including methods useful for comparison.

<!-- LOOP-BOT:CATALOG:START -->
| Reading topic | Listed works |
| :-- | --: |
| [Recurrent depth](#catalog-recurrent-depth) | 91 |
| [Latent feedback](#catalog-latent-feedback) | 25 |
| [Sample refinement](#catalog-sample-refinement) | 45 |
| [Temporal memory](#catalog-temporal-memory) | 99 |
| [Agent feedback](#catalog-agent-feedback) | 59 |
| [Foundations and related models](#catalog-foundations-and-related-models) | 36 |
| [Training and execution](#catalog-training-and-execution) | 114 |
| [Evaluation and interpretability](#catalog-evaluation-and-interpretability) | 20 |
| **Total** | **489** |

<a id="catalog-recurrent-depth"></a>
### Recurrent depth · 91 works

Shared blocks, adaptive depth, fixed points, and recurrent reasoning.

- **2026** · [ALoDLM: Adaptively Looped Diffusion Language Models](<https://arxiv.org/abs/2610.04198>)
- **2026** · [Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models](<https://arxiv.org/abs/2601.10679>)
- **2026** · [ARLoop: Fully-Open Pre-trained Looped Transformers with Attention Residuals](<https://arxiv.org/abs/2611.05234>)
- **2026** · [Beyond the Training Horizon: Mechanisms and Limits of Length Generalization in Looped Transformers](<https://arxiv.org/abs/2609.33144>)
- **2026** · [CART: Context-Anchored Recurrent Transformer -- A Parameter-Efficient Architecture with Learned Stability](<https://arxiv.org/abs/2606.01495>)
- **2026** · [CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield](<https://arxiv.org/abs/2606.31796>)
- **2026** · [Classical Energies Learn to Reason 1,000x Faster than Looped Models](<https://arxiv.org/abs/2611.17309>)
- **2026** · [Consistency Deep Equilibrium Models](<https://arxiv.org/abs/2602.03024>)
- **2026** · [DeepLoop: Depth Scaling for Looped Transformers](<https://arxiv.org/abs/2607.13491>)
- **2026** · [Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models](<https://arxiv.org/abs/2606.24898>)
- **2026** · [Depth Memory](<https://arxiv.org/abs/2610.18809>)
- **2026** · [Depth through recurrence: Looped transformers for flow-matching TTS](<https://arxiv.org/abs/2609.29768>)
- **2026** · [Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves](<https://arxiv.org/abs/2601.21582>)
- **2026** · [DiscoLoop: Looping Discrete Embeddings and Continuous Hidden States for Multi-hop Reasoning](<https://arxiv.org/abs/2607.00341>)
- **2026** · [ELT: Elastic Looped Transformers for Visual Generation](<https://arxiv.org/abs/2604.09168>)
- **2026** · [Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model](<https://arxiv.org/abs/2611.08977>)
- **2026** · [Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning](<https://arxiv.org/abs/2605.21488>)
- **2026** · [Fixed-Point Masked Generative Modeling](<https://arxiv.org/abs/2605.31215>)
- **2026** · [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](<https://arxiv.org/abs/2606.18206>)
- **2026** · [Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation](<https://arxiv.org/abs/2608.15062>)
- **2026** · [Generative Recursive Reasoning](<https://arxiv.org/abs/2605.19376>)
- **2026** · [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](<https://z.ai/blog/glm-5.4>)
- **2026** · [How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](<https://arxiv.org/abs/2609.19107>)
- **2026** · [How to Loop MoE: Flatten the Experts, Untie the Attention](<https://arxiv.org/abs/2609.35751>)
- **2026** · [How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference](<https://arxiv.org/abs/2610.40325>)
- **2026** · [HRM-Text: Efficient Pretraining Beyond Scaling](<https://arxiv.org/abs/2605.20613>)
- **2026** · [Hyperloop Transformers](<https://arxiv.org/abs/2604.21254>)
- **2026** · [Inkling 2 Mini Model Card](<https://thinkingmachines.ai/model-card/inkling-2-mini/>)
- **2026** · [LiFT: Loop Flow Transformers](<https://arxiv.org/abs/2610.05538>)
- **2026** · [Loop Dropout: Regularizing Shared Updates in Looped Language Models](<https://arxiv.org/abs/2609.34218>)
- **2026** · [Loop the Loopies!](<https://arxiv.org/abs/2607.16051>)
- **2026** · [Loop, Think, \\& Generalize: Implicit Reasoning in Recurrent-Depth Transformers](<https://arxiv.org/abs/2604.07822>)
- **2026** · [Loopback Transformer: Towards a Unified View of Residual Looped Transformers](<https://arxiv.org/abs/2611.07226>)
- **2026** · [LoopDVR: Looped Transformer for Efficient Dense Visual Recognition](<https://arxiv.org/abs/2611.32067>)
- **2026** · [Looped Diffusion Language Models](<https://arxiv.org/abs/2605.26106>)
- **2026** · [Looped Diffusion Transformer](<https://arxiv.org/abs/2609.40305>)
- **2026** · [LoopFormer: Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation](<https://arxiv.org/abs/2602.11451>)
- **2026** · [Looping Back to Move Forward: Recursive Transformers for Efficient and Flexible Large Multimodal Models](<https://arxiv.org/abs/2602.09080>)
- **2026** · [Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts](<https://arxiv.org/abs/2610.01153>)
- **2026** · [LoopMoE: Unifying Iterative Computation with Mixture-of-Experts for Language Modeling](<https://arxiv.org/abs/2606.04438>)
- **2026** · [LoopREG: Representation Supervision Enables Test-Time Recurrent Depth in Diffusion Transformers](<https://arxiv.org/abs/2610.17877>)
- **2026** · [LoOPSD: On-Policy Self-Distillation with Looped Teachers](<https://arxiv.org/abs/2610.18162>)
- **2026** · [LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models](<https://arxiv.org/abs/2605.11011>)
- **2026** · [LoopViT: Scaling Visual ARC with Looped Transformers](<https://arxiv.org/abs/2602.02156>)
- **2026** · [LoopVL: Recurrent Visual Intelligence](<https://arxiv.org/abs/2609.38426>)
- **2026** · [LT2: Linear-Time Looped Transformers](<https://arxiv.org/abs/2605.20670>)
- **2026** · [One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models](<https://arxiv.org/abs/2604.18839>)
- **2026** · [Parcae: Scaling Laws For Stable Looped Language Models](<https://arxiv.org/abs/2604.12946>)
- **2026** · [Probabilistic Tiny Recursive Model](<https://arxiv.org/abs/2605.19943>)
- **2026** · [Recursive Inference Machines for Neural Reasoning](<https://arxiv.org/abs/2603.05234>)
- **2026** · [Recursive Scaling in Masked Diffusion Models](<https://arxiv.org/abs/2606.18022>)
- **2026** · [Retrofitting Recurrent Vision-Language Models from Pretrained Backbones](<https://arxiv.org/abs/2610.22075>)
- **2026** · [Scaling Laws for Looped Mixture of Experts](<https://arxiv.org/abs/2609.40316>)
- **2026** · [Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention Residuals](<https://arxiv.org/abs/2610.11570>)
- **2026** · [Simply Stabilizing the Loop via Fully Looped Transformer](<https://arxiv.org/abs/2605.18797>)
- **2026** · [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](<https://arxiv.org/abs/2606.06574>)
- **2026** · [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](<https://arxiv.org/abs/2609.01343>)
- **2026** · [Solve the Loop: Attractor Models for Language and Reasoning](<https://arxiv.org/abs/2605.12466>)
- **2026** · [Sparse Layers are Critical to Scaling Looped Language Models](<https://arxiv.org/abs/2605.09165>)
- **2026** · [Spherical Fixed-Point Reasoners: Adaptive Loop Halting on the Hypersphere](<https://arxiv.org/abs/2610.25646>)
- **2026** · [SpiralFormer: Looped Transformers Can Learn Hierarchical Dependencies via Multi-Resolution Recursion](<https://arxiv.org/abs/2602.11698>)
- **2026** · [Stability and Generalization in Looped Transformers](<https://arxiv.org/abs/2604.15259>)
- **2026** · [Stabilizing Extrapolation in Looped Transformers via Learned Stochastic Stopping](<https://arxiv.org/abs/2606.29983>)
- **2026** · [Tiny Autoregressive Recursive Models](<https://arxiv.org/abs/2603.08082>)
- **2026** · [Towards Looped Models Done Right. Part I: Topology, Input Injection, Recurrent-State Design](<https://huskydoge.github.io/husky-blog/posts/recursive_models/towards-looped-models-done-right/>)
- **2026** · [Training-Free Looped Transformers](<https://arxiv.org/abs/2605.23872>)
- **2026** · [Universal YOCO for Efficient Depth Scaling](<https://arxiv.org/abs/2604.01220>)
- **2026** · [What Makes Recurrence Effective in Looped Language Models?](<https://arxiv.org/abs/2609.36636>)
- **2025** · [Encode, Think, Decode: Scaling test-time reasoning with recursive latent thoughts](<https://arxiv.org/abs/2510.07358>)
- **2025** · [Hierarchical Reasoning Model](<https://arxiv.org/abs/2506.21734>)
- **2025** · [Hierarchical Reasoning Models: Perspectives and Misconceptions](<https://arxiv.org/abs/2510.00355>)
- **2025** · [Improving Recursive Transformers with Mixture of LoRAs](<https://arxiv.org/abs/2512.12880>)
- **2025** · [Less is More: Recursive Reasoning with Tiny Networks](<https://arxiv.org/abs/2510.04871>)
- **2025** · [MeSH: Memory-as-State-Highways for Recursive Transformers](<https://arxiv.org/abs/2510.07739>)
- **2025** · [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](<https://arxiv.org/abs/2507.10524>)
- **2025** · [Recursive Inference Scaling: A Winning Path to Scalable Inference in Language and Multimodal Systems](<https://arxiv.org/abs/2502.07503>)
- **2025** · [Scaling Latent Reasoning via Looped Language Models](<https://arxiv.org/abs/2510.25741>)
- **2025** · [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](<https://arxiv.org/abs/2502.05171>)
- **2025** · [Skip a Layer or Loop it? Test-Time Depth Adaptation of Pretrained LLMs](<https://arxiv.org/abs/2507.07996>)
- **2025** · [Teaching Pretrained Language Models to Think Deeper with Retrofitted Recurrence](<https://arxiv.org/abs/2511.07384>)
- **2025** · [Universal Reasoning Model](<https://arxiv.org/abs/2512.14693>)
- **2024** · [Fixed Point Diffusion Models](<https://arxiv.org/abs/2401.08741>)
- **2024** · [Investigating Recurrent Transformers with Dynamic Halt](<https://arxiv.org/abs/2402.00976>)
- **2024** · [MoEUT: Mixture-of-Experts Universal Transformers](<https://arxiv.org/abs/2405.16039>)
- **2024** · [Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](<https://arxiv.org/abs/2410.20672>)
- **2023** · [CoTFormer: A Chain-of-Thought Driven Architecture with Budget-Adaptive Computation Cost at Inference](<https://arxiv.org/abs/2310.10845>)
- **2023** · [One-Step Diffusion Distillation via Deep Equilibrium Models](<https://arxiv.org/abs/2401.08639>)
- **2023** · [Sparse Universal Transformer](<https://aclanthology.org/2023.emnlp-main.12/>)
- **2022** · [Deep Equilibrium Approaches to Diffusion Models](<https://arxiv.org/abs/2210.12867>)
- **2019** · [Deep Equilibrium Models](<https://arxiv.org/abs/1909.01377>)
- **2019** · [Universal Transformers](<https://arxiv.org/abs/1807.03819>)

<a id="catalog-latent-feedback"></a>
### Latent feedback · 25 works

Hidden-state reasoning and feedback across token positions.

- **2026** · [$T^2$MLR: Transformer with Temporal Middle-Layer Recurrence](<https://arxiv.org/abs/2607.15178>)
- **2026** · [AdaPonderLM: Gated Pondering Language Models with Token-Wise Adaptive Depth](<https://arxiv.org/abs/2603.01914>)
- **2026** · [Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers](<https://arxiv.org/abs/2606.31779>)
- **2026** · [Full-bandwidth transformer](<https://arxiv.org/abs/2608.08888>)
- **2026** · [Latent Recurrent Transformer: Architecture Exploration, Training Strategies, and Scaling Behavior](<https://arxiv.org/abs/2605.26797>)
- **2026** · [Length Generalization with Log-Depth Recurrent Units](<https://arxiv.org/abs/2605.26035>)
- **2026** · [Log-Depth Recurrent Language Modeling](<https://arxiv.org/abs/2609.28212>)
- **2026** · [PonderLM-3: Adaptive Token-Wise Pondering with Differentiable Masking](<https://arxiv.org/abs/2603.02023>)
- **2026** · [Pretraining Latent Information Feedback Transformers with Teacher Supervision](<https://arxiv.org/abs/2609.38149>)
- **2026** · [Reasoning with Latent Tokens in Diffusion Language Models](<https://arxiv.org/abs/2602.03769>)
- **2026** · [Recirculation](<https://arxiv.org/abs/2608.17981>)
- **2026** · [Recurrent Looped Transformer](<https://arxiv.org/abs/2610.07591>)
- **2026** · [Register Tokens for Bounded-State Reasoning in Diffusion Language Models](<https://arxiv.org/abs/2609.16372>)
- **2026** · [The Recurrent Transformer: Greater Effective Depth and Efficient Decoding](<https://arxiv.org/abs/2604.21215>)
- **2026** · [Write Back the $\\Delta$: Revisiting the Same Tokens with Fresh Representations](<https://arxiv.org/abs/2609.32457>)
- **2025** · [Hybrid Latent Reasoning via Reinforcement Learning](<https://arxiv.org/abs/2505.18454>)
- **2025** · [PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space](<https://arxiv.org/abs/2509.23184>)
- **2025** · [PonderLM: Pretraining Language Models to Ponder in Continuous Space](<https://arxiv.org/abs/2505.20674>)
- **2025** · [Training Large Language Models to Reason in a Continuous Latent Space](<https://arxiv.org/abs/2412.06769>)
- **2024** · [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](<https://arxiv.org/abs/2405.14838>)
- **2024** · [Hopping Too Late: Exploring the Limitations of Large Language Models on Multi-Hop Queries](<https://aclanthology.org/2024.emnlp-main.781/>)
- **2024** · [Let's Think Dot by Dot: Hidden Computation in Transformer Language Models](<https://arxiv.org/abs/2404.15758>)
- **2023** · [Implicit Chain of Thought Reasoning via Knowledge Distillation](<https://arxiv.org/abs/2311.01460>)
- **2023** · [Think before you speak: Training Language Models With Pause Tokens](<https://arxiv.org/abs/2310.02226>)
- **2020** · [Addressing Some Limitations of Transformers with Feedback Memory](<https://arxiv.org/abs/2002.09402>)

<a id="catalog-sample-refinement"></a>
### Sample refinement · 45 works

Iterative generation, self-conditioning, and related sampling methods.

- **2026** · [Coevolving Representations in Joint Image-Feature Diffusion](<https://arxiv.org/abs/2604.17492>)
- **2026** · [CORE: Context-Robust Remasking for Diffusion Language Models](<https://arxiv.org/abs/2602.04096>)
- **2026** · [Dino Forcing Flow Models: Do not denoise what you can predict](<https://arxiv.org/abs/2610.11751>)
- **2026** · [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models](<https://arxiv.org/abs/2609.37533>)
- **2026** · [Equilibrium Forcing: Adaptive Video Generation Without Noise Conditioning](<https://arxiv.org/abs/2608.14706>)
- **2026** · [Few-Step Generation via Data-Space Iteration](<https://arxiv.org/abs/2610.12102>) — A shared generator repeatedly refines its current data estimate, conditioned on source noise and iteration, using distribution matching.
- **2026** · [Flow Reasoning Models: Turning Flows Into Efficient Recurrent Reasoners](<https://arxiv.org/abs/2606.29150>)
- **2026** · [Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](<https://arxiv.org/abs/2602.11401>)
- **2026** · [Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models](<https://arxiv.org/abs/2606.16700>)
- **2026** · [Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces](<https://arxiv.org/abs/2609.40362>)
- **2026** · [Reasoning on the Simplex: Geometric Fixed-Point Models](<https://arxiv.org/abs/2609.33540>)
- **2026** · [Residual Context Diffusion Language Models](<https://arxiv.org/abs/2601.22954>)
- **2026** · [Self-conditioned Flow Map Language Models via Fixed-point Flows](<https://arxiv.org/abs/2607.00714>)
- **2026** · [Simple Self-Conditioning Adaptation for Masked Diffusion Models](<https://arxiv.org/abs/2604.26985>)
- **2026** · [Thinking with Looped Flows](<https://arxiv.org/abs/2609.11801>)
- **2026** · [V-Co: A Closer Look at Visual Representation Alignment via Co-Denoising](<https://arxiv.org/abs/2603.16792>)
- **2025** · [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](<https://arxiv.org/abs/2503.09573>)
- **2025** · [Boosting Generative Image Modeling via Joint Image-Feature Synthesis](<https://arxiv.org/abs/2504.16064>)
- **2025** · [Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner](<https://arxiv.org/abs/2510.03206>)
- **2025** · [Don't Settle Too Early: Self-Reflective Remasking for Diffusion Language Models](<https://arxiv.org/abs/2509.23653>)
- **2025** · [Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement](<https://arxiv.org/abs/2511.05562>)
- **2025** · [Energy-Based Transformers are Scalable Learners and Thinkers](<https://arxiv.org/abs/2507.02092>)
- **2025** · [Lookahead Unmasking Elicits Accurate Decoding in Diffusion Language Models](<https://arxiv.org/abs/2511.05563>)
- **2025** · [REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion](<https://arxiv.org/abs/2512.16636>)
- **2025** · [Remasking Discrete Diffusion Models with Inference-Time Scaling](<https://arxiv.org/abs/2503.00307>)
- **2025** · [Representation Entanglement for Generation: Training Diffusion Transformers Is Much Easier Than You Think](<https://arxiv.org/abs/2507.01467>)
- **2025** · [Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](<https://arxiv.org/abs/2512.04926>)
- **2024** · [Searching Latent Program Spaces](<https://arxiv.org/abs/2411.08706>)
- **2023** · [Consistency Models](<https://proceedings.mlr.press/v202/song23a.html>)
- **2023** · [Flow Matching for Generative Modeling](<https://openreview.net/forum?id=PqvMRDCJT9t>)
- **2023** · [TESS: Text-to-Text Self-Conditioned Simplex Diffusion](<https://arxiv.org/abs/2305.08379>)
- **2022** · [Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning](<https://arxiv.org/abs/2208.04202>)
- **2022** · [MaskGIT: Masked Generative Image Transformer](<https://openaccess.thecvf.com/content/CVPR2022/html/Chang_MaskGIT_Masked_Generative_Image_Transformer_CVPR_2022_paper.html>)
- **2022** · [Scalable Adaptive Computation for Iterative Generation](<https://arxiv.org/abs/2212.11972>)
- **2022** · [Self-conditioned Embedding Diffusion for Text Generation](<https://arxiv.org/abs/2211.04236>)
- **2020** · [Denoising Diffusion Probabilistic Models](<https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html>)
- **2019** · [Levenshtein Transformer](<https://arxiv.org/abs/1905.11006>)
- **2019** · [Mask-Predict: Parallel Decoding of Conditional Masked Language Models](<https://aclanthology.org/D19-1633/>)
- **2018** · [Deterministic Non-Autoregressive Neural Sequence Modeling by Iterative Refinement](<https://arxiv.org/abs/1802.06901>)
- **2017** · [Learning to Generate Samples from Noise through Infusion Training](<https://arxiv.org/abs/1703.06975>)
- **2017** · [Variational Walkback: Learning a Transition Operator as a Stochastic Recurrent Net](<https://arxiv.org/abs/1711.02282>)
- **2015** · [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](<https://arxiv.org/abs/1503.03585>)
- **2015** · [DRAW: A Recurrent Neural Network For Image Generation](<https://proceedings.mlr.press/v37/gregor15.html>)
- **2014** · [Iterative Neural Autoregressive Distribution Estimator (NADE-k)](<https://arxiv.org/abs/1406.1485>)
- **2013** · [Deep Generative Stochastic Networks Trainable by Backprop](<https://arxiv.org/abs/1306.1091>)

<a id="catalog-temporal-memory"></a>
### Temporal memory · 99 works

Persistent state, sequence models, and memory in video world models.

- **2026** · [$\\delta$-mem: Efficient Online Memory for Large Language Models](<https://arxiv.org/abs/2605.12357>)
- **2026** · [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](<https://arxiv.org/abs/2606.17730>)
- **2026** · [AdaState: Self-Evolving Anchors for Streaming Video Generation](<https://arxiv.org/abs/2605.30349>)
- **2026** · [Addressable Memory for Video World Models](<https://arxiv.org/abs/2608.07408>)
- **2026** · [Advancing Open-source World Models](<https://arxiv.org/abs/2601.20540>) — LingBot-World adapts video diffusion to causal generation with cached history and interactive action conditioning.
- **2026** · [Anchor Forcing: Anchor Memory and Tri-Region RoPE for Interactive Streaming Video Diffusion](<https://arxiv.org/abs/2603.13405>)
- **2026** · [AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories](<https://arxiv.org/abs/2602.14941>)
- **2026** · [Composition of Memory Experts for Diffusion World Models](<https://arxiv.org/abs/2605.18813>)
- **2026** · [Continuous Memory Machines](<https://arxiv.org/abs/2610.07907>)
- **2026** · [Dynamic Compression in Recurrent Networks](<https://arxiv.org/abs/2608.17896>)
- **2026** · [DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time](<https://arxiv.org/abs/2609.35704>)
- **2026** · [Fast Weight Attention for Continual Learning](<https://arxiv.org/abs/2608.27763>)
- **2026** · [Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments](<https://arxiv.org/abs/2601.01075>)
- **2026** · [Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](<https://arxiv.org/abs/2604.06939>)
- **2026** · [Hy-Nomas: Towards Free-form Interactive World Generation](<https://arxiv.org/abs/2610.36729>) — Segment-wise causal generation reuses cached text and video history, with action-aware masking for successive instructions.
- **2026** · [Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models](<https://arxiv.org/abs/2605.18601>) — Per-frame language control is combined with a sliding history cache, bounded positions, and self-forcing distillation.
- **2026** · [Latent Spatial Memory for Video World Models](<https://arxiv.org/abs/2606.09828>)
- **2026** · [Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models](<https://arxiv.org/abs/2609.34677>)
- **2026** · [LiveWorld: Simulating Out-of-Sight Dynamics in Generative Video World Models](<https://arxiv.org/abs/2603.07145>)
- **2026** · [LoL: Longer than Longer, Scaling Video Generation to Hour](<https://arxiv.org/abs/2601.16914>)
- **2026** · [Long-Horizon Streaming Video Generation via Hybrid Attention with Decoupled Distillation](<https://arxiv.org/abs/2604.10103>)
- **2026** · [Looped World Models](<https://arxiv.org/abs/2606.18208>)
- **2026** · [Marionette: Predicting World States, Rendering Geometry, Painting Appearance](<https://arxiv.org/abs/2608.14530>)
- **2026** · [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory](<https://arxiv.org/abs/2604.08995>)
- **2026** · [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](<https://arxiv.org/abs/2608.29910>)
- **2026** · [MemCam: Memory-Augmented Camera Control for Consistent Video Generation](<https://arxiv.org/abs/2603.26193>)
- **2026** · [MemLearner: Learning to Query Context memory for Video World Models](<https://arxiv.org/abs/2606.31734>)
- **2026** · [Memorize When Needed: Decoupled Memory Control for Spatially Consistent Long-Horizon Video Generation](<https://arxiv.org/abs/2604.18215>)
- **2026** · [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](<https://arxiv.org/abs/2610.11756>) — Archive and working cache banks retain intermediate events alongside recent motion, with bank-aware temporal positions.
- **2026** · [MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](<https://arxiv.org/abs/2603.12513>)
- **2026** · [MilliVid: Hierarchical Latents for Long-Range Consistency in Video Generation](<https://arxiv.org/abs/2606.09056>)
- **2026** · [Modular TTT: Rethinking Test-Time Training as Composable Modules](<https://arxiv.org/abs/2608.07110>)
- **2026** · [MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](<https://arxiv.org/abs/2603.17117>)
- **2026** · [Multi-Head Recurrent Memory Agents](<https://arxiv.org/abs/2607.01523>)
- **2026** · [Pooling Representation Autoencoders for Efficient Diffusion](<https://arxiv.org/abs/2610.09242>)
- **2026** · [Proteus: Incremental Memory Activation for Long-Context Sequence Modeling](<https://arxiv.org/abs/2608.16844>)
- **2026** · [RAE-NWM: Navigation World Model in Dense Visual Representation Space](<https://arxiv.org/abs/2603.09241>)
- **2026** · [Relax Forcing: Relaxed KV-Memory for Consistent Long Video Generation](<https://arxiv.org/abs/2603.21366>)
- **2026** · [Retrieval-Aware Distillation for Transformer-SSM Hybrids](<https://arxiv.org/abs/2602.11374>) — Retrieval-critical attention heads are retained while other heads are distilled into recurrent state-space components.
- **2026** · [ReWorld: An Interactive World Model with Long-Horizon Memory](<https://arxiv.org/abs/2608.23565>)
- **2026** · [SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](<https://arxiv.org/abs/2605.15178>)
- **2026** · [SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](<https://arxiv.org/abs/2610.00686>)
- **2026** · [Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](<https://arxiv.org/abs/2610.02521>)
- **2026** · [Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers](<https://arxiv.org/abs/2607.21594>)
- **2026** · [Switching Linear Attention](<https://arxiv.org/abs/2609.39034>)
- **2026** · [The Topological Trouble With Transformers](<https://arxiv.org/abs/2604.17121>)
- **2026** · [UCM: Unified Modeling of Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](<https://arxiv.org/abs/2602.22960>)
- **2026** · [V-RAE: Rethinking Video Latent Spaces for Generation](<https://arxiv.org/abs/2608.13556>)
- **2026** · [Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](<https://arxiv.org/abs/2609.20744>)
- **2026** · [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](<https://arxiv.org/abs/2610.17434>) — Pose-indexed fast weights consolidate evicted visual history through recursive least-squares updates and support later memory reads.
- **2026** · [WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](<https://arxiv.org/abs/2609.34606>)
- **2026** · [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](<https://arxiv.org/abs/2609.24984>)
- **2026** · [WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon](<https://arxiv.org/abs/2609.35560>)
- **2026** · [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](<https://arxiv.org/abs/2609.21712>)
- **2025** · [Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval](<https://arxiv.org/abs/2506.03141>)
- **2025** · [DeltaProduct: Improving State-Tracking in Linear RNNs via Householder Products](<https://arxiv.org/abs/2502.10297>)
- **2025** · [End-to-End Test-Time Training for Long Context](<https://arxiv.org/abs/2512.23675>)
- **2025** · [Frame Context Packing and Drift Prevention in Next-Frame-Prediction Video Diffusion Models](<https://arxiv.org/abs/2504.12626>)
- **2025** · [GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control](<https://arxiv.org/abs/2503.03751>)
- **2025** · [Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout](<https://arxiv.org/abs/2511.20649>)
- **2025** · [Long-Context State-Space Video World Models](<https://arxiv.org/abs/2505.20171>)
- **2025** · [Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents](<https://arxiv.org/abs/2509.23040>)
- **2025** · [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](<https://arxiv.org/abs/2507.02259>)
- **2025** · [One-Minute Video Generation with Test-Time Training](<https://arxiv.org/abs/2504.05298>)
- **2025** · [Recurrent Autoregressive Diffusion: Global Memory Meets Local Attention](<https://arxiv.org/abs/2511.12940>)
- **2025** · [RELIC: Interactive Video World Model with Long-Horizon Memory](<https://arxiv.org/abs/2512.04040>)
- **2025** · [RIFLEx: A Free Lunch for Length Extrapolation in Video Diffusion Transformers](<https://arxiv.org/abs/2502.15894>)
- **2025** · [Spatia: Video Generation with Updatable Spatial Memory](<https://arxiv.org/abs/2512.15716>)
- **2025** · [Test-time regression: a unifying framework for designing sequence models with associative memory](<https://arxiv.org/abs/2501.12352>)
- **2025** · [UltraViCo: Breaking Extrapolation Limits in Video Diffusion Transformers](<https://arxiv.org/abs/2511.20123>)
- **2025** · [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](<https://arxiv.org/abs/2411.12537>)
- **2025** · [Video World Models with Long-term Spatial Memory](<https://arxiv.org/abs/2506.05284>)
- **2025** · [VideoSSM: Autoregressive Long Video Generation with Hybrid State-Space Memory](<https://arxiv.org/abs/2512.04519>)
- **2025** · [VMem: Consistent Interactive Video Scene Generation with Surfel-Indexed View Memory](<https://arxiv.org/abs/2506.18903>)
- **2025** · [VRAG: Learning World Models for Interactive Video Generation](<https://arxiv.org/abs/2505.21996>)
- **2025** · [WORLDMEM: Long-term Consistent World Simulation with Memory](<https://arxiv.org/abs/2504.12369>)
- **2025** · [WorldPack: Dynamic Frame Compression for Long-context Video World Modeling](<https://arxiv.org/abs/2512.02473>)
- **2025** · [WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](<https://arxiv.org/abs/2512.14614>)
- **2024** · [Gated Delta Networks: Improving Mamba2 with Delta Rule](<https://arxiv.org/abs/2412.06464>)
- **2024** · [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](<https://arxiv.org/abs/2407.04620>)
- **2024** · [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](<https://arxiv.org/abs/2404.07143>)
- **2024** · [Parallelizing Linear Transformers with the Delta Rule over Sequence Length](<https://arxiv.org/abs/2406.06484>)
- **2024** · [The Illusion of State in State-Space Models](<https://proceedings.mlr.press/v235/merrill24a.html>)
- **2024** · [Titans: Learning to Memorize at Test Time](<https://arxiv.org/abs/2501.00663>)
- **2024** · [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](<https://arxiv.org/abs/2405.21060>)
- **2023** · [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](<https://arxiv.org/abs/2312.00752>)
- **2023** · [RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](<https://arxiv.org/abs/2305.13304>)
- **2022** · [Block-Recurrent Transformers](<https://arxiv.org/abs/2203.07852>)
- **2022** · [Memorizing Transformers](<https://arxiv.org/abs/2203.08913>)
- **2022** · [Recurrent Memory Transformer](<https://arxiv.org/abs/2207.06881>)
- **2021** · [Linear Transformers Are Secretly Fast Weight Memory Systems](<https://arxiv.org/abs/2102.11174>)
- **2020** · [Memformer: The Memory-Augmented Transformer](<https://arxiv.org/abs/2010.06891>)
- **2020** · [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](<https://arxiv.org/abs/2006.16236>)
- **2019** · [Compressive Transformers for Long-Range Sequence Modelling](<https://arxiv.org/abs/1911.05507>)
- **2019** · [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](<https://arxiv.org/abs/1901.02860>)
- **2018** · [Recurrent World Models Facilitate Policy Evolution](<https://arxiv.org/abs/1809.01999>)
- **2017** · [Recurrent Environment Simulators](<https://arxiv.org/abs/1704.02254>)
- **2016** · [Using Fast Weights to Attend to the Recent Past](<https://arxiv.org/abs/1610.06258>)
- **1992** · [Learning to Control Fast-Weight Memories: An Alternative to Dynamic Recurrent Networks](<https://people.idsia.ch/~juergen/fastweights/>)

<a id="catalog-agent-feedback"></a>
### Agent feedback · 59 works

Critique, search, tool use, and feedback between model calls.

- **2026** · [4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes](<https://arxiv.org/abs/2610.03715>)
- **2026** · [AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward](<https://arxiv.org/abs/2605.12495>)
- **2026** · [AutoHarness: improving LLM agents by automatically synthesizing a code harness](<https://arxiv.org/abs/2603.03329>)
- **2026** · [ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction](<https://arxiv.org/abs/2605.14398>)
- **2026** · [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](<https://arxiv.org/abs/2609.26458>)
- **2026** · [Code Video Model](<https://code-video-model.github.io/tech_report.pdf>)
- **2026** · [Code World Model: Coding Agent as World Brain](<https://arxiv.org/abs/2608.25927>)
- **2026** · [Gen-Searcher: Reinforcing Agentic Search for Image Generation](<https://arxiv.org/abs/2603.28767>)
- **2026** · [Harness Learning Enables Generalizable Test-Time Adaptation](<https://arxiv.org/abs/2609.35738>)
- **2026** · [Meta-Harness: End-to-End Optimization of Model Harnesses](<https://arxiv.org/abs/2603.28052>)
- **2026** · [NEWTON: Agentic Planning for Physically Grounded Video Generation](<https://arxiv.org/abs/2605.18396>)
- **2026** · [Programmable World Model](<https://arxiv.org/abs/2609.10540>)
- **2026** · [Recursive Multi-Agent Systems](<https://arxiv.org/abs/2604.25917>)
- **2026** · [Rethinking the Evaluation of Harness Evolution for Agents](<https://arxiv.org/abs/2607.12227>)
- **2026** · [Temporal Backtracking Search for Test-time Generative Video Reasoning](<https://arxiv.org/abs/2606.13861>)
- **2026** · [Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning](<https://arxiv.org/abs/2609.38147>)
- **2026** · [TTHE: Test-Time Harness Evolution](<https://arxiv.org/abs/2607.08124>)
- **2026** · [VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](<https://arxiv.org/abs/2607.27380>)
- **2026** · [VideoGen-Agent: Reinforcing Video Generation Agents](<https://arxiv.org/abs/2609.24997>)
- **2026** · [Vision-as-Inverse-Graphics Agent via Interleaved Multimodal Reasoning](<https://arxiv.org/abs/2601.11109>)
- **2026** · [X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving](<https://arxiv.org/abs/2606.28758>)
- **2025** · [A-MEM: Agentic Memory for LLM Agents](<https://arxiv.org/abs/2502.12110>)
- **2025** · [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](<https://arxiv.org/abs/2510.04618>)
- **2025** · [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](<https://arxiv.org/abs/2510.03215>)
- **2025** · [Code World Models for General Game Playing](<https://arxiv.org/abs/2510.04542>)
- **2025** · [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](<https://arxiv.org/abs/2505.22954>)
- **2025** · [Enabling Agents to Communicate Entirely in Latent Space](<https://arxiv.org/abs/2511.09149>)
- **2025** · [KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems](<https://arxiv.org/abs/2510.12872>)
- **2025** · [Latent Collaboration in Multi-Agent Systems](<https://arxiv.org/abs/2511.20639>)
- **2025** · [Maestro: Self-Improving Text-to-Image Generation via Agent Orchestration](<https://arxiv.org/abs/2509.10704>)
- **2025** · [Optimizing generative AI by backpropagating language model feedback](<https://www.nature.com/articles/s41586-025-08661-4>)
- **2025** · [PoE-World: Compositional World Modeling with Products of Programmatic Experts](<https://arxiv.org/abs/2505.10819>)
- **2025** · [Recursive Language Models](<https://arxiv.org/abs/2512.24601>)
- **2025** · [Scaling Image and Video Generation via Test-Time Evolutionary Search](<https://arxiv.org/abs/2505.17618>)
- **2025** · [VChain: Chain-of-Visual-Thought for Reasoning in Video Generation](<https://arxiv.org/abs/2510.05094>)
- **2025** · [Video-T1: Test-Time Scaling for Video Generation](<https://arxiv.org/abs/2503.18942>)
- **2025** · [VideoCoF: Unified Video Editing with Temporal Reasoner](<https://arxiv.org/abs/2512.07469>)
- **2025** · [VISTA: A Test-Time Self-Improving Video Generation Agent](<https://arxiv.org/abs/2510.15831>)
- **2024** · [BlenderAlchemy: Editing 3D Graphics with Vision-Language Models](<https://arxiv.org/abs/2404.17672>)
- **2024** · [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](<https://arxiv.org/abs/2405.15383>)
- **2024** · [Large Language Models have Intrinsic Self-Correction Ability](<https://arxiv.org/abs/2406.15673>)
- **2024** · [PhyT2V: LLM-Guided Iterative Self-Refinement for Physics-Grounded Text-to-Video Generation](<https://arxiv.org/abs/2412.00596>)
- **2024** · [Training Language Models to Self-Correct via Reinforcement Learning](<https://arxiv.org/abs/2409.12917>)
- **2024** · [VideoAgent: Self-Improving Video Generation](<https://arxiv.org/abs/2410.10076>)
- **2024** · [WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment](<https://arxiv.org/abs/2402.12275>)
- **2023** · [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](<https://arxiv.org/abs/2305.11738>)
- **2023** · [Large Language Models Cannot Self-Correct Reasoning Yet](<https://arxiv.org/abs/2310.01798>)
- **2023** · [Let Models Speak Ciphers: Multiagent Debate through Embeddings](<https://arxiv.org/abs/2310.06272>)
- **2023** · [MemGPT: Towards LLMs as Operating Systems](<https://arxiv.org/abs/2310.08560>)
- **2023** · [Reflexion: Language Agents with Verbal Reinforcement Learning](<https://arxiv.org/abs/2303.11366>)
- **2023** · [Self-Refine: Iterative Refinement with Self-Feedback](<https://papers.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html>)
- **2023** · [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](<https://arxiv.org/abs/2310.02304>)
- **2023** · [Teaching Large Language Models to Self-Debug](<https://arxiv.org/abs/2304.05128>)
- **2023** · [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](<https://arxiv.org/abs/2305.10601>)
- **2022** · [Generating Sequences by Learning to Self-Correct](<https://arxiv.org/abs/2211.00053>)
- **2022** · [PEER: A Collaborative Language Model](<https://arxiv.org/abs/2208.11663>)
- **2022** · [Re3: Generating Longer Stories With Recursive Reprompting and Revision](<https://arxiv.org/abs/2210.06774>)
- **2022** · [ReAct: Synergizing Reasoning and Acting in Language Models](<https://arxiv.org/abs/2210.03629>)
- **2021** · [Learning to Repair: Repairing model output errors after deployment using a dynamic memory of feedback](<https://arxiv.org/abs/2112.09737>)

<a id="catalog-foundations-and-related-models"></a>
### Foundations and related models · 36 works

Theory, surveys, parameter sharing, and comparison architectures.

- **2026** · [AtlasVid: Efficient Ultra-High-Resolution Long Video Generation via Decoupled Global-Local Modeling](<https://arxiv.org/abs/2605.16649>) — A global semantic proxy guides local high-resolution denoising; a comparison for scaling long-video generation.
- **2026** · [Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation](<https://arxiv.org/abs/2605.30757>)
- **2026** · [FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction](<https://arxiv.org/abs/2605.06509>) — Global-local singular-spectrum fusion extends video generation without training; a comparison for temporal consistency.
- **2026** · [Inference and learning in sparse autoencoders as natural gradient flow](<https://arxiv.org/abs/2610.07389>)
- **2026** · [Looped Transformers with Layer Normalization Provably Learn the Power Method](<https://arxiv.org/abs/2606.00605>)
- **2026** · [When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied Looped Transformers](<https://arxiv.org/abs/2607.20594>)
- **2025** · [A Formal Comparison Between Chain of Thought and Latent Thought](<https://arxiv.org/abs/2509.25239>)
- **2025** · [A Little Depth Goes a Long Way: The Expressive Power of Log-Depth Transformers](<https://arxiv.org/abs/2503.03961>)
- **2025** · [A Survey on Latent Reasoning](<https://arxiv.org/abs/2507.06203>)
- **2025** · [A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?](<https://arxiv.org/abs/2503.24235>)
- **2025** · [Looped Transformers for Length Generalization](<https://arxiv.org/abs/2409.15647>)
- **2025** · [On Expressive Power of Looped Transformers: Theoretical Analysis and Enhancement via Timestep Encoding](<https://arxiv.org/abs/2410.01405>)
- **2025** · [Reasoning by Superposition: A Theoretical Perspective on Chain of Continuous Thought](<https://arxiv.org/abs/2505.12514>)
- **2025** · [Reasoning with Latent Thoughts: On the Power of Looped Transformers](<https://arxiv.org/abs/2502.17416>)
- **2025** · [To CoT or To Loop? A Formal Comparison Between Chain-of-Thought and Looped Transformers](<https://arxiv.org/abs/2505.19245>)
- **2025** · [What Makes Looped Transformers Perform Better Than Non-Recursive Ones](<https://arxiv.org/abs/2510.10089>)
- **2024** · [AlgoFormer: An Efficient Transformer Framework with Algorithmic Structures](<https://arxiv.org/abs/2402.13572>)
- **2024** · [Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?](<https://arxiv.org/abs/2410.08292>)
- **2024** · [Diffusion Models and Representation Learning: A Survey](<https://arxiv.org/abs/2407.00783>)
- **2024** · [Looped Transformers are Better at Learning Learning Algorithms](<https://arxiv.org/abs/2311.12424>)
- **2024** · [On the Role of Depth and Looping for In-Context Learning with Task Diversity](<https://arxiv.org/abs/2410.21698>)
- **2024** · [Simulation of Graph Algorithms with Looped Transformers](<https://arxiv.org/abs/2402.01107>)
- **2023** · [Looped Transformers as Programmable Computers](<https://arxiv.org/abs/2301.13196>)
- **2023** · [Scalable Diffusion Models with Transformers](<https://openaccess.thecvf.com/content/ICCV2023/html/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.html>)
- **2023** · [The Parallelism Tradeoff: Limitations of Log-Precision Transformers](<https://aclanthology.org/2023.tacl-1.31/>)
- **2023** · [Transformers Learn Shortcuts to Automata](<https://openreview.net/forum?id=De4FYqjFueZ>)
- **2022** · [End-to-end Algorithm Synthesis with Recurrent Networks: Logical Extrapolation Without Overthinking](<https://arxiv.org/abs/2202.05826>)
- **2022** · [Path Independent Equilibrium Models Can Better Exploit Test-Time Computation](<https://arxiv.org/abs/2211.09961>)
- **2021** · [Can You Learn an Algorithm? Generalizing from Easy to Hard Problems with Recurrent Networks](<https://arxiv.org/abs/2106.04537>)
- **2021** · [Lessons on Parameter Sharing across Layers in Transformers](<https://arxiv.org/abs/2104.06022>)
- **2021** · [PonderNet: Learning to Ponder](<https://arxiv.org/abs/2107.05407>)
- **2021** · [Stabilizing Equilibrium Models by Jacobian Regularization](<https://arxiv.org/abs/2106.14342>)
- **2021** · [Subformer: Exploring Weight Sharing for Parameter Efficiency in Generative Transformers](<https://arxiv.org/abs/2101.00234>)
- **2020** · [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](<https://arxiv.org/abs/1909.11942>)
- **2020** · [Monotone operator equilibrium networks](<https://arxiv.org/abs/2006.08591>)
- **2016** · [Adaptive Computation Time for Recurrent Neural Networks](<https://arxiv.org/abs/1603.08983>)

<a id="catalog-training-and-execution"></a>
### Training and execution · 114 works

Learning objectives, distillation, caching, and efficient inference.

- **2026** · [2DSD: Two-Dimensional Speculative Decoding for Looped Language Models](<https://github.com/SqueezeAILab/2DSD/blob/main/paper/2DSD.pdf>)
- **2026** · [A Mechanistic Analysis of Looped Reasoning Language Models](<https://arxiv.org/abs/2604.11791>)
- **2026** · [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](<https://arxiv.org/abs/2605.13724>)
- **2026** · [BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion](<https://arxiv.org/abs/2610.12307>)
- **2026** · [Categorical Flow Maps](<https://arxiv.org/abs/2602.12233>)
- **2026** · [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](<https://arxiv.org/abs/2605.15141>)
- **2026** · [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](<https://arxiv.org/abs/2602.02214>)
- **2026** · [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](<https://arxiv.org/abs/2606.25473>)
- **2026** · [Compressing History into Memory: Distilling Transformers into Recurrent Transformers](<https://arxiv.org/abs/2606.21562>)
- **2026** · [Context Forcing: Consistent Autoregressive Video Generation with Long Context](<https://arxiv.org/abs/2602.06028>)
- **2026** · [Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation](<https://arxiv.org/abs/2608.13391>)
- **2026** · [Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](<https://arxiv.org/abs/2605.18530>)
- **2026** · [D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](<https://arxiv.org/abs/2605.05204>)
- **2026** · [Decoding Looped Transformers Better for (Almost) Free](<https://arxiv.org/abs/2610.02185>)
- **2026** · [Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching](<https://arxiv.org/abs/2608.09444>)
- **2026** · [DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](<https://arxiv.org/abs/2605.15055>)
- **2026** · [Discrete Flow Maps](<https://arxiv.org/abs/2604.09784>)
- **2026** · [Distribution Matching Distillation for Continuous Diffusion Language Models](<https://arxiv.org/abs/2609.40235>)
- **2026** · [Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](<https://arxiv.org/abs/2605.01896>) — M2-REPA aligns decoupled RGB, depth, and mask features with modality-specific foundation models during training.
- **2026** · [DLoop: Looped Speculative Decoding](<https://arxiv.org/abs/2610.07659>)
- **2026** · [Dory1.0-4B: A Looped Normalized-GPT](<https://arxiv.org/abs/2611.03998>)
- **2026** · [DSA: Dynamic Step Allocation for Fast Autoregressive Video Generation](<https://arxiv.org/abs/2606.04432>)
- **2026** · [Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](<https://arxiv.org/abs/2602.01801>)
- **2026** · [Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers](<https://www.alphaxiv.org/abs/2611.feedback-shortcut-speculative-decoding>)
- **2026** · [FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates](<https://arxiv.org/abs/2609.29812>)
- **2026** · [Flow Map Language Models: One-step Language Modeling via Continuous Denoising](<https://arxiv.org/abs/2602.16813>)
- **2026** · [Flow-OPD: On-Policy Distillation for Flow Matching Models](<https://arxiv.org/abs/2605.08063>)
- **2026** · [How to train a frontier-level world model](<https://next-state.github.io/open-dreamer/>)
- **2026** · [Hybrid Latent Attention for Looped Language Models](<https://arxiv.org/abs/2610.07940>)
- **2026** · [Improved Distributional Diffusion Models](<https://arxiv.org/abs/2609.37147>)
- **2026** · [Improving Test-Time Scaling with Adaptive Looped Transformers](<https://arxiv.org/abs/2609.35748>)
- **2026** · [Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory](<https://arxiv.org/abs/2602.02393>)
- **2026** · [KV Caching in Flow Models](<https://sayak.dev/posts/kv-flow.html>)
- **2026** · [KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration](<https://arxiv.org/abs/2605.14278>)
- **2026** · [LASER: Low-Rank Activation SVD for Efficient Recursion](<https://arxiv.org/abs/2604.17224>)
- **2026** · [Level-of-Token Diffusion](<https://arxiv.org/abs/2610.05816>)
- **2026** · [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](<https://arxiv.org/abs/2605.31158>)
- **2026** · [LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](<https://arxiv.org/abs/2610.03636>)
- **2026** · [LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](<https://arxiv.org/abs/2609.38562>)
- **2026** · [Loop as a Bridge: Can Looped Transformers Truly Link Representation Space and Natural Language Outputs?](<https://arxiv.org/abs/2601.10242>)
- **2026** · [LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models](<https://arxiv.org/abs/2609.24196>)
- **2026** · [Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers](<https://arxiv.org/abs/2607.15456>)
- **2026** · [LoopRPT: Reinforcement Pre-Training for Looped Language Models](<https://arxiv.org/abs/2603.19714>)
- **2026** · [LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers](<https://arxiv.org/abs/2609.17184>)
- **2026** · [Maglev: Sliding Recurrent Memory](<https://arxiv.org/abs/2608.02870>)
- **2026** · [Memorizon: Training World Models Beyond Their Context Window](<https://arxiv.org/abs/2610.00544>)
- **2026** · [Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models](<https://arxiv.org/abs/2605.07721>)
- **2026** · [NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation](<https://arxiv.org/abs/2611.06377>) — Compressed historical keys and values use shared centers and quantized residuals; an optional variant attends in reduced dimensions.
- **2026** · [On the Design Space of Continuous Diffusion Language Models](<https://arxiv.org/abs/2610.13834>)
- **2026** · [On the Residual Scaling of Looped Transformers: Stability and Transferability](<https://arxiv.org/abs/2606.18524>)
- **2026** · [One Model to Loop Them All: Elastic Latent Recurrence for Language Models](<https://arxiv.org/abs/2610.12582>)
- **2026** · [One-Forcing: Towards Stable One-Step Autoregressive Video Generation](<https://arxiv.org/abs/2605.23458>)
- **2026** · [OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](<https://arxiv.org/abs/2607.08766>)
- **2026** · [PackCache: A Training-Free Acceleration Method for Unified Autoregressive Video Generation via Compact KV-Cache](<https://arxiv.org/abs/2601.04359>)
- **2026** · [PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](<https://arxiv.org/abs/2603.25730>)
- **2026** · [Parallel Decoding Distillation for Fast Image and Video Generation](<https://arxiv.org/abs/2607.26004>)
- **2026** · [Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion](<https://arxiv.org/abs/2601.21896>)
- **2026** · [Posterior Refinement: Fast Language Generation via Any-Order Flow Maps](<https://arxiv.org/abs/2606.24773>)
- **2026** · [Pretraining Recurrent Networks without Recurrence](<https://arxiv.org/abs/2606.06479>)
- **2026** · [Prioritize the Process, Not Just the Outcome: Rewarding Latent Thought Trajectories Improves Reasoning in Looped Language Models](<https://arxiv.org/abs/2602.10520>)
- **2026** · [RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](<https://arxiv.org/abs/2605.15190>)
- **2026** · [Recursive Flow Matching](<https://arxiv.org/abs/2605.26535>)
- **2026** · [Reward-Forcing: Autoregressive Video Generation with Reward Feedback](<https://arxiv.org/abs/2601.16933>)
- **2026** · [Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion](<https://arxiv.org/abs/2602.07775>)
- **2026** · [Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation](<https://arxiv.org/abs/2609.36995>)
- **2026** · [Self Gradient Forcing: Native Long Video Extrapolation](<https://arxiv.org/abs/2607.20368>)
- **2026** · [Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](<https://arxiv.org/abs/2603.06507>)
- **2026** · [Shallow Queries, Mature Values: Depth-Asynchronous Self-Speculation for Looped Transformers](<https://arxiv.org/abs/2609.34538>)
- **2026** · [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](<https://arxiv.org/abs/2609.02886>) — A shared data pipeline and staged adaptation recipe train causal video world models across several backbones.
- **2026** · [Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](<https://arxiv.org/abs/2604.21221>)
- **2026** · [Speculative Forcing for Efficient Autoregressive Video Generation](<https://arxiv.org/abs/2610.22347>)
- **2026** · [Step-resolved data attribution for looped transformers](<https://arxiv.org/abs/2602.10097>)
- **2026** · [Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution](<https://arxiv.org/abs/2605.25333>)
- **2026** · [The Surprising Effectiveness of Shared Memory in Looped Transformers](<https://arxiv.org/abs/2610.02383>)
- **2026** · [Towards Looped Models Done Right. Part II: Rethinking at Fixed Points](<https://www.alphaxiv.org/abs/2610.looped-models-fixed-points>)
- **2026** · [Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation](<https://arxiv.org/abs/2610.26030>)
- **2026** · [UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal Models](<https://arxiv.org/abs/2609.32831>)
- **2026** · [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](<https://arxiv.org/abs/2609.04010>)
- **2026** · [WorldCompass: Reinforcement Learning for Long-Horizon World Models](<https://arxiv.org/abs/2602.09022>)
- **2025** · [Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression](<https://arxiv.org/abs/2512.05081>)
- **2025** · [Dynamic Rebatching for Efficient Early-Exit Inference with DREX](<https://arxiv.org/abs/2512.15705>)
- **2025** · [Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models](<https://arxiv.org/abs/2510.14961>)
- **2025** · [Latent Chain-of-Thought? Decoding the Depth-Recurrent Transformer](<https://arxiv.org/abs/2507.02199>)
- **2025** · [MAGI-1: Autoregressive Video Generation at Scale](<https://arxiv.org/abs/2505.13211>)
- **2025** · [Mean Flows for One-step Generative Modeling](<https://arxiv.org/abs/2505.13447>)
- **2025** · [Memory Forcing: Spatio-Temporal Memory for Consistent Scene Generation on Minecraft](<https://arxiv.org/abs/2510.03198>)
- **2025** · [Next-Latent Prediction Transformers Learn Compact World Models](<https://arxiv.org/abs/2511.05963>)
- **2025** · [Parallel Loop Transformer for Efficient Test-Time Computation Scaling](<https://arxiv.org/abs/2510.24824>)
- **2025** · [Pusa V1.0: Unlocking Temporal Control in Pretrained Video Diffusion Models via Vectorized Timestep Adaptation](<https://arxiv.org/abs/2507.16116>)
- **2025** · [Region-Adaptive Sampling for Diffusion Transformers](<https://arxiv.org/abs/2502.10389>)
- **2025** · [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](<https://arxiv.org/abs/2509.25161>)
- **2025** · [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](<https://arxiv.org/abs/2506.08009>)
- **2025** · [Self-Forcing++: Towards Minute-Scale High-Quality Video Generation](<https://arxiv.org/abs/2510.02283>)
- **2025** · [SkyReels-V2: Infinite-length Film Generative Model](<https://arxiv.org/abs/2504.13074>)
- **2025** · [Stable Video Infinity: Infinite-Length Video Generation with Error Recycling](<https://arxiv.org/abs/2510.09212>)
- **2025** · [The Belief State Transformer](<https://arxiv.org/abs/2410.23506>)
- **2024** · [Accelerating Diffusion Transformers with Token-wise Feature Caching](<https://arxiv.org/abs/2410.05317>)
- **2024** · [Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing](<https://arxiv.org/abs/2411.16375>)
- **2024** · [Causal Diffusion Transformers for Generative Modeling](<https://arxiv.org/abs/2412.12095>)
- **2024** · [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](<https://arxiv.org/abs/2407.01392>)
- **2024** · [FIFO-Diffusion: Generating Infinite Videos from Text without Training](<https://arxiv.org/abs/2405.11473>)
- **2024** · [Flow map matching with stochastic interpolants: A mathematical framework for consistency models](<https://arxiv.org/abs/2406.07507>)
- **2024** · [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](<https://arxiv.org/abs/2412.07772>)
- **2024** · [Improved Distribution Matching Distillation for Fast Image Synthesis](<https://arxiv.org/abs/2405.14867>)
- **2024** · [LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding](<https://arxiv.org/abs/2404.16710>)
- **2024** · [One Step Diffusion via Shortcut Models](<https://arxiv.org/abs/2410.12557>)
- **2024** · [Rolling Diffusion Models](<https://arxiv.org/abs/2402.09470>)
- **2023** · [Consistent Diffusion Models: Mitigating Sampling Drift by Learning to be Consistent](<https://arxiv.org/abs/2302.09057>)
- **2023** · [EE-LLM: Large-Scale Training and Inference of Early-Exit Large Language Models with 3D Parallelism](<https://arxiv.org/abs/2312.04916>)
- **2023** · [Elucidating the Exposure Bias in Diffusion Models](<https://arxiv.org/abs/2308.15321>)
- **2023** · [One-step Diffusion with Distribution Matching Distillation](<https://arxiv.org/abs/2311.18828>)
- **2022** · [Progressive Distillation for Fast Sampling of Diffusion Models](<https://arxiv.org/abs/2202.00512>)
- **2016** · [Professor Forcing: A New Algorithm for Training Recurrent Networks](<https://arxiv.org/abs/1610.09038>)
- **2015** · [Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks](<https://arxiv.org/abs/1506.03099>)

<a id="catalog-evaluation-and-interpretability"></a>
### Evaluation and interpretability · 20 works

Benchmarks, controlled comparisons, mechanisms, and oversight.

- **2026** · [Can Video World Models Track Unobserved World States?](<https://arxiv.org/abs/2608.30692>)
- **2026** · [DepthBench: Measuring How Residual Connections Enable More Computational Depth](<https://arxiv.org/abs/2609.32534>)
- **2026** · [Echo-Memory: A Controlled Study of Memory in Action World Models](<https://arxiv.org/abs/2606.09803>)
- **2026** · [How Depth Growth and Looping Shape In-Context Learning in Language Models](<https://arxiv.org/abs/2610.31421>)
- **2026** · [How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](<https://arxiv.org/abs/2604.21106>)
- **2026** · [MemoBench: Benchmarking World Modeling in Dynamically Changing Environments](<https://arxiv.org/abs/2606.27537>)
- **2026** · [MIND: Benchmarking Memory Consistency and Action Control in World Models](<https://arxiv.org/abs/2602.08025>)
- **2026** · [Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models](<https://arxiv.org/abs/2603.13215>)
- **2026** · [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](<https://arxiv.org/abs/2608.27345>)
- **2026** · [Prefix Sliding for efficient test-time scaling](<https://arxiv.org/abs/2608.26070>)
- **2026** · [Shared Weights, Selected Computations: How Looped Transformers Route What Each Loop Does](<https://arxiv.org/abs/2609.39892>)
- **2026** · [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](<https://arxiv.org/abs/2604.10027>)
- **2026** · [Sliding-window beats linear attention](<https://arxiv.org/abs/2608.28444>)
- **2025** · [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](<https://arxiv.org/abs/2507.11473>)
- **2025** · [LoopNav: Benchmarking Spatial Consistency in World Models](<https://arxiv.org/abs/2505.22976>)
- **2025** · [Monitoring Monitorability](<https://arxiv.org/abs/2512.18311>)
- **2025** · [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](<https://arxiv.org/abs/2503.11926>)
- **2025** · [Racing Thoughts: Explaining Contextualization Errors in Large Language Models](<https://aclanthology.org/2025.naacl-long.155/>)
- **2025** · [Reasoning Models Don't Always Say What They Think](<https://arxiv.org/abs/2505.05410>)
- **2025** · [Two-Scale Latent Dynamics for Recurrent-Depth Transformers](<https://arxiv.org/abs/2509.23314>)
<!-- LOOP-BOT:CATALOG:END -->

## Scope and selection

We focus on generative models that reuse computation or carry information between
updates: shared-depth blocks, latent reasoning, sample refinement, temporal
memory, and agent feedback. Related theory, training methods, efficient inference,
and evaluation help explain when these mechanisms are useful.

A reading topic indicates how a work connects to the survey. For example,
memory compression supports temporal recurrence, while global-local video
generation provides a comparison for maintaining consistency over time.
Inclusion does not imply independent reproduction of reported results.

## Contribute

- **Suggest a paper:** open an issue or pull request with its primary link and a short explanation of its relevance.
- **Improve an entry:** correct the title, link, year, or reading topic in [the paper data](data/papers.json).
- **Improve the reading path:** suggest accessible starting points for a feedback family.

---

<p align="center">
  Maintained by <a href="https://github.com/vibe-hust">VibeLab</a> ·
  <a href="PAPERS.md">Read the bibliography</a> ·
  <a href="data/papers.json">Use the data</a>
</p>
