# Architectures

## Convolutional networks
- Convolution = weight sharing + locality → translation equivariance; pooling/striding → partial invariance and larger receptive field.
- Output size: ⌊(n + 2p − k)/s⌋ + 1. Params per layer: k·k·C_in·C_out (+C_out). Receptive field grows with depth, dilation, stride.
- Variants: 1×1 conv (channel mixing), depthwise-separable (MobileNet), dilated/atrous (segmentation), transposed conv (upsampling; beware checkerboard), grouped conv (ResNeXt), deformable conv.
- Lineage: LeNet → AlexNet (ReLU, dropout, GPU) → VGG (3×3 stacks) → GoogLeNet/Inception (multi-branch) → ResNet (residuals) → DenseNet → ResNeXt → EfficientNet (compound scaling) → RegNet → ConvNeXt (CNN modernized with transformer design choices).
- Encoder–decoder: U-Net (skip connections) for segmentation, depth, diffusion denoisers. FPN for multi-scale detection.
- Read: `prince-udl/11-convolutional-networks.md`, `12-residual-networks.md`; `zhang-d2l/10-…`, `11-modern-convolutional-neural-networks.md`; `torralba-fcv/25-24-convolutional-neural-nets.md`; `goodfellow-dl/10-9-convolutional-networks.md`; `scardapane-alice/08-…`, `09-…`, `10-…`; `murphy-pml1/15-14-neural-networks-for-images.md`.

## Recurrent networks and state-space models
- RNN: hₜ = tanh(W hₜ₋₁ + U xₜ). BPTT; vanishing/exploding gradients.
- LSTM (input/forget/output gates + cell state), GRU (update/reset gates) fix long-range credit assignment.
- Seq2seq encoder–decoder + attention (Bahdanau) → origin of the transformer.
- Linear recurrences / SSMs (S4, Mamba-style selective SSMs, linear attention): parallel training, O(1)-per-step inference.
- Read: `zhang-d2l/12-…`, `13-modern-recurrent-neural-networks.md`; `goodfellow-dl/11-10-sequence-modeling-recurrent.md`; `jurafsky-slp3/14-rnns-and-lstms.md`; `scardapane-alice/14-recurrent-models.md`; `torralba-fcv/26-25-recurrent-neural-nets.md`.

## Attention and transformers
- Scaled dot-product attention: Attn(Q,K,V) = softmax(QKᵀ/√d_k)V. √d_k keeps logits' variance ~1.
- Multi-head: h parallel heads with projections, concatenated. Self-attention is permutation-equivariant → needs positional information: sinusoidal, learned, relative, RoPE (rotary), ALiBi.
- Block (pre-norm): x = x + MHA(LN(x)); x = x + FFN(LN(x)); FFN often SwiGLU in LLMs.
- Encoder-only (BERT), decoder-only with causal mask (GPT, LLaMA), encoder–decoder (T5, original Transformer).
- Cost O(n²d) in sequence length → FlashAttention (IO-aware exact), sparse/local/windowed attention, linear attention, KV cache at inference, GQA/MQA to shrink KV cache.
- Mixture of Experts: router picks top-k FFN experts per token; more parameters at same FLOPs; needs load-balancing loss.
- Read: `prince-udl/13-transformers.md`; `zhang-d2l/14-attention-mechanisms-and-transformers.md`; `scardapane-alice/11-transformer-models.md`, `12-transformers-in-practice.md`; `torralba-fcv/27-26-transformers.md`; `jurafsky-slp3/07-transformers-and-pretraining.md`; `xiao-zhu-llm/02-generative-models.md`.

## Vision transformers
- ViT: split image into 16×16 patches → linear embedding + position embedding + [CLS] → transformer. Weak inductive bias → needs large data or strong augmentation/distillation (DeiT).
- Swin: windowed attention with shifted windows, hierarchical feature maps (good backbone for detection/segmentation).
- Hybrid/conv stems; ConvNeXt shows that design choices, not attention alone, explain much of the gap.
- Read: `zhang-d2l/14-…` (ViT section); `prince-udl/13-transformers.md` (transformers for images); `torralba-fcv/27-26-transformers.md`.

## Graph neural networks
- Message passing: hᵥ' = φ(hᵥ, ⊕_{u∈N(v)} ψ(hᵥ, h_u, e_uv)) with permutation-invariant aggregation ⊕ (sum/mean/max).
- GCN, GraphSAGE, GAT (attention weights over neighbors), GIN (as expressive as 1-WL test). Over-smoothing with depth.
- Transformers = GNNs on complete graphs; CNNs = GNNs on grids (geometric-DL unification).
- Read: `prince-udl/14-graph-neural-networks.md`; `scardapane-alice/13-graph-models.md`; `bronstein-gdl/07-5-geometric-deep-learning-models.md`; `murphy-pml2/31-30-graph-learning.md`.

## Autoencoders and representation bottlenecks
- Undercomplete, denoising, sparse, contractive autoencoders; masked autoencoders (MAE) for vision pretraining.
- Read: `goodfellow-dl/15-14-autoencoders.md`, `16-15-representation-learning.md`.

## Symmetry view (Geometric Deep Learning)
- Domain → symmetry group → equivariant layers + local pooling + invariant readout. Grids/translations → CNNs; sets/permutations → DeepSets/transformers; graphs → GNNs; manifolds/meshes → gauge-equivariant nets; groups (rotations) → G-CNNs, E(3)-equivariant nets for molecules/3D.
- Read: `bronstein-gdl/05-3-geometric-priors.md`, `06-4-geometric-domains-the-5-gs.md`, `07-5-…`.
