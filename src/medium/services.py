from . import apis, config, utils, formatter

def uploadImagesInMarkdown(data: str) -> str:
    image_links = utils.getImagesLinksInMarkdown(data)
    replace_links = {}
    for link in image_links:
        filepath = link.split('](')[1][:-1]
        with open(filepath, 'rb') as file_image:
            files = formatter.assembleFilesForMediumImage(file_image, filepath)
            response = apis.uploadImage(config.HEADERS, files)

            url = formatter.getUrlFromResponse(response)
            replace_links[filepath] = url

    for origin, target in replace_links.items():
        data = data.replace(f']({origin})', f']({target})')

    return data
