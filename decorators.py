from custom_exceptions import (
    DuplicateEntry, IncorrectDateFormat, IncorrectPhoneFormat, NoBirthDay, NoData, NoDataFound, ContactNotFound, PhoneNotFound
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            raise ValueError("Give me name and phone please.")
        except NoData:
            raise NoData("No data entered.")
        except IncorrectPhoneFormat:
            raise IncorrectPhoneFormat(
                "Please, enter a valid phone format (10 digits).")
        except NoDataFound:
            raise NoDataFound("No data found.")
        except DuplicateEntry:
            raise DuplicateEntry("A duplicate entry was found.")
        except PhoneNotFound:
            raise PhoneNotFound("Phone number or contact not found.")
        except IncorrectDateFormat:
            raise IncorrectDateFormat("Invalid date format. Use DD.MM.YYYY.")
        except ContactNotFound:
            raise ContactNotFound("Contact not found.")
        except NoBirthDay:
            raise NoBirthDay("No upcoming birthdays in the next week")
        except Exception as e:
            raise Exception(str(e))
    return inner
