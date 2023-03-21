
import csv

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:
with open('resources/MA Database 170323 for upload.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        count = count + 1

        category = row[1]
        # score = row[11]
        ddm_type = row[5]
        internal_name = row[6]
        display_name = row[8]
        summary = row[9]
        description = row[10]
        # Content Type
        content_text = row[11]

        if ddm_type == 'Development':
            page = {"display-name": display_name,
                    "summary-description": summary,
                    "full-description": description,
                    "additional-text": content_text}

            primary_link_1 = row[24]
            primary_link_name_1 = row[22]
            primary_link_paid_free_1 = row[27]
            primary_link_tp_rating_1 = row[32]
            primary_link_tp_link_1 = row[33]

            primary_link_2 = row[39]
            primary_link_name_2 = row[37]
            primary_link_paid_free_2 = row[42]
            primary_link_tp_rating_2 = row[47]
            primary_link_tp_link_2 = row[48]

            primary_link_3 = row[54]
            primary_link_name_3 = row[52]
            primary_link_paid_free_3 = row[57]
            primary_link_tp_rating_3 = row[62]
            primary_link_tp_link_3 = row[63]

            content_pages[internal_name] = page

            # if int(score) == 1:
            #     score = "Bronze"
            # elif int(score) == 2:
            #     score = "Silver"
            # elif int(score) == 3:
            #     score = "Gold"
            #
            # content_pages[internal_name]["tags"] =  category + ", " + score

            content_pages[internal_name]["internal-name"] = internal_name

            content_pages[internal_name]["primary-links"] = "[" + primary_link_name_1 + "]" + \
                                                            "(" + primary_link_1 + ")" + \
                                                            '\n\nOther Providers\n\n' + \
                                                            "[" + primary_link_name_2 + "]" + \
                                                            "(" + primary_link_2 + ")" + \
                                                            '\n\n' + \
                                                            "[" + primary_link_name_3 + "]" + \
                                                            "(" + primary_link_3 + ")"

            def build_primary_link_row (link_name, link, paid_free, tp_rating, tp_link):
                line = ""
                if link_name:
                    line = line + "| [" + link_name + "](" + link + ") | "
                    line = line + paid_free + " | "
                    if tp_rating == "N/A":
                        line = line + tp_rating + "\n"
                    else:
                        line = line + "[" + tp_rating + "](" + tp_link + ") | \n"
                return line


            content_pages[internal_name]["primary-links-table"] = build_primary_link_row(primary_link_name_1,
                                                                                         primary_link_1,
                                                                                         primary_link_paid_free_1,
                                                                                         primary_link_tp_rating_1,
                                                                                         primary_link_tp_link_1) + \
                                                                  build_primary_link_row(primary_link_name_2,
                                                                                         primary_link_2,
                                                                                         primary_link_paid_free_2,
                                                                                         primary_link_tp_rating_2,
                                                                                         primary_link_tp_link_2) + \
                                                                  build_primary_link_row(primary_link_name_3,
                                                                                             primary_link_3,
                                                                                             primary_link_paid_free_3,
                                                                                             primary_link_tp_rating_3,
                                                                                             primary_link_tp_link_3)

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


    # print(page)

    display_name = page['display-name']
    internal_name = page['internal-name']
    name = display_name.strip().replace(" ", "-").replace("?", "") + "-" + internal_name
    filename = "content/ma/" + name.lower() + ".md"

    print("https://www.halixia.com/ma/" + name.lower())

    with open(filename, "w") as md_file:
        md_file.write(template)
    md_file.close()
