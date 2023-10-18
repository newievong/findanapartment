def apt_search1(city,  max_rent, min_beds, pets_allowed):
    if pets_allowed == True:
        return(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} "
              f"bedroom apartments that allow pets, all within a budget of {max_rent} per month...")

    else:
        return (f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} "
              f"bedroom apartments, all within a budget of {max_rent} per month...")

print(apt_search1("Grand Rapids", 1300, 2, True))


def apt_search2(city, max_rent, min_beds = 1, pets_allowed = True):
    if pets_allowed == True:
        return(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} "
              f"bedroom apartments that allow pets, all within a budget of {max_rent} per month...")

    else:
        return(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} "
              f"bedroom apartments, all within a budget of {max_rent} per month...")

print(apt_search2("Dallas", 1300))
print(apt_search2("New York City", 1700, 3))
print(apt_search2("Miami", 1500, pets_allowed = False))

plus_one_hundred = lambda x : x + 100
result1 = plus_one_hundred(30)
print(result1)

square_num = lambda x : x**3
result2 = square_num(4)
print(result2)

concatenate = lambda str : "- " + str
result3 = concatenate('Hello')
print(result3)

divide_by_three = lambda x : x / 3
result4 = divide_by_three(9)
print(result4)


 
