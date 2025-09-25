import requests

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    print(response.text)
    data = response.json()
    print(data['value'])
    print(data['id'])


topic = input("izvēle tematu")
catjokes = f"https://api.chucknorris.io/jokes/random?category={topic}"   
response = requests.get(catjokes)
print(response.text)
data = response.json()
print(data['value'])
print(data['id'])