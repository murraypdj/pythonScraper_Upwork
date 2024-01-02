# Company Details Scraper

## Overview

This project was initiated in response to a client's request posted on the UpWork job board. The objective was to create a script that could gather information on all the firms listed in the American Institute of Architects, including their contact details, and store the data in an Excel file.

## Problem Encountered

Initially, I attempted to achieve this task using Beautiful Soup 4. However, an issue surfaced after scraping the sixth page, leading to duplicated content on all subsequent pages. A thorough code review revealed no errors in the scraping logic. To investigate further, I examined the page source and discovered a JSON containing the required data.

## Solution

To address the issue, I pivoted the approach and focused on parsing the JSON data from the page source. I utilized Python's pandas library to efficiently handle and structure the data, subsequently saving it to an Excel file.

## Project Highlights

- Efficient data gathering from the American Institute of Architects website.
- Identification and resolution of a scraping issue through source code inspection.
- Implementation of data parsing using the pandas library.
- Storage of the collected data in an Excel file for easy access and analysis.
