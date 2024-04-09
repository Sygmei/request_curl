import pytest

import curlquest


@pytest.fixture()
def session():
    return curlquest.Session(verify=False)
