def on_button_pressed_a():
    global lenyomta, y
    if lenyomta == 1:
        led.plot(x, y)
        lenyomta = 0
    if lenyomta == 0:
        y += 1
        led.unplot(x, y)
        if y != 4:
            y += 1
        else:
            y = 0
        led.plot(x, y)
        lenyomta = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

#def on_gesture_shake():
    #if randint(0, 2) == 0:
        #basic.show_icon(IconNames.SCISSORS)
    #elif randint(0, 2) == 1:
        #basic.show_icon(IconNames.SMALL_SQUARE)
    #else:
        #basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            #""")
#input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global lenyomta
    lenyomta = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global lenyomta, x
    if lenyomta == 1:
        led.plot(x, y)
        lenyomta = 0
        if x != 4:
            x += 1
        else:
            x = 0
    else:
        led.unplot(x, y)
        if x != 4:
            x += 1
        else:
            x = 0
        led.plot(x, y)
        lenyomta = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
lenyomta = 0
lenyomta = 0
x = 0
y = 0
led.plot(x, y)

def on_forever():
    pass
basic.forever(on_forever)
