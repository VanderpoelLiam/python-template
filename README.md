# python-template

A Python project template

## Quickstart

It is recommended to set up Python using [pyenv](https://github.com/pyenv/pyenv#getting-pyenv). This quickstart guide assumes Python is already installed.

Install [Poetry](https://python-poetry.org/):

```
curl -sSL https://install.python-poetry.org | python3 -
```

Install [Nox]() and [nox-poetry](https://nox-poetry.readthedocs.io):

```
pip install nox nox-poetry
```

## Installing Python with pyenv

We recommend using `pyenv` to manage different Python environments, see [pyenv](https://github.com/pyenv/pyenv#getting-pyenv) for more details.
To install `pyenv` run:

```
curl https://pyenv.run | bash
```

Then add the following lines to `~/.bashrc` by running:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Reload `~/.bashrc`:

```
source ~/.bashrc
```

To install Python 3.10.5 run:

```
pyenv install 3.10.5
```

Create a new environment:

```
pyenv virtualenv 3.10.5 python-template
```

Then set this to the default Python version inside the repository:

```
pyenv local python-template
```

This initializes the `pyproject.toml` file.

## Setting up the project using Poetry

[Poetry](https://python-poetry.org/) is a tool to manage Python packaging and dependencies. See the [docs](https://python-poetry.org/docs/) for up to date installation instructions. To install Poetry run:

```
curl -sSL https://install.python-poetry.org | python3 -
```

To initialize the project with poetry run:

```
poetry init
```

and follow the interactive instructions.

## Testing

To test the code run:

```
nox -r
```

Nox uses `noxfile.py` for configuration. By default Nox recreates the virtual environments from scratch on each run. To speed things up we recommend passing the `-r` flag, see [re-using-virtualenvs](https://nox.thea.codes/en/stable/usage.html#re-using-virtualenvs) for details.

You can pass any additional arguments to `pytest` using `--`. For example, to run a specific test module:

```
nox -r -- tests/test_console.py
```

If you do not want to run any linting. You can run only the tests with:

```
nox -rs tests
```

You can also run a single test without linting:

```
nox -rs tests -- -k "test_main_succeeds"
```

## Adding dependencies

Poetry manages all dependencies of this repository, for details see [dependency-specification](https://python-poetry.org/docs/dependency-specification/). In short, to add a new dependency, such as `pandas`, run:

```
poetry add pandas
```

For a dependency of only the testing environment, such as `pytest`, run:

```
poetry add --group dev pytest
```

## Versioning

Poetry manages the version of this project, below I summarize the main points from [poetry version management](https://python-poetry.org/docs/cli/#version). To see the current version run:

```
poetry version
```

To bump the version of the project and write the new version back to `pyproject.toml` run:

```
poetry version <major/minor/patch>
```

e.g. to bump to the next major version run:

```
poetry version major
```

The effect of these rules are illustrated in the table below:
| rule | before | after |
|:-----: |:------: |:-----: |
| major | 1.3.0 | 2.0.0 |
| minor | 2.1.4 | 2.2.0 |
| patch | 4.1.1 | 4.1.2 |

## Credits

This project is inspired by [hypermodern-python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
