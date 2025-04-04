import requests

name_input = "Anna"
predicted_age = 27

url = f"https://api.agify.io?name={name_input}"
response = requests.get(url)
data = response.json()
predicted_age = data.get("age", "27")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I might be {self.age} years old.")


person = Person(name_input, predicted_age)
person.introduce()