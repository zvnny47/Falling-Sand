import pygame
import random
import colorsys
import copy

pygame.init()

def draw_grid(screen, _grid, color):
    for x in range(len(_grid)):
        for y in range(len(_grid)):
            pixel = pygame.Rect(x*pixel_size, y*pixel_size, pixel_size, pixel_size)
            if grid[x][y] != (0, 0, 0):
                pygame.draw.rect(screen, grid[x][y], pixel)

def apply_physics(grid):
    next_grid = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid)-1,-1,-1):
            if y < len(grid)-1:
                rand = 1 if random.randint(0, 100) < 50 else -1

                if grid[x][y] != (0, 0, 0):
                    if grid[x][y+1] == (0, 0, 0):
                        next_grid[x][y] = (0, 0, 0)
                        next_grid[x][y+1] = grid[x][y]
                    elif 0 <= x + rand < len(grid) and grid[x+rand][y+1] == (0, 0, 0):
                        next_grid[x][y] = (0, 0, 0)
                        next_grid[x+rand][y+1] = grid[x][y]
    return next_grid

def rainbow(color):
    r, g, b = color
    r, g, b = r/255.0, g/255.0, b/255.0
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h += 0.001
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

clock = pygame.time.Clock()
timer = 0
screen_size = 500
pixel_size = 5
pixel_color = (255, 0, 0)
grid = [[(0, 0, 0) for i in range(screen_size//pixel_size)] for j in range(screen_size//pixel_size)]
screen = pygame.display.set_mode([screen_size, screen_size])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        x = mouseX // pixel_size
        y = mouseY // pixel_size
        if x >= 0 and x <= len(grid)-1 and y > 0 and y < len(grid)-1:
            grid[x][y] = pixel_color
            if x > 0 and x < len(grid)-1 and y > 0 and y < len(grid)-1:
                grid[x-1][y] = pixel_color
                grid[x+1][y] = pixel_color
                grid[x][y-1] = pixel_color
                grid[x][y+1] = pixel_color
                grid[x-1][y-1] = pixel_color
                grid[x+1][y-1] = pixel_color
                grid[x-1][y-1] = pixel_color
                grid[x-1][y+1] = pixel_color
                grid[x-1][y+1] = pixel_color
                grid[x+1][y+1] = pixel_color
                grid[x+1][y-1] = pixel_color
                grid[x+1][y+1] = pixel_color

    screen.fill((25, 25, 25))
    pixel_color = rainbow(pixel_color)
    draw_grid(screen, grid, pixel_color)
    timer += clock.tick()
    if timer>10:
        grid = apply_physics(grid)
        timer = 0
    pygame.display.flip()

pygame.quit()