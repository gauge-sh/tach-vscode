# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Constants for use with tests.
"""

from __future__ import annotations

import pathlib

TEST_ROOT = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = TEST_ROOT.parent.parent.parent
TEST_DATA = TEST_ROOT / "test_data"

BUNDLED_PYTHON_LIBS_DIR = PROJECT_ROOT / "bundled" / "libs"
