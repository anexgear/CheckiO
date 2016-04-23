#“ри аргумента.  ортеж кортежей с числами (1/0), номер строки и колонки в виде целых чисел.
#¬ыходные данные: —колько соседей имеет клетка в виде целого числа. 

NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1), (1, -1), (1, 0), (1, 1))
def count_neighbours(grid, row, col):
    count =0
    for diff in NEIGHBORS:
        n_row = row + diff[0]
        n_col = col + diff[1]
        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):
            if grid[n_row][n_col]:
                count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
