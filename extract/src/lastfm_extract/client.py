from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from .utils import RateLimiter


@dataclass
class LastFmClient:
    api_key: str
    user_agent: str = "end-to-end-data-engineer"
    base_url: str = "https://ws.audioscrobbler.com/2.0/"
    timeout_seconds: int = 30
    rate_limiter: Optional[RateLimiter] = None

    def __post_init__(self) -> None:
        if self.rate_limiter is None:
            self.rate_limiter = RateLimiter(min_interval_seconds=0.25)

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=20))
    def _get(self, params: Dict[str, Any]) -> Dict[str, Any]:
        assert self.rate_limiter is not None
        self.rate_limiter.wait()

        final_params = {
            "api_key": self.api_key,
            "format": "json",
            **params,
        }
        headers = {"User-Agent": self.user_agent}

        resp = requests.get(self.base_url, params=final_params, headers=headers, timeout=self.timeout_seconds)
        resp.raise_for_status()
        return resp.json()

    def geo_get_top_tracks(self, country: str, limit: int = 200, page: int = 1) -> Dict[str, Any]:
        return self._get(
            {
                "method": "geo.getTopTracks",
                "country": country,
                "limit": limit,
                "page": page,
            }
        )
