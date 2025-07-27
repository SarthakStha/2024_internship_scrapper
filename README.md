# 2024_internship_scrapper
A script that scrapes archived summer internship postings from GitHub and creates word clouds to visualize the most common skills and requirements.

## What it does

- Scrapes internship postings from SimplifyJobs GitHub repository ([link](https://github.com/SimplifyJobs/Summer2026-Internships/blob/dev/archived/README-2024.md))
- Processes the text to find common words and skills
- Creates a visual word cloud showing trending requirements

## Files
- **scrape.py** - Downloads internship data from GitHub and stores it as a CSV
 - **analysis.py** - Filters the data and creates the word cloud visualization
 - **requirements.txt** - Lists all the dependencies of the project
 - **data/** - Folder where scraped data is saved
 - **visuals/** - Folder where word cloud images are saved

## Setup

1. **Install Python packages:**
```bash
pip install -r requirements.txt
```

## Results
![preview](https://github.com/SarthakStha/2024_internship_scrapper/blob/main/visuals/summer_2024_word_cloud.png)
