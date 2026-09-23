"""Mini Project 03: Temperature Converter"""


def convert(value, from_unit, to_unit):
    to_celsius = {
        "C": lambda v: v,
        "F": lambda v: (v - 32) * 5 / 9,
        "K": lambda v: v - 273.15,
    }
    from_celsius = {
        "C": lambda v: v,
        "F": lambda v: v * 9 / 5 + 32,
        "K": lambda v: v + 273.15,
    }
    celsius_value = to_celsius[from_unit](value)
    return from_celsius[to_unit](celsius_value)


def main():
    print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")
    value = float(input("Enter temperature value: "))
    from_unit = input("From unit (C/F/K): ").strip().upper()
    to_unit = input("To unit (C/F/K): ").strip().upper()
    result = convert(value, from_unit, to_unit)
    print(f"{value}{from_unit} = {result:.2f}{to_unit}")


if __name__ == "__main__":
    main()
