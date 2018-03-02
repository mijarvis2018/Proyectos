import time

def sleeper(argv):
    while True:
        num = argv
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
        # Run our time.sleep() command,
        time.sleep(num)
