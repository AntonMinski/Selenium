import csv
import os.path

from flashtext.keyword import KeywordProcessor

from match_dict import arr_fin, specs_dict, specs_dict_list
from match_dict import cpu_s_list

print('\n' * 2)



with open("result.csv") as r_file:

    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter=",")

    count = 0
    desc_list = []
    link_list = []
    price_sum_list = []
    price_UAH_list = []
    title_list = []

    for row in file_reader:
        if row != []:
            if len(row) == 5:
                price_sum = float(row[2]) + float(row[3])
                price_UAH = (price_sum + 20) * 27.5 * 1.3
                price_sum_list.append(price_sum)
                price_UAH_list.append(price_UAH)
                title_list.append(row[1])
                link = row[0]
                full_desc = row[1] + row[4]
                link_list.append(link)
                desc_list.append(full_desc)



def refine_list(start_array, target_list):
    fin_array = []
    for current_text in start_array:
        for arrays in target_list:
            for el in arrays:
                if el in current_text:
                    new_key = el + ' '
                    current_text = current_text.replace(el, new_key)
        fin_array.append(current_text)

    return fin_array

refined_desc_list = refine_list(desc_list, cpu_s_list)
# print(refined_list[1])



keyword_processor = KeywordProcessor(case_sensitive=False)

# for key in arr_fin:
#     keyword_processor.add_keywords_from_list(key)

for dict_cur in specs_dict_list:
    # print(dict_cur)
    keyword_processor.add_keywords_from_dict(dict_cur)

kw_fin_array = []
for key, value in enumerate(refined_desc_list):

    # print(key, value)
    keywords_found = keyword_processor.extract_keywords(value)
    kw_set = set(keywords_found)
    kw_fin_array.append(list(kw_set))
    print(keywords_found, link_list[key])

# print(kw_fin_array)

print('\n' * 2)

for number, arr in enumerate(kw_fin_array):
    price = 0
    for el in arr:
        for key, value in specs_dict.items():
            if el == key:
                price = price + value
                print(el, price, arr)
    print(price, link_list[number], price_UAH_list[number])

        # print(price)
        # print


























