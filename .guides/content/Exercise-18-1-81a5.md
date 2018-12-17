---------

For the following program, draw a UML class diagram that shows these classes and the relationships among them.

    class PingPongParent:
        pass

    class Ping(PingPongParent):
        def __init__(self, pong):
            self.pong = pong


    class Pong(PingPongParent):
        def __init__(self, pings=None):
            if pings is None:
                self.pings = []
            else:
                self.pings = pings

        def add_ping(self, ping):
            self.pings.append(ping)

    pong = Pong()
    ping = Ping(pong)
    pong.add_ping(ping)



