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


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25.0, 0.8, 30),
        Plant("Oak", 200.0, 0.2, 365),
        Plant("Cactus", 5.0, 0.3, 90),
        Plant("Sunflower", 80.0, 0.6, 45),
        Plant("Fern", 15.0, 0.4, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
