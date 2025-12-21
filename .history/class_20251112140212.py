class Robot:
    def __init__(self, name, model, weight):
        self.name = name
        self.model = model
        self.weight = weight

        def introduce_self(self):
            print("My name is " + self.name)
            print("My model is " + self.model)
            print("My weight is " + str(self.weight) + " kg")

            ri = Robot ("Tom", "RX100", 50)
            r2 = Robot ("Jerry", "RX200", 60)

            