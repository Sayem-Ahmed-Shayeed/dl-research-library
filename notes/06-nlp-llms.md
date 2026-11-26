# NLP and large language models

Primary sources: `jurafsky-slp3/` (chapter order follows the Aug 2026 draft) and `xiao-zhu-llm/`.

## Text representation
- Tokenization: words vs subwords. BPE (merge most frequent pairs), WordPiece, Unigram LM (SentencePiece); byte-level BPE avoids unknown tokens. Unicode normalization, regex pre-tokenization.
- Read: `jurafsky-slp3/02-words-and-tokens.md`.

## Language modeling basics
- Chain rule p(w₁…w_n) = ∏ p(wₜ|w<ₜ). N-gram models with smoothing (add-k, Kneser–Ney), backoff/interpolation.
- Perplexity PP = exp(−(1/N) Σ log p(wₜ|w<ₜ)).
- Read: `jurafsky-slp3/03-n-gram-language-models.md`.

## Embeddings
- Distributional hypothesis; sparse (tf-idf, PPMI) vs dense vectors; word2vec skip-gram with negative sampling, GloVe, fastText; cosine similarity; analogies; bias in embeddings. Contextual embeddings from transformers replace static ones.
- Read: `jurafsky-slp3/05-embeddings.md`; `zhang-d2l/18-natural-language-processing-pretraining.md`.

## Neural LMs and transformers
- Feed-forward LMs → RNN/LSTM LMs → transformer decoders. Training = next-token cross-entropy with teacher forcing.
- Decoding: greedy, beam search (MT), temperature, top-k, nucleus (top-p), min-p; repetition penalties; speculative decoding.
- Read: `jurafsky-slp3/06-neural-networks.md`, `07-transformers-and-pretraining.md`, `14-rnns-and-lstms.md`; `xiao-zhu-llm/02-generative-models.md`.

## Pretraining paradigms
- Masked LM (BERT, RoBERTa; [CLS] for classification, span prediction for QA), encoder–decoder denoising (T5, BART), causal LM (GPT family). Fine-tuning vs feature extraction; parameter-efficient fine-tuning (adapters, LoRA, prefix/prompt tuning).
- Scaling laws, data mixtures and deduplication, long-context extension (RoPE scaling).
- Read: `jurafsky-slp3/09-masked-language-models.md`; `xiao-zhu-llm/01-pre-training.md`.

## Post-training and alignment
- Instruction tuning / SFT on (prompt, response) pairs.
- RLHF: reward model from pairwise preferences (Bradley–Terry), then PPO with KL penalty to reference policy.
- DPO: closed-form reparameterization, loss −log σ(β[log π(y_w|x)/π_ref(y_w|x) − log π(y_l|x)/π_ref(y_l|x)]). Variants (IPO, KTO, ORPO), RL from verifiable rewards (GRPO-style group-relative advantages) for reasoning.
- Read: `jurafsky-slp3/08-post-training.md`; `xiao-zhu-llm/04-alignment.md`.

## Prompting, reasoning, inference
- In-context learning, few-shot prompts, chain-of-thought, self-consistency, tree/graph-of-thought, tool use; reasoning models trained with RL and test-time compute scaling.
- Inference systems: KV cache, paged attention, batching, quantization (INT8/INT4, GPTQ/AWQ-style), distillation, speculative decoding.
- Read: `xiao-zhu-llm/03-prompting.md`, `05-inference.md`, `06-reasoning.md`.

## Retrieval, agents, interpretability
- RAG: dense retrievers (bi-encoders, contrastive training), BM25, rerankers (cross-encoders), chunking, citing sources; evaluation of faithfulness.
- Agents: tool calling, planning loops, memory, environment feedback.
- Interpretability: probing, attention analysis, attribution, mechanistic interpretability (circuits, sparse autoencoder features).
- Read: `jurafsky-slp3/11-retrieval-based-models.md`, `12-agents.md`, `10-interpretability.md`; `murphy-pml2/34-33-interpretability.md`.

## Classic NLP tasks (still used as evaluations and in pipelines)
- Machine translation (seq2seq, BLEU/chrF/COMET) — `13-machine-translation.md`.
- Sequence labeling (POS, NER; BIO tagging, CRF/HMM, Viterbi) — `18-…`; HMMs in depth: `bishop-prml/15-13-sequential-data.md`.
- Parsing (CFG/CKY, dependency transition/graph parsers) — `19-…`, `20-…`.
- Information extraction, SRL, sentiment lexicons, coreference & entity linking, discourse, dialogue — `21-…` to `26-…`.
- Speech: features (MFCC, log-mel), ASR (CTC, attention encoder–decoder, Whisper-style), TTS — `15-…`, `16-…`, `17-…`.
- Code-level walkthroughs (sentiment with RNN/CNN, NLI with attention, BERT fine-tuning): `zhang-d2l/19-natural-language-processing-applications.md`.
