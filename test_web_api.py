"""
Unit tests for trivia_fetch function in trivia.py module.
1.- Instalar pytest: pip install pytest
2.- Ejecutar los tests: pytest test.py
3.- Ver resultados: pytest test.py -v
"""
# import the trivia_fetch function from the web-api file
from web_api import trivia_fetch

# Test 1
def test_trivia_42():
  assert trivia_fetch(42)["number"] == 42

# Test 2
def test_trivia_1000():
  assert trivia_fetch(1000)["number"] == 1000
