from vector.vector3d import Vector3D

def test_vector3d():
    v1 = Vector3D(1, 2, 2)
    v2 = Vector3D(4, 0, 3)
    v0 = Vector3D(0, 0, 0)

    print("--- Testy Podstawowe ---")
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"Długość v1 (abs): {abs(v1)} (Oczekiwane: (3.0))")
    print(f"Długość v2 (abs): {abs(v2)} (Oczekiwane: (5.0))")
    print(f"Wymiarowość (len): {len(v1)}")

    print("\n--- Operacje Arytmetyczne ---")
    v_sum = v1 + v2
    v_sub = v1 - v2
    print(f"v1 + v2 = {v_sum} (Oczekiwane: (5, 2, 5))")
    print(f"v1 - v2 = {v_sub} (Oczekiwane: (-3, 2, -1))")

    print("\n--- Operatory Porównania ---")
    print(f"v1 < v2:  {v1 < v2}  (True)")
    print(f"v1 > v2:  {v1 > v2}  (False)")
    print(f"v1 == v2: {v1 == v2} (False)")
    print(f"v1 != v2: {v1 != v2} (True)")
    print(f"v1 <= v2: {v1 <= v2} (True)")

    print("\n--- Testy Logiczne ---")
    print(f"bool(v1): {bool(v1)} (True, bo niezerowy)")
    print(f"bool(v0): {bool(v0)} (False, bo zerowy)")

    print("\n--- Metody Dodatkowe ---")
    print(f"Iloczyn skalarny v1 i v2: {v1.dot_product(v2)} (Oczekiwane: 1*4 + 2*0 + 2*3 = 10)")
    print(f"Kąt między v1 i v2: {v1.angle_between(v2):.2f}°")

    v_norm = v1.normalize()
    print(f"Normalizacja v1: {v_norm}")
    print(f"Długość znormalizowanego v1: {abs(v_norm)} (Oczekiwane: 1.0)")


if __name__ == "__main__":
    try:
        test_vector3d()
    except Exception as e:
        print(f"\nWystąpił problem: {e}")