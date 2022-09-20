from test.engine import eg


def test_success_engine():
    engine = eg()
    assert (True == engine.ALL()), "Test case failed!"
