# Installation

## Step 1 — Clone the repository

```bash
git clone https://github.com/John-salvin/script-bias-comet-indic-mt.git
cd script-bias-comet-indic-mt
```

## Step 2 — Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

## Step 3 — Install dependencies

### CPU (any machine, no GPU required)

```bash
pip install -r requirements.txt
```

This installs PyTorch CPU-only and all notebook dependencies.  
All notebooks will run correctly on CPU; scoring ~7,000 sentences will be slower (plan for 30–60 min per metric on CPU).

### GPU (NVIDIA, recommended for indic/03 scoring)

First install the CUDA build of PyTorch that matches your driver, **before** running `pip install -r requirements.txt`:

```bash
# CUDA 12.1 (most common on modern NVIDIA GPUs)
pip install torch==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121

# CUDA 11.8
pip install torch==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118

# Then install the rest
pip install -r requirements.txt
```

Not sure which CUDA version you have? Run `nvidia-smi` — the top-right corner shows the driver's CUDA version.

## Step 4 — Launch JupyterLab

```bash
jupyterlab
```

Open the notebooks in order starting from `notebooks/indic/01_fetch_indicmt_eval.ipynb`.

---

## Python version

Python **3.10** is required. The AI4Bharat transliteration library does not support 3.11+.
