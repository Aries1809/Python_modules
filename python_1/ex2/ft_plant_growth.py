#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 rate: float, days: int) -> None:
        self.name = name
        self.height = height
        self.rate = rate
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.rate, 1)

    def age(self) -> None:
        self.days += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 0.8, 30)
    start: float = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
