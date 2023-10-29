class NoData(Exception):
    """Raised when no data is entered."""
    pass

class PhoneNotFound(Exception):
    """Raised when the entered phone number is not found."""
    pass


class IncorrectPhoneFormat(Exception):
    """Raised when the phone format is incorrect."""
    pass


class NoDataFound(Exception):
    """Raised when no data is found for the provided input."""
    pass


class DuplicateEntry(Exception):
    """Raised when a duplicate entry is found."""
    pass


class IncorrectDateFormat(Exception):
    """Raised when the date format is incorrect."""
    pass


class ContactNotFound(Exception):
    """Raised when a contact is not found."""
    pass


class NoBirthDay(Exception):
    """Raised when a birthday is not found."""
    pass
