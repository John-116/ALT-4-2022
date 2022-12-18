def on_button_pressed_a():
    basic.show_number(input.magnetic_force(Dimension.X))
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(43)

def on_forever():
    if input.magnetic_force(Dimension.X) < 100:
        radio.send_string("door opened")
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # # # . .
                        # # # . .
                        # # # . .
        """)
    else:
        radio.send_string("door closed")
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    basic.pause(2000)
basic.forever(on_forever)
