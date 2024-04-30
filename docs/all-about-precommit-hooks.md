Exercise 3 is learning about pre-commit hooks. Link: https://medium.com/@anton-k./how-to-set-up-pre-commit-hooks-with-python-2b512290436

Pre-commit hooks are script tests ran before you commit your changes. They check for format and validity.

To setup:

- Make sure you have a local git repository to pre-commit to, for starters
- You want to install pre-commit into the root folder of the git repo with `pip install pre-commit`
- Add a `.pre-commit-config.yaml`. You can generate a basic one with `pre-commit sample-config`
- Then install the git hook scripts by going to the repo root folder and entering `pre-commit install`

Now when you commit changes to this repo, checks will run.
OR
If you would like to run the pre-commits before committing you can enter:

```bash
task pre-commit
```

To run a specific hook, enter `pre-commit run <hook-id> --all-files` with `<hook-id>` being the name of the hook.

Recommendations:
Here are some basic hooks, linters, and formatters to make everything look pretty.
None are necessary but all are useful. (Also revs may vary)

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace # removes whitespace
    -   id: end-of-file-fixer   # adds empty stringto end of file
    -   id: check-yaml  # structures yamls
    -   id: check-toml  # structures tomls
    -   id: check-json  # structures jsons
    -   id: check-xml  # structures xmls
    -   id: check-added-large-files # stops big commits
        args: [— maxkb=1000]
    -   id: check-merge-conflict    # stops unresolved conflicts
    -   id: check-ast   # checks .py files are valid
    -   id: debug-statements    # helps debugger statements

-   repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
    -   id: isort

-   repo: https://github.com/executablebooks/mdformat
    rev: 0.7.17
    hooks:
    -   id: mdformat
        additional_dependencies:
        -   mdformat-gfm
        -   mdformat-black
        -   mdformat-config
        -   mdformat-toc

-   repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
    -   id: black

-   repo: https://github.com/pre-commit/mirrors-mypy
    # Mypy is a static type checker for Python
    rev: v1.7.1
    hooks:
    -   id: mypy
        entry: mypy

-   repo: https://github.com/PyCQA/pylint
    rev: v3.0.3
    hooks:
    -   id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        args: ["-rn", # Only display messages
          "-sn"] # Don't display the score

```
