import pygame
import scenes # Import scene classes

pygame.init()

# Prepare screen
screen = pygame.display.set_mode((800, 820))
pygame.display.set_caption("PacMan")

# Sets active scene to the titlescreen
activescene = scenes.TitleScreen()

done = False
while not done:

    # Setup clock
    clock = pygame.time.Clock()

    # Event loop to close the window when user clicks close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Handle events (like keypresses) and draws the frame according to whatever the scene says
    activescene.HandleEvents()
    activescene.RenderScreen(screen)

    # Checks if the scene is calling for a scene change or to close the game, and then act upon said call.
    if activescene.changescene:
        if activescene.changeto == "exit":
            done = True
        else:
            exec("activescene = scenes." + str(activescene.changeto))

    # Shows the user the already drawn frame
    pygame.display.flip()

    # Limit framerate to 30fps
    clock.tick(30)

pygame.quit()