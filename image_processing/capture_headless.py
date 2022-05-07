#!//usr/bin/python3

from picamera2.picamera2 import Picamera2

tuning = Picamera2.load_tuning_file("imx219_noir.json")

picam2 = Picamera2(tuning=tuning)
config = picam2.still_configuration()
picam2.configure(config)

picam2.start()

np_array = picam2.capture_array()
print(np_array)
picam2.capture_file("demo.jpg")
picam2.stop()

