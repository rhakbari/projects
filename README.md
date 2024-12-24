# Projects

## Personal project/practices

https://realpython.com/primer-on-python-decorators/

# Installing packages using pip and virtual environments

This guide discusses how to install packages using pip and a virtual environment manager: virtualenv for Python 3. 

## Installing pip
pip is the reference Python package manager. It’s used to install and update packages. You’ll need to make sure you have the latest version of pip installed.


## This is for Linux only 
Debian and most other distributions include a python-pip package, if you want to use the Linux distribution-provided versions of pip see Installing pip/setuptools/wheel with Linux Package Managers.

You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
$ python3 -m pip install --user --upgrade pip
```
Afterwards, you should have the newest pip installed in your user site:
```
$ python3 -m pip --version
```

# Installing Virtualenvwrapper

If you're using Ubuntu 24.04 or above then write:

```
sudo apt install python3-virtualenvwrapper

```
This is because python2 has been deleted from ubuntu 20.04 and in order to use python or pip we have to write "3" in the end:

After that open your terminal and write:

```
$ sudo nano .bashrc
```

Then in the last add these lines:

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/home/YOUR_USERNAME/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```
## To make your virtual environment write the below command:

```
$ mkvirtualenv (name of your environment)
```

## Leaving the virtual environment

If you want to switch projects or otherwise leave your virtual environment, simply run:

```
$ deactivate
```

## In order to continue working with your previous environment just write the below command:

```
$ workon (name of your environment)
```

If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment. There’s no need to re-create the virtual environment.

## Terminal Shortcuts: 
### Terminal Window Tabs
- Shift+Ctrl+T: Open a new tab.
- Shift+Ctrl+W Close the current tab.
- Ctrl+Page Up: Switch to the previous tab.
- Ctrl+Page Down: Switch to the next tab.
- Shift+Ctrl+Page Up: Move to the tab to the left.
- Shift+Ctrl+Page Down: Move to the tab to the right.
- Alt+1: Switch to Tab 1.
- Alt+2: Switch to Tab 2.
