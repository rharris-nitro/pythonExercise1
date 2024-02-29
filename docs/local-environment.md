# Local environment<a name="debugging-the-app"></a>

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Setup local environment](#setup-local-environment)
  - [Clone the repository.](#clone-the-repository)
  - [Setup pre-commit hooks and install hooks for git repo.](#setup-pre-commit-hooks-and-install-hooks-for-git-repo)
  - [Installing Python](#installing-python)
  - [Install Docker](#install-docker)
  - [Install Task](#install-task)
- [Build Docker image and run container using Task](#build-docker-image-and-run-container-using-task)
  - [Run App](#run-app)
  - [Testing App](#testing-app)

<!-- mdformat-toc end -->

## Setup local environment<a name="setup-local-environment"></a>

Setting up the local environment is simple:

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

## Build Docker image and run container using Task<a name="build-docker-image-and-run-container-using-task"></a>

### Run App<a name="run-app"></a>

- Build the Docker image:

  ```bash
  task build-app
  ```

- Run a container from the built Docker image:

  ```bash
  task run-app
  ```

You should see the output of your Python script:
\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]

### Testing App<a name="testing-app"></a>

- Build the Docker image:

  ```bash
  task build-test
  ```

- Run a container from the built Docker image:

  ```bash
  task run-test
  ```

You should see the output of your pytest test:

```bash
============================= test session starts ==============================
platform linux -- Python 3.11.8, pytest-7.4.3, pluggy-1.4.0
rootdir: /
collected 2 items

test_main.py ..                                                          [100%]

============================== 2 passed in 0.01s ===============================
```

For more info about how pyTest works, visit [Pytest for Absolute Beginners](https://medium.com/analytics-vidhya/pytest-for-absolute-beginners-4a166324b350)
