from . import config
from typing import Dict
from io import TextIOBase
from click import STRING, BOOL, Tuple

def assembleDataForMediumPost(title: STRING, html: BOOL, file: TextIOBase, tags: Tuple, public: BOOL, notify: BOOL) -> Dict:
    return {
        'title': title,
        'contentFormat': config.CONTENT_TYPE_HTML if html else config.CONTENT_TYPE_MARKDOWN,
        'content': file.read(),
        'tags': tags,
        'publishStatus': config.PUBLISH_STATUS_PUBLIC if public else config.PUBLISH_STATUS_DRAFT,
        'license': config.LICENSE_ALL,
        'notifyFollowers': notify
    }
