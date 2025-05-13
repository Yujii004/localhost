def convert_units(value, from_unit, to_unit):
   
    units_to_meters = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001
    }

    value_in_meters = value * units_to_meters[from_unit]
    converted_value = value_in_meters / units_to_meters[to_unit]
    return converted_value

value = float(input("Значение: "))
from_unit = input("Из  (m, km, cm, mm): ").strip()
to_unit = input("В (m, km, cm, mm): ").strip()

if from_unit not in ['m', 'km', 'cm', 'mm'] or to_unit not in ['m', 'km', 'cm', 'mm']:
    print("Неправильный ввод значений")

converted_value = convert_units(value, from_unit, to_unit)
print(f"{value} {from_unit} = {converted_value:.4f} {to_unit}")


