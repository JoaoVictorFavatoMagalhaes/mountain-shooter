import pygame


class Entity:
    def __init__(self, name: str, position: tuple):
        self.name: str = name

        # imagem
        self.surf: pygame.Surface = pygame.image.load(
            f'./asset/{name}.png'
        ).convert_alpha()

        # retângulo de colisão / posição
        self.rect: pygame.Rect = self.surf.get_rect(center=position)
