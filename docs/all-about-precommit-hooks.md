Exercise 3 is learning about pre-commit hooks. Link: https://medium.com/@anton-k./how-to-set-up-pre-commit-hooks-with-python-2b512290436

```
Pre-commit hooks are script tests ran before you commit your changes. They check for format and validity.

To setup:
    - Make sure you have a local git repository to pre-commit to, for starters
    - You want to install pre-commit into the root folder of the git repo with `pip install pre-commit`
    - Add a `.pre-commit-config.yaml`. You can generate a basic one with `pre-commit sample-config`
    - Then install the git hook scripts by going to the repo root folder and entering `pre-commit install`

Now when you commit changes to this repo, checks will run.
```
