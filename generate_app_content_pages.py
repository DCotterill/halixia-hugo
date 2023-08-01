
import csv

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:
with open('resources/MA Database 220523.xlsx - Upload Prep -v7.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        # print(row)
        count = count + 1

        category = row[1]
        # score = row[11]
        ddm_type = row[5]
        #Topic col 6, Mot col 7
        internal_name = row[8]
        display_name = row[10]
        summary = row[11]
        description = row[12]
        # Content Type
        content_text = row[13]

        print (ddm_type)
        if ddm_type == 'Development':
            page = {"display-name": display_name,
                    "summary-description": summary,
                    "full-description": description,
                    "additional-text": content_text}

            primary_link_1 = row[28]
            primary_link_name_1 = row[26]
            primary_link_paid_free_1 = row[31]
            primary_link_tp_rating_1 = row[36]
            primary_link_tp_link_1 = row[37]

            primary_link_2 = row[43]
            primary_link_name_2 = row[41]
            primary_link_paid_free_2 = row[46]
            primary_link_tp_rating_2 = row[51]
            primary_link_tp_link_2 = row[52]

            primary_link_3 = row[58]
            primary_link_name_3 = row[56]
            primary_link_paid_free_3 = row[61]
            primary_link_tp_rating_3 = row[66]
            primary_link_tp_link_3 = row[67]

            primary_link_4 = row[73]
            primary_link_name_4 = row[71]
            primary_link_paid_free_4 = row[76]
            primary_link_tp_rating_4 = row[81]
            primary_link_tp_link_4 = row[82]

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

            content_pages[internal_name]["primary-links"] = "[**" + primary_link_name_1 + "**]" + \
                                                            "(" + primary_link_1 + ")" + \
                                                            '\n\nOther Providers\n\n' + \
                                                            "[**" + primary_link_name_2 + "**]" + \
                                                            "(" + primary_link_2 + ")" + \
                                                            '\n\n' + \
                                                            "[**" + primary_link_name_3 + "**]" + \
                                                            "(" + primary_link_3 + ")" \
                                                            '\n\n' + \
                                                            "[**" + primary_link_name_4 + "**]" + \
                                                            "(" + primary_link_4 + ")"


            def build_primary_link_row (link_name, link, paid_free, tp_rating, tp_link):
                line = ""
                if link_name:
                    line = line + "| [**" + link_name + "**](" + link + ") | "
                    line = line + paid_free + " | \n"
                    # if tp_rating == "N/A":
                    #     line = line + tp_rating + "\n"
                    # else:
                    #     line = line + "[" + tp_rating + "](" + tp_link + ") | \n"
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
                                                                                         primary_link_tp_link_3) + \
                                                                  build_primary_link_row(primary_link_name_4,
                                                                                         primary_link_4,
                                                                                         primary_link_paid_free_4,
                                                                                         primary_link_tp_rating_4,
                                                                                         primary_link_tp_link_4)

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


    print(page)

    display_name = page['display-name']
    internal_name = page['internal-name']
    name = display_name.strip().replace(" ", "-").replace("?", "").replace("&", "and")\
               .replace("'", "").replace("’", "").replace("!", "") \
           + "-" + internal_name
    filename = "content/ma/" + name.lower() + ".md"

    print("https://www.halixia.com/ma/" + name.lower())

    with open(filename, "w") as md_file:
        md_file.write(template)
    md_file.close()
