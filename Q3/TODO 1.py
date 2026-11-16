def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234'"""
    return text.replace(" ", "").replace("-", "").upper()
def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits."""
    if len(reg) not in (9, 10):
        return False
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]
 return (
        state.isalpha()
        and district.isdigit()
        and len(series) in (1, 2)
        and series.isalpha()
        and number.isdigit()
    )
def format_receipt(reg):
    if not is_valid(reg):
        return "Invalid registration number"
    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
inputs = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "Tn09Ab1234",
    "TN9AB1234",
    "TN 22 1234 AB",
    "ABC-09-AB-1234"
]
for raw in inputs:
    reg = normalise(raw)
    result = "valid" if is_valid(reg) else "INVALID"
    print(f"{raw:15} -> {reg:11} {result}")
print("\nReceipt format:")
print(format_receipt(normalise("tn 09 ab 1234")))
