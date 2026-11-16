def subsidy_separate(units, ration_card, senior_member):
    result = []

    if units <= 100:
        result.append("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        result.append("Partial subsidy")

    if 101 <= units <= 200 and not ration_card:
        result.append("No subsidy")

    if units > 200 and senior_member:
        result.append("Special subsidy")

    if units > 200 and not senior_member:
        result.append("No subsidy")

    return result


households = [
    ("H1", 80, False, False),
    ("H2", 100, True, False),
    ("H3", 101, True, False),
    ("H4", 101, False, False),
    ("H5", 200, True, False),
    ("H6", 200, False, False),
    ("H7", 201, False, True),
    ("H8", 201, True, False)
]

for name, units, ration, senior in households:
    print(name, units, subsidy_separate(units, ration, senior))