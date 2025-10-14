# Development Workflow
 

## Action Items

- [x] 1. **Edit code** in `src/cli_pets/__init__.py`
- [x] **Interactive test:**
- [x] Build package:


## Logs


```powershell
uv run python
from cli_pets import greet, walk, race
greet()
walk()
race()
```

```shell
(base) (cli-pets) PS D:\GitHub\cli-pets> uv build
Building source distribution (uv build backend)...
Building wheel from source distribution (uv build backend)...
Successfully built dist\cli_pets-0.1.0.tar.gz
Successfully built dist\cli_pets-0.1.0-py3-none-any.whl
```
