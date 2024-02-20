Second exercise was to properly understand how to push something to GitHub

```
Clone repo:
    -   git clone {git@github.com:Nitro... ...app.git}

Create local branch:
    -   git fetch origin
    -   git checkout -b {branch-name} origin/main

Add to Staging Area:
    -   git status  # copy filepath
    -   git diff    # to see the changes
    -   git add {filepath}

Commit files to local repo: # best practice is one file at a time
    -   git commit -m "commit message"

Push to origin:
    -   git push (-u) origin <branch-name> # only use -u if branch is on GitHub

Create Pull Request on GitHub webapp:
    -   Under "Pull requests", a new notification should show up to "Compare & pull requests". Click this.  # refer to PR#406
    -   In order to merge without PR, use `git merge main`. YOU DO NOT WANT TO DO THIS!!! It merges your personal remote branch to the main without review.
```
