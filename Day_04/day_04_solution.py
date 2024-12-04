# Solution for Day 04 of Advent of Code 2024

# Part 1
def search_from(grid, rows, cols, word, row, column, direction_row, direction_column):
    word_length = len(word)
    for i in range(word_length):
        end_row = row + direction_row * i
        end_column = column + direction_column * i
        if (
            end_row < 0
            or end_row >= rows
            or end_column < 0
            or end_column >= cols
            or grid[end_row][end_column] != word[i]
        ):
            return False
    return True


def count_xmas(grid):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (1, -1),  # uown-left
        (-1, 1),  # up-right
        (-1, -1),  # up-left
    ]

    for row in range(rows):
        for column in range(cols):
            for direction_row, direction_column in directions:
                if search_from(
                    grid, rows, cols, word, row, column, direction_row, direction_column
                ):
                    count += 1

    return count


def load_grid_from_file():
    row_length = 0
    with open("Day_04/input_data.txt", "r") as file:
        read_file = file.read()
        row_length = len(read_file.split("\n")[0])
        content = read_file.strip().replace("\n", "")
    return [
        list(content[i : i + row_length]) for i in range(0, len(content), row_length)
    ]


grid = load_grid_from_file()
result = count_xmas(grid)


# Part 2
def count_x_dash_mas(grid):
    count_x = 0
    a_indices = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "A":
                a_indices.append((i, j))
    for a_i, a_j in a_indices:
        upper = grid[a_i - 1][a_j - 1] + grid[a_i][a_j] + grid[a_i + 1][a_j + 1]
        lower = grid[a_i - 1][a_j + 1] + grid[a_i][a_j] + grid[a_i + 1][a_j - 1]
        if lower in ["MAS", "SAM"] and upper in ["MAS", "SAM"]:
            count_x += 1
    return count_x


cross_result = count_x_dash_mas(grid)

with open("Day_04/output_data.txt", "w") as file:
    file.write(f"XMAS count: {result}\n")
    file.write(f"XMAS as cross count: {cross_result}\n")
