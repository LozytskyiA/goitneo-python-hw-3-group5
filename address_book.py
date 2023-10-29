import datetime
import re

from custom_exceptions import IncorrectDateFormat, NoBirthDay, NoDataFound, ContactNotFound, DuplicateEntry, IncorrectPhoneFormat, PhoneNotFound
from decorators import input_error


class Birthday:
    def __init__(self, date_str):
        if not self.validate_date(date_str):
            raise IncorrectDateFormat()

        self.date_str = date_str

    @staticmethod
    def validate_date(date_str):
        date_pattern = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")
        return bool(date_pattern.match(date_str))

    def __str__(self):
        return self.date_str


class Phone:
    def __init__(self, phone_str):
        if not self.validate_phone(phone_str):
            raise IncorrectPhoneFormat()

        self.phone_str = phone_str

    @staticmethod
    def validate_phone(phone_str):
        phone_pattern = re.compile(r"^\d{10}$")
        return bool(phone_pattern.match(phone_str))

    def __str__(self):
        return self.phone_str


class Person:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = Phone(phone) if phone else None
        self.birthday = Birthday(birthday) if birthday else None

    def __str__(self):
        return f"{self.name} - Phone: {self.phone}, Birthday: {self.birthday}"


class AddressBook:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone=None, birthday=None):
        if name in self.contacts:
            raise DuplicateEntry()

        self.contacts[name] = Person(name, phone, birthday)

    @input_error
    def change_contact(self, name, phone=None):
        if name not in self.contacts:
            raise ContactNotFound()

        if phone:
            self.contacts[name].phone = Phone(phone)

    @input_error
    def show_phone(self, name):
        if name not in self.contacts:
            raise PhoneNotFound()

        return self.contacts[name].phone

    @input_error
    def show_all(self):
        if not self.contacts:
            raise NoDataFound()

        return [f'{contact.name}: {contact.phone}' for contact in self.contacts.values()]

    @input_error
    def add_birthday(self, name, date_str):
        if not date_str:
            raise IncorrectDateFormat(
                "Usage: add-birthday [ім'я] [DD.MM.YYYY]")

        try:
            birthday = Birthday(date_str)
        except ValueError:
            raise IncorrectDateFormat("Invalid date format. Use DD.MM.YYYY.")

        contact = self.find_contact(name)
        if not contact:
            raise ContactNotFound(f"Contact '{name}' not found.")

        if not contact.birthday:
            contact.birthday = birthday
            return f"Birthday added for {name}."
        else:
            return f"Birthday already exists for {name}."

    @input_error
    def find_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None

    @input_error
    def show_birthday(self, name):
        if name not in self.contacts or not self.contacts[name].birthday:
            return "No birthday data found."
        return str(self.contacts[name].birthday)

    @input_error
    def get_birthdays_per_week(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(days=7)
        upcoming_birthdays = []

        for name, person in self.contacts.items():
            if person.birthday:
                birth_date = datetime.datetime.strptime(
                    person.birthday.date_str, "%d.%m.%Y").date()

                birthdate_this_year = birth_date.replace(year=today.year)
                birthdate_next_year = birth_date.replace(year=today.year + 1)

                if today <= birthdate_this_year <= next_week or today <= birthdate_next_year <= next_week:
                    upcoming_birthdays.append(f"{name}: {person.birthday}")

        if not upcoming_birthdays:
            raise NoBirthDay()

        return upcoming_birthdays
