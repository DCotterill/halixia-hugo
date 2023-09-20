
import csv
import requests

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:

f = open('resources/url-errors-18-09-23.csv', 'a')
f_whitelist = open('resources/url-whitelist.csv')

whitelist_urls = []
whitelist_reader = csv.reader(f_whitelist, delimiter=',')
for whitelist_url in whitelist_reader:
    whitelist_urls.append(whitelist_url)

writer = csv.writer(f)
links = []

def is_whitelisted(link):
    for url in whitelist_urls:
        # print(url[0])
        if link.startswith(url[0]):
            return True
    return False

def test_url(internal_name, link):
    if link and link not in links:
        links.append(link)
        if is_whitelisted(link):
            print("Whitelist:" + link)
        else:
            # print("Testing:" + link)
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
                request = requests.get(link, timeout=10, headers = headers)
                if request.status_code != 200:
                    print("Error:" + link + ":" + request.status_code)
                    writer.writerow([link, request.status_code])
            except:
                print("Error:" + link )
                writer.writerow([internal_name, link, "Error"])

with open('resources/MA Database 220523.xlsx - Upload Prep-v11.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        print (count)
        category = row[1]
        # score = row[11]
        ddm_type = row[5]
        internal_name = row[6]
        display_name = row[8]
        summary = row[9]
        description = row[10]
        # Content Type
        content_text = row[11]

        primary_link_1 = row[20]
        primary_link_2 = row[28]
        primary_link_3 = row[43]
        primary_link_4 = row[58]
        primary_link_5 = row[73]
        # if count < 500:
        if count >= 500:
            test_url(internal_name, primary_link_1)
            test_url(internal_name, primary_link_2)
            test_url(internal_name, primary_link_3)
            test_url(internal_name, primary_link_4)
            test_url(internal_name, primary_link_5)

        count = count + 1

        f.flush()

# close the file
f.close()
