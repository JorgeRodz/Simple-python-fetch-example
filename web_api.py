import requests

def trivia_fetch(number):
    # Fetch trivia about the number from the Numbers API
    trivia_fetch = requests.get(f"http://numbersapi.com/{number}?json")

    # Check if the request was successful
    print("Codigo de estado -> ", trivia_fetch.status_code)
    print("---------------------------------")

    # Parse the JSON response
    return trivia_fetch.json()


if __name__ == "__main__":
    number = input("Ingrese el numero de la trivia que desea consultar: ")
    print("Numero ingresado -> ", number)
    print("---------------------------------")

    trivia = trivia_fetch(number)

    print("Informacion de la trivia -> ", trivia)
    print("---------------------------------")

    # Print the trivia text
    print("Mensaje de la trivia -> ", trivia['text'])

    # Print the trivia number
    print("Numero de la trivia -> ", trivia['number'])
