# ALT 4 Microbit Code

serial_in = ""


def on_data_received():
    global serial_in
    serial_in = serial.read_line()
    basic.show_string(serial_in)


serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)


def on_forever():
    basic.show_string(serial_in)


basic.forever(on_forever)
