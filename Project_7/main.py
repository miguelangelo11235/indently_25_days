import sys
from typing import Any

def custom_print(*values: Any,
                 sep: str | None = ' ',
                 end: str | None = '\n',
                 caps: bool = False,
                 include_types: bool = False,
                 count: bool = False,
                 reverse: bool = False) -> None:
    # new_values: list[Any] = []
    # for value in values:
    #     if isinstance(value, str) and caps:
    #         new_values.append(value.upper())
    #     else:
    #         new_values.append(value)
    #
    # values_with_type: list[Any] = []
    # if include_types:
    #     for value in new_values:
    #         values_with_type.append((value, type(value)))
    #     print(*values_with_type, sep=sep, end=end)
    # else:
    #     print(*new_values, sep=sep, end=end)

    capped_values = map(lambda x: x.upper() if isinstance(x, str) and caps else x, values)
    reversed_values = map(lambda x: x[::-1] if isinstance(x, str) and reverse else x, capped_values)
    typed_values = map(lambda x: (x, type(x)) if include_types else x, reversed_values)

    list_values: list[Any] = list(typed_values)

    print(*list_values, sep=sep, end=end)

    if count:
        print(f"{len(list_values)} element(s). ")

if __name__ == "__main__":
    test_values = ['Mikheltodd', 1, 'Yahoo', 2, 3.14, False, "Hehe", "Dragon"]
    custom_print(*test_values, sep=', ', end='.\n', caps=True, include_types=True, count=True, reverse=True)