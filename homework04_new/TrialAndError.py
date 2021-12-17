from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """

    pass


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))


    for cell in empty_cells:
        x, y = cell[0], cell[1]
        direction = choice(("up", "right"))
        if x == 1 and y == cols - 2:
            direction = "nowhere"
        elif x == 1:
            direction = "right"
        elif y == cols - 2:
            direction = "up"

        if direction == "up":
            grid[x - 1][y] = ' '
        elif direction == "right":
            grid[x][y + 1] = ' '

    #for x, row in enumerate(grid):
        #print(x, row)


    '''
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x != 0 and y != cols - 1 and not (x == 1 and y == cols - 2):
                print((x,y))
                direction = choice(("up", "right"))
                if x == 1:
                    direction = "right"
                if y == cols - 2:
                    direction = "up"
                if direction == "up":
                    grid[x-]
    '''

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    for x, row in enumerate(grid):
        print(x, row)
    return grid

#create_grid(7,7))
#print(bin_tree_maze(7,7,True))
#bin_tree_maze(15,15,True)


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    #for x, row in enumerate(grid):
        #for y, _ in enumerate(row):
    #[(grid.index(row), row.index(cell)) for row in grid for cell in row if cell == "X"]
    return [(row[0], cell[0]) for row in enumerate(grid) for cell in enumerate(row[1]) if cell[1] == "X"]

#print(bin_tree_maze(7,7,True))
#print(get_exits([['■', '■', '■', '■', '■', '■', '■'], ['■', ' ', ' ', ' ', ' ', ' ', '■'], ['X', '■', '■', ' ', '■', ' ', 'X'], ['■', ' ', ' ', ' ', '■', ' ', '■'], ['■', '■', '■', ' ', '■', ' ', '■'], ['■', ' ', ' ', ' ', '■', ' ', '■'], ['■', '■', '■', '■', '■', '■', '■']]))

def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y = coord[0], coord[1]
    if x == 0:
        if grid[x + 1][y] == '■':
            return True
    elif x == len(grid) - 1:
        if grid[x - 1][y] == '■':
            return True
    elif y == 0:
        if grid[x][y + 1] == '■':
            return True
    elif y == len(grid[0]) - 1:
        if grid[x][y - 1] == '■':
            return True
    return False

def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    '''
    2. находим на поле первую клетку (считая слева направо сверху вниз) с полученным значением k
3. увеличиваем значение счетчика на 1 и заполняем им все пустые (нулевые) клетки вокруг текущей
'''

    #grid[out[0]][out[1]]

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == k:
                if x != len(grid) - 1 and grid[x + 1][y] == 0:
                    grid[x + 1][y] = k + 1
                if x != 0 and grid[x - 1][y] == 0:
                    grid[x - 1][y] = k + 1
                if y != len(grid[0]) - 1 and grid[x][y + 1] == 0:
                        grid[x][y + 1] = k + 1
                if y != 0 and grid[x][y - 1] == 0:
                    grid[x][y - 1] = k + 1
    return grid

#[['■', '■', '■', '■', '■', '■', '■'], [1, 0, 0, 0, 0, 0, '■'], ['■', '■', '■', 0, '■', 0, '■'], ['■', 0, 0, 0, '■', 0, '■'], [0, 0, '■', '■', '■', 0, '■'], ['■', 0, '■', 0, 0, 0, '■'], ['■', '■', '■', '■', '■', '■', '■']]

def shortest_path(
        grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    path = [exit_coord]
    x, y = exit_coord[0], exit_coord[1]
    shortest = grid[x][y]
    k = shortest
    while k > 1:
        if x != len(grid) - 1 and grid[x + 1][y] == k - 1:
            # grid[x + 1][y] = k + 1
            x += 1
            path.append((x, y))
        elif x != 0 and grid[x - 1][y] == k - 1:
            # grid[x - 1][y] = k + 1
            x -= 1
            path.append((x, y))
        elif y != len(grid[0]) - 1 and grid[x][y + 1] == k - 1:
            # grid[x][y + 1] = k + 1
            y += 1
            path.append((x, y))
        elif y != 0 and grid[x][y - 1] == k - 1:
            # grid[x][y - 1] = k + 1
            y -= 1
            path.append((x, y))
        else:
            grid[x][y] = " "
        k -= 1
    # if len(path) > shortest:
    #
    #     return shortest_path(grid, exit_coord)
    return path

def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    exits = get_exits(grid)
    if len(exits) == 1:
        return grid, exits
    else:
        in_, out = exits
    if encircled_exit(grid, in_) or encircled_exit(grid, out):
        return grid, None
    grid[in_[0]][in_[1]], grid[out[0]][out[1]] = 1, 0

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == ' ':
                grid[x][y] = 0

    k = 0
    while grid[out[0]][out[1]] == 0:
        k += 1
        grid = make_step(grid, k)
    for row in grid:
        print(row)

    path = shortest_path(grid, out)
    print(path)
solve_maze(bin_tree_maze(7,7,True))


"""
1. запрыгиваем в клетку выхода
2. пока не придем в клетку входа (пока не найдем 1):
    1. если в одной из соседних с текущей клеток лежит значение, на один меньшее текущего k (длины пути), записываем в путь координаты найденной клетки, уменьшаем счетчик k на 1
    2. переходим в следующую клетку, направление задает только что найденная клетка
3. если длина пути (списка координат) не равна длине пути, записанной в клетке выхода
    1. отпрыгиваем на клетку пути назад
    2. заполняем неудачную клетку пробелом, чтобы никогда больше в нее не вернуться
    3. рекурсивно повторяем пункт 3, пока не найдем путь (ситуация, когда его нет, к этому моменту уже исключена)
"""
# [(5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (2, 0)]
[(5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 0)]
#g = bin_tree_maze(15,15,True)
#a, b = (get_exits(g))
#print(a,b)
#print(encircled_exit(g, a))
#print(encircled_exit(g, b))


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid