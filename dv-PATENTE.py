def dv(patente):
  number_by_letter = {
      "A": "14",
      "B": "01",
      "C": "00",
      "D": "16",
      "E": "05",
      "F": "20",
      "G": "19",
      "H": "09",
      "I": "24",
      "J": "07",
      "K": "21",
      "L": "08",
      "M": "04",
      "N": "13",
      "O": "25",
      "P": "22",
      "Q": "18",
      "R": "10",
      "S": "02",
      "T": "06",
      "U": "12",
      "V": "23",
      "W": "11",
      "X": "03",
      "Y": "15",
      "Z": "17",
  }

  patente = patente.upper().replace(" ", "").replace("-", "")

  numbers = patente
  for letter, number in number_by_letter.items():
    numbers = numbers.replace(letter, number)

  num1 = 0
  num2 = 0

  for i, digit in enumerate(numbers):
    if i % 2 == 0:
      num1 += int(digit)
    else:
      num2 += int(digit)

  num1 = numero(num1)
  num2 = numero(num2)

  return str(num1) + str(num2)

def numero(n):
  while n > 9:
    n = sum(int(d) for d in str(n))
  return n

# EJEMPLO
patente = "ABC123"
digito = dv(patente)
print(f"Patente: {patente} DV: {digito}")
