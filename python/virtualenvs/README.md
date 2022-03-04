# Introduction to Virtual Environments
Virtual environments are the preferred method of choice for managing dependencies in Python.

## What is a virtual environment?
A virtual environment is an isolated Python environment. It creates a directory for your Python packages and resolves dependencies by checking that directory first.

## Why is it useful?
When working locally, we might have multiple projects, each with their own sets of dependencies. Sometimes these dependencies might conflict, with one using an earlier package version, or even a different Python version than another. Virtual environments keep these dependencies project-specific, so that they are not conflicting. Similarly, we might run multiple different applications on a single server.


## How to use them
### Create
You can create a virtual environment using Python 3's `-m` (mod) option.
```sh
python3 -m venv my_virtual_env
```
This will create a virtual environment called `my_virtual_env`.

### Activate
To activate your virtual environment, you have to use `source` (there are utilities available to make this easier).
```sh
source my_virtual_env/bin/activate
```

### Installing dependencies
The best way to install Python dependencies is using `pip`.

To install a simple dependency by name, you can do:
```sh
pip install requests
```
This will install the latest version of the package by default.

You can specify a specific version using `==`. For instance,
```sh
pip install requests==2.25.1
```
You can also install dependencies from a file. This is what you need to use when building any sort of application. To create a file listing requirements, you can use `pip freeze`.
```sh
pip freeze > requirements.txt
```
This will dump the package names and versions into the file. Another user can then setup their virtual environment as such:
```sh
pip install -r requirements.txt
```
