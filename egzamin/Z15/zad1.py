def make_label(name, /, category, *, price):
    return f"{name} ({category}): {price}"


print(make_label("test", 1, price=10))
