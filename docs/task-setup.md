# Installing Task on your machine

## Using Homebrew:

```bash
brew install go-task/tap/go-task
```

After installed, check it is working by creating a `Taskfile.yml`.

## Example:

```bash
version: '3'

tasks:
  hello:
    cmds:
      - echo 'Hello World from Task!'
    silent: true
```

Then on the command line, run `task hello` and it should print "Hello World from Task!" on the terminal.
