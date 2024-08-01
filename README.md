# Reproduction of [pytorch/issues/131765](https://github.com/pytorch/pytorch/issues/131765)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
pyright src
```

Expected message:

> `src/torch_131765/__init__.py:5:27` - error: "Adam" is not exported from module "torch.optim" (reportPrivateImportUsage)
