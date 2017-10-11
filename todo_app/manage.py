from manager import Manager

from todo_app.app import app

manager = Manager()


@manager.command
def serve(host='0.0.0.0', port=5000, debug=False):
    app.run(host, port, debug=debug)


@manager.command
def test():
    pass


if __name__ == '__main__':
    manager.main()
