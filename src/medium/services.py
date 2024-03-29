from typing import Dict
from . import apis, config, utils, formatter

def uploadImagesInMarkdown(data: str) -> str:
    image_links = utils.getImagesLinksInMarkdown(data)
    replace_links = {}
    for link in image_links:
        filepath = link.split(formatter.IMAGE_LINK_SPLITTER)[1][:-1]
        with open(filepath, 'rb') as file_image:
            files = formatter.assembleFilesForMediumImage(file_image, filepath)
            response = apis.uploadImage(config.HEADERS, files)

            url = formatter.getUrlFromResponse(response)
            replace_links[filepath] = url

    for origin, target in replace_links.items():
        data = data.replace(formatter.assembleMarkdownImageLinkReplacer(origin), formatter.assembleMarkdownImageLinkReplacer(target))

    return data

def createPost(data: Dict) -> Dict:
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    return apis.createPost(author_id, data, config.HEADERS)
