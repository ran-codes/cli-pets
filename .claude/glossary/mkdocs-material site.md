# MkDocs Material

**Type:** Static site generator for Python documentation

**R Analog:** pkgdown

**Purpose:** Converts markdown + docstrings → beautiful documentation website

**Key Features:**
- Auto-generates API reference from docstrings (via mkdocstrings plugin)
- Markdown-based manual pages
- Built-in search, themes, mobile-responsive
- Hosts on GitHub Pages

**Workflow:** Write docstrings in code → mkdocstrings extracts them → MkDocs builds static site

**Popular users:** FastAPI, Pydantic, UV, Ruff


# Adding MkDocs Material to Your Python Package

## Overview
MkDocs Material is a documentation framework that generates static HTML from Markdown files. You can deploy it to GitHub Pages alongside your Next.js SSG or as a separate docs subdirectory.

## Setup Steps

### 1. Install MkDocs Material

```bash
pip install mkdocs-material
```

### 2. Initialize Your Docs

```bash
mkdocs new .
```

This creates:
- `mkdocs.yml` - Configuration file
- `docs/` - Markdown files directory

### 3. Configure `mkdocs.yml`

```yaml
site_name: Your Package Docs
site_url: https://yourusername.github.io/your-repo/

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
    - search.suggest
    - search.highlight
  palette:
    - scheme: default
      primary: indigo
      accent: indigo

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference: api.md

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - admonition
  - codehilite
```

### 4. GitHub Pages Deployment Options

**Option A: Deploy docs to `docs/` folder on main branch**

In `mkdocs.yml`:
```yaml
site_dir: docs
```

Build and commit:
```bash
mkdocs build
git add docs/
git commit -m "Build docs"
git push
```

GitHub Settings → Pages → Source: `main` branch, `/docs` folder

**Option B: Deploy to `gh-pages` branch (recommended)**

```bash
mkdocs gh-deploy
```

This automatically builds and pushes to the `gh-pages` branch.

GitHub Settings → Pages → Source: `gh-pages` branch

### 5. Integration with Next.js

If deploying both Next.js and MkDocs:

**Structure:**
```
your-repo/
├── next-app/          # Your Next.js app
├── docs/              # MkDocs source
├── mkdocs.yml
└── package.json
```

**Deploy Next.js to root, docs to `/docs` path:**

In `mkdocs.yml`:
```yaml
site_url: https://yourusername.github.io/your-repo/docs/
```

Use GitHub Actions to deploy both (create `.github/workflows/deploy.yml`):

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      # Deploy Next.js
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Build Next.js
        run: |
          cd next-app
          npm ci
          npm run build
          npm run export
      
      # Deploy MkDocs
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x
      
      - name: Install dependencies
        run: pip install mkdocs-material
      
      - name: Build docs
        run: mkdocs build -d next-app/out/docs
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./next-app/out
```

This deploys your Next.js site to the root and MkDocs to `/docs`.

## Key Points

- MkDocs generates static HTML, perfect for GitHub Pages
- `mkdocs gh-deploy` handles deployment automatically
- Can coexist with Next.js SSG using subdirectories or subdomains
- All content is Markdown-based in the `docs/` folder