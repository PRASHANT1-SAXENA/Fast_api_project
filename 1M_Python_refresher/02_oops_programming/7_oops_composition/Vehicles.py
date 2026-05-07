class Engine:
    def start(self):
        print("Engine starts")

    def stop(self):
        print("Engine stops")


class Vehicle:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        self.engine.start()
        print("Vehicle is moving")

    def park(self):
        self.engine.stop()
        print("Vehicle is parked")


