# 📚 Number Trivia Fetcher

This is a simple Python script that fetches trivia about any number using the [Numbers API](http://numbersapi.com/). It uses the `requests` library to retrieve trivia in JSON format and prints out interesting facts about the number entered by the user.

---

## 🚀 Features

- Accepts a number input from the user.
- Fetches trivia facts from the [Numbers API](http://numbersapi.com/).
- Displays:
  - HTTP response status code
  - The full JSON response
  - Trivia message
  - Trivia number

---

## 🧰 Requirements

- Python 3.6 or higher
- `requests` library

You can install the required library with:

```bash
pip install requests
```
---

## 📂 File Structure
```
web_api.py              # Main Python script
test_web_api.py         # Unit tests using pytest
README.md               # Project documentation

```
## 💡 Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/number-trivia-fetcher.git

cd number-trivia-fetcher
```

2. Run the script:

```bash
python number_trivia.py
```

3. Run the script:

```bash
# Example output:

Ingrese el numero de la trivia que desea consultar: 42
Numero ingresado ->  42
---------------------------------
Codigo de estado ->  200
---------------------------------
Informacion de la trivia ->  {'text': '42 is the answer to the ultimate question of life, the universe, and everything.', 'number': 42, 'found': True, 'type': 'trivia'}
---------------------------------
Mensaje de la trivia -> 42 is the answer to the ultimate question of life, the universe, and everything.
Numero de la trivia -> 42

```
---
## 🧪 Running Tests
This project includes basic unit tests for the trivia_fetch function using pytest.

### 📦 Install pytest (if you haven't already):
```bash
pip install pytest
```

### ▶️ Run the tests:
Make sure you're in the project directory, then run:

```bash
python -m pytest test_web_api.py -v
```

You should see output like:

```bash
test_web_api.py::test_trivia_42 PASSED
test_web_api.py::test_trivia_1000 PASSED
```
These tests check that the function returns the correct trivia number when querying the Numbers API.

---
## 📄 License
This project is licensed under the MIT License. You can modify and use it freely.

---
## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the proposed changes.

---
## 📫 Contact
Feel free to reach out via GitHub Issues if you have questions or suggestions.
