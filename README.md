# Projects

## personal project/practices

https://realpython.com/primer-on-python-decorators/

# Installing packages using pip and virtual environments

This guide discusses how to install packages using pip and a virtual environment manager: either venv for Python 3 or virtualenv for Python 2. These are the lowest-level tools for managing Python packages and are recommended if higher-level tools do not suit your needs.

Note This doc uses the term package to refer to a Distribution Package which is different from a Import Package that which is used to import modules in your Python source code.
## Installing pip
pip is the reference Python package manager. It’s used to install and update packages. You’ll need to make sure you have the latest version of pip installed.

## Windows
The Python installers for Windows include pip. You should be able to access pip using:
```
py -m pip --version
```
pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
You can make sure that pip is up-to-date by running:
```
py -m pip install --upgrade pip
```
## Linux and macOS
Debian and most other distributions include a python-pip package, if you want to use the Linux distribution-provided versions of pip see Installing pip/setuptools/wheel with Linux Package Managers.

You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
python3 -m pip install --user --upgrade pip
```
Afterwards, you should have the newest pip installed in your user site:
```
python3 -m pip --version
```
pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)
Installing virtualenv
Note If you are using Python 3.3 or newer, the venv module is the preferred way to create and manage virtual environments. venv is included in the Python standard library and requires no additional installation. If you are using venv, you may skip this section.
virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

## On macOS and Linux:
```
python3 -m pip install --user virtualenv
```
## On Windows:
```
py -m pip install --user virtualenv
```
Creating a virtual environment
venv (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

On macOS and Linux:
```
python3 -m venv env
```
On Windows:
```
py -m venv env
```
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.

venv will create a virtual Python installation in the env folder.

Note You should exclude your virtual environment directory from your version control system using .gitignore or similar.
Activating a virtual environment
Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

## On macOS and Linux:
```
source env/bin/activate
```
## On Windows:
```
.\env\Scripts\activate
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.
```
## On macOS and Linux:
```
which python
.../env/bin/python
```
## On Windows:

where python
.../env/bin/python.exe
As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

## Leaving the virtual environment
If you want to switch projects or otherwise leave your virtual environment, simply run:
```
deactivate
```
If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment. There’s no need to re-create the virtual environment.
