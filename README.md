# LinkedInJobCleaner

## About
This script automates the deletion of archived jobs from a LinkedIn profile using Selenium WebDriver to interact with the LinkedIn website, mimicking the manual process of deleting each archived job listing.
LinkedIn does not provide you with the option of removing multiple archived or saved jobs. This script will save your time, especially if you are not being able to add any more jobs.

## Prerequisites
- Python 3.6 or newer
- Selenium WebDriver
- ChromeDriver (matching your Chrome browser version)
- `webdriver_manager` Python package

## Installation
1. Ensure Python 3.6+ is installed on your system.
2. Install the necessary Python packages:
   ```cmd
   pip install selenium webdriver_manager

## Usage
1. Clone this repository or download the script to your machine.  
2. Set your LinkedIn credentials as environment variables:  
- **For Windows:**  
   ```cmd
   set LINKEDIN_USERNAME=your_email@example.com
   set LINKEDIN_PASSWORD=your_password
- **For macOS/Linux:**  
   ```cmd
   export LINKEDIN_USERNAME="your_email@example.com"
   export LINKEDIN_PASSWORD="your_password"
3. Run the script:
   ```cmd
   python purger.py
