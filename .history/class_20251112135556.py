class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def greet(self):
        return f"Hello, I am {self.name}, model {self.model}."

    def perform_task(self, task):
        return f"{self.name} is performing the task: {task}."
#Greet the user
print("Hello, " + name + "! You live in " + city + ".")#Greet the user  
#Ask for user country