#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    for data in ["25", "abc"]:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
