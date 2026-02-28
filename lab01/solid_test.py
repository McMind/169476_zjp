if __name__ == '__main__':
    import solid.polyhedron as pl
    import solid.revolution as rv

    a1 = 5
    h1 = 6

    print(f"Pole kostki o boku {a1} wynosi {pl.cube.total_surface_area(a1)}")
    print(f"Objętość kostki o boku {a1} wynosi {pl.cube.volume(a1)}")
    print(f"Pole ośmiościanu o boku {h1} wynosi {pl.octahedron.total_surface_area(h1)}")
    print(f"Objętość ośmiościanu o boku {h1} wynosi {pl.octahedron.volume(h1)}")
    print(f"Pole czworościanu o boku {a1} wynosi {pl.tetrahedron.total_surface_area(a1)}")
    print(f"Objętość czworościanu o boku {a1} wynosi {pl.tetrahedron.volume(a1)}")
    print(f"Pole stożka o promieniu {a1} i wysokości {h1} wynosi {rv.cone.total_surface_area(a1, h1)}")
    print(f"Objętość stożka o promieniu {a1} i wysokości {h1} wynosi {rv.cone.volume(a1, h1)}")
    print(f"Pole walca o promieniu {a1} i wysokości {h1} wynosi {rv.cylinder.total_surface_area(a1, h1)}")
    print(f"Objętość walca o promieniu {a1} i wysokości {h1} wynosi {rv.cylinder.volume(a1, h1)}")
    print(f"Pole kuli o promieniu {a1} wynosi {rv.sphere.total_surface_area(a1)}")
    print(f"Objętość kuli o promieniu {a1} wynosi {rv.sphere.volume(a1)}")

    print("---")

    print(rv.cone.total_surface_area.__name__)
    print(rv.cone.total_surface_area.__doc__)
    help(rv.cone.total_surface_area)

    print("---")

    print(pl.__file__)
    print(pl.cube.__file__)
