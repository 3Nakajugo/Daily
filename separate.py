def separate():
    items = []
    for item in range(2000, 3600):
        if item % 7 == 0 and item % 5 != 0:
            items.append(item)

    return items


print(separate())
