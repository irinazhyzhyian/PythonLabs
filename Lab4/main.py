# Обчисліть загальну суму кредитів, що
# видані банком і середній вік усіх чоловіків-клієнтів банку.
from BankCustomer import BankCustomer


a = BankCustomer("Name", "Surname", "FathersName", "28-02-2001", "123456", "man", "1000", "3256976")
b = BankCustomer("Name", "Surname", "FathersName", "28-02-2000", "123456", "woman", "30000", "3256976")
c = BankCustomer("Name", "Surname", "FathersName", "28-02-2001", "123456", "man", "10000", "3256976")
d = BankCustomer("Name", "Surname", "FathersName", "28-02-1935", "123456", "man", "15000", "3256976")

print("Загальна сума кредитів, що видані банком:", BankCustomer.get_average_amount())
print("Середній вік усіх чоловіків-клієнтів банку:", BankCustomer.get_men_average_age())
