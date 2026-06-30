# Python Packaging (`pyproject.toml`, Virtual Environments, `uv`, Poetry)

## What is Packaging?

Packaging is the process of organizing a Python project so that:

* Dependencies are managed
* The project can be installed easily
* Every developer uses the same environment
* The application works consistently across different machines

Modern Python projects use:

* `pyproject.toml`
* Virtual Environments
* Package managers like **uv** or **Poetry**

---

# Why Do We Need Packaging?

Imagine two developers.

Developer A has:

```text
Python 3.12
FastAPI 0.115
Pydantic 2.10
```

Developer B has:

```text
Python 3.10
FastAPI 0.95
Pydantic 1.10
```

The same code may work for A but fail for B.

Packaging ensures everyone uses the same versions.

---

# Virtual Environments

A virtual environment creates an isolated Python installation for one project.

Instead of installing packages globally:

```text
Computer

├── Project A
├── Project B
└── Project C
```

each project has its own environment.

```text
Project A
│
└── .venv

Project B
│
└── .venv

Project C
│
└── .venv
```

This prevents dependency conflicts.

---

# Why Not Install Everything Globally?

Suppose:

Project A needs:

```text
FastAPI 0.95
```

Project B needs:

```text
FastAPI 0.115
```

A global installation cannot satisfy both versions simultaneously.

Virtual environments solve this problem.

---

# What is `pyproject.toml`?

`pyproject.toml` is the modern configuration file for Python projects.

It replaces older files like:

* `setup.py`
* `setup.cfg`
* `requirements.txt` (partially)

It stores:

* Project metadata
* Dependencies
* Python version
* Build system
* Tool configurations

Example:

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "Demo Project"
requires-python = ">=3.11"

dependencies = [
    "fastapi",
    "uvicorn",
    "pydantic"
]
```

---

# What is `uv`?

`uv` is a modern Python package manager written in Rust.

Advantages:

* Extremely fast
* Creates virtual environments
* Installs packages
* Locks dependencies
* Compatible with `pyproject.toml`

Example:

```bash
uv init
uv venv
uv add fastapi
uv run main.py
```

---

# Why is `uv` Popular?

Traditional installation:

```text
pip

↓

Slow dependency resolution
```

Modern:

```text
uv

↓

Very fast dependency resolution
```

Large projects install significantly faster.

---

# What is Poetry?

Poetry is another package manager.

It manages:

* Dependencies
* Virtual environments
* Packaging
* Publishing libraries

Example:

```bash
poetry init
poetry add fastapi
poetry install
poetry run python main.py
```

---

# `uv` vs Poetry

| Feature               | uv                   | Poetry               |
| --------------------- | -------------------- | -------------------- |
| Speed                 | Very Fast            | Fast                 |
| Written In            | Rust                 | Python               |
| Dependency Management | Yes                  | Yes                  |
| Virtual Environments  | Yes                  | Yes                  |
| Package Publishing    | Basic                | Excellent            |
| Current Trend         | Increasingly Popular | Mature & Widely Used |

---

# Typical Project Structure

```text
my_project/

├── .venv/
├── src/
│   └── app.py
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# Installing Packages

Using uv:

```bash
uv add fastapi
uv add requests
```

Using Poetry:

```bash
poetry add fastapi
poetry add requests
```

Dependencies are automatically written to `pyproject.toml`.

---

# Running a Project

Using uv:

```bash
uv run python src/app.py
```

Using Poetry:

```bash
poetry run python src/app.py
```

---

# Lock Files

Package managers generate lock files.

Purpose:

* Freeze exact dependency versions
* Ensure every developer installs identical packages

Examples:

```text
uv.lock
poetry.lock
```

---

# Real-World Example

Suppose you're building an AI chatbot.

Dependencies:

```text
FastAPI
OpenAI
LangChain
Pydantic
SQLAlchemy
```

Instead of asking teammates to install each package manually, they simply run:

```bash
uv sync
```

or

```bash
poetry install
```

Everything is installed automatically.

---

# Why Companies Use Packaging

Without packaging:

```text
Developer A

↓

Works

Developer B

↓

ModuleNotFoundError
```

or

```text
Different package versions

↓

Unexpected bugs
```

With packaging:

```text
Clone Repository

↓

Install Dependencies

↓

Run Application

↓

Works Everywhere
```

---

# Advantages

* Reproducible environments
* No dependency conflicts
* Easy onboarding
* Easy deployment
* Consistent Python versions
* Professional project structure

---

# Interview Questions

### What is a virtual environment?

An isolated Python environment for a project that has its own interpreter and installed packages.

---

### Why use virtual environments?

To prevent dependency conflicts between projects.

---

### What is `pyproject.toml`?

The modern configuration file for Python projects containing metadata, dependencies, and build information.

---

### What does `uv` do?

It manages virtual environments, installs dependencies, resolves packages, and runs Python projects quickly.

---

### Difference between pip and uv?

| pip               | uv                   |
| ----------------- | -------------------- |
| Older             | Modern               |
| Slower            | Much Faster          |
| Package Installer | Full Project Manager |

---

### Difference between uv and Poetry?

* `uv` focuses on speed and modern workflows.
* Poetry provides a mature ecosystem for dependency management and publishing.

---

# Quick Revision

```text
Virtual Environment
        │
        ├── Isolated Python
        ├── Prevents dependency conflicts
        └── One per project

pyproject.toml
        │
        ├── Project metadata
        ├── Dependencies
        ├── Python version
        └── Build configuration

uv
        │
        ├── Fast package manager
        ├── Creates virtual environments
        ├── Installs packages
        └── Runs projects

Poetry
        │
        ├── Dependency manager
        ├── Virtual environments
        ├── Packaging
        └── Publishing
```

---

# One-Line Summary

> Modern Python packaging uses virtual environments and `pyproject.toml` to create reproducible, isolated projects, while tools like `uv` and Poetry manage dependencies, environments, and project execution efficiently.
