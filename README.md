# smormlpy

A cookiecutter skeleton and style guide lines for SMO/MRML python tools.

---
## Usage

This serves as our main repository on how to build tools and code. Additionally it comes with a cookiecutter-template which has the main features of our code-habits already integrated.

### Version-Control

### Documentation

To generate HTML/PDF documentation via pdoc3 run either of the following in your venv-shell:

- `pdoc3 --html --http localhost:8090 your_new_project/` for an interactive preview of the HTML-docs.
## Installation and Project Generation

1. Install `poetry` if you don't have it: `pip install poetry`.
2. Clone this repo, go into the repo's folder.
3. Install the dependencies with `poetry install` and spawn a shell in your new virtual environment with `poetry shell`.
3. Generate your new project: `cookiecutter smormlpy/`. This will ask you a couple of questions about your new project, finally a new folder named after your new project will be created.   
4. Create a Git-repository in your newly created project folder.
5. Done, over and out.

---

[Philipp Kessling](mailto:p.kessling@leibniz-hbi.de) under the MIT license.
