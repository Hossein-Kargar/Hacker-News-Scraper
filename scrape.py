"""
Hacker News Scraper
===================

This script fetches the latest stories from Hacker News (https://news.ycombinator.com/),
applies filtering based on their score (greater than 100), and then sorts the resulting
top stories based on their scores in descending order.

Author: Hossein Kargar
Date: January 6, 2025
Version: 1.0
License: MIT
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Extracted constant
HN_URL = "https://news.ycombinator.com/"


def fetch_hacker_news_data(url):
    """
    Fetches HTML content from the given URL and parses it using BeautifulSoup.

    This function sends a GET request to the specified URL, retrieves the raw HTML
    response, and parses it into a BeautifulSoup object for further processing.

    :param url: URL to fetch HTML content from
    :type url: str
    :return: Parsed HTML content as a BeautifulSoup object
    :rtype: bs4.BeautifulSoup
    :raises requests.exceptions.RequestException: If the GET request fails due
        to network issues or invalid URLs.
    """
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def extract_score(subtext_item):
    """
    Extracts the score from a given subtext item.

    This function parses the provided subtext item for a score value associated
    with it. If a score is present, it is extracted, cleaned of additional text
    (e.g., "points"), and converted to an integer. If no score is found, it
    returns a default value of 0.

    :param subtext_item: A BeautifulSoup tag object representing the subtext
        section of an HTML element. It is expected that the subtext contains
        a score represented as text.
    :type subtext_item: bs4.element.Tag

    :return: The numeric value representing the score found in the subtext,
        or 0 if no score is available.
    :rtype: int
    """
    vote = subtext_item.select(".score")
    return int(vote[0].getText().replace(" points", "")) if vote else 0


def create_story(link, subtext_item):
    """
    Extracts story details such as title, hyperlink, and score from provided HTML elements.

    This function processes an HTML element `link` for the story title and hyperlink,
    and a corresponding `subtext_item` for extracting the score. If the score is greater
    than 100, it returns a dictionary with the extracted data; otherwise, it returns None.

    :param link: The HTML element containing the story's title and hyperlink.
    :type link: bs4.element.Tag
    :param subtext_item: The HTML element containing the story's score data.
    :type subtext_item: bs4.element.Tag
    :return: A dictionary with the story's details (title, hyperlink, and score)
        if the score exceeds 100, otherwise None.
    :rtype: dict[str, Union[str, int]] | None
    """
    a_tag = link.find("a")
    if a_tag and a_tag.get("href"):
        title = a_tag.getText()
        score = extract_score(subtext_item)
        return (
            {"Title": title, "href": a_tag["href"], "Score": score}
            if score > 100
            else None
        )


def create_custom_hn(links, subtext):
    """
    Filters and sorts Hacker News (HN) stories based on their scores and links. Only the
    stories that meet specific criteria, such as sufficient score and valid data,
    are included in the final list of stories. Returns the sorted list of stories
    based on their vote counts.

    :param links: List of story URLs or identifiers from the HN source.
    :type links: list
    :param subtext: List of associated metadata such as scores and comments for
        each link in the same order as links.
    :type subtext: list
    :return: A list of filtered and sorted stories based on votes.
    :rtype: list
    """
    filtered_stories = []
    for index, link in enumerate(links):
        story = create_story(link, subtext[index])
        if story:  # Filter out stories with insufficient score or missing link
            filtered_stories.append(story)
    return sort_stories_by_votes(filtered_stories)


def sort_stories_by_votes(stories):
    """
    Sorts a list of stories based on their vote counts in descending order.

    This function takes a list of stories, each represented as a dictionary with a
    "Score" key, and returns a new list where the stories are sorted from the
    highest to the lowest score.

    :param stories: A list of dictionaries, where each dictionary represents a
        story and must have a "Score" key.
    :type stories: list[dict]
    :return: A list of stories sorted by their "Score" key in descending order.
    :rtype: list[dict]
    """
    return sorted(stories, key=lambda story: story["Score"], reverse=True)


# Main logic
soup = fetch_hacker_news_data(HN_URL)
links = soup.select(".titleline")
subtext = soup.select(".subtext")
pprint(create_custom_hn(links, subtext))
