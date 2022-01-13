import pytest
from tictactoe import build_grid;
from pytest import approx

def grid_build_test():
    testing = build_grid(3)
    assert testing[0] == 1
    assert testing[1] == 2
    assert testing[2] == 3
    assert testing[3] == 4
    assert testing[4] == 5
    assert testing[5] == 6
    assert testing[6] == 7
    assert testing[7] == 8
    assert testing[8] == 9


pytest.main(["-v", "--tb=line", "-rN", __file__])