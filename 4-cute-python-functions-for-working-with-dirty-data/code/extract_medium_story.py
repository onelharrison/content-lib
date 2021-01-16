import time

from dig import dig


def extract_medium_story(story):
    medium_story = MediumStory()
    medium_story.title = story["title"]
    medium_story.description = story["description"]
    medium_story.body = story["body"]
    medium_story.published_at = story["published_at"]

    # notice in the example data that
    # image_url_large is missing
    medium_story.featured_image_url = coalesce(
        dig(story, "image", "image_url_large"),
        dig(story, "image", "image_url_medium"),
        dig(story, "image", "image_url_small"),
    )
    medium_story.views_30days = dig(story, "stats", "views_30days")
    medium_story.reads_30days = dig(story, "stats", "reads_30days")
    medium_story.fans_30days = dig(story, "stats", "fans_30days")

    medium_story.top_comment_author = dig(story, "top_comments", 0, "author")
    medium_story.top_comment_body = dig(story, "top_comments", 0, "body")
    medium_story.updated_at = int(time.time())
    return medium_story


extract_medium_story(story)
