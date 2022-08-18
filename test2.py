import sys
import time

if __name__ == "__main__":

    count = int(sys.argv[1])
    size = int(sys.argv[2])

    for i in range(count):

        print("Generating file {}".format(i))

        with open("file{}.dat".format(i), "w") as fh:
            fh.write("a" * size)
            time.sleep(0.1)

    print("Done.")
