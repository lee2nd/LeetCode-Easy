# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")

# with walrus，只需要兩行，其實 := 就等於 =
if (n := 30) > 10:
    print(f"{n} is greater than 10")
