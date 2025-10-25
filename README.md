# GPT-2 Advanced Analysis

## Overview

This project demonstrates a comprehensive analysis and evaluation of the GPT-2 language model using a Jupyter notebook environment. It covers model setup, text generation, experiment design, metric evaluation, and visualization of GPT-2’s outputs across diverse domains and generation settings.

## Features

- Load and configure GPT-2 using Hugging Face Transformers and PyTorch
- Accepts custom text prompts for domain adaptation experiments
- Generates samples under varied temperature, top-k, and top-p parameters
- Computes quality metrics (Perplexity, Distinct-1 lexical diversity, word repetition)
- Plots diversity, coherence, and surprise over experimental runs
- Generates word clouds and token probability heatmaps for model interpretation
- Saves experiment results for reporting and review

## Installation


## Usage

1. Open `GPT2_analysis.ipynb` in Jupyter Notebook or Jupyter Lab.
2. Run all cells step-by-step to:
    - Initialize, load the pretrained GPT-2 model, and set random seeds.
    - Test and analyze outputs for multiple types of prompts.
    - Visualize metrics and interpret model behavior.
    - Save results as JSON for future reporting.

## Project Structure

| File                 | Purpose                                     |
|----------------------|---------------------------------------------|
| GPT2_analysis.ipynb  | Main analysis notebook                      |
| experimentresults.json  | Saved outputs and metrics for reference   |

## Results

- Compares model responses across temperatures and prompt types
- Reports diversity, coherence, and confidence in generated text
- Highlights strengths and weaknesses from experimental evidence

## Contributing

Fork the repo and submit pull requests for new metrics, prompt categories, or visualization styles.

## License

MIT License

