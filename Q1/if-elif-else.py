def subsidy(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    else:
        if senior_member:
            return "Special subsidy"
        else:
            return "No subsidy"
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
    print(name, units, subsidy(units, ration, senior))
