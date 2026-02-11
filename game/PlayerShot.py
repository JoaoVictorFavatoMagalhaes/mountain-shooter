from game.Const import ENTITY_SPEED
import game.Entity


class PlayerShot(game.Entity.Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]