print("""
        Swallow Speed Analysis: Version 1.0
        """
      )


def miles_to_kms(miles):
    return miles * 1.61


def kms_to_miles(miles):
    return miles / 1.61


def get_input_values():
    user_input = input("Enter the Next Reading: ")
    if not user_input:
        return False
    try:
        reading_type = user_input[0]
        if reading_type.upper() == 'E':
            kms = float(user_input[1:])
        elif reading_type.upper() == 'U':
            miles = float(user_input[1:])
            kms = miles_to_kms(miles)
        else:
            print("Invalid input")
            return None
        return {"reading_type": reading_type, "kms": kms}
    except ValueError:
        print("That wasn't a correct format")
        return None


input_value = True
arrays = []
while input_value is not False:
    input_value = get_input_values()
    if input_value is None:
        input_value = True  # set to false,if invalid format ends program
        continue
    if input_value is not False:
        arrays.append(input_value)
        print("Reading saved.")

if arrays == []:
    exit("No Readings Entered. Nothing to do.")


print(len(arrays),"Readings Analysed.")

total_kms = []
for item in arrays:
    total_kms.append(item["kms"])

max_speed = max(total_kms)
min_speed = min(total_kms)
avg_speed = sum(total_kms) / len(total_kms)

print("Max Speed: {} MPH, {} KPH.".format(max_speed, kms_to_miles(max_speed)))
print("Min Speed: {} MPH, {} KPH.".format(min_speed, kms_to_miles(min_speed)))
print("Avg Speed: {} MPH, {} KPH.".format(avg_speed, kms_to_miles(avg_speed)))
