import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    
    def draw(self):
        """Draws the grid and all cells."""
        # Draw grid lines for the Sudoku board, bold lines for the 3x3 sections
        for row in range(1, 9):
            width = 3 if row % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * self.cell_size), (self.width, row * self.cell_size), width)
            pygame.draw.line(self.screen, (0, 0, 0), (row * self.cell_size, 0), (row * self.cell_size, self.height),width)

        # Draw each cell in the grid
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

    def select(self, row, col):
        """Marks the cell at (row, col) as the currently selected cell."""
        if self.selected_cell:
            self.selected_cell.selected = False  # Deselect the current cell
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True  # Select the new cell

    def click(self, x, y):
        """Returns the (row, col) of the clicked cell, or None if outside the grid."""
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        row = y // self.cell_size
        col = x // self.cell_size
        return row, col

    def clear(self):
        """Clears the value of the currently selected cell, if it's user-inputted."""
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(None)

    def sketch(self, value):
        """Sets the sketched value of the selected cell."""
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        """Places a number in the selected cell."""
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)
            self.selected_cell.set_sketched_value(None)

    def reset_to_original(self):
        """Resets all cells to their original values."""
        for row in range(9):
            for col in range(9):
                original_value = self.original_values[row][col]
                self.cells[row][col].set_cell_value(original_value)
                self.cells[row][col].set_sketched_value(None)

    def is_full(self):
        """Returns True if the board is full."""
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        """Updates the underlying 2D board with the current cell values."""
        for row in range(9):
            for col in range(9):
                # Update the value of the external 2D list or matrix with the value of each cell
                self.board_state[row][col] = self.cells[row][col].value

    def find_empty(self):
        """Finds an empty cell and returns its (row, col), or None if no empty cells exist."""
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        """Checks whether the board is solved correctly."""
        # Placeholder for checking if the Sudoku puzzle is solved correctly.
        return True