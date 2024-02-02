import pytest
import Grid


def test_grid_init_typical():
    grid = Grid.Grid()


def test_grid_init_negative_cell_size():
    with pytest.raises(TypeError):
        grid = Grid.Grid(cell_size=-10)

def test_grid_init_negative_width():
    with pytest.raises(TypeError):
        grid = Grid.Grid(width=-10)

def test_grid_init_negative_height():
    with pytest.raises(TypeError):
        grid = Grid.Grid(height=-10)

