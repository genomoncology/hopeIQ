import pytest
from hopeiq import SyncKB


@pytest.fixture(scope="session")
def kb():
    return SyncKB()
