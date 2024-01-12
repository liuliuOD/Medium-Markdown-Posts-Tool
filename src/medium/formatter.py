import typing
from . import config
from io import TextIOBase
from click import STRING, BOOL, Tuple

def assembleCommandsData(title: STRING, html: BOOL, file: TextIOBase, tags: Tuple, public: BOOL, notify: BOOL) -> typing.Dict:
    content_format = config.CONTENT_TYPE_HTML if html else config.CONTENT_TYPE_MARKDOWN
    publish_status = config.PUBLISH_STATUS_PUBLIC if public else config.PUBLISH_STATUS_DRAFT

    return assembleDataForMediumPost(title, content_format, file, tags, publish_status, notify)

def assembleDataForMediumPost(title: str, content_format: str, file: TextIOBase, tags: typing.Tuple, publish_status: str, notify: bool) -> typing.Dict:
    return {
        'title': title,
        'contentFormat': content_format,
        'content': file.read(),
        'tags': tags,
        'publishStatus': publish_status,
        'license': config.LICENSE_ALL,
        'notifyFollowers': notify
    }
