import torch, json, os, numpy as np, random
import matplotlib.pyplot as plt
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from wordcloud import WordCloud
from collections import Counter
from tqdm import tqdm

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device)

MODEL_NAME = "gpt2"
tokenizer = GPT2TokenizerFast.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME).to(device)
model.eval()

def generate_text(prompt, max_length=120, temperature=1.0, top_k=0, top_p=0.0):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output_ids = model.generate(
        **inputs,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k if top_k>0 else None,
        top_p=top_p if top_p>0 else None,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def compute_perplexity(text):
    enc = tokenizer(text, return_tensors="pt").to(device)
    max_len = model.config.n_positions
    stride = 512
    nlls = []
    input_ids = enc.input_ids
    seq_len = input_ids.size(1)

    for i in range(0, seq_len, stride):
        begin = max(i + stride - max_len, 0)
        end = min(i + stride, seq_len)
        target_ids = input_ids[:, begin:end]
        with torch.no_grad():
            out = model(input_ids[:, begin:end], labels=target_ids)
            nlls.append(out.loss * (end - begin))

    return torch.exp(torch.stack(nlls).sum() / seq_len).item()

def distinct_n(text, n=1):
    toks = tokenizer.tokenize(text)
    if not toks: return 0
    ngrams = set(zip(*[toks[i:] for i in range(n)]))
    return len(ngrams) / len(toks)

def repetition_rate(text):
    toks = tokenizer.tokenize(text)
    c = Counter(toks)
    rep = sum(v-1 for v in c.values() if v > 1)
    return rep / len(toks)

prompts = {
    "tech": "Artificial intelligence will change how humans work, learn, and",
    "story": "The haunted mirror whispered every night until",
    "medical": "The patient experienced chest pain because",
}

temps = [0.2, 0.7, 1.0, 1.2]
results = []

for name, text in prompts.items():
    for t in temps:
        out = generate_text(text, temperature=t)
        ppl = compute_perplexity(out)
        d1 = distinct_n(out, 1)
        rep = repetition_rate(out)

        results.append({
            "prompt": name,
            "temperature": t,
            "output": out,
            "perplexity": ppl,
            "distinct_1": d1,
            "repetition": rep
        })
        print(f"[{name}] temp={t} -> PPL {ppl:.2f} | D1={d1:.3f} | REP={rep:.3f}")

os.makedirs("results", exist_ok=True)
with open("results/experiment_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved experiment results to results/experiment_results.json")

# Word Cloud
wc = WordCloud(width=1000, height=400, background_color="white")
all_text = " ".join(r["output"] for r in results)
wc.generate(all_text)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title("GPT-2 Generated Word Cloud")
plt.show()
