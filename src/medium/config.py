import os
from fake_useragent import UserAgent
from dotenv import load_dotenv
load_dotenv()

HEADERS = {
    'Authorization': 'Bearer {}'.format(os.getenv('TOKEN')),
    'User-Agent': UserAgent().random
}

CONTENT_TYPE_HTML = 'html'
CONTENT_TYPE_MARKDOWN = 'markdown'

PUBLISH_STATUS_PUBLIC = 'public'
PUBLISH_STATUS_DRAFT = 'draft'
PUBLISH_STATUS_UNLISTED = 'unlisted'

LICENSE_ALL = 'all-rights-reserved'
