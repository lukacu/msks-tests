import sys
import time

if __name__ == "__main__":

    sleep = float(sys.argv[1])

    print("Sleeping for {} seconds".format(sleep))

    time.sleep(sleep)

    print("Done.")
