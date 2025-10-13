# Package Get Started

## UV

We will use uv for dependency management. See the UV isntalliation instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

```shell
uv --version
```

## UV > PyPI library

There are many types of projects that UV can manage and initialize. A packges is a project that is intended to be built and distributed as a Python package. To intiate a package project, run the following command:

```shell
uv init --lib cli-pets
```

## Dependencies

- `rich` for terminal animations
- `click` for command line interface (optional later)