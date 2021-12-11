import json

import requests
from django.conf import settings

translate_url = getattr(settings, "TRANSLATE_BOT_URL")


def translate_text(text, source="ok", target="en") -> str:
    _r = requests.post(
        translate_url,
        json={
            "text": text,
            "source": source,
            "target": target,
        },
    )
    _data = json.loads(_r.text)
    return _data["TranslatedText"]
