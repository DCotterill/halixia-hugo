
import csv

content_pages = {}
count = 0
with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
        , newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        count = count + 1

        category = row[10]
        score = row[11]
        ddm_type = row[12]
        internal_name = row[15]
        display_name = row[16]
        summary = row[18]
        description = row[20]
        content_text = row[22]

        page = {"display-name": display_name,
                "summary-description": summary,
                "full-description": description,
                "additional-text": content_text}

        primary_link_1 = row[57]
        primary_link_2 = row[72]
        primary_link_3 = row[87]

        content_pages[internal_name] = page

        if int(score) == 1:
            score = "Bronze"
        elif int(score) == 2:
            score = "Silver"
        elif int(score) == 3:
            score = "Gold"

        content_pages[internal_name]["tags"] =  category + ", " + score

        content_pages[internal_name]["primary-links"] = primary_link_1 + '\n\n' + \
                                                        primary_link_2 + '\n\n' +\
                                                        primary_link_3

        row = next(reader)

        additional_url_1 = row[57]
        additional_url_2 = row[72]

        content_pages[internal_name]["additional-providers"] = additional_url_1 + '\n\n' + additional_url_2

print(content_pages)

with open('resources/content-template.md','r') as file:
    template = file.read()

for k, page in content_pages.items():
    template = ""
    with open('resources/content-template.md', 'r') as file:
        template = file.read()

    filename = ""
    for k, v in page.items():
        template = template.replace("*" + k + "*", v)
        if k == "display-name":
            filename = "content/ma/" + v.lower().strip().replace(" ", "_").replace("/", "_") + ".md"

            print("https://www.halixia.com/ma/" + v.lower().strip().replace(" ", "_").replace("/", "_"))

    with open(filename, "w") as md_file:
        md_file.write(template)
    md_file.close()
