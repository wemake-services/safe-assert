# safe-assert

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.org/wemake-services/docker-image-size-limit.svg?branch=master)](https://travis-ci.org/sobolevn/safe-assert)
[![Coverage](https://coveralls.io/repos/github/sobolevn/safe-assert/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/safe-assert?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/safe-assert.svg)](https://pypi.org/project/safe-assert/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/docker-image-size-limit)

Allows users to write `assert`s that are not stripped away in [optimized mode](https://docs.python.org/3/using/cmdline.html#cmdoption-o).


## Features

- Single simple, pythonic, fast, tested, typed, documented function. That's it!
- Because `safe_assert` is a function, it can be easily composed with other functions
- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

```bash
pip install safe-assert
```


## Examples

The usage is identical to `assert` keyword, but a function:

```python
from safe_assert import safe_assert

def sort_positive_number(numbers: List[int]) -> List[int]:
    safe_assert(all(num >= 0 for num in numbers), 'found negative')
    return sorted(numbers)
```

How is it different from regular `assert`?
The major one is that it would not be stripped away with `-O` flag.
So, it still allows to write declarative checks that are safe in production.

The second one is that you can compose it as any other regular function.
Useful in conjuction with [`dry-python`](https://github.com/dry-python) projects.


## Internals

How does it work internally?
It internally raises [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError) that is also used by the `assert` keyword itself.

See [docs](https://github.com/sobolevn/safe-assert/blob/master/safe_assert/__init__.py) to learn more.


## License

MIT.
