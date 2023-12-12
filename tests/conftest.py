import os

import pytest
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    # TODO: workaround to set calling root path, because pytest runs from the root dir
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
