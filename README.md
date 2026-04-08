# 🧠 Active Prompt Engineering (APE)
Control-layer framework for reducing LLM hallucinations using structured prompting. No fine-tuning or RAG required.

<p align="center">
  <img src="https://img.shields.io/badge/LLM-Reliability-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prompt-Engineering-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Hallucination-Reduction-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Research-Project-purple?style=for-the-badge" />
</p>

<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<h1 align="center">🧠 Active Prompt Engineering</h1>
<h3 align="center">A Control-System Approach for Reliable LLM Outputs</h3>

---

## 📌 Overview

Large Language Models (LLMs) often generate **hallucinations** — outputs that are fluent but factually incorrect.

This project introduces **Active Prompt Engineering (APE)**, a lightweight framework that treats prompts as **control systems** rather than simple instructions.

---

## 💡 Key Idea

P = C + R + V

Where:

- **C — Constraints** → Reduce speculation and enforce uncertainty  
- **R — Reasoning** → Structure step-by-step thinking  
- **V — Verification** → Enable self-checking before output  

👉 Together, these form a **control pipeline over LLM behavior**.

---

## 🔬 Results

| Prompt Strategy       | Hallucination ↓ | Accuracy ↑ | Faithfulness ↑ |
|---------------------|----------------|------------|----------------|
| Baseline            | 34%            | 66%        | 61%            |
| Constraint          | 24%            | 74%        | 70%            |
| Chain-of-Thought    | 19%            | 80%        | 76%            |
| Verification        | 11%            | 88%        | 84%            |
| **APE (C+R+V)**     | **8%**         | **91%**    | **89%**        |

👉 ~76% reduction in hallucination

---

## ⚙️ Why It Works

APE addresses three key failure modes:

- **Overconfidence** → controlled via constraints  
- **Logical inconsistency** → improved via reasoning  
- **Undetected errors** → reduced via verification  

---

## 🧪 APE Prompt Template

```
[CONSTRAINTS]
Only respond if highly confident. If uncertain, say "I don't know"

[REASONING]
1. What is being asked?
2. What are the relevant facts?
3. What is the logical conclusion?

[VERIFICATION]
- Are all claims supported?
- Any contradictions?
- Can this be improved?
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/ape-llm-hallucination.git
cd ape-llm-hallucination
pip install -r requirements.txt
python run_experiment.py --strategy ape
```

---

## 📂 Project Structure

```
├── prompts/
├── experiments/
├── data/
├── results/
├── paper/
└── README.md
```

---

## 📉 Error Analysis

Residual hallucinations fall into:

- Knowledge gaps  
- Reasoning failures  
- Prompt misinterpretation  
- Ambiguous queries  

---

## ⚠️ Limitations

- Cannot fix missing knowledge (needs RAG)
- Sensitive to prompt phrasing
- Limited for open-ended tasks

---

## 📄 Paper

👉 Add your paper link here

---

## 🧠 Key Insight

Prompting is not just input formatting — it is a control interface over LLM behavior

---

## 🤝 Contributions

Solo research project. Contributions welcome.


