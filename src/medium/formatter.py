import typing
import pathlib
from . import config
from io import TextIOBase
from click import STRING, BOOL, Tuple

IMAGE_LINK_SPLITTER: str = ']('

def assembleCommandsData(title: STRING, html: BOOL, file_content: str, tags: Tuple, public: BOOL, notify: BOOL) -> typing.Dict:
    content_format = config.CONTENT_TYPE_HTML if html else config.CONTENT_TYPE_MARKDOWN
    publish_status = config.PUBLISH_STATUS_PUBLIC if public else config.PUBLISH_STATUS_DRAFT

    return assembleDataForMediumPost(title, content_format, file_content, tags, publish_status, notify)

def assembleDataForMediumPost(title: str, content_format: str, file_content: str, tags: typing.Tuple, publish_status: str, notify: bool) -> typing.Dict:
    return {
        'title': title,
        'contentFormat': content_format,
        'content': file_content,
        'tags': tags,
        'publishStatus': publish_status,
        'license': config.LICENSE_ALL,
        'notifyFollowers': notify
    }

def getContentTypeByExtension(filepath: str) -> str:
    match pathlib.Path(filepath).suffix:
        case '.jpg' | '.jpeg':
            return 'image/jpeg'
        case '.png':
            return 'image/png'
        case '.gif':
            return 'image/gif'
        case _:
            return 'image/tiff'

def assembleFilesForMediumImage(file: TextIOBase, filepath: str) -> typing.List:
    return [
        (
            'image', (
                file.name,
                file.read(),
                getContentTypeByExtension(filepath),
            )
        )
    ]

def assembleMarkdownImageLinkReplacer(target: str) -> str:
    return f'{IMAGE_LINK_SPLITTER}{target})'

def getUrlFromResponse(response: typing.Dict) -> str:
    return response['data']['url']
