def subsidy_match(units, ration_card, senior_member):
    match units:
        case n if n <= 100:
            return "Full subsidy"
        case n if 101 <= n <= 200 and ration_card:
            return "Partial subsidy"
        case n if 101 <= n <= 200:
            return "No subsidy"
        case n if n > 200 and senior_member:
            return "Special subsidy"
        case _:
            return "No subsidy"
print(subsidy_match(101, True, False))
print(subsidy_match(201, False, True))
