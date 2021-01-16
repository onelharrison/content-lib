from dataclasses import dataclass
from typing import Optional


@dataclass
class MediumStory:
    title: str
    description: str
    body: str
    published_at: int
    featured_image_url: Optional[str] = None
    views_30days: int
    reads_30days: int
    fans_30days: int
    top_comment_author: Optional[str] = None
    top_comment_body: Optional[str] = None
    updated_at: int


story = {
    "title": "Improving Code Quality in Python Codebases",
    "description": "...",
    "body": "...",
    "published_at": 1608346617,
    "image": {
        "image_url_medium": "https://cdn.images.site/medium.png",
        "image_url_small": "https://cdn.images.site/small.png",
    },
    "stats": {
        "views_30days": 30,
        "reads_30days": 28,
        "fans_30days": 10,
    },
    "top_comments": [
        {"author": "@alanajones", "body": "..."},
        {"author": "@jacksparrow", "body": "..."},
        {"author": "@peterwest", "body": "..."},
    ],
}
