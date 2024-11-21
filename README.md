# stringenum

<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/stringenum?link=https%3A%2F%2Fpypi.org%2Fproject%2Fstringenum%2F)](https://pypi.org/project/stringenum/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stringenum)
![License](https://img.shields.io/github/license/Ravencentric/stringenum)
![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Ravencentric/stringenum/release.yml)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ravencentric/stringenum/tests.yml?label=tests)
[![codecov](https://codecov.io/gh/Ravencentric/stringenum/graph/badge.svg?token=812Q3UZG7O)](https://codecov.io/gh/Ravencentric/stringenum)

</div>

## Table Of Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

# About

A small, dependency-free library offering additional [enum.StrEnum](https://docs.python.org/3/library/enum.html#enum.StrEnum) subclasses and a backport for older Python versions.

## Installation

`stringenum` is available on [PyPI](https://pypi.org/project/stringenum/), so you can simply use [pip](https://github.com/pypa/pip) to install it.

```sh
pip install stringenum
```

# Usage

- `stringenum.StrEnum` - A backport of [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum). While `StrEnum` was added in Python 3.11, version 3.12 brought changes to the `__contains__` method in `EnumType`, which also impacts `StrEnum`. `stringenum.StrEnum` includes this `__contains__` update from Python 3.12.

  - `enum.StrEnum` on Python <=3.11
    ```py
    >>> class Color(enum.StrEnum):
    ...     RED = "RED"
    ...     GREEN = "GREEN"

    >>> Color.RED in Color
    True
    >>> "RED" in Color
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for 'in': 'str' and 'EnumType'
    ```

  - `enum.StrEnum` on Python >=3.12
    ```py
    >>> class Color(enum.StrEnum):
    ...     RED = "RED"
    ...     GREEN = "GREEN"

    >>> Color.RED in Color
    True
    >>> "RED" in Color
    True
    >>> 12 in Color
    False
    ```

  - `stringenum.StrEnum` on Python >=3.9
    ```py
    >>> class Color(stringenum.StrEnum):
    ...     RED = "RED"
    ...     GREEN = "GREEN"

    >>> Color.RED in Color
    True
    >>> "RED" in Color
    True
    >>> 12 in Color
    False
    ```

- `stringenum.CaseInsensitiveStrEnum` - A subclass of `StrEnum` that supports case-insensitive lookup.

    ```py
    >>> class Pet(CaseInsensitiveStrEnum):
    ...     CAT = "meow"
    ...     DOG = "bark"

    >>> Pet("Meow")
    <Pet.CAT: 'meow'>

    >>> Pet("BARK")     
    <Pet.DOG: 'bark'>

    >>> Pet["Cat"]
    <Pet.CAT: 'meow'>

    >>> Pet["dog"] 
    <Pet.DOG: 'bark'>
    ```

- `stringenum.DuplicateFreeStrEnum` - A subclass of `StrEnum` that ensures all members have unique values and names, raising a `ValueError` if duplicates are found.

    ```py
    >>> class Fruits(DuplicateFreeStrEnum):
    ...     APPLE = "apple"
    ...     BANANA = "banana"
    ...     ORANGE = "apple"
    ...
    Traceback (most recent call last):
      ...
    ValueError: Duplicate values are not allowed in Fruits: <Fruits.ORANGE: 'apple'>
    ```

- `stringenum.DoubleSidedStrEnum` - A subclass of `DuplicateFreeStrEnum` that supports double-sided lookup, allowing both member values and member names to be used for lookups.

    ```py
    >>> class Status(DoubleSidedStrEnum):
    ...     PENDING = "waiting"
    ...     REJECTED = "denied"

    >>> Status("PENDING")
    <Status.PENDING: 'waiting'>

    >>> Status("waiting")
    <Status.PENDING: 'waiting'>

    >>> Status["REJECTED"]
    <Status.REJECTED: 'denied'>

    >>> Status["denied"]
    <Status.REJECTED: 'denied'>
    ```

- `stringenum.DoubleSidedCaseInsensitiveStrEnum` - A subclass of `DuplicateFreeStrEnum` that supports case-insenitive double-sided lookup, allowing both member values and member names to be used for lookups.

    ```py
    >>> class Status(DoubleSidedCaseInsensitiveStrEnum):
    ...     PENDING = "waiting"
    ...     REJECTED = "denied"

    >>> Status("pending")
    <Status.PENDING: 'waiting'>

    >>> Status("Waiting")
    <Status.PENDING: 'waiting'>

    >>> Status["Rejected"]
    <Status.REJECTED: 'denied'>

    >>> Status["DenieD"]
    <Status.REJECTED: 'denied'>
    ```

## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See [LICENSE](https://github.com/Ravencentric/stringenum/blob/main/LICENSE) for more information.
