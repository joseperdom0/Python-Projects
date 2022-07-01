def runner(brand, model ="", year =2021, convertible = False):
    var = (brand, str(year),str(convertible))
    print(var)
    print(type(var))
    return brand, str(year), str(convertible)


print(runner("Fermi")[2][2])

