datalogger.set_column_titles("Time", "Motion ")
timeanddate.set_time(12, 20, 0, timeanddate.MornNight.AM)
basic.show_string("START")

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        datalogger.log(datalogger.create_cv("Time", timeanddate.time(timeanddate.TimeFormat.HMMSSAMPM)))
        datalogger.log(datalogger.create_cv("Motion ", 1))
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . # .
                        # . # . .
                        . # . . .
        """)
        basic.pause(500)
        basic.clear_screen()
        basic.pause(2000)
    else:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
basic.forever(on_forever)
