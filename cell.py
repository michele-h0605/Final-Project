import pygame
class Cell:
    # constructors for the cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = None
        self.selected = False

    def set_cell_value(self, value):
        """Sets the actual value of the cell."""
        self.value = value

    #sets the sketched value of the cell
    def set_sketched_value(self, value):
        """Sets the sketched value of the cell."""
        self.sketch = value

    # draws the cell, its value, and it sketched value
    def draw(self):
        """Draws the cell and its value, with a red outline if selected."""
        rect = pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size)

        # Draw the cell's outline
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)  # Red border if selected
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Regular border

        # If the cell has a non-zero value, draw it in the center of the cell
        if self.value != 0:
            font = pygame.font.Font(None, 40)  
            text = font.render(str(self.value), True, (0, 0, 0))  
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)