"""Get all links from the website Content."""


from bs4 import BeautifulSoup


def get_all_links_in_the_page(website_content: BeautifulSoup) -> list[str]:
    """Get all the links in the website content.

    Args:
        website_content (BeautifulSoup): Website content to get links

    Returns:
        list[str]: list of links in the website
    """
    links = []
    for anchor_tag in website_content.find_all("a"):
        link = anchor_tag.get("href")
        if link is not None:
            if link.startswith("http"):
                links.append(link)
    return links
