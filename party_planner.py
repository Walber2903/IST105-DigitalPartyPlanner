import sys

party_dic = {
    "20": "Cake 🎂",
    "21": "Balloons 🎈",
    "10": "Music System 🎶",
    "5": "Party Lights 💡",
    "8": "Catering 🍕",
    "3": "DJ 🎧",
    "15": "Photo Booth 📸",
    "7": "Tables & Chairs 🪑",
    "6": "Drinks & Beverages 🥤",
    "4": "Invitations ✉️",
}

def calc_base_party_code(partyItemList):
    partyCode = int(partyItemList[0])
    for idx, item in enumerate(partyItemList[1:], start=1):
        partyCode = partyCode & int(item)
    return partyCode

def adjust_party_code(basePartyCode):
    adjustedPartyCode = basePartyCode
    formula = ""
    message = "Chill vibes only! 😌"

    if basePartyCode == 0:
        adjustedPartyCode += 5
        formula = f"{basePartyCode} + 5"
        message = "Epic party incoming! 🎉"
    elif basePartyCode > 5:
        adjustedPartyCode -= 2
        formula = f"{basePartyCode} - 2"
        message = "Let's keep it classy! 🍷"

    return adjustedPartyCode, message, formula

def getSelectedItemNames(partyItemList):
    return ", ".join(party_dic.get(item, f"Unknown ({item})") for item in partyItemList)

def main():
    partyItemCsv = sys.argv[1] if len(sys.argv) > 1 else ""
    partyItemList = partyItemCsv.split(",") if partyItemCsv else []

    if not partyItemList or partyItemList == ['']:
        print("<h2>Please select party item options.</h2>")
        return

    print("<h2>🎉 Welcome to the CCTB Digital Party Planner 🎉</h2><br>")
    print(f"<strong>Selected Item Codes:</strong> {partyItemCsv}<br>")
    selectedItems = getSelectedItemNames(partyItemList)
    print(f"<strong>Selected Items:</strong> {selectedItems}<br>")

    basePartyCode = calc_base_party_code(partyItemList)
    print(f"<strong>Base Party Code:</strong> {' & '.join(partyItemList)} = {basePartyCode}<br>")

    adjustedPartyCode, message, formula = adjust_party_code(basePartyCode)
    print(f"<strong>Adjusted Party Code:</strong> {formula} = {adjustedPartyCode}<br>")
    print(f"<strong>Final Party Code:</strong> {adjustedPartyCode}<br>")
    print(f"<strong>Message:</strong> {message}<br>")

main()
