import pybind11_test_dmpytain as ptd

def test():
    assert ptd.__version__ == '0.0.1'
    assert ptd.add(1, 2) == 3
    assert ptd.subtract(1, 2) == -1