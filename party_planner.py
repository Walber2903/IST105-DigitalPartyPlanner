import sys

# Step 1: Define party item names and values
party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11)
]

# Step 2: Create a lookup dictionary for quick access
item_dict = {str(i): value for i, (_, value) in enumerate(party_items)}
item_name_dict = {str(i): name for i, (name, _) in enumerate(party_items)}

# Step 3: Function to display party items in HTML format
def display_party_items():
    print("<h2>Available Party Items:</h2>")
    print("<ul>")
    for i, (name, _) in enumerate(party_items):
        print(f"<li>{i}: {name}</li>")
    print("</ul><br>")

# Step 4: Function to calculate base party code using bitwise AND
def calculate_base_code(indices):
    values = [int(item_dict[i]) for i in indices if i in item_dict]
    if not values:
        return None
    base_code = values[0]
    for val in values[1:]:
        base_code &= val
    return base_code

# Step 5: Function to adjust the base party code and return message
def adjust_code(base_code):
    if base_code == 0:
        return base_code + 5, "Epic Party Incoming!"
    elif base_code > 5:
        return base_code - 2, "Let's keep it classy!"
    else:
        return base_code, "Chill vibes only!"

# Step 6: Main function to handle user input and render output
def main():
    if len(sys.argv) < 2:
        print("<h2>Please provide item indices separated by commas (e.g., 0,1,2)</h2>")
        return

    input_indices = sys.argv[1].split(",")
    selected_names = [item_name_dict[i] for i in input_indices if i in item_name_dict]

    print("<html><body>")
    display_party_items()
    print(f"<strong>Enter item indices separated by commas (e.g., 0, 2):</strong> {', '.join(input_indices)}<br><br>")
    print(f"<strong>Selected Items:</strong> {', '.join(selected_names)}<br>")

    base_code = calculate_base_code(input_indices)
    if base_code is None:
        print("<strong>Error:</strong> Invalid input or no valid items selected.<br>")
        return

    values_used = [item_dict[i] for i in input_indices if i in item_dict]
    bitwise_formula = " & ".join(values_used)
    print(f"<strong>Base Party Code:</strong> {bitwise_formula} = {base_code}<br>")

    final_code, message = adjust_code(base_code)
    if base_code == 0:
        adjusted_formula = f"{base_code} + 5"
    elif base_code > 5:
        adjusted_formula = f"{base_code} - 2"
    else:
        adjusted_formula = f"{base_code}"

    print(f"<strong>Adjusted Party Code:</strong> {adjusted_formula} = {final_code}<br>")
    print(f"<strong>Final Party Code:</strong> {final_code}<br>")
    print(f"<strong>Message:</strong> {message}<br>")
    print("</body></html>")

if __name__ == "__main__":
    main()