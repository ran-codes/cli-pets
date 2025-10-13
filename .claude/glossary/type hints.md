# Type Hints & py.typed

## Type Hints
Optional Python syntax declaring what types variables/parameters should be:

```python
def walk(pet: str = "🐱", steps: int = 30) -> None:
    #        ^^^^^ str      ^^^^^ int    ^^^^^ returns None
```

## Benefits
- **IDE autocomplete** - VSCode knows `pet` is a string
- **Type checking** - `mypy` catches bugs before runtime
- **Documentation** - Clearer function signatures

## py.typed file
Empty marker file in your package root signals:
> "This package includes type hints - type checkers can use them"

## R Package Analog
Similar to documenting types in roxygen2 `@param` tags, but **enforced by tools**.

## For cli-pets
Keep `py.typed` - you're using type hints (`-> None`, `: str`). Best practice for modern Python packages.