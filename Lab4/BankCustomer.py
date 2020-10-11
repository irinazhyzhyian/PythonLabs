# Напишіть клас BankCustomer, який
# наслідуватиме Person і доповнюватиме його наступною інформацією про клієнта банку:
# серія паспорту, стать, сума кредиту(грн), телефон. Обчисліть загальну суму кредитів, що
# видані банком і середній вік усіх чоловіків-клієнтів банку.
from Person import Person


class BankCustomer(Person):

    men_count = 0
    men_total_age = 0
    total_amount = 0

    def __init__(self, first_name, last_name, father_name, birthday, id_number, gender, loan_amount, phone):
        self._id_number = id_number
        self._gender = gender
        self._loan_amount = float(loan_amount)
        self._phone = phone
        BankCustomer.total_amount += self._loan_amount
        super().__init__(first_name, last_name, father_name, birthday)
        if gender == 'man':
            BankCustomer.men_count += 1
            BankCustomer.men_total_age += Person.get_age(self)

    @staticmethod
    def get_men_average_age():
        if BankCustomer.men_count > 0:
            return int(BankCustomer.men_total_age / BankCustomer.men_count)
        else:
            return "В банку немає клієнтів чоловіків!"

    @staticmethod
    def get_average_amount():
        if Person.count > 0:
            return BankCustomer.total_amount 
        else:
            return "Банк ще не має клієнтів!"

    # @property
    # def id_number(self):
    #     return self._father_name
    #
    # @id_number.setter
    # def id_number(self, id_number):
    #     self._id_number = id_number
    #
    # @property
    # def gender(self):
    #     return self._gender
    #
    # @gender.setter
    # def id_number(self, gender):
    #     self._gender = gender
    #
    # @property
    # def loan_amount(self):
    #     return self._loan_amount
    #
    # @loan_amount.setter
    # def loan_amount(self, loan_amount):
    #     self._loan_amount = loan_amount
    #
    # @property
    # def phone(self):
    #     return self._phone
    #
    # @phone.setter
    # def phone(self, phone):
    #     self._phone = phone
