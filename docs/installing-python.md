# Installing Python<a name="installing-python"></a>

- [For Windows](#for-windows)
- [For macOS](#for-macOS)
- [For Linux (Ubuntu/Debian)](#for-ubuntu-debian)
- [For Linux (Fedora)](#for-fedora)

## For Windows<a name="for-windows"></a>

1. Open a Web Browser:
   Open your preferred web browser and go to the official Python website: [Python Downloads](https://www.python.org/downloads/).

1. Download Python:
   Click on the "Downloads" tab and select the version of Python you want. Choose the latest version marked as "Latest Python 3 Release."

1. Run the Installer:
   Once the installer is downloaded, double-click on the downloaded file (python-3.x.x.exe) to run the installer.

1. Configure Python:
   During the installation, make sure to check the box that says "Add Python to PATH." This makes it easier to run Python from the terminal.

1. Complete Installation:
   Follow the prompts in the Python Installer. Click "Install Now" to start the installation process.

1. Verify Installation:
   Open a new Command Prompt and type `python --version`

You should see the installed Python version.

## For macOS<a name="for-macOS"></a>

1. Open Terminal:
   Open the Terminal application. You can find it using Spotlight by pressing Cmd + Space and typing "Terminal."

1. Install Homebrew (if not installed):
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

1. Install Python using Homebrew:
   `brew install python`

1. Verify Installation:
   Type the following command to check the installed Python version with `python3 --version`

## For Linux (Ubuntu/Debian)<a name="for-ubuntu-debian"></a>

1. Open Terminal:
   Open a terminal window by pressing Ctrl + Alt + T.

1. Update Package List:
   `sudo apt-get update`

1. Install Python:
   `sudo apt-get install python3`

1. Verify Installation:
   Type the following command to check the installed Python version:
   `python3 --version`

## For Linux (Fedora)<a name="for-fedora"></a>

1. Open Terminal:
   Open a terminal window by pressing Ctrl + Alt + T.

1. Install Python:
   `sudo dnf install python3`

1. Verify Installation:
   Type the following command to check the installed Python version:
   `python3 --version`
