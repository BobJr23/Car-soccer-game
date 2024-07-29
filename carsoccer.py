import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()
width, height = 1400, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car game!")
white = (255, 255, 255)
green = (50, 168, 82)
black = (0, 0, 0)
red = (200, 0, 0)
grey = (105, 105, 105)
blue = (66, 185, 189)
FONT = pygame.font.Font(None, 40)
c1 = pygame.image.load("car.png")
c1 = pygame.transform.flip(c1, flip_x=True, flip_y=False)
c1 = pygame.transform.scale(c1, (60, 30))
bal = pygame.image.load("ball.png")
bal = pygame.transform.scale(bal, (80, 80))


def calculate_distance(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)


def calculate_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


def create_boundaries(space, width, height):
    l = []
    rects = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(80, 40), (20, height / 3)],  # LEFT WALL
        [(80, height - 120), (20, height / 2)],
        [(10, 130), (120, 20)],
        [(10, height / 2 + 40), (120, 20)],
        [(width - 80, 40), (20, height / 3)],  # RIGHT WALL
        [(width - 80, height - 120), (20, height / 2)],
        [
            (width - 10, 130),
            (120, 20),
        ],
        [
            (width - 10, height / 2 + 40),
            (120, 20),
        ],
        [
            (0, 200),
            (20, 300),
        ],
        [
            (width, 200),
            (20, 300),
        ],
    ]
    for pos, size in rects:

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        shape.pair_index = "wall"

        space.add(body, shape)

        l.append(shape)

    return l[0]


def create_car(space, width, height):
    l = []
    x = 0
    rects = [
        [(100, height - 120), (60, 30), (*blue, 100), 120],
        [(900, height - 120), (60, 30), (*blue, 100), 120],
    ]
    for pos, size, color, mass in rects:
        x += 1
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Poly.create_box(body, size, radius=1)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.4

        space.add(body, shape)
        l.append(shape)

    return l


def play():

    run = True
    clock = pygame.time.Clock()
    FPS = 60
    dt = 1 / FPS
    space = pymunk.Space()
    draw_options = pymunk.pygame_util.DrawOptions(window)
    space.gravity = (0, 600)
    create_boundaries(space, width, height)
    car1, car2 = create_car(space, width, height)
    while run:

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        space.step(dt)
        clock.tick(FPS)
        window.fill(blue)
        space.debug_draw(draw_options)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    play()
