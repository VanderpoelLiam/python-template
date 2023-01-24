# python-template
A Python project template

## Installing Python with pyenv
We recommend using `pyenv` to manage different Python environments, see [Pyenv](https://github.com/pyenv/pyenv#getting-pyenv) for more details.
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

