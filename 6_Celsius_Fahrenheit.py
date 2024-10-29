# Poproś użytkownika o wprowadzenie temperatury w stopniach Celsjusza
celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))

# Przelicz temperaturę na Fahrenheita
fahrenheit = celsius * (9/5) + 32

# Wyświetl wynik
print(f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")
