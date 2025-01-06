# Hacker News Scraper

This Python program scrapes the latest stories from [Hacker News](https://news.ycombinator.com/), filters out stories
with scores greater than 100, and sorts them based on their scores in descending order.

---

## Features:

- Fetches the latest stories from Hacker News.
- Filters stories based on a minimum score threshold (100 points).
- Automatically sorts stories by scores, listing the most popular stories at the top.
- Outputs a clear, structured result in the console.

---

## How it Works:

1. **Fetch Data**: The script retrieves raw HTML from Hacker News using the `requests` library.
2. **Parse Content**: The HTML is parsed using the `BeautifulSoup` library to find relevant elements (story titles,
   links, and scores).
3. **Filter Stories**: Only stories with a score above 100 points are included.
4. **Sort Stories**: The stories are sorted in descending order based on their scores.
5. **Pretty Print Results**: The final result is neatly printed in the console for user readability.

---

## Dependencies:

Before using the script, ensure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`

You can install the libraries via pip:

```bash
pip install requests beautifulsoup4
```

---

## Usage:

1. Clone or download the script to your local machine.
2. Run the script using Python:
   ```bash
   python hacker_news_scraper.py
   ```
3. The script will output the top-scoring stories in your terminal.

---

## Example Output:

Here is an example of what the output might look like:

```python
[{'Title' : 'GPT-4 goes viral' ,
  'href' : 'https://example.com/gpt4' ,
  'Score' : 250} ,
 {'Title' : 'Exploring the Moon' ,
  'href' : 'https://example.com/moon-exploration' ,
  'Score' : 125}]
```

---

## File Structure:

- `hacker_news_scraper.py`: Primary script that contains all logic for fetching, filtering, and displaying data from
  Hacker News.

---

## Limitations:

- The program relies on the structure of Hacker News' HTML. If the website's structure changes, the script would need to
  be updated.
- Only filters stories in the "Top Stories" section of Hacker News.

---

## License:

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Author:

Created by **Hossein Kargar**  
Date: `January 6, 2025`  
Version: 1.0

Feel free to share feedback or improvements!
