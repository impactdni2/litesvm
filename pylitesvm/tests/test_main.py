from pylitesvm import hello

def test_with_log_success():
    hello()

def test_with_log_fail():
    hello()
    assert 1 == 0
