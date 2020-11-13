import pygame

# creates the screen
(width, height) = (400, 400)  # make sure this is a square otherwise the drawing of the separators will go wrong
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
separator = (int(width / 3), int(width * 2 / 3))


def draw_screen():
    screen.fill(white)
    for i in separator:
        pygame.draw.line(screen, black, (i, 0), (i, height))
        pygame.draw.line(screen, black, (0, i), (width, i))


def win(piece):
    font = pygame.font.Font('freesansbold.ttf', 80)
    w = font.render(piece + " Won", True, blue)
    screen.blit(w, (80, height // 2 - 30))


# graphics of the X and O (would need altering if the width and height change)
class Piece:
    def __init__(self, position):
        self.position = position
        self.x = position[0] * width // 3
        self.y = position[1] * width // 3

    def draw_x(self):
        pygame.draw.line(screen, black, (20 + self.x, 20 + self.y), (113 + self.x, 113 + self.y), 3)
        pygame.draw.line(screen, black, (20 + self.x, 113 + self.y), (113 + self.x, 20 + self.y), 3)

    def draw_o(self):
        pygame.draw.circle(screen, black, (67 + self.x, 67 + self.y), 60)
        pygame.draw.circle(screen, white, (67 + self.x, 67 + self.y), 57)
