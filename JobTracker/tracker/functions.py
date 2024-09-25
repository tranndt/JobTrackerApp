# Import BS4
from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time

def fetch_html_using_requests(url):
    HEADERS = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Connection": "keep-alive",
        # "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
    }
    response = requests.get(url, headers=HEADERS)
    return response.status_code, response.text


def fetch_html_using_webdriver(url):
    """
    Scrapes the given URL using Edge WebDriver and returns the HTML content as a string.

    :param url: The URL of the page to scrape.
    :return: The HTML content of the page as a string.
    """
    # Set Up WebDriver
    edge_options = Options()
    edge_options.add_argument("--disable-popup-blocking")  # Enable popups

    # Initialize EdgeDriver
    driver_path = '/usr/local/bin/msedgedriver'
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        # Navigate to the Page
        driver.get(url)

        # Handle Popups (if any)
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        # Wait for the page to load completely
        time.sleep(5)

        # Extract Content and Status Code
        html_content = driver.page_source
        return html_content
    finally:
        # Close the browser
        driver.quit()

def fetch_html(url):
    """
    Fetches the HTML content of the given URL using Requests or WebDriver.

    :param url: The URL of the page to scrape.
    :return: The HTML content of the page as a string.
    """
    short_url = url[:25] + "..." + url[-25:] if len(url) > 50 else url
    try:
        # Try fetching using Requests
        status_code, html_content = fetch_html_using_requests(url)
        if status_code == 200:
            print(f"Fetched HTML {short_url} using Requests")
            return html_content
    except Exception as e:
        print(f"Failed to fetch HTML {short_url} using Requests due to: {e}")

    try:
        # Try fetching using WebDriver
        html_content = fetch_html_using_webdriver(url)
        print(f"Fetched HTML {short_url} using WebDriver")
        return html_content
    except Exception as e:
        print(f"Failed to fetch HTML {short_url} using WebDriver due to: {e}")

    # Return None if both methods fail
    return None

def to_bs4(html_content):
    """
    Converts the given HTML content into a BeautifulSoup object.

    :param html_content: The HTML content to parse.
    :return: BeautifulSoup object.
    """
    return BeautifulSoup(html_content, "html.parser")

def parse_job_posting_linkedin(html:str):
    soup = to_bs4(html)
    company_selector = "div.sub-nav-cta__sub-text-container > a"
    loaction_selector = "div.sub-nav-cta__sub-text-container > span"
    job_title_selector = "div.sub-nav-cta__text-container > h3.sub-nav-cta__header"
    # job_description_selector = "div.description__text > section > div"
    job_description_selector = "div#job-details"

    company = soup.select(company_selector)[0].text.strip()
    location = soup.select(loaction_selector)[0].text.strip()
    job_title = soup.select(job_title_selector)[0].text.strip()
    # job_description = "\n".join([child.text for child in soup.select(job_description_selector)[0].children])
    # job_description = re.sub(r"\n+", "\n", job_description).strip()
    job_description = soup.select(job_description_selector)[0].prettify()

    job_posting_data = {
        "job_title": job_title,
        "company_name": company,
        "location": location,
        "description": job_description
    }
    return job_posting_data

def parse_job_posting_indeed(html:str):
    soup = to_bs4(html)
    company_selector = "div[data-testid='inlineHeader-companyName']"
    loaction_selector = "div[data-testid='inlineHeader-companyLocation']"
    job_title_selector = "h1[data-testid='jobsearch-JobInfoHeader-title']"
    job_description_selector = "div#jobDescriptionText"

    company = soup.select(company_selector)[0].text.strip()
    location = soup.select(loaction_selector)[0].text.strip()
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
        html_content = fetch_html(url)
        if "linkedin" in url:
            job_posting_data = parse_job_posting_linkedin(html_content)
        elif "indeed" in url:
            job_posting_data = parse_job_posting_indeed(html_content)
        else:
            raise ValueError("Unsupported job posting URL")
        return job_posting_data
    except Exception as e:
        return f"Failed to import from url due to {str(e)}"