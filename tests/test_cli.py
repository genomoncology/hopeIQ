from hopeiq.cli import bootstrap, sync_config


def test_commands():
    assert bootstrap, "Didn't find bootstrap."
    assert sync_config, "Didn't find sync_config."
