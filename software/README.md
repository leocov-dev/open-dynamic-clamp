# Open Dynamic Clamp Workbench

- This is a PySide6 rewrite of the [original](https://github.com/christianrickert/pyClamp) with UI and communication protocol changes.  

Cross-platform desktop companion application
for [instrument hardware](../firmware/README.md).

![GUI example image](.github/img/workbench_gui.png)

## Install

```diff
! No release available at this time
```

The app can only be run in [development mode](#development) at this time.

## Development

### Setting up your environment

You must set up a Python virtual environment (preferably a new one) and activate it.

Example:

```shell
# from repository root directory
$ python -m venv .venv
# mac/linux
$ source .venv/bin/activate
# Windows
$ .venv/Scripts/activate.bat
```

### Install dependencies

This project uses [Invoke](https://www.pyinvoke.org/) to manage development tasks.
It may be globally installed or installed only in the local virtualenv.

```shell
# if needed
$ pip install invoke
```

```shell
# install all requirements, etc.
$ invoke setup
```

### Run locally for development

```shell
# start the app UI
$ invoke run

# additional in-app debug tools can be enabled with
$ invoke run --debug
```

### Running tests

```shell
$ invoke test
```

### Create a release package locally

```diff
! NOTE: The release process and scripts are still under development
```

```shell
$ invoke release
```