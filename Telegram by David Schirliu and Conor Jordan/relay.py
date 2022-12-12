def on_received_number(receivedNumber):
    if receivedNumber == 1:
        radio.send_number(1)
    elif receivedNumber == 2:
        radio.send_number(2)
    elif receivedNumber == 3:
        radio.send_number(3)
    elif receivedNumber == 4:
        radio.send_number(4)


radio.on_received_number(on_received_number)


def on_forever():
    radio.set_group(44)


basic.forever(on_forever)
