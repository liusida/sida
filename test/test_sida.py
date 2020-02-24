import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"src"))
import sida

def test_version():
    assert sida.__version__ == "0.1.0"

def test_fullname():
    # test full name, run by travis
    assert sida.fullname() == "Sida Liu"

def test_travis():
    assert True

def test_numpy_version():
    version = float(".".join("1.17.1".split(".")[:2]))
    assert version >= 1.16
