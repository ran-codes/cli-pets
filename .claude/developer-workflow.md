# Development Workflow

**Daily loop:** Edit → Interactive test → Write unit tests → Commit

## 1. **Edit code** in `src/cli_pets/__init__.py`

## 2. **Interactive test:**
```powershell
uv run python
>>> from cli_pets import hello
>>> hello()
```

## 3. **Test as CLI** (once you add entry point):
```powershell
uv run pet-walk
```

## 4. **Write tests** in `tests/test_cli_pets.py`:
```python
from cli_pets import hello
def test_hello():
assert hello() == "Hello from cli-pets!"
```

## 5. **Run tests:**
```powershell
uv run pytest
```

## 6. **Build package:**
```powershell
uv build
```

## 7. **Publish to PyPI:**
```powershell
uv publish
```
