input.onButtonPressed(Button.A, function () {
    if (lenyomta == 1) {
        led.plot(x, y)
        lenyomta = 0
    } else {
        led.unplot(x, y)
    }
    if (y != 4) {
        y += 1
    } else {
        y = 0
    }
    led.plot(x, y)
})
// def on_gesture_shake():
// if randint(0, 2) == 0:
// basic.show_icon(IconNames.SCISSORS)
// elif randint(0, 2) == 1:
// basic.show_icon(IconNames.SMALL_SQUARE)
// else:
// basic.show_leds("""
// # # # #
// # # # #
// # # # #
// # # # #
// # # # #
// """)
// input.on_gesture(Gesture.SHAKE, on_gesture_shake)
input.onButtonPressed(Button.AB, function () {
    lenyomta = 1
})
input.onButtonPressed(Button.B, function () {
    if (lenyomta == 1) {
        led.plot(x, y)
        lenyomta = 0
    } else {
        led.unplot(x, y)
    }
    if (y != 4) {
        y += 1
    } else {
        y = 0
    }
    led.plot(x, y)
})
let y = 0
let x = 0
let lenyomta = 0
lenyomta = 0
x = 0
y = 0
led.plot(x, y)
basic.forever(function () {
	
})
