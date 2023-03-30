"""
This file is for time calculation - sometimes we need to wait and when we don't know how long wait, we decide what
maximum time we can wait, use 'while' loop and check the changes.
"""
import time
from collections.abc import Callable
from typing import Union


class Timer:
    """Timer class."""

    def __init__(self, timeout: Union[int, float] = 15) -> None:
        self._timeout = timeout
        self._start = time.time()

    def __repr__(self) -> str:
        return f'Timer(timeout={self._timeout:.2f} remainder={self.remainder():.2f} ' \
               f'elapsed={self.elapsed():.2f})'

    def remainder(self) -> float:
        """Returns remaining time.

        :return: Remaining time.
        :rtype: float
        """
        return max(0, self._timeout - self.elapsed())

    def fired(self) -> bool:
        """Returns true if timer expired.

        :return: True if timer expired (i.e. remainder == 0), False otherwise.
        :rtype: bool
        """
        return self.remainder() == 0

    def elapsed(self) -> float:
        """Returns how much time passed since Timer object created.

        :return: Elapsed time.
        :rtype: float
        """
        return time.time() - self._start

    def wait(self) -> None:
        """Waits until timer fires.

        :return: None.
        """
        time.sleep(self.remainder())

    def check_timeout(self, assertion: Exception) -> None:
        """Checks timeout and raises assertion if elapsed >= timeout.

        :param Exception assertion: Assertion to raise.

        :return: None.

        :raises assertion: If elapsed >= timeout.
        """
        if not self.elapsed() < self._timeout:
            raise assertion

    def wait_done(self, func: Callable, assertion: Exception, delay: Union[float, int] = 0) -> None:
        """Waits until the predicate function return True (in the allotted time).

        :param Callable func: Predicate function that stops the wait if returns True.
        :param Exception assertion: Assertion to raise it time elapsed.
        :param float|int delay: Delay to sleep after each check.

        :return: None.

        :raises assertion: If predicate function not returned True in the allotted time.
        """
        while not self.fired():
            if func():
                return
            self.check_timeout(assertion=assertion)
            time.sleep(min(delay, self.remainder()))

    def restart(self) -> None:
        """Restarts the timer.

        :return: None.
        """
        self._start = time.time()
