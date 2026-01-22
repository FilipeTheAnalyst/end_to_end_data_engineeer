import os
import time
from typing import Optional


def env(name: str, default: Optional[str] = None) -> str:
    val = os.getenv(name, default)
    if val is None or val == "":
        raise ValueError(f"Missing required env var: {name}")
    return val


class RateLimiter:
    """Very small client-side rate limiter.

    Last.fm has rate limits; keep this conservative.
    """

    def __init__(self, min_interval_seconds: float = 0.25):
        self.min_interval_seconds = min_interval_seconds
        self._last = 0.0

    def wait(self) -> None:
        now = time.time()
        elapsed = now - self._last
        if elapsed < self.min_interval_seconds:
            time.sleep(self.min_interval_seconds - elapsed)
        self._last = time.time()
