#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 rate: float, days: int) -> None:
        self._name = name
        self._height = 0.0
        self._rate = 0.0
        self._days = 0
        self.set_height(height)
        self.set_rate(rate)
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


class Flower(Plant):
    def __init__(self, name: str, height: float, rate: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, rate, days)
        self._color = color
        self._status: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._status:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._status = True


class Tree(Plant):
    def __init__(self, name: str, height: float, rate: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, rate, days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", end=" ")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, rate: float,
                 days: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, rate, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 0.8, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 0.2, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 2.1, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(0, 20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
