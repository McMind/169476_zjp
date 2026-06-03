def make_record(title, /, author, *, year):
    return f"{title} - {author} ({year})"


if __name__ == "__main__":
    print(make_record("Tytuł", "Autor", year=2026))
    print(make_record("Tytuł2", year=2024, author="Autor2"))
