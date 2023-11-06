"""Web Scraper with no Exceptions."""

from get_all_links_in_the_page import get_all_links_in_the_page  # type: ignore
from get_content_from_url import get_content_from_url  # type: ignore
from write_content_in_file import write_content_in_file  # type: ignore


input_site_link = input("Enter website link to scrap : ")
input_file_name = input("Enter file name to write content : ")
website_content = get_content_from_url(input_site_link)
if website_content is not None:
    write_content_in_file(input_file_name, website_content)
    links_in_the_website = get_all_links_in_the_page(website_content)
    for link in links_in_the_website:
        content_from_url = get_content_from_url(link)
        if content_from_url is not None:
            write_content_in_file(input_file_name, content_from_url)
