# Напишіть клас Person, який містить наступну інформацію: прізвище, ім’я, по-батькові
# та дата народження людини. В класі створіть метод, який по заданій даті народження
# виводитиме повну кількість років людини.
from datetime import datetime


class Person:
    count = 0

    def __init__(self, first_name, last_name, father_name, birthday):
        self._first_name = first_name
        self._last_name = last_name
        self._father_name = father_name
        self._birthday = datetime.strptime(birthday, "%d-%m-%Y")
        if self.get_age() < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        Person.count += 1

    def get_age(self):
        return int((datetime.today() - self._birthday).total_seconds() / (365.242 * 24 * 3600))

    # @property
    # def first_name(self):
    #     return self._first_name
    #
    # @first_name.setter
    # def first_name(self, first_name):
    #     self._first_name = first_name
    #
    # @property
    # def last_name(self):
    #     return self._last_name
    #
    # @last_name.setter
    # def last_name(self, last_name):
    #     self._last_name = last_name
    #
    # @property
    # def father_name(self):
    #     return self._father_name
    #
    # @father_name.setter
    # def father_name(self, father_name):
    #     self._father_name = father_name
    #
    # @property
    # def birthday(self):
    #     return self._birthday
    #
    # @birthday.setter
    # def birthday(self, birthday):
    #     d = datetime.stripe(birthday, "%d-%m-%Y")
    #     num_years = int((datetime.today() - d).total_seconds() / (365.242 * 24 * 3600))
    #     if num_years >= 18:
    #         pass
    #     else:
    #         raise ValueError("Sorry you age is below eligibility criteria")
