# Local environment<a name="debugging-the-app"></a>

- [Setup local environment](#setup-local-environment)
  - [Overview](#overview)
  - [Cloning the Repository](#clone-repo)
  - [Pre-commit Hooks](#precommit-hooks)
  - [Installing Python](#installing-python)
- [Docker Build & Run](#build-and-run)
  - [Run App](#running)

## Setup local environment<a name="setup-local-environment"></a>

### Overview<a name="overview"></a>

Setting up the local environment is simple:

- Clone the repository in a specific file path.
  See also: [How To: Git](how-to-git.md)

- Setup pre-commit hooks.
  [All About Precommit Hooks](all-about-precommit-hooks.md)

- Install Hook for git repo

```bash
cd pythonExercise1
pre-commit install
```

- Download and install Python
  [Installing Python](installing-python.md)

- Build Docker image and run container
  [Setting Up Docker](docker-setup.md)

### Cloning the Repository<a name="clone-repo"></a>

- Head to where you want to put the repo on your machine with:
  `cd /path/to/your/directory`

- Then use the clone command:
  `git clone https://github.com/rharris-nitro/pythonExercise1.git`

### Pre-commit Hooks<a name="precommit-hooks"></a>

- Head to the current `.pre-commit-config.yaml` in this repo to see what is best to use in my opinion.

### Installing Python<a name="installing-python"></a>

- Download and install Python
  [Installing Python](installing-python.md)

## Build Docker image and run container<a name="build-and-run"></a>

### Run App<a name="running"></a>

- Build the Docker image using the provided Dockerfile:

  ```bash
  docker build -t my-python-app-main --target main .
  ```

  Replace my-python-app-main with your desired name for your main Docker image

- Run a container from the built Docker image:
  `docker run my-python-app-main`

You should see the output of your Python script:
\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]

### Testing App<a name="testing"></a>

- Build the Docker image using the provided Dockerfile:

  ```bash
  docker build -t my-python-app-test --target test .
  ```

  Replace my-python-app-test with your desired name for your testing Docker image

- Run a container from the built Docker image:
  `docker run my-python-app-test`

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
