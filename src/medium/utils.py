import re
from typing import List

def getImagesLinksInMarkdown(data: str) -> List[str]:
    return re.findall(r'\!\[[^]\(]*]\([^)]+\)', data)
