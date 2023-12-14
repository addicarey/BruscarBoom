def on_button_pressed_a():
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        90)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        100)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        100)
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def leftSwitch():
    basic.show_icon(IconNames.HEART)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    control.wait_micros(5000000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        100)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        90)
    control.wait_micros(5000000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    control.wait_micros(5000000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        100)
    control.wait_micros(5000000)

def on_button_pressed_b():
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_icon(IconNames.HEART)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    basic.pause(5000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        100)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.REVERSE,
        90)
    basic.pause(5000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    basic.pause(5000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        0)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        100)
    basic.pause(5000)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        90)
    Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR4,
        Kitronik_Robotics_Board.MotorDirection.FORWARD,
        100)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
