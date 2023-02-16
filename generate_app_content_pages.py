
import csv

content_pages = {}
with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
        , newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        internal_name = row[15]
        display_name = row[16]
        summary = row[18]
        description = row[20]
        content_text = row[22]
        cta_url_1 = row[57]
        cta_url_2 = row[72]
        cta_url_3 = row[87]

        page = {"display-name": display_name,
                "summary-description": summary,
                "full-description": description,
                "additional-text": content_text,
                "primary-link": cta_url_1,
                "additional-providers": cta_url_2 + '\n' + cta_url_3}

        content_pages[internal_name] = page


with open('resources/content-template.md','r') as file:
    template = file.read()

for k,page in content_pages.items():
    template = ""
    with open('resources/content-template.md', 'r') as file:
        template = file.read()

    filename = ""
    for k, v in page.items():
        template = template.replace("*" + k + "*", v)
        if k == "display-name":
            filename = "content/ma/" + v.lower().strip().replace(" ", "_").replace("/", "_") + ".md"

    with open(filename, "w") as md_file:
        md_file.write(template)
    md_file.close()
