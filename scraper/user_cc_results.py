from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Step 1: Open website page in browser using selenium
driver = webdriver.Chrome()
num_pages = 1
card_list = []

for i in range(1, num_pages + 1):
    try:
        driver.get(
            f"https://helpmebuildcredit.com/user-cc-results/?card_id=&sort=&bank=&state=&bureau=&paged={i}&quickFilter="
        )

        # Step 3: Wait for API response and main content to load
        wait = WebDriverWait(driver, 10)
        main_content = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="d-recent-card"]'))
        )

        # Step 4: Extract necessary information from HTML content using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        data = soup.find_all("div", class_ = "d-recent-card")

        for card_item in data:
            div_title = card_item.find("div", class_ = "recent-card-title")
            if div_title is not None:
                a_tag = div_title.find("a")

                if a_tag is not None:
                    card_title = a_tag.text.strip()
                else:
                    card_title = "NaN"
            else:
                card_title = "NaN"

            div_views = card_item.find("div", class_ = "recent-card-views")
            if div_views is not None:
                card_views = int(div_views.text.strip())
            else:
                card_views = 0

            div_link_btn = card_item.find("div", class_ = "recent-card-button")
            if div_link_btn is not None:
                a_tag = div_link_btn.find("a")

                if a_tag is not None:
                    card_link = a_tag['href']
                else:
                    card_link = "NaN"
            else:
                card_link = "NaN"

            div_image = card_item.find("div", class_ = "recent-card-image")
            if div_image is not None:
                img_tag = div_image.find("img")

                if img_tag is not None:
                    card_image = img_tag['src']
                else:
                    card_image = "NaN"
            else:
                card_image = "NaN"

            div_status = card_item.find("div", class_ = "status")
            if div_status is not None:
                card_status = div_status.find("div")['class'][0]
            else:
                card_status = "NaN"

            div_limit = card_item.find("div", class_ = "limit")
            if div_limit is not None:
                span_tag = div_limit.find("span", class_ = "value")

                if span_tag is not None:
                    card_limit = span_tag.text.strip()
                else:
                    card_limit = "N/A"
            else:
                card_limit = "N/A"

            div_score = card_item.find("div", class_ = "score")
            if div_score is not None:
                span_tag = div_score.find("span", class_ = "value")

                if span_tag is not None:
                    card_score = int(span_tag.text.strip())
                else:
                    card_score = "N/A"
            else:
                card_score = "N/A"

            div_annual_income = card_item.find("div", class_ = "annual_income")
            if div_annual_income is not None:
                span_tag = div_annual_income.find("span", class_ = "value")

                if span_tag is not None:
                    card_annual_income = span_tag.text.strip()
                else:
                    card_annual_income = "N/A"
            else:
                card_annual_income = "N/A"

            div_card_info_col = card_item.select("div.card-info-col:not(.fist-info):not(.second-card-info)")[0]
            
            div_applied_from = div_card_info_col.find("div", class_ = "bureau")
            if div_applied_from is not None:
                span_tag = div_applied_from.find("span", class_ = "value")

                if span_tag is not None:
                    card_applied_from = span_tag.text.strip()
                else:
                    card_applied_from = "N/A"
            else:
                card_applied_from = "N/A"

            div_card_second_info_col = card_item.find("div", class_ = "second-card-info")

            div_bureau = div_card_second_info_col.find("div", class_ = "bureau")
            if div_bureau is not None:
                span_tag = div_bureau.find("span", class_ = "value")

                if span_tag is not None:
                    card_bureau = span_tag.text.strip()
                else:
                    card_bureau = "N/A"
            else:
                card_bureau = "N/A"

            div_age = div_card_second_info_col.find("div", class_ = "age")
            if div_age is not None:
                span_tag = div_age.find("span", class_ = "value")

                if span_tag is not None:
                    card_age = span_tag.text.strip()
                else:
                    card_age = "N/A"
            else:
                card_age = "N/A"

            div_notes = card_item.find("div", class_ = "card-notes")
            if div_notes is not None:
                span_tag = div_notes.find('span')

                if span_tag is not None:
                    card_notes = span_tag.text
                else:
                    card_notes = "NaN"
            else:
                card_notes = "NaN"

            div_author_name =  card_item.find("a", class_ = "user-submitted")
            if div_author_name is not None:
                card_author_name = div_author_name.text
            else:
                card_author_name = "NaN"

            div_meta_date =  card_item.find("div", class_ = "card-meta-date")
            if div_meta_date is not None:
                card_meta_date = div_meta_date.text
            else:
                card_meta_date = "NaN"

            div_dislike = card_item.find("div", class_ = "card-dislike")
            if div_dislike is not None:
                span_tag = div_dislike.find("span")

                if span_tag is not None:
                    card_dislike = int(span_tag.text)
                else:
                    card_dislike = 0
            else:
                card_dislike = 0

            div_like = card_item.find("div", class_ = "card-like")
            if div_like is not None:
                span_tag = div_like.find("span")

                if span_tag is not None:
                    card_like = int(span_tag.text)
                else:
                    card_like = 0
            else:
                card_like = 0

            card_list.append(
                {
                    "card_title": card_title,
                    "card_reviews": card_views,
                    "card_link": card_link,
                    "card_image": card_image,
                    "card_status": card_status,
                    "card_limit": card_limit,
                    "card_score": card_score,
                    "card_annual_income": card_annual_income,
                    "card_applied_from": card_applied_from,
                    "card_bureau": card_bureau,
                    "card_age": card_age,
                    "card_notes": card_notes,
                    "card_author_name": card_author_name,
                    "card_meta_date": card_meta_date,
                    "card_dislike": card_dislike,
                    "card_like": card_like
                }
            )
    except Exception as e:
        print(f"Error occurred while scraping page {i}: {e}")

# open a new CSV file in write mode
with open('user_cc_results_output.csv', mode='w') as file:
    # get the fieldnames from the first dictionary in the list
    fieldnames = card_list[0].keys()

    # create a CSV writer object with the fieldnames
    writer = csv.DictWriter(file, fieldnames)

    # write the header row to the CSV file
    writer.writeheader()

    # write the data rows to the CSV file
    for row in card_list:
        writer.writerow(row)
# # Close browser window
driver.quit()
