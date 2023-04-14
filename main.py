import pygame
import sys

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


# Game variables
# questions = [
#     {"question": "What is 5 + 3?", "answer": "8"},
#     {"question": "What is the capital of France?", "answer": "Paris"},
#     {"question": "What is the square root of 64?", "answer": "8"},
# ]
# current_question_index = 0

pet_stock_languages = {"greetings": "Hello, I am your pet. Talk to me by typing on the screen! <3 ",
                       "dummy_response": "Hi, I heard you say this! "}
chat_history = {}

user_text = ""
result = pet_stock_languages["greetings"]
# score = 0

background_image = pygame.image.load("pet_background.jpeg").convert()
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
                result = pet_stock_languages["dummy_response"] + user_text
                user_text = ""

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            # elif event.key == pygame.K_n:
            #     user_text = ""
            #     # result = ""
            #     current_question_index += 1
            #     if current_question_index >= len(questions):
            #         current_question_index = 0

    screen.fill(bg_color)
    screen.blit(background_image, (0, 0))

    # Draw the current question, user's answer, result, and score
    draw_text(result, 50, 100, img_width)
    draw_text("You are saying: " + user_text, 50, 550, img_width)
    # draw_text("Score: " + str(score), 50, 400, img_width)

    # Update the screen
    pygame.display.update()