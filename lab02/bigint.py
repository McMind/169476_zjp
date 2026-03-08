class BigInt:
    def __init__(self, value: str | int | BigInt) -> None:
        val_str = str(value).strip().replace('+', '')
        if val_str == "-0" or val_str == "":
            val_str = "0"

        if val_str.startswith('-'):
            digits = val_str[1:].lstrip('0')
            self.value = "-" + (digits if digits else "0")
        else:
            digits = val_str.lstrip('0')
            self.value = digits if digits else "0"

        if self.value == "-0": self.value = "0"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"BigInt('{self.value}')"

    @staticmethod
    def _abs_compare(v1: str, v2: str) -> int:
        """Zwraca 1 jeśli |v1| > |v2|, -1 jeśli |v1| < |v2|, 0 jeśli równe."""
        s1 = v1.lstrip('-')
        s2 = v2.lstrip('-')
        if len(s1) != len(s2):
            return 1 if len(s1) > len(s2) else -1
        if s1 > s2: return 1
        if s1 < s2: return -1
        return 0

    @staticmethod
    def _raw_add(v1: str, v2: str) -> str:
        """Dodaje dwa stringi z samymi cyframi."""
        res, carry, i, j = [], 0, len(v1) - 1, len(v2) - 1
        while i >= 0 or j >= 0 or carry:
            d1 = int(v1[i]) if i >= 0 else 0
            d2 = int(v2[j]) if j >= 0 else 0
            s = d1 + d2 + carry
            res.append(str(s % 10))
            carry = s // 10
            i, j = i - 1, j - 1
        return "".join(res[::-1])

    @staticmethod
    def _raw_sub(v1: str, v2: str) -> str:
        """Odejmuje v2 od v1 (zakłada v1 >= v2, same cyfry)."""
        res, borrow, i, j = [], 0, len(v1) - 1, len(v2) - 1
        while i >= 0:
            d1 = int(v1[i])
            d2 = int(v2[j]) if j >= 0 else 0
            diff = d1 - d2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            res.append(str(diff))
            i, j = i - 1, j - 1
        final = "".join(res[::-1]).lstrip('0')
        return final if final else "0"

    def __lt__(self, other: BigInt) -> bool:
        s_neg = self.value.startswith('-')
        o_neg = other.value.startswith('-')
        if s_neg != o_neg:
            return s_neg

        comp = self._abs_compare(self.value, other.value)
        if not s_neg:
            return comp == -1
        return comp == 1

    def __eq__(self, other: BigInt) -> bool:
        o_val = other.value if isinstance(other, BigInt) else str(other)
        return self.value == o_val

    def __gt__(self, other: BigInt) -> bool:
        return not (self <= other)

    def __le__(self, other: BigInt) -> bool:
        return self < other or self == other

    def __ge__(self, other: BigInt) -> bool:
        return not (self < other)

    def __ne__(self, other: BigInt) -> bool:
        return not (self == other)

    def __add__(self, other: BigInt) -> BigInt:
        s_neg = self.value.startswith('-')
        o_neg = other.value.startswith('-')
        s_abs = self.value.lstrip('-')
        o_abs = other.value.lstrip('-')

        if s_neg == o_neg:
            res = self._raw_add(s_abs, o_abs)
            return BigInt("-" + res if s_neg else res)

        comp = self._abs_compare(s_abs, o_abs)
        if comp == 0: return BigInt("0")
        if comp == 1:
            res = self._raw_sub(s_abs, o_abs)
            return BigInt("-" + res if s_neg else res)
        else:
            res = self._raw_sub(o_abs, s_abs)
            return BigInt("-" + res if o_neg else res)

    def __iadd__(self, other: BigInt) -> BigInt:
        result = self + other
        self.value = result.value
        return self

    def __sub__(self, other: BigInt) -> BigInt:
        o_val = other.value
        new_o = o_val[1:] if o_val.startswith('-') else "-" + o_val
        return self + BigInt(new_o)

    def __isub__(self, other: BigInt) -> BigInt:
        result = self - other
        self.value = result.value
        return self

    def __mul__(self, other: BigInt) -> BigInt:
        s_neg = self.value.startswith('-')
        o_neg = other.value.startswith('-')
        s_abs, o_abs = self.value.lstrip('-'), other.value.lstrip('-')

        n1, n2 = len(s_abs), len(o_abs)
        res = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = int(s_abs[i]) * int(o_abs[j])
                res[i + j + 1] += mul
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] %= 10

        final_str = "".join(map(str, res)).lstrip('0') or "0"
        if final_str == "0": return BigInt("0")
        return BigInt("-" + final_str if s_neg != o_neg else final_str)

    def __imul__(self, other: BigInt) -> BigInt:
        result = self * other
        self.value = result.value
        return self