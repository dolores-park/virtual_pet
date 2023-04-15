import pygame
import sys
from pet import Pet
import random
import logging

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 1600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
MAX_CHAT_WIDTH = 400

# Set font and colors
font = pygame.font.Font(None, 26)
text_color = (255, 255, 255)
bg_color = (173, 216, 230)

SPECIAL_EVENT = pygame.USEREVENT + 1

def set_random_timer_interval():
    pygame.time.set_timer(SPECIAL_EVENT, millis = random.randint(20000, 30000))

set_random_timer_interval()

# Create a function to draw text
def draw_text(text, x, y, offset_width):

    x = x + offset_width
    words = text.split()
    line = ""
    line_height = font.get_linesize()

    for word in words:
        test_line = line + " " + word
        test_line_width, _ = font.size(test_line)

        if test_line_width < MAX_CHAT_WIDTH:
            line = test_line
        else:
            surface = font.render(line.strip(), True, text_color)
            screen.blit(surface, (x, y))
            y += line_height
            line = word

    # Render the last line
    if line:
        surface = font.render(line.strip(), True, text_color)
        screen.blit(surface, (x, y))

chat_history = []
my_pet = Pet()

user_text = ""
result = my_pet.get_filler_sentences()["greetings"]
# score = 0

background_image = pygame.image.load("assets/pet_background.jpeg").convert()
img_width, img_height = background_image.get_size()
img_width = img_width * screen_height/img_height
background_image = pygame.transform.scale(background_image, (img_width, screen_height))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.unicode.isprintable():
                user_text += event.unicode

            elif event.key == pygame.K_RETURN:
                # result = my_pet.get_filler_sentences()["dummy_response"] + user_text
                result = my_pet.process_user_input(user_text)
                user_text = ""

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

        if event.type == SPECIAL_EVENT:
            logging.info("*****__*****SPECIAL EVENTS:::")
            result = my_pet.process_special_events()
            set_random_timer_interval()

    screen.fill(bg_color)
    screen.blit(background_image, (0, 0))

    # Draw the current question, user's answer, result, and score
    draw_text(result, 50, 100, img_width)
    draw_text("You are saying: " + user_text, 50, 550, img_width)
    # draw_text("Score: " + str(score), 50, 400, img_width)

    # Update the screen
    pygame.display.update()

    if not my_pet.is_initialized():
        result = my_pet.get_initial_response()
        my_pet.initialized = True