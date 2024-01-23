# pythonExercise1
First coding exercise to get experience in a professional environment

    This script demonstrates a simple Python program that initializes an array of integers with predefined values and prints the array.


    Usage:
        - Run the script using a Python interpreter.

    Example:
        $ python3 main.py




Second exercise was to add pre-commit hooks and make sure to run them

    Clone repo:
        -   git clone {git@github.com:Nitro... ...app.git}
    
    Create local branch:
        -   git fetch origin
        -   git checkout --no-track -b {branch-name} origin/main

    Add to Staging Area:
        -   git status  # copy filepath
        -   git add {filepath}

    Commit files to local repo: # best practice is one file at a time
        -   git commit -m "commit message"

    Push to origin:
        -   git push -u origin {branch-name}

    Create Pull Request on GitHub webapp:
        -   Under "Pull requests", a new notification should show up to "Compare & pull requests". Click this.
        -   In order to merge without PR, use `git merge main`. YOU DO NOT WANT TO DO THIS!!! It merges your personal remote branch to the main without review.