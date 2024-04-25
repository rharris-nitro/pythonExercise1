# Local environment<a name="debugging-the-app"></a>

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Setup local environment](#setup-local-environment)
  - [Clone the repository.](#clone-the-repository)
  - [Setup pre-commit hooks and install hooks for git repo.](#setup-pre-commit-hooks-and-install-hooks-for-git-repo)
  - [Installing Python](#installing-python)
  - [Install Docker](#install-docker)
  - [Install Task](#install-task)
  - [Install VSCode](#install-vscode)
- [Build Docker image and run container using Task](#build-docker-image-and-run-container-using-task)
  - [Run App](#run-app)
  - [Testing App](#testing-app)
- [Debugging](#debugging)
  - [Debugging main](#debugging-main)

<!-- mdformat-toc end -->

## Setup local environment<a name="setup-local-environment"></a>

### Clone the repository.<a name="clone-the-repository"></a>

```bash
git clone https://github.com/rharris-nitro/pythonExercise1.git
```

See [How To: Git](how-to-git.md) for more info.

### Setup pre-commit hooks and install hooks for git repo.<a name="setup-pre-commit-hooks-and-install-hooks-for-git-repo"></a>

```bash
pip install pre-commit
cd pythonExercise1
pre-commit install
```

See [All About Precommit Hooks](all-about-precommit-hooks.md) for more info.

### [Installing Python](installing-python.md)<a name="installing-python"></a>

### [Install Docker](docker-setup.md)<a name="install-docker"></a>

### Install Task<a name="install-task"></a>

If you are using Homebrew, enter this into the command line:

```bash
brew install go-task/tap/go-task
```

For more info, visit the [Taskfile website](https://taskfile.dev/)

### Install VSCode<a name="install-vscode"></a>

Install VSCode from [here](https://code.visualstudio.com/).
After setting up, you should open the folder in VSCode in the directory where the repo is cloned.

## Build Docker image and run container using Task<a name="build-docker-image-and-run-container-using-task"></a>

### Run App<a name="run-app"></a>

- Build and run a container using Task:

  ```bash
  task build
  task up
  ```

You should see the output of your Python script:

```bash
my-python-app  | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Testing App<a name="testing-app"></a>

- Build and run a container using Task:

  ```bash
  task up-test
  ```

You should see the output of your pytest test:

```bash
my-python-app  | ============================= test session starts ==============================
my-python-app  | platform linux -- Python 3.11.9, pytest-7.4.3, pluggy-1.5.0
my-python-app  | rootdir: /pythonExercise1
my-python-app  | collected 3 items
my-python-app  |
my-python-app  | tests/test_main.py ...                                                   [100%]
my-python-app  |
my-python-app  | ============================== 3 passed in 0.06s ===============================
my-python-app  | Name                 Stmts   Miss  Cover
my-python-app  | ----------------------------------------
my-python-app  | app/__init__.py          0      0   100%
my-python-app  | app/data.py              7      0   100%
my-python-app  | tests/__init__.py        0      0   100%
my-python-app  | tests/test_main.py      12      0   100%
my-python-app  | ----------------------------------------
my-python-app  | TOTAL                   19      0   100%
my-python-app  | Wrote HTML report to htmlcov/index.html
```

This shows the pytest on the first half, the coverage report on the second half, and the last line shows there is a nicer HTML format at the given folder path if you don't like the CLI report format

For more info about how pyTest works, visit [Pytest for Absolute Beginners](https://medium.com/analytics-vidhya/pytest-for-absolute-beginners-4a166324b350)
For more info on coverage.py, go to \<coverage-testing.md>

## Debugging<a name="debugging"></a>

### Debugging main<a name="debugging-main"></a>

To debug the main image in VSCode, run the image using task and set USE_DEBUG to true:

```bash
task up USE_DEBUGPY=true
```

The same can be done for the test image (FYI: this can only debug unit test, not coverage test)

Go to the Run and Debug section in VSCode, make sure the Debugger is on Remote Attach, and press the green play button.

See \<debugging.md> for more info
