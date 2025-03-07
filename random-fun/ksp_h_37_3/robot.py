from queue import Queue


def read_input():
    CONVERT = {
        "#": -1,
        ".": 0,
        "P": 1,
        "V": 0
    }
    with open("robot.in", "r", encoding="utf-8") as file_in:
        R, S = tuple(int(x) for x in file_in.readline().strip().split())
        board = [[0 for _ in range(S)] for _ in range(R)]
        robot = 0, 0
        traps = {}
        for row in range(R):
            line = file_in.readline().strip()
            for col in range(S):
                board[row][col] = CONVERT[line[col]]
                if line[col] == "P":
                    traps[(row, col)] = False
                if line[col] == "V":
                    robot = row, col

    return board, robot, traps


def get_neighbors(pos, board):
    neighbors = []
    row, col = pos

    for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        try:
            if board[row + row_shift][col + col_shift] != -1:
                neighbors.append((row + row_shift, col + col_shift))
        except IndexError:
            pass

    return neighbors


def main():
    robot, board, traps = read_input()
    q = Queue()

    q.put(robot)
    while not q.empty():
        pos = q.get()
        row, col = pos

        # trap

        neighbors = get_neighbors(pos, board)


if __name__ == "__main__":
    main()
