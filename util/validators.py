# utils.py
import re
from exceptions.invalid_customer_detail_exception import InvalidEmailException, InvalidPhoneNumberException

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise InvalidEmailException("Invalid email format.")

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise InvalidPhoneNumberException("Phone number must be exactly 10 digits.")
