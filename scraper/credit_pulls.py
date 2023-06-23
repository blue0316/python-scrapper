from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# cp = CreditPulls

# Step 1: Open website page in browser using selenium
driver = webdriver.Chrome()
num_pages = 344
cp_list = []

for i in range(1, num_pages + 1):
    try:
        driver.get(f"https://creditboards.com/forums/index.php?/creditpulls/page/{i}/&d=5")

        # Step 3: Wait for API response and main content to load
        wait = WebDriverWait(driver, 10)
        main_content = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ipsDataItem_responsivePhoto"))
        )

        # Step 4: Extract necessary information from HTML content using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        data = soup.find_all("li", class_="ipsDataItem_responsivePhoto")

        for cp_item in data:
            h4_title = cp_item.find("h4", class_="ipsDataItem_title")
            if h4_title is not None:
                a_tag = h4_title.find("a")

                if a_tag is not None:
                    cp_title = a_tag.text.strip()
                    cp_link = a_tag["href"]
                else:
                    cp_title = "NaN"
                    cp_link = "NaN"
            else:
                cp_title = "NaN"
                cp_link = "NaN"

            span_views = cp_item.find("span", class_="ipsDataItem_stats_number")
            if span_views is not None:
                cp_views = int(span_views.text.strip())
            else:
                cp_views = 0

            label_consumer_state = cp_item.find("strong", string = "Consumer State:")
            if label_consumer_state is not None:
                cp_consumer_state = label_consumer_state.next_sibling.strip()
            else:
                cp_consumer_state = "NaN"

            label_consumer_zip = cp_item.find("strong", string = "Consumer Zip:")
            if label_consumer_zip is not None:
                cp_consumer_zip = label_consumer_zip.next_sibling.strip()
            else:
                cp_consumer_zip = "NaN"

            label_cra = cp_item.find("strong", string = "CRA:")
            if label_cra is not None:
                cp_cra = label_cra.next_sibling.strip()
            else:
                cp_cra = "NaN"

            label_applied_data = cp_item.find("strong", string = "Date Applied:")
            if label_applied_data is not None:
                cp_applied_data = label_applied_data.next_sibling.strip()
            else:
                cp_applied_data = "NaN"

            label_approved = cp_item.find("strong", string = "Approved:")
            if label_approved is not None:
                cp_approved = label_approved.next_sibling.strip()
            else:
                cp_approved = "NaN"

            label_score = cp_item.find("strong", string = "Score:")
            if label_score is not None:
                cp_score = int(label_score.next_sibling.strip())
            else:
                cp_score = "NaN"

            label_credit_limit = cp_item.find("strong", string = "Credit Limit:")
            if label_credit_limit is not None:
                cp_credit_limit = int(label_credit_limit.next_sibling.strip())
            else:
                cp_credit_limit = "NaN"

            label_comments = cp_item.find("strong", string = "Comments:")
            if label_comments is not None:
                cp_comments = label_comments.next_sibling.strip()
            else:
                cp_comments = "NaN"

            cp_list.append(
                {
                    "cp_title": cp_title,
                    "cp_link": cp_link,
                    "cp_consumer_state": cp_consumer_state,
                    "cp_consumer_zip": cp_consumer_zip,
                    "cp_cra": cp_cra,
                    "cp_applied_data": cp_applied_data,
                    "cp_approved": cp_approved,
                    "cp_score": cp_score,
                    "cp_credit_limit": cp_credit_limit,
                    "cp_comments": cp_comments,
                    "cp_views": cp_views,
                }
            )

    except Exception as e:
        print(f"Error occurred while scraping page {i}: {e}")

# open a new CSV file in write mode
with open('credit_pulls_output.csv', mode='w', encoding='utf-8') as file:
    # get the fieldnames from the first dictionary in the list
    fieldnames = cp_list[0].keys()

    # create a CSV writer object with the fieldnames
    writer = csv.DictWriter(file, fieldnames)

    # write the header row to the CSV file
    writer.writeheader()

    # write the data rows to the CSV file
    for row in cp_list:
        writer.writerow(row)
# # Close browser window
driver.quit()

