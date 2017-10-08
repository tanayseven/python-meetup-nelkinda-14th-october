# /usr/bin/env python3

from manager import Manager

manager = Manager()


@manager.command
def serve(host='0.0.0.0', port=5000):
    pass


@manager.command
def test():
    pass


if __name__ == '__main__':
    manager.main()
