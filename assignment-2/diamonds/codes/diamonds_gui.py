import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 350
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Load background image
background_image = pygame.image.load(r"card_images\background.jpg").convert()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define button parameters
button_width = 200
button_height = 50
button_color = BLACK
button_text_color = WHITE
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Start Game", True, button_text_color)
button_text_rect = button_text.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
button_text_rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
# Main game loop

MAIN_MENU = 0
INSTRUCTIONS = 1
NEW_FRAME = 2
current_state = MAIN_MENU

def display_instructions():
    screen.fill(WHITE)
    # Display title
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Instructions", True, BLACK)
    title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(title_text, title_text_rect)
    # Display instructions
    instruction_font = pygame.font.Font(None, 20)
    instructions = [
        "1. Each player is dealt a suit of cards, excluding the diamond suit.",
        "2. The diamond cards are shuffled and placed on auction one by one.",
        "3. Players bid with one of their own cards face down.",
        "4. The banker awards the diamond card to the highest bidder, based on the card's point value.",
        "5. Points from the diamond card are added to the winning player's score.",
        "6. If multiple players bid the same highest value card, points are divided equally among them.",
        "7. The player with the most points at the end wins the game."
    ]
    for i, text in enumerate(instructions):
        text_surface = instruction_font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 150 + i * 30))
        screen.blit(text_surface, text_rect)
    # Draw button
    button_width = 200
    button_height = 50
    button_color = BLACK
    button_text_color = WHITE
    button_font = pygame.font.Font(None, 36)

    button_text = button_font.render("Next Frame", True, button_text_color)
    button_text_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
    pygame.draw.rect(screen, button_color, (button_text_rect.topleft, (button_width, button_height)))
    screen.blit(button_text, button_text_rect)

        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_text_rect.collidepoint(mouse_pos):
                if current_state == MAIN_MENU:
                    print("Button clicked! Showing instructions...")
                    current_state = INSTRUCTIONS
                elif current_state == INSTRUCTIONS:
                    print("Button clicked! Redirecting to new frame...")
                    current_state = NEW_FRAME

    # Fill the background with the resized image
    screen.blit(background_image, (0, 0))


    # Draw the button based on the current state
    if current_state == MAIN_MENU:
        pygame.draw.rect(screen, button_color, (button_text_rect.topleft, (button_width, button_height)))
        screen.blit(button_text, button_text_rect)
    elif current_state == INSTRUCTIONS:
        display_instructions()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()