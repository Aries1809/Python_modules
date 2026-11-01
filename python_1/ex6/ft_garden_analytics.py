#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float,
                 rate: float, days: int) -> None:
        self._name = name
        self._stats = self.Stats()
        self._height = 0.0
        self._rate = 0.0
        self._days = 0
        self.set_height(height)
        self.set_rate(rate)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")
        self._stats.add_show()

    def grow(self) -> None:
        self._height = round(self._height + self._rate, 1)
        self._stats.add_grow()

    def age(self, days: int) -> None:
        self._days += days
        self._stats.add_age()

    def get_height(self) -> float:
        return self._height

    def get_rate(self) -> float:
        return self._rate

    def get_age(self) -> int:
        return self._days

    def get_name(self) -> str:
        return self._name

    def print_stats(self) -> None:
        self._stats.display()

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

    @staticmethod
    def is_old(age: int) -> bool:
        return age > 365

    @classmethod
    def anonym(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0.0, 0)


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
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def add_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float, rate: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, rate, days)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree.Stats()
        self._stats = self._tree_stats

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", end=" ")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._tree_stats.add_shade()


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


class Seed(Flower):
    def __init__(self, name: str, height: float, rate: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, rate, days, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.print_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_old(400)}")
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 8.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 0.2, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 30.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("")

    print("=== Anonymous")
    unknown = Plant.anonym()
    display_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
