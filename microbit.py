def on_received_number(receivedNumber):
    if receivedNumber == 1:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
    elif receivedNumber == 2:
        music.play_tone(349, music.beat(BeatFraction.DOUBLE))
        basic.show_leds("""
            . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        . . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
    elif receivedNumber == 3:
        for index in range(4):
            music.play_melody("C5 A C5 A C5 A C5 A ", 140)
            basic.show_string("SOS")
        basic.clear_screen()
    elif receivedNumber == 4:
        music.play_melody("A F A F A - - - ", 80)
        basic.show_string("END")
        basic.pause(500)
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if input.acceleration(Dimension.STRENGTH) >= 3500:
        radio.send_number(4)
basic.forever(on_forever)

def on_forever2():
    radio.set_group(44)
basic.forever(on_forever2)