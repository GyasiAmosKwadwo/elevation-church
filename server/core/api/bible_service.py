import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

BIBLE_API_BASE = "https://bible-api.com"


def fetch_bible_passage(reference: str, translation: str = "kjv") -> dict:
    reference = (reference or '').strip()
    translation = (translation or 'kjv').strip().lower() or 'kjv'

    if not reference:
        raise ValueError('Bible reference is required.')

    url = f"{BIBLE_API_BASE}/{urllib.parse.quote(reference)}?translation={urllib.parse.quote(translation)}"
    request = urllib.request.Request(url, headers={"User-Agent": "ElevationChurchBibleClient/1.0"})

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            raw_text = response.read().decode('utf-8')
            data = json.loads(raw_text)
    except HTTPError as exc:
        raise ValueError(f'Bible API request failed: {exc.code} {exc.reason}') from exc
    except URLError as exc:
        raise ValueError(f'Bible API request failed: {exc.reason}') from exc

    if 'error' in data:
        raise ValueError(data.get('error', 'Bible passage not found.'))

    return {
        'reference': data.get('reference', reference),
        'translation': translation,
        'passage_text': data.get('text', '').strip(),
        'raw_response': data,
    }
