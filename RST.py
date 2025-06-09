# /bin/env python3
# Created by: Enoch O
# Created on: May 14, 2025
# This program is the "Space-Aliens" Program on the PyBadge


import stage
import ugame
import constants

def game_scene():
    # Load image banks for background and sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Initialize button states
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Prepare sound
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Create background grid
    background = stage.Grid(image_bank_background, 10, 8)

    # Create player ship sprite
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # Create alien sprite positioned at top-center
    alien = stage.Sprite(image_bank_sprites, 9,
                         int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                         16)

    # Initialize game stage with 60 FPS
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        # Handle A button press logic for firing
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button placeholder (no action)
        if keys & ugame.K_X != 0:
            pass

        # Start button pressed
        if keys & ugame.K_START != 0:
            print("Start")

        # Select button pressed
        if keys & ugame.K_SELECT != 0:
            print("Select")

        # Move ship right with boundary check
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)

        # Move ship left with boundary check
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)

        # Up and Down buttons currently unused
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # Play pew sound if A was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw screen and tick clock
        game.render_block()
        game.tick()

if __name__ == "__main__":
    game_scene()
