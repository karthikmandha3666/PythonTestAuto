class Example:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value

    # Instance Method
    def show(self):
        return f"Instance Variable: {self.instance_variable}"

    # Class Method
    @classmethod
    def show_class(cls):
        return f"Class Variable: {cls.class_variable}"

    # Static Method
    @staticmethod
    def info():
        return "I am a static method!"

# Creating an object
obj = Example("Python")

print(obj.show())         # Instance method
print(Example.show_class())  # Class method
print(Example.info())        # Static method
