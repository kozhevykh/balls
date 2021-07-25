import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, name):
        super().__init__(all_sprites)
        self.radius = radius
        self.name = name
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
    def update(self):
            self.rect = self.rect.move(self.vx, self.vy)
            if pygame.sprite.spritecollideany(self, horizontal_borders):
                self.vy = -self.vy
            if pygame.sprite.spritecollideany(self, vertical_borders):
                self.vx = -self.vx
            hit_ball = pygame.sprite.spritecollide(self, all_sprites, False, collided=pygame.sprite.collide_circle)
            hit_ball.remove(self)
            for other in hit_ball:
                if other.name != 'border':
                    self.vx = -self.vx
                    self.vy = -self.vy
                    other.vx = -other.vx
                    other.vy = -other.vy
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.name = "border"
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(0):
    Ball(20, 100, 100, i)
cnt = 0
running = True
screen.fill((0, 0, 0))
while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            Ball(20, x, y, cnt)
            cnt += 1
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
