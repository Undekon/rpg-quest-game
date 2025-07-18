import pygame

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False
        self.is_clicked = False

        #Colors
        self.normal_color = (70, 70, 90)
        self.hover_color = (100, 100, 120)
        self.clicked_color = (130, 130, 150)

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        mouse_clicked = pygame.mouse.get_pressed()[0]
        if not mouse_clicked and self.is_clicked and self.is_hovered:
            if self.action:
                self.action()
        
        self.is_clicked = mouse_clicked and self.is_hovered
        return self.is_hovered

    def draw(self, surface): 
        if self.is_clicked:
             color = self.clicked_color
        elif self.is_hovered:
             color = self.hover_color
        else:
             color = self.normal_color

        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)

        font = pygame.font.SysFont(None, 24)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
