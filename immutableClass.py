from dataclasses import dataclass
from datetime import date
from typing import List


# Private Address class
@dataclass(frozen=True)
class _Address:  # Private class (by convention)
    street: str
    city: str
    postal_code: str


@dataclass(frozen=True)
class Employee:
    name: str
    id: str
    date_of_joining: date
    addresses: List[_Address]  # List of Address objects, which are also immutable

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_addresses(self):
        return self.addresses



address1 = _Address("123 Main St", "Springfield", "12345")
address2 = _Address("456 Oak St", "Shelbyville", "67890")

employee = Employee(
    name="John Doe",  # Employee Name
    id="E123",        # Employee ID
    date_of_joining=date(2020, 1, 1),  # Date of Joining (January 1, 2020)
    addresses=[address1, address2]  # List of Address objects
)

print("Employee Name:", employee.get_name())  # Output: John Doe
print("Employee ID:", employee.get_id())  # Output: E123
print("Date of Joining:", employee.date_of_joining)  # Output: 2020-01-01

# Accessing Employee addresses
print("Employee Addresses:")
for address in employee.get_addresses():
    print(f"{address.street}, {address.city}, {address.postal_code}")

