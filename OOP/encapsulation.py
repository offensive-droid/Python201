class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_name(self):
        return self._name

    def _get_age(self):
        return self._age

    def _set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age value.")

    def display_info(self):
        print(f"Name: {self._get_name()}, Age: {self._get_age()}")

# Create an instance of the Person class
person = Person("Alice", 25)

# Accessing attributes and methods (encapsulation)
person.display_info()  # Output: Name: Alice, Age: 25
person._name = "Bob"  # Modifying private attribute directly (not recommended)
person.display_info()  # Output: Name: Bob, Age: 25

person._set_age(-10)  # Attempting to set an invalid age value (error message)
person._set_age(30)  # Setting a valid age value
person.display_info()  # Output: Name: Bob, Age: 30
