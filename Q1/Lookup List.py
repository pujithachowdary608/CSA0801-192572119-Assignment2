def subsidy_lookup(units):
    slabs = [
        (100, "Full subsidy"),
        (200, "Partial subsidy"),
        (float("inf"), "No subsidy")
    ]
    for limit, decision in slabs:
        if units <= limit:
            return decision
print(subsidy_lookup(80))
print(subsidy_lookup(150))
print(subsidy_lookup(250))
