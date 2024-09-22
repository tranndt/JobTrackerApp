# Import BS4
from bs4 import BeautifulSoup
import requests
import re

def get_soup(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError('Failed to fetch web page with status code: {}'.format(response.status_code))
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_job_posting(soup):
    company_selector = "div.sub-nav-cta__sub-text-container > a"
    location_selector = "div.sub-nav-cta__sub-text-container > span"
    job_title_selector = "div.sub-nav-cta__text-container > h3.sub-nav-cta__header"
    job_description_selector = "div.description__text > section > div"

    company = soup.select(company_selector)[0].text.strip()
    location = soup.select(location_selector)[0].text.strip()
    job_title = soup.select(job_title_selector)[0].text.strip()
    job_description = "\n".join([child.text for child in soup.select(job_description_selector)[0].children])
    job_description = re.sub(r"\n+", "\n", job_description).strip()

    job_posting_data = {
        "job_title": job_title,
        "company_name": company,
        "location": location,
        "description": job_description
    }
    return job_posting_data

def import_from_url (url):
    try:
        soup = get_soup(url)
        job_posting_data = parse_job_posting(soup)
        return job_posting_data
    except Exception as e:
        return f"Failed to import from url due to {str(e)}"