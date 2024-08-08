# dmypy bug: Final name must be initialized with a value

Mypy currently does not support `Final` annotation on dataclasses
(see [mypy issue 5608](https://github.com/python/mypy/issues/5608)).
Therefore, the error message `Final name must be initialized with a value` is expected on `MyDataclass` in `__init__.py`.
However, running `dmypy check src` a second time spreads this error message to `MyModule` and `ImmutablePoint`.



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
src/dmypy_final_bug/__init__.py:10: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:11: error: Final name must be initialized with a value  [misc]
```

and the second run yields different results, spreading the error message:

```text
src/dmypy_final_bug/__init__.py:10: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:11: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:15: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:16: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:25: error: Final name must be initialized with a value  [misc]
src/dmypy_final_bug/__init__.py:26: error: Final name must be initialized with a value  [misc]
```

