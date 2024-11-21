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

A small, dependency-free library that provides additional subclasses of [enum.StrEnum](https://docs.python.org/3/library/enum.html#enum.StrEnum).

## Installation

`stringenum` is available on [PyPI](https://pypi.org/project/stringenum/), so you can simply use [pip](https://github.com/pypa/pip) to install it.

```sh
pip install stringenum
```

# Usage

- `stringenum.StrEnum` - Identical to [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum).

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
