from src.cell import Cell
from src.jump import Jump


class Board:

    def __init__(self, board_size):
        self.cells = []
        self.board_size = board_size
        self.initialize_cells(board_size)
        self.initialize_snakes(board_size)
        self.initialize_ladders(board_size)

    def initialize_cells(self, board_size):
        for row in range(board_size):
            self.cells.append([])
            for col in range(board_size):
                self.cells[row].append(Cell(None))

    def get_cell(self, position):
        board_row = position // len(self.cells)
        board_column = position % len(self.cells)
        return self.cells[board_row][board_column]

    def initialize_snakes(self, board_size):
        total_snakes = int(input("Enter total number of Snakes: "))
        index = 1
        while index <= total_snakes:
            snake_head = int(input("Enter snake start position: "))
            snake_tail = int(input("Enter snake end position: "))
            if snake_head <= snake_tail or snake_head >= board_size * board_size:
                print("Start of snake must be less than end and less than board_size")
            else:
                snake_obj = Jump(snake_head, snake_tail)
                cell = self.get_cell(snake_head)
                cell.set_jump(snake_obj)
                index += 1

    def initialize_ladders(self, board_size):
        total_snakes = int(input("Enter total number of Ladders: "))
        index = 1
        while index <= total_snakes:
            ladder_start = int(input("Enter ladder start position: "))
            ladder_end = int(input("Enter ladder end position: "))
            if ladder_start >= ladder_end or ladder_start <= 0 or ladder_end >= board_size * board_size or ladder_start <0:
                print("Start of Ladder must be less than end and in the range of 0-%s" % (board_size * board_size -1))
            else:
                ladder_obj = Jump(ladder_start, ladder_end)
                cell = self.get_cell(ladder_start)
                cell.set_jump(ladder_obj)
                index += 1
