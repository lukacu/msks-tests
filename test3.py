import sys
import time
import math

if __name__ == "__main__":

    samples = int(sys.argv[1])
    amplitude = float(sys.argv[2])
    frequency = float(sys.argv[3])

    for i in range(samples):
        value = amplitude * math.sin(i / frequency)
        print("sine_wave: {}".format(value))

    print("Done.")

