# Setup

- [x] Install as development depednency 
    - [x] `uv add --dev mkdocs-material` (docs site packge - e.g. pkgdown)
    - [x] `uv add --dev mkdocstrings[python]` (auto populate site from docs strings - e.g. roxygenate)
- [x] create MkDocs project structure `uv run mkdocs new .`
- [x] Configure mkdocs.yml (for auto population based on doc strings)
 ```yaml
 site_name: CLI-PETS

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
```          
- [x] Create an API page (R refrence page) `mkdir docs/api`


# Function Documentaiton edits


- [x] For each function write Google style docstrings
- [x] For each function add a `{function_name}.md` files in the API folder each file just needs
```md
# walk()

::: cli_pets.walk
```

# Deploy

- [ ] build site with `uv run mkdocs build` or just deploy with `uv run mkdocs gh-deploy`
- [ ] Enable pages deplyoed from gh-pages branch