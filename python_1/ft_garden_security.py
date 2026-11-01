#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 rate: float, days: int) -> None:
        self._name = name
        self._height = 0.0
        self._rate = 0.0
        self._days = 0
        self.set_height(height)
        self.set_rate(height)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._rate, 1)

    def age(self) -> None:
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_rate(self) -> float:
        return self._rate

    def get_age(self) -> int:
        return self._days

    def set_height(self, att: float) -> bool:
        if att < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = att
        return True

    def set_rate(self, att: float) -> bool:
        if att < 0:
            print(f"{self._name}: Error, rate can't be negative")
            return False
        self._rate = att
        return True

    def set_age(self, att: int) -> bool:
        if att < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._days = att
        return True


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 0.8, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25):
        print(f"Height updated: {rose.get_height()}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()}cm")
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
