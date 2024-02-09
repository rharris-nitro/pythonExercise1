# Local environment<a name="debugging-the-app"></a>

- [Setup local environment](#setup-local-environment)
  - [Overview](#overview)
  - [Cloning the Repository](#clone-repo)
  - [Installing Python](#installing-python)

## Setup local environment<a name="setup-local-environment"></a>

### Overview<a name="overview"></a>

Setting up the local environment is simple:

- Clone the repository in a specific file path.
  See also: [How To: Git](how-to-git.md)

- Download and install Python
  [Installing Python](installing-python.md)

- Build Docker image and run container
  [Setting Up Docker](docker-setup.md)

### Cloning the Repository<a name="clone-repo"></a>

- Head to where you want to put the repo on your machine with:
  `cd /path/to/your/directory`

- Then use the clone command:
  `git clone https://github.com/rharris-nitro/pythonExercise1.git`

### Installing Python<a name="installing-python"></a>

- Download and install Python
  [Installing Python](installing-python.md)

### Build Docker image and run container

- Build the Docker image using the provided Dockerfile:
  `docker build -t my-python-app .`
  Replace my-python-app with your desired name for your Docker image

- Run a container from the built Docker image:
  `docker run my-python-app`

You should see the output of your Python script:
\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]

Additional notes:
If you encounter any issues during the build or run steps, ensure that your Dockerfile and Python script are in the correct locations, and there are no typos in the commands.

