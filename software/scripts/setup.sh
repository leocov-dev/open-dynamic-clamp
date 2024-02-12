#!/usr/bin/env bash

set -e

__repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
# shellcheck source=./lib/utilities
source "${__repo}/scripts/lib/utilities"

# ------------------------------------------------------------------------------
# If you want to use a custom location for the python venv
# you must set ODC_VENV_OVERRIDE environment variable with
# the path to the venv directory
# ------------------------------------------------------------------------------

skip_in_ci activate_venv
skip_in_ci install_python_deps
