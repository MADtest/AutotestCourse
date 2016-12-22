import pytest


def f():
    raise SystemExit(1)

# @pytest.mark.xfail(raises=SystemExit, reason='I have exited')
def test_exeption():
    with pytest.raises(SystemExit):
        f()
