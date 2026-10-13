def ft_plant_age() -> None:
    age: int = int(input("Age of plant: "))
    if (age > 60):
        print("Ready for harvest")
    if (age <= 60):
        print("Not ready for harvest")
