from faker import Faker
import logging

import sys

# Create a Logger object
my_logger = logging.getLogger('my_logger')

# Create a formatter object
default_formattor = logging.Formatter(
    fmt='%(name)s:%(asctime)s: %(levelname)s: %(module)s: %(filename)s: %(pathname)s - %(message)s')

# Define handler objects
# Console handler - prints everything in the console
console_handler = logging.StreamHandler(stream=sys.stdout)
# Add a formattor to a logger object
console_handler.setFormatter(default_formattor)

# File handler - records everything in the fils
file_handler = logging.FileHandler(filename='error.txt')
file_handler.setFormatter(default_formattor)

my_logger.setLevel('DEBUG')
my_logger.addHandler(console_handler)
my_logger.addHandler(file_handler)


def division(n, d):
    try:
        result = n/d
        my_logger.info(f'Result: {n}/{d}={result}')
    except ZeroDivisionError as e:
        my_logger.info(f'Result: {n}/{d}={0}')
        my_logger.error(f"Division by zero with paramteres {n} and {d}: {e}")


def print_data():
    faker = Faker()

    first_name, last_name = faker.name().split()
    email = faker.email()

    level = faker.items

    print(first_name, last_name, email, level)


if __name__ == '__main__':
    division(2, 0)
    division(3, 6)

    print_data()
