# Contributing to fathomnet-py

Thanks in advance for contributing to fathomnet-py! We appreciate your help in making this project better.

## The basics

The FathomNet team welcomes contributions in the form of pull requests. If you're new to the project, you may want to start by reading the [README](README.md) to get an overview of the project.

For small changes (e.g., bug fixes), feel free to open a pull request right away. For larger changes, we recommend opening an issue first to discuss the proposed changes.

### Prerequisites

fathomnet-py is written in Python and uses the [uv](https://docs.astral.sh/uv/) project management system. To contribute to fathomnet-py, you'll need to have Python 3.8 or later installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### :hammer_and_wrench: Setting up your development environment

To set up your development environment, follow these steps:

#### 1. Install `uv`

First, install `uv` by running the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2. Clone the repository

Next, clone the fathomnet-py repository to your local machine:

```bash
git clone git@github.com:fathomnet/fathomnet-py.git
```

#### 3. Install the project dependencies

Navigate to the project directory and install the project dependencies by running:

```bash
uv sync
```

This command will create a virtual environment at `.venv` and install the project dependencies. This will include the development dependencies needed to run the tests, build the documentation, lint, format, and manage the pre-commit hooks.

#### 4. Activate the virtual environment

Activate the virtual environment by running:

```bash
. .venv/bin/activate
```

This will activate the virtual environment with the installed packages from the previous step.

#### 5. Install the pre-commit hooks

Install the pre-commit hooks by running:

```bash
pre-commit install
```

You can run the pre-commit hooks at any time with:
    
```bash
pre-commit run [--all-files]
```

Using the `--all-files` flag will run the pre-commit hooks on all files in the repository. If you don't use the flag, the pre-commit hooks will only run on the files you've staged for commit.

### :rocket: Development

Now that you have your development environment set up, you can:
1. Make changes to the code and run the code in a consistent environment.
2. Run the tests.
3. Build the documentation.
4. Lint and format the code.
5. Commit your changes.

#### Running tests

To run the tests, use the following command:

```bash
pytest
```

This command will run the tests in the `test` directory.

#### Building the documentation

To build the documentation, use the following command:

```bash
make -C docs html
```

This command builds the documentation using [Sphinx](https://www.sphinx-doc.org/en/master/). The documentation will be built in the `docs/build/html` directory.

#### Linting and formatting the code

To lint and format the code, run the pre-commit hooks:

```bash
pre-commit run --all-files
```

The first step in the pre-commit hook is to lint the code using [`ruff`](https://docs.astral.sh/ruff/). `ruff` is installed as a development dependency and is used to enforce code quality standards as well as format the code. If `ruff` finds any issues, it will print them to the console and exit with a non-zero status code.

If you want to automatically fix the issues printed in this stage, you can run:

```bash
ruff check --fix
```

Doing this will automatically fix any issues that can be fixed automatically. If there are any issues that can't be fixed automatically, you'll need to fix them manually.