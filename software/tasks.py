import hashlib
import os
import sys
from pathlib import Path

from invoke import Context, task
from pkg_resources import parse_version

_root = Path(__file__).parent


def _assert_py_version():
    current = sys.version_info

    version_file = _root / ".python-version"
    with open(version_file, "r") as vf:
        expected = parse_version(vf.readline())

    if current.minor < expected.minor and current.major <= expected.major:
        print(f"Python version is {current.major}.{current.minor} but minimum is {expected.major}.{expected.minor}")
        exit(1)


def _assert_venv():
    if os.environ.get("CI"):
        return

    venv_var = os.environ.get("VIRTUAL_ENV")
    if venv_var:
        return

    print("Must create/activate a virtual environment first.")
    exit(1)


def safe_task(*args, **kwargs):
    _assert_py_version()
    _assert_venv()

    return task(*args, **kwargs)


@safe_task()
def setup(ctx: Context):
    ctx.run("python -m pip install -U pip setuptools wheel")

    ctx.run(f"pip install -U " f'-r "{_root}/requirements.txt" ' f'-r "{_root}/requirements-dev.txt" ')

    ctx.run("pre-commit install")


@safe_task()
def compile_resources(ctx: Context):
    _assert_py_version()
    _assert_venv()

    ctx.run(
        f"compile-pyside-theme "
        f"--extra-python-path {_root / 'src'} "
        f"--custom-theme theme.ODC_THEME "
        f"--extra-qresources theme.ODC_RESOURCES "
        f"--extra-qss-templates {_root / 'src' / 'theme' / 'connection-config-widget.qss.jinja2'} "
        f"--extra-qss-templates {_root / 'src' / 'theme' / 'experiment-control-widget.qss.jinja2'} "
        f"--extra-qss-templates {_root / 'src' / 'theme' / 'param-list-widget.qss.jinja2'} "
        f"{_root / 'src' / 'theme'}",
        in_stream=False,
    )


@safe_task(compile_resources)
def run(ctx, debug=True):
    _assert_py_version()
    _assert_venv()

    flags = [" "]
    if debug:
        flags.append("debug")

    app_file = _root / "src" / "app.py"

    ctx.run(f"python {app_file}{' --'.join(flags)}")


@safe_task()
def lint(ctx: Context):
    ctx.run(f"black -t py311 {_root}")


@safe_task()
def test(ctx: Context):
    _assert_py_version()
    _assert_venv()

    test_root = _root / "test" / "unit"

    ctx.run(f'pytest -k "test_" "{test_root}"')


@safe_task(compile_resources)
def release(ctx: Context):
    _assert_py_version()
    _assert_venv()

    spec_file = _root / "spec" / "macos.spec"

    ctx.run(f'pyinstaller --clean --noconfirm "{spec_file}"')

    exe_file = (
        _root / "dist" / "Open Dynamic Clamp Workbench.app" / "Contents" / "MacOS" / "Open Dynamic Clamp Workbench"
    )

    _write_hash(exe_file, _root / "dist" / "checksum.sha256")


def _write_hash(file: Path, target: Path):
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(block)

    with open(target, "w") as t:
        t.write(sha256_hash.hexdigest())
