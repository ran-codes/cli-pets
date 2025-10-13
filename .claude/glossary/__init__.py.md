# Glossary

## `__init__.py` 

- Marks the directory as a Python package. This code runs when you import the package. So when users run `import cli_pets`, this file is executed.
- This is where you can set package-level variables, import submodules, and define the package version. if its a small pacakge thend efine main functions here.

## entry point 

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


##