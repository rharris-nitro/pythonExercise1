# Configuring coverage.py for Python Projects

Coverage.py is a powerful tool for measuring code coverage of Python programs. It helps developers understand which parts of their code are executed during testing and which parts are not. This guide will walk you through the process of configuring `coverage.py` for your project.

## Creating a Configuration File

`coverage.py` can be configured using a `.coveragerc` file or a `pyproject.toml` file. For this guide, we'll focus on the `.coveragerc` file.

1. **Create a `.coveragerc` file**: In the root directory of your project, create a new file named `.coveragerc`.

1. **Edit the `.coveragerc` file**: Open the `.coveragerc` file in your text editor and add your configuration settings. Here's an example configuration:

```bash
[run]
omit = "/usr/local/*", "tests/*"

[report]
exclude_lines = "pragma: no cover", "if name == 'main':"
```

### Understanding the Configuration

- **\[run\]**: This section contains settings that affect the execution of your program under coverage.py.

- `omit`: Specifies files or directories to omit from coverage collection. This is useful for excluding third-party libraries or test code.

- **\[report\]**: This section contains settings that affect the generation of coverage reports.

- `exclude_lines`: Specifies lines to exclude from coverage reports. This is useful for excluding lines that are not relevant to coverage, such as lines marked with `# pragma: no cover` or the `if __name__ == '__main__':` block.

## More Info:

Full documentation is [here](https://coverage.readthedocs.io/en/7.4.4)
