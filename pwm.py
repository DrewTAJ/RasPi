from Tkinter import *
import RPi.GPIO as GPIO

output_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT)

pwm = GPIO.PWM(output_pin, 500)
pwm.start(100)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text="PWM").grid(row=0,column=0)

        scalePWM = Scale(frame, from_=0,to=100,orient=HORIZONTAL,command=self.updatePWM)
        scalePWM.grid(row=0, column=1)

    def updatePWM(self, duty):
        pwm.ChangeDutyCycle(100 - float(duty))

root = Tk()
root.wm_title('PWM Control')
app = App(root)
root.geometry("200x150+0+0")

try:
    root.mainloop()
finally:
    print("Cleaning up")
    GPIO.cleanup()