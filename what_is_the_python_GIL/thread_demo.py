from threading import Thread
import os


def loop():
    i = 0
    while True:
        i += 1


def main():
    print('start')
    for _ in range(os.cpu_count()):
        t = Thread(target=loop)
        t.start()


if __name__ == '__main__':
    main()
