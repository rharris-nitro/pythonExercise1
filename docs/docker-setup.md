# Setting Up Docker<a name="setting-up-docker"></a>

- [Download Docker](#download-docker)
  - [For Windows](#for-windows)
  - [For macOS](#for-macOS)
  - [For Linux](#for-linux)
- [Verify Docker Installation](#docker-verification)

## Download Docker:<a name="download-docker">

Visit the official Docker website: [Get Docker](https://docs.docker.com/get-docker/).

### For Windows:<a name="for-windows"></a>

1. Click on the "Download for Windows" button.
1. Follow the on-screen instructions to download the Docker Desktop Installer.
1. Once the download is complete, run the installer.
1. During the installation process, you may be prompted to enable Hyper-V. Allow this if prompted.
1. After installation, Docker Desktop will start automatically.
1. You should see the Docker icon in the system tray. Docker is now installed and running on your Windows machine.

### For macOS:<a name="for-macOS"></a>

1. Click on the "Download for Mac" button.
1. Follow the on-screen instructions to download the Docker Desktop Installer.
1. Once the download is complete, open the Docker.dmg file.
1. Drag the Docker icon to the Applications folder.
1. Open Docker from the Applications folder.
1. You should see the Docker icon in the menu bar. Docker is now installed and running on your macOS machine.

### For Linux:<a name="for-linux"></a>

1. Click on the "Download for Linux" button.
1. Follow the instructions for your specific Linux distribution. Docker provides installation instructions for various Linux distributions like Ubuntu, Debian, Fedora, CentOS, etc.
1. After completing the installation steps, start the Docker service.
1. On Ubuntu, you can use the following commands:
   `sudo service docker start`
1. On systems using systemd (e.g., Ubuntu 16.04 and later), you can use:
   `sudo systemctl start docker`
1. Docker is now installed and running on your Linux machine.

## Verify Docker Installation:

To verify that Docker is installed correctly, open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run the following command:
`docker --version`
You should see information about the Docker version.
Additionally, you can run the following command to verify that Docker is able to run containers:
`docker run hello-world`
This command downloads a small test image and runs it in a container. If everything is set up correctly, you'll see a "Hello from Docker!" message.
