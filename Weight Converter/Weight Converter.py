import math

# Get user input for weight
weight = input("Type in your weight: ")

# Check if weight is not empty and is a valid number
if weight == "":
    print("Error: Please enter your weight!")

elif not weight.replace(".", "").isdigit():
    print("Error: Invalid weight input. Please enter a valid number.")
else:
    weight = float(weight)

    # Get user input for weight unit
    w_unit = input("Is the weight stated above in kilograms(kg), Tonnes(t), Pounds(lb) or Ounces(oz): ").lower()

    # Check if the unit is valid
    if w_unit not in ["kg", "t", "lb", "oz"]:
        print("Error: Invalid unit. Please choose from kilograms(kg), Tonnes(t), Pounds(lb), or Ounces(oz).")

    else:
        # Get user input for conversion unit
        cw_unit = input(
            "Would you like to convert the weight stated above to kilograms(kg), Tonnes(t), Pounds(lb) or Ounces(oz): ").lower()

        # Check if the conversion unit is valid
        if cw_unit not in ["kg", "t", "lb", "oz"]:
            print("Error: Invalid unit. Please choose from kilograms(kg), Tonnes(t), Pounds(lb), or Ounces(oz).")

        else:
            # Conversion rates to kilograms (as base unit)
            if w_unit == "kg":
                weight_in_kg = weight
            elif w_unit == "t":
                weight_in_kg = weight * 1000
            elif w_unit == "lb":
                weight_in_kg = weight * 0.453592
            elif w_unit == "oz":
                weight_in_kg = weight * 0.0283495

            # Convert from kilograms to the desired unit
            if cw_unit == "kg":
                converted_weight = weight_in_kg
            elif cw_unit == "t":
                converted_weight = weight_in_kg / 1000
            elif cw_unit == "lb":
                converted_weight = weight_in_kg / 0.453592
            elif cw_unit == "oz":
                converted_weight = weight_in_kg / 0.0283495

            # Output the converted weight
            print(f"{weight} {w_unit.upper()} is equal to {round(converted_weight, 2)} {cw_unit.upper()}.")
