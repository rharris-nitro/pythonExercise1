# Local environment<a name="debugging-the-app"></a>

- [Setup local environment](#setup-local-environment)
  - [Overview](#overview)
  - [Docker Build & Run](#build-and-run)
  - [Run App](#running)

## Setup local environment<a name="setup-local-environment"></a>

### Overview<a name="overview"></a>

Setting up the local environment is simple:

- Clone the repository.

```bash
git clone https://github.com/rharris-nitro/pythonExercise1.git
```

See [How To: Git](how-to-git.md) for more info.

- Setup pre-commit hooks and install hooks for git repo.

```bash
pip install pre-commit
cd pythonExercise1
pre-commit install
```

See [All About Precommit Hooks](all-about-precommit-hooks.md) for more info.

- [Installing Python](installing-python.md)

- [Install Docker](docker-setup.md)

## Build Docker image and run container<a name="build-and-run"></a>

### Run App<a name="running"></a>

- Build the Docker image using the provided Dockerfile:

  ```bash
  docker build -t my-python-app --target main .
  ```

- Run a container from the built Docker image:

  ```bash
  docker run my-python-app
  ```

You should see the output of your Python script:
\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]

### Testing App<a name="testing"></a>

- Build the Docker image using the provided Dockerfile:

  ```bash
  docker build -t my-python-test --target test .
  ```

- Run a container from the built Docker image:

  ```bash
  docker run my-python-test
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
