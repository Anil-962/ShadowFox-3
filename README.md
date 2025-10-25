# GPT-2 Language Model Analysis — ShadowFox AIML Internship (Advanced Task)

This project implements and analyzes **GPT-2**, a transformer-based language model for natural language generation.  
The goal is to explore how GPT-2 behaves under different conditions and understand its limitations, strengths, and ethical concerns.

---

## 📌 Project Objectives
✅ Implement GPT-2 using Transformer libraries  
✅ Run controlled experiments on text generation  
✅ Measure performance using:
- Perplexity (language model quality)
- Lexical diversity (Distinct-1)
- Repetition rate

✅ Visualize results and interpret model behavior  
✅ Provide ethical and research-based insights  
✅ Publish Proof of Work to GitHub + LinkedIn

---

## 🚀 How It Works

### ✅ Prompts Used
- Technology text
- Story writing
- Medical domain text

### ✅ Experimental Variables
- Temperature values: **0.2, 0.7, 1.0, 1.2**
- Sampling method: Random sampling enabled

These settings reveal GPT-2’s behavior across creativity vs coherence trade-offs.

---

## 📊 Key Results

| Temperature | Behavior Summary |
|------------:|----------------|
| 0.2 | Safe, repetitive, less creative |
| 0.7 | Balanced creativity + coherence |
| 1.0 | More narrative flow, some hallucination |
| 1.2 | Very creative but unstable and inaccurate |

### Domain Sensitivity
| Domain | Performance | Observation |
|--------|:-----------:|-------------|
| Story | ⭐⭐⭐⭐ | Very fluent narrative |
| Tech | ⭐⭐⭐ | Good but generic |
| Medical | ⭐⭐ | High hallucination + safety risks |

### Perplexity Trends
Higher temperature tends to produce:
- Higher perplexity (less confident prediction)
- More randomness in words

---

## 🎨 Visualizations Included (in Notebook)
✔ Perplexity vs Temperature plots  
✔ Lexical diversity vs Temperature  
✔ Token confidence graph  
✔ Word cloud of all generated text  

---

## 🔍 Research Questions & Findings
1️⃣ **How does temperature affect generation?**  
Higher temperature = more creativity, less reliability  

2️⃣ **Can GPT-2 maintain long-term context?**  
Maintains short context, drifts after ~70+ tokens  

3️⃣ **Does GPT-2 adapt to domain-specific input?**  
Performs poorly on specialized fields (e.g., medical)

---

## ⚠ Ethical Considerations
- GPT-2 hallucinates facts (not suitable for authoritative info)
- Bias from internet training data persists
- Outputs must be validated before real-world use

---

## ✅ Conclusion
GPT-2 is excellent for **creative text generation** but unreliable for:
- Factual responses
- Domain-critical content

Recommendations:
- Fine-tune on specific data for improved accuracy
- Add safety filtering + fact verification

---

## 🛠 Setup Instructions

### Run Notebook in Google Colab
Open `GPT2_analysis.ipynb` and run all cells  
Requirements auto-install inside Colab

### Run Locally in VS Code

```bash
cd ShadowFox
python -m venv env
env\Scripts\activate   # (Windows)
pip install -r requirements.txt
cd src
python experiment.py
