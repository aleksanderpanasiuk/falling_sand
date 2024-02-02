import pytest
import Grid


def test_mouse_not_on_grid():
    grid = Grid.Grid()

    assert grid._is_mouse_on_grid((0, 0)) == False


def test_mouse_not_on_grid_negative_values():
    grid = Grid.Grid()

    assert grid._is_mouse_on_grid((-12, -213)) == False


def test_mouse_not_on_grid_big_values():
    grid = Grid.Grid()

    assert grid._is_mouse_on_grid((141521, 512512)) == False


def test_mouse_on_grid():
    grid = Grid.Grid()

    assert grid._is_mouse_on_grid((110, 110))


def test_mouse_on_grid2():
    grid = Grid.Grid()

    assert grid._is_mouse_on_grid((500, 300))
