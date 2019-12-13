from django.conf import settings

from .db import Post


__all__ = ["Post"]


stop_words = getattr(settings, "STOP_WORDS", None)


def get_stop_words() -> set:
    with open(stop_words, mode="r") as fp:
        stopwords = fp.readlines()
        stop_set = set(m.strip() for m in stopwords if m.strip() != "")
        return frozenset(stop_set)