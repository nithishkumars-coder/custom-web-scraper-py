"""Write data in file."""

import re
from bs4 import BeautifulSoup


def write_content_in_file(file_name: str, content: BeautifulSoup) -> None:
    """Write data in file.

    Args:
        file_name (str): file name to write content
        content (_type_): content to be written
    """
    with open(file_name, "a", encoding="utf-8") as file:
        try:
            website_content = re.sub("\n+", "\n", content.text)
            file.write(website_content)
            file.write("\n\n\n\n\n")
            splitter = "*" * 75
            file.write("".join([splitter, "Next Page content", splitter]))
        except IOError:
            print("Error in writting content to the file,Please verify it.")
