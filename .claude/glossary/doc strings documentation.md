# Python Docstrings Glossary

## What are docstrings?
Triple-quoted strings right after function/class definition. Used for documentation.

## Syntax
```python
def walk(pet: str = "🐱", steps: int = 20) -> None:
    """Make a pet walk across the terminal.
    
    Args:
        pet: Emoji character to display
        steps: Number of steps to take
        
    Returns:
        None
        
    Example:
        >>> walk("🐶", 10)
    """
```

## Major Formats

### Google Style (most popular)
```python
"""Short description.

Args:
    param1 (int): Description
    param2 (str): Description

Returns:
    bool: Description

Raises:
    ValueError: When something wrong
"""
```

### NumPy Style
```python
"""Short description.

Parameters
----------
param1 : int
    Description
param2 : str
    Description

Returns
-------
bool
    Description
"""
```

### reStructuredText (Sphinx default)
```python
"""Short description.

:param param1: Description
:type param1: int
:param param2: Description
:type param2: str
:returns: Description
:rtype: bool
"""
```

## roxygen2 → Python Equivalents

| roxygen2 | Python (Google) |
|----------|----------------|
| `@param` | `Args:` |
| `@return` | `Returns:` |
| `@export` | N/A (use `__all__`) |
| `@examples` | `Example:` |
| `@seealso` | `See Also:` |

## Tools
- **mkdocstrings**: Auto-generates docs from docstrings
- **Sphinx**: Alternative documentation generator
- **pdoc**: Simpler auto-doc tool

## Best Practices
- Use Google style (cleanest, most popular)
- Include type hints in signature, not docstring
- Keep first line under 80 chars
- Use present tense ("Returns X" not "Will return X")