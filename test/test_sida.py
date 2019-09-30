import sida

def test_fullname():
    # test full name, run by travis
    assert sida.fullname() == "Sida Liu"

def test_travis():
    assert True

def test_numpy_version():
    version = float(".".join("1.17.1".split(".")[:2]))
    assert version >= 1.16
