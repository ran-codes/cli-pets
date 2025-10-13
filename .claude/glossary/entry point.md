# entry point 

An **entry point** is a command that runs your package from the terminal.

Add this to `pyproject.toml`:

```toml
[project.scripts]
pet-walk = "cli_pets:walk"
pet-race = "cli_pets:race"
```

Then define those functions in `__init__.py`:

```python
def walk():
    print("🐱 walking...")
```

After syncing (`uv sync`), you can run:
```powershell
uv run pet-walk
```

This maps the terminal command `pet-walk` to your Python function `walk()`.

