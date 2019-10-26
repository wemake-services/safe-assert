# -*- coding: utf-8 -*-

from typing import NoReturn, Optional


def safe_assert(  # type: ignore
    expression: bool,
    message: Optional[str] = None,
) -> NoReturn:
    """
    This function mimics ``assert`` keyword behavior.

    Why do we need it?
    Basically for just one reason: it is a common practice
    that we check things in our code with ``assert`` keyword.

    The only downside of this approach is that it does not work
    with ``-O`` command line option or ``PYTHONOPTIMIZED`` env variable.

    That's why I have to introduce this helper.

    Examples
    --------
    That's see how ``safe_assert`` and ``assert`` compares.

    >>> from safe_assert import safe_assert
    >>> safe_assert('a' in 'abc')

    >>> safe_assert('x' in 'abc')
    Traceback (most recent call last):
      ...
    AssertionError

    >>> safe_assert('y' in 'abc', 'missing')
    Traceback (most recent call last):
      ...
    AssertionError: missing

    These calls are equal to the regular ``assert`` usage:

    >>> assert 'a' in 'abc'
    >>> assert 'x' in 'abc'
    Traceback (most recent call last):
      ...
    AssertionError

    >>> assert 'y' in 'abc', 'missing'
    Traceback (most recent call last):
      ...
    AssertionError: missing

    Extras
    ------
    You can check that regular ``assert`` is not used with:

    - https://github.com/openstack/bandit
    - https://github.com/wemake-services/wemake-python-styleguide

    You can also check that you
    use ``assert x, y`` and not ``assert(x, y)`` with:

    - ``F631``: https://flake8.pycqa.org/en/latest/user/error-codes.html

    See also:
        https://docs.python.org/3/using/cmdline.html#cmdoption-o

    """
    if not expression:
        if message:
            raise AssertionError(message)
        raise AssertionError
