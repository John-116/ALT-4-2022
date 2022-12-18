def on_button_pressed_a():
    music.set_volume(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.set_volume(255)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "door opened":
        music.play_tone(262, music.beat(BeatFraction.DOUBLE))
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
    elif receivedString == "door closed":
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        music.stop_all_sounds()
radio.on_received_string(on_received_string)

radio.set_group(43)