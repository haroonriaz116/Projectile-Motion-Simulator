import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Define the screen size
screen_width = 600
screen_height = 700

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Projectile Motion Physics Simulator")

# Define colors
Red = (255, 0, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Yellow = (255, 255, 0)

# Define the circle's properties
circle_radius = 25  # Adjust the radius as needed
circle_x = 30  # Starting x position of the circle
circle_y = 450  # Starting y position of the circle

# Constants for projectile motion
g = 9.81  # Acceleration due to gravity (m/s^2)

# Font for error messages
font = pygame.font.Font(None, 36)


def get_valid_input(prompt):
    while True:
        # Clear the screen
        screen.fill(Black)
        pygame.display.flip()

        # Render the prompt
        prompt_text = font.render(prompt.replace(':', ''), True, White)
        prompt_rect = prompt_text.get_rect(center=(screen_width / 2, 40))
        screen.blit(prompt_text, prompt_rect)
        pygame.display.flip()

        # Get user input
        try:
            value = float(input(prompt))  # Console prompt with colon
            if value > 0:
                return value
            else:
                print_error_message("Invalid input!",
                                    "Please enter a value greater than 0.")
        except ValueError:
            print_error_message("Invalid input!",
                                "Please enter a value greater than 0.")


def print_error_message(line1, line2):
    # Render the error messages
    error_text1 = font.render(line1, True, Red)
    error_text2 = font.render(line2, True, Red)

    # Get the dimensions of the error messages
    text1_rect = error_text1.get_rect(center=(screen_width / 2, 40))
    text2_rect = error_text2.get_rect(center=(screen_width / 2, 80))

    # Clear the screen
    screen.fill(Black)

    # Draw the error messages on the screen
    screen.blit(error_text1, text1_rect)
    screen.blit(error_text2, text2_rect)

    # Update the display
    pygame.display.flip()

    # Wait for 2 seconds to show the error messages
    pygame.time.wait(2000)


def display_message(lines, color):
    screen.fill(Black)

    for i, line in enumerate(lines):
        message_text = font.render(line.replace('(Y/N)', ''), True, color)
        message_rect = message_text.get_rect(center=(screen_width / 2,
                                                     40 + i * 40))
        screen.blit(message_text, message_rect)

    pygame.display.flip()


def main():
    while True:
        # Define initial values for projectile motion
        velocity = get_valid_input("Enter the launch velocity (m/s): ")
        angleDegrees = get_valid_input("Enter the launch angle (degrees): ")
        height = get_valid_input("Enter the height (m): ")

        # Convert angle from degrees to radians
        angleRadians = angleDegrees * math.pi / 180.0

        # Calculate intermediate values for projectile motion
        horizontalVelocity = velocity * math.cos(angleRadians)
        verticalVelocity = velocity * math.sin(angleRadians)

        # Calculate the range using variables
        range_ = (horizontalVelocity *
                  (verticalVelocity + math.sqrt(verticalVelocity**2 +
                                                (2 * g * height)))) / g

        # Output range
        print(f"The range of the projectile is {range_:.2f} meters.")

        # Initialize current_x and current_y
        current_x = circle_x
        current_y = circle_y

        # Set the flag to start the animation
        launching = True
        launch_time = pygame.time.get_ticks()
        original_vertical_position = circle_y

        # Main game loop for the projectile motion
        while launching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the screen with black color
            screen.fill(Black)

            # Handle projectile motion simulation
            if launching:
                # Calculate the time elapsed since launch
                time_elapsed = pygame.time.get_ticks() - launch_time
                time_elapsed_seconds = time_elapsed / 1000.0

                # Update the current position of the ball
                current_x = circle_x + horizontalVelocity * time_elapsed_seconds
                current_y = original_vertical_position - (
                    verticalVelocity * time_elapsed_seconds -
                    0.5 * g * time_elapsed_seconds**2)

                # Check if the ball hits the ground
                if current_y >= original_vertical_position:
                    current_y = original_vertical_position
                    launching = False

            # Draw a red circle at the current position
            pygame.draw.circle(screen, Red, (int(current_x), int(current_y)),
                               circle_radius)

            # Update the display
            pygame.display.flip()

        while True:
            pygame.time.wait(1000)
            display_message(
                ["Would you like to perform", "another calculation? (Y/N)"],
                White)
            pygame.display.flip()

            user_response = input(
                "Would you like to perform another calculation? (Y/N): "
            ).strip().upper()

            if user_response == 'Y':
                screen.fill(Black)
                pygame.display.flip()
                break
            elif user_response == 'N':
                display_message(["Goodbye!"], Yellow)
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
            else:
                display_message(["Invalid input!"], Red)
                pygame.display.flip()


# Start the main function
main()