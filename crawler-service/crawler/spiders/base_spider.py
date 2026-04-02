import scrapy
from abc import abstractmethod


class BaseStartupSpider(scrapy.Spider):
    """
    All crawlers inherit from here.
    Stack matching and profile config are centralised so each
    spider only needs to worry about parsing its own source.
    """

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._target_stack: set[str] = set()
        self._target_role: str = ""

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        raw_stack = crawler.settings.get("JOBSEEKER_STACK", "")
        spider._target_stack = {s.strip().lower() for s in raw_stack.split(",") if s.strip()}
        spider._target_role = crawler.settings.get("JOBSEEKER_ROLE", "").lower()
        return spider

    def stack_matches(self, tags: list[str]) -> bool:
        """Return True if any tag from the posting overlaps with the target stack."""
        if not self._target_stack:
            return True   # no filter set → accept everything
        normalised = {t.strip().lower() for t in tags}
        return bool(self._target_stack.intersection(normalised))

    def role_matches(self, role_text: str) -> bool:
        """Loose check: does the role title contain any word from the target role?"""
        if not self._target_role:
            return True
        role_words = set(self._target_role.split())
        return any(word in role_text.lower() for word in role_words)

    @abstractmethod
    def parse(self, response): ...
