"""Get all the content from the website."""


import requests
from bs4 import BeautifulSoup
from typing import Union


def get_content_from_url(website_link: str) -> Union[BeautifulSoup, None]:
    """Get all the content from the website.

    Args:
        website_link (str): website link to get content

    Raises:
        StatusCodeError: Error for invalid status code

    Returns:
        BeautifulSoup | None: Content from the link
    """
    try:
        response = requests.get(website_link, timeout=10)
        content_from_url = BeautifulSoup(response.content, "html.parser")
        if content_from_url is not None:
            return content_from_url
    except requests.ConnectionError:
        print(
            f"\nThe site : {website_link}" " can't be unreachable",
        )
    except requests.HTTPError:
        print(
            f"\nInvalid response from : {website_link}" "please verify it.",
        )
    except ValueError as value_error:
        print(value_error)
    else:
        print(f"\nCretrived contents from{website_link}")
    return None
