import RPi.GPIO as GPIO
import time

class AlphaBot(object):
	
	def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26, dr=16, dl=19):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb
		self.DR = dr
		self.DL = dl

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)
		GPIO.setup(self.ENA, GPIO.OUT)
		GPIO.setup(self.ENB, GPIO.OUT)

		GPIO.setup(self.DR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.DL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		self.PWMA = GPIO.PWM(self.ENA, 500)
		self.PWMB = GPIO.PWM(self.ENB, 500)
		self.PWMA.start(50)
		self.PWMB.start(50)
		self.stop()  # ferma i motori all'avvio

	def forward(self):
		GPIO.output(self.IN1, GPIO.HIGH)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.HIGH)

	def stop(self):
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.LOW)

	def backward(self):
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.HIGH)
		GPIO.output(self.IN3, GPIO.HIGH)
		GPIO.output(self.IN4, GPIO.LOW)

	def left(self):
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.HIGH)

	def right(self):
		GPIO.output(self.IN1, GPIO.HIGH)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.LOW)
		
	def setPWMA(self, value):
		self.PWMA.ChangeDutyCycle(value)

	def setPWMB(self, value):
		self.PWMB.ChangeDutyCycle(value)	
		
	def setMotor(self, left, right):
		if (0 <= right <= 100):
			GPIO.output(self.IN1, GPIO.HIGH)
			GPIO.output(self.IN2, GPIO.LOW)
			self.PWMA.ChangeDutyCycle(right)
		elif (-100 <= right < 0):
			GPIO.output(self.IN1, GPIO.LOW)
			GPIO.output(self.IN2, GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(-right)

		if (0 <= left <= 100):
			GPIO.output(self.IN3, GPIO.HIGH)
			GPIO.output(self.IN4, GPIO.LOW)
			self.PWMB.ChangeDutyCycle(left)
		elif (-100 <= left < 0):
			GPIO.output(self.IN3, GPIO.LOW)
			GPIO.output(self.IN4, GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(-left)

# -------------------------------------------------------------
# BLOCCO DI TEST / EXPORT
# -------------------------------------------------------------
if __name__ == '__main__':
	print("🔧 Test manuale AlphaBot – premi Ctrl+C per uscire")
	bot = AlphaBot()
	try:
		while True:
			bot.forward()
			time.sleep(1)
			bot.backward()
			time.sleep(1)
			bot.left()
			time.sleep(1)
			bot.right()
			time.sleep(1)
			bot.stop()
			time.sleep(1)
	except KeyboardInterrupt:
		print("\n🛑 Terminato manualmente.")
	finally:
		bot.stop()
		GPIO.cleanup()
