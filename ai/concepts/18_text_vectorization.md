---
tags:
  - ai
  - ml
created_at: 2026-04-27T08:33:02
updated_at: 2026-04-27T09:27:45
recent_editor: CODEX
---

# Text Vectorization

## What It Is

Text vectorization turns text into numeric features so machine learning systems can compare, rank, classify, or cluster documents. TF-IDF is a classic sparse vectorization method: each document becomes a vector whose dimensions are terms, and each value measures how important that term is in that document.

## Analogy

A document fingerprint. Instead of remembering every sentence, TF-IDF keeps a weighted list of terms that make the document distinctive compared with the rest of the collection.

## How It Works

TF-IDF means **term frequency-inverse document frequency**.

- **Term frequency (TF)** increases when a term appears often in one document.
- **Inverse document frequency (IDF)** decreases when a term appears in many documents.
- **TF-IDF** multiplies them so common terms across the corpus are downweighted and document-specific terms stand out.

The Stanford IR book defines IDF as `log(N / df_t)`, where `N` is the number of documents and `df_t` is the number of documents containing term `t`. [Stanford IR Book - Inverse document frequency](https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html)

scikit-learn's `TfidfVectorizer` combines tokenization, vocabulary building, term counts, IDF weighting, and optional normalization into a document-term matrix. [scikit-learn TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

### BM25

BM25 is a keyword-search ranking function in the same family as TF-IDF. It still rewards query terms that are rare across the corpus and present in a document, but it adds two practical controls:

- **Term-frequency saturation:** repeated terms help, but each extra repeat adds less value.
- **Document-length normalization:** long documents are adjusted so they do not win only because they contain more words.

BM25 is a ranking formula, not usually a document vector used directly for clustering. Search engines such as Lucene, Elasticsearch, and OpenSearch commonly use BM25-style lexical ranking for sparse retrieval.

### Sparse vs. Dense Vectors

TF-IDF and BM25 are **sparse lexical methods**: most possible terms do not appear in a given document, and matching depends on explicit terms. [Embedding models](./17_embedding_models.md) create **dense vectors**: every dimension has a value learned from model training.

TF-IDF is strong when exact words matter, such as product codes, error messages, names, and technical terms. Embeddings are stronger when semantic similarity matters, such as "reset password" matching "change login credentials."

## Example

In a small support-document corpus, the term `timeout` may receive a high TF-IDF score in a networking troubleshooting page because it appears often there and not in most other pages. The word `the` receives a low score because it appears everywhere and does not identify the document.

## Why It Matters

TF-IDF and BM25 are still useful because they are simple, explainable, cheap, and effective for exact lexical matching. Modern retrieval systems often combine sparse keyword signals with dense embedding search in a hybrid search pipeline.

---
[Overview](./00_concepts_overview.md)

**Related:** [Embedding Models](./17_embedding_models.md), [RAG](./16_rag.md), [Clustering](./19_clustering.md)
**Tags:** #ai #ml
