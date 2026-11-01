#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        i: int = int("abc")
    elif operation_number == 1:
        x: int = 5
        y: int = 0
        z: float = x / y
    elif operation_number == 2:
        open('stuff.txt', 'r')
    elif operation_number == 3:
        s: str = "abc"
        n: int = 123
        p: int = s + n
    return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
