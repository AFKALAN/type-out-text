import pygame
import math

pygame.init()

WIN = pygame.display.set_mode((600, 400))
TEXT_FONT = pygame.font.SysFont('calibri', 16)
TEXT_FONT.align = pygame.FONT_CENTER
CLOCK = pygame.time.Clock()

shown_text = ''
message = "Got a simple text player working which was pretty cool. Can't wait to put it in a speech bubble!"
render_start = False

typewriter_click = pygame.mixer.Sound('typewriter_click.wav')
typewriter_click.set_volume(0.01)

frame = 0


def render_text(text, color, surface):
    global shown_text
    if text.__len__() != shown_text.__len__():
        if text[shown_text.__len__()] != " ":
            typewriter_click.play()
        else:
            typewriter_click.stop()
        shown_text += text[shown_text.__len__()]
    else: 
        typewriter_click.stop()
    
    text_dimensions = TEXT_FONT.size(message)
    dialog_box_width = WIN.width
    dialog_box_height = math.ceil(text_dimensions[0] / dialog_box_width) * text_dimensions[1]
    dialog_box_surface = pygame.Surface((dialog_box_width, dialog_box_height))

    dialog_box_surface.fill('white')
    text_render = TEXT_FONT.render(shown_text, False, color, wraplength=surface.width)

    dialog_box_surface.blit(text_render, (0, 0))
    surface.blit(dialog_box_surface, (0, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            render_start = True

    if frame % 3 == 0 and render_start:
        render_text(message, 'black', WIN)

    pygame.display.update()
    CLOCK.tick(60)
    frame += 1
    
    if frame > 100:
        frame = 0
