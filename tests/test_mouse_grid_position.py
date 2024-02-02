import Grid


def test_mouse_grid_pos_zero_zero():
    grid = Grid.Grid()

    assert grid._calculate_mouse_position_on_grid((100, 100)) == (0, 0)


def test_mouse_grid_pos_furthest():
    grid = Grid.Grid()

    assert grid._calculate_mouse_position_on_grid((1099, 599)) == (99, 49)


def test_mouse_grid_pos_negative_result():
    grid = Grid.Grid()

    assert grid._calculate_mouse_position_on_grid((90, 90)) == (-1, -1)


def test_mouse_grid_pos_negative_result_2():
    grid = Grid.Grid()

    assert grid._calculate_mouse_position_on_grid((-100, -100)) == (-20, -20)

