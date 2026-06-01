def make_label(name, /, category, *, price):
    return f"{name} ({category}): {price}"


obj1 = make_label("test", 1, price=10)

print(obj1)
