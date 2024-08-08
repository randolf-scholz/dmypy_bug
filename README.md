# dmypy bug: Final name must be initialized with a value

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
dmypy start
dmypy check src
dmypy check src  # second run
```

The first run should produce:

```text
src/dmypy_final_bug/__init__.py:30: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:31: error: Final name must be initialized with a value  [misc]
```

and the second run:

```text
src/dmypy_final_bug/__init__.py:9: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:10: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:19: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:20: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:30: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:31: error: Final name must be initialized with a value  [misc]
```