from sida import fullname

def test_fullname():
    # test full name, run by travis
    assert fullname() == "Sida Liu"