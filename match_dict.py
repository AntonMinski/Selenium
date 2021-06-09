def add_similar(target_dict, old_key, new_key_list):
    new_dict = target_dict.copy()
    for key, value in target_dict.items():
        for new_key in new_key_list:
            key_to_add = key.replace(old_key, new_key)
            new_dict.update({key_to_add: value})
    return new_dict

def common_lst(target_key, old_key, new_key_list):
    # new_dict = target_dict.copy()
    common_list = []
    for new_key in new_key_list:
        changed_key = target_key.replace(old_key, new_key)
        common_list.append(changed_key)
    return common_list

def common_dct(target_key, old_key, new_key_list):
    # new_dict = target_dict.copy()
    common_dict = {}
    common_list = []
    for new_key in new_key_list:
        changed_key = target_key.replace(old_key, new_key)
        common_list.append(changed_key)
        print(common_list)
    common_dict.update({target_key: common_list})
    print(common_dict)
    return common_dict

# def common_dict_kwarg(target_key, **kwargs):
#     # new_dict = target_dict.copy()
#     for i in kwargs:
#         key = i.key
#         value = i.value
#     common_dict = {}
#     common_list = []
#     for new_key in new_key_list:
#         changed_key = target_key.replace(old_key, new_key)
#         common_list.append(changed_key)
#         print(common_list)
#     common_dict.update({target_key: common_list})
#     print(common_dict)
#     return common_dict

##################################         #################

def common_dict_kwarg(target_key, dict):
    common_dict = {}
    common_list = []
    for old_key, values in dict.items():
        for new_key in values:
            changed_key = target_key.replace(old_key, new_key)
            common_list.append(changed_key)
    common_set = set(common_list)
    common_list_upd = list(common_set)
    common_dict.update({target_key: common_list_upd})
    return common_dict


def common_dict(dict_to_process, dict_to_replace):
    final_dict = {}
    for key in dict_to_process:
        temp_dict = common_dict_kwarg(target_key=key, dict=dict_to_replace)
        final_dict.update(temp_dict)
    final_list = []
    for key1, value1 in final_dict.items():
        value1.insert(0, key1)
        print(value1)
        final_list.append(value1)
    return final_list































def start_kwarg_dict(start_dict, kw_dict):
    start_list = []
    for start_key in start_dict.keys():
        arr1 = [start_key]
        start_list.append(arr1)

    fin_array = []
    fin_dict = {}
    for elements in start_list:
        new_array = elements.copy()  # [a1, a2
        for element in elements:  # [a1]
            for key, values_list in kw_dict.items():  # r.key : [r.values]
                for value in values_list:   # r.key : r.value
                    new_key = element.replace(key, value)   # a1_
                    if new_key not in new_array:
                        new_array.append(new_key)

            elements = new_array.copy()
        fin_array.append(new_array)
        fin_dict.update({elements[0]: new_array})


    return fin_array

def kwarg_dict(start_list, kw_dict):
    fin_array = []
    fin_dict = {}

    for elements in start_list:
        new_array = elements.copy()  # [a1, a2
        for element in elements:  # [a1]
            key = list(kw_dict.keys())[0]  # r.key : [r.values]
            values = list(kw_dict.values())[0]
            for value in values:  # r.key : r.value
                new_key = element.replace(key, value)  # a1_
                if new_key not in new_array:
                    new_array.append(new_key)
        fin_array.append(new_array)
        fin_dict.update({new_array[0]: new_array})
    return fin_array

def re_add(start_dict, dict_to_repl):
    dict_list = []
    for key, value in dict_to_repl.items():
        m = {key: value}
        dict_list.append(m)

    cur_list = start_kwarg_dict(start_dict, dict_list[0])
    next_dict_list = dict_list[1:]
    for cur_dict in next_dict_list:
        cur_list = kwarg_dict(cur_list, cur_dict)
    return cur_list


def keyw_dict(start_list):
    cpu_s_dict = {}
    for arr in start_list:
        cpu_s_dict.update({arr[0]: arr})

    return cpu_s_dict


models = {
    'dell 6410': 2500,
    'dell 5410': 2400,
    'dell 6510': 2800,
    'dell 5510': 2800,
    'dell 6420': 3500,
    'dell 5420': 3500,
    'dell 5520': 4000,
    'dell 6520': 4000,
    'dell 5530': 4300,
    'dell 6530': 4300,
    'dell 5430': 4000,
    'dell 5440': 4500,
    'dell 5540': 5000,
    'dell 6440': 4500,
    'dell 7440': 4800,
    'dell 7240': 4000,
    'dell 7250': 4500,
    'dell 7450': 5200,
    'dell 5450': 5000,
    'dell 5550': 5500,
    'dell 7470': 6500,
    'dell 5470': 6500,
    'dell 5570': 7000,
    'dell 5480': 7000,
    'dell 5580': 7500,
    'dell 7480': 7000,
    'dell 5490': 9000,
    'dell 5590': 9500,

    'dell 3558': 5000,

    'dell 7559': 12000,
    'dell inspirion g7': 15000,

    'hp 440 g1': 4500,
    'hp 640 g1': 4500,
    'hp 840 g1': 4500,

    'hp 850 g1': 5000,
    'hp 650 g1': 5000,
    'hp 450 g1': 5000,

    'hp 440 g2': 5000,
    'hp 640 g2': 5000,
    'hp 840 g2': 5000,

    'hp 850 g2': 5500,
    'hp 650 g2': 5500,
    'hp 450 g2': 5500,

    'hp 440 g3': 5800,
    'hp 640 g3': 5800,
    'hp 840 g3': 5800,

    'hp 850 g3': 6500,
    'hp 650 g3': 6500,
    'hp 450 g3': 6500,

    'hp 440 g4': 6300,
    'hp 640 g4': 6300,
    'hp 840 g4': 6300,

    'hp 850 g4': 7000,
    'hp 650 g4': 7000,
    'hp 450 g4': 7000,

    'hp 440 g5': 8500,
    'hp 640 g5': 8500,
    'hp 840 g5': 8500,

    'hp 850 g5': 9000,
    'hp 650 g5': 9000,
    'hp 450 g5': 9000,

    'hp 440 g6': 10000,
    'hp 640 g6': 10000,
    'hp 840 g6': 10000,

    'hp 850 g6': 10500,
    'hp 650 g6': 10500,
    'hp 450 g6': 10500,

    'acer e5': 6500,
}

dict_new_models = {
    'dell ': ['dell e', 'del ', 'делл '],
    'hp': ['hewlett packard', 'hewlet packard', 'hewlett-packard', 'hewlettpackard'],
    ' ': ['', '-'],
}

models_list = re_add(models, dict_new_models)
models_dict = keyw_dict(models_list)
# print(models_dict)
# print(models_list)


# cpu_s = {
#     'i5 2520': 3500,
#     'i5 2530': 3500,
#     'i5 2440': 3500,
#     'i5 2420': 3500,
#     'i5 2450': 3500,
#     'i5 2540': 3500,
#     'i5 2560': 3500,
#
#     'i7 2620': 4000,
#     'i7 2640': 4000,
#     'i7 2720': 4000,
#     'i7 2740': 4000,
#
#     'i5 3210': 4000,
#     'i5 3220': 4000,
#     'i5 3230': 4000,
#     'i5 3240': 4000,
#     'i5 3310': 4000,
#     'i5 3320': 4000,
#     'i5 3340': 4000,
#     'i5 3350': 4000,
#
#     'i7 3510': 4300,
#     'i7 3520': 4300,
#     'i7 3530': 4300,
#     'i7 3540': 4300,
#     'i7 3760': 4600,
#     'i7 3770': 4600,
#
#     'i5 4200': 4500,
#     'i5 4210': 4500,
#     'i5 4215': 4500,
#
#     'i7 4600': 5000,
#     'i7 4610': 5000,
#
#     'i7 4700': 5300,
#     'i7 4710': 5300,
#
#     'i3 5005': 4500,
#     'i3 5010': 4500,
#
#     'i3 6006': 5000,
#     'i3 6157': 5000,
#     'i3 6100': 5000,
#     'i3 6167': 5000,
#
#     'i3 7007': 5500,
#     'i3 7020': 5500,
#     'i3 7100': 5500,
#     'i3 7110': 5500,
#
#     'i3 8100': 6200,
#
#     'i3 8100': 6200,
#
#
#
# }

cpu_s = {
    'i3 2': 2800,
    'i5 2': 3500,
    'i7 2': 4000,

    'i3 3': 3000,
    'i5 3': 3800,
    'i7 3': 4200,

    'i3 4': 3800,
    'i5 4': 4500,
    'i7 4': 5200,

    'i3 5': 4500,
    'i5 5': 5000,
    'i7 5': 5700,

    'i3 6': 5000,
    'i5 6': 5500,
    'i7 6': 6500,

    'i3 7': 5550,
    'i5 7': 6000,
    'i7 7': 7000,

    'i3 8': 6200,
    'i5 8': 8000,
    'i7 8': 9000,

    'i3 9': 7500,
    'i5 9': 13000,
    'i7 9': 15000,
    'i7 9750': 15000,
    'i7 9850': 15000,

    'i3 10': 8000,
    'i3 1000': 8000,
    'i3 1005': 8000,
    'i3 1011': 8000,

    'i5 10': 10000,
    'i5 102': 10000,
    'i5 103': 10000,
    'i5 104': 10000,

    'i7 10': 12000,
    'i7 105': 12000,
    'i7 106': 12000,
    'i7 107': 12000,
    'i7 108': 15000,
    'i7 109': 15000,
    'i9 9': 18000,
    'i9 10': 18000,

    'i3 11': 8500,
    'i5 11': 10500,
    'i7 11': 12500,
}

dict_new_cpu = {' ': ['-']}

cpu_s_list = re_add(cpu_s, dict_new_cpu)
# print(cpu_s_list)
cpu_s_dict = keyw_dict(cpu_s_list)



memory = {
    '0 gb': -400,
    '1 gb': -400,
    '2 gb': -200,
    '3 gb': -200,
    '4 gb': 0,
    '5 gb': 0,
    '6 gb': 200,
    '8 gb': 400,
    '12 gb': 800,
    '16 gb': 1200,
}

dict_new_ram = {
    'gb': ['gig', 'гб', 'гиг'],
    ' ': ['', '-'],
}

ram_list = re_add(memory, dict_new_ram)
# print(ram_list)
ram_dict = keyw_dict(ram_list)
# print(ram_dict)

hard_drive = {
    '60 gb': -300,
    '320 hdd': 0,
    '500 hdd': 100,
    '750 hdd': 200,
    '1 tb': 300,
    '2 tb': 500,

    '128 ssd': 300,
    '180 ssd': 300,
    '240 ssd': 500,
    '250 ssd': 500,
    '256 ssd': 500,
    '480 ssd': 1000,
    '500 ssd': 1000,
    '512 ssd': 1000,
    '960 ssd': 1500,
    '1 tb ssd': 1500,
    '2 tb ssd': 2000,
}

dict_new_hdd = {
    'hdd': ['gb hdd'],
    'ssd': ['gb ssd', 'ссд', 'гиг ссд'],
    'gb': ['гб', 'гиг'],
    'tb': ['terrabyte', 'terabyte'],
    '1 tb': ['1024 gb', '1024 гиг', '1000 gb'],
    '2 tb': ['2048 gb', '2048 гиг'],
    ' ': ['', '-'],
    ' gb hdd': ['gb hdd'],
    ' tb hdd': ['tb hdd'],
    ' gb ssd': ['gb ssd'],
    ' tb ssd': ['tb ssd'],
}

hard_drive_list = re_add(hard_drive, dict_new_hdd)
# print(hard_drive_list)
hard_drive_dict = keyw_dict(hard_drive_list)
# print(hard_drive_dict)

screen_size = {
    '10.6 "': -800,
    '11.6 "': -600,
    '12.5 "': -500,
    '13 "': -200,
    '14 "': 0,
    '15 "': 500,
    '17 "': 1200,
}


dict_new_sc_size = {
    '10': ['10.0', '10.6'],
    '11': ['11.0', '11.6'],
    '12': ['12.0', '12.5'],
    '13': ['13.0', '13.3'],
    '14': ['14.0', '13.3'],
    '15': ['15.0', '15.6'],
    '17': ['17.0', '17.3'],
    ' "': ['',' ', 'inch', ' дюймов', ' \''],
}

screen_size_list = re_add(screen_size, dict_new_sc_size)

screen_size_dict = keyw_dict(screen_size_list)
# print(screen_size_dict)

# print(screen_size_list)

screen_res = {
    '1366 768': 0,
    '1600 900': 300,
    '1920 1080': 500,
    '2560 1440': 1500,
    '2k': 1500,
    '2.5k': 1500,
    '4k': 1500,
}

dict_new_res = {
    ' ': ['x', '*', ' x ', ' * '],
    '2k': ['2 k', '2560'],
    '2.5k': ['2.5 k', '2560 x 1440', '2560*1440'],
    '4k': ['4 k', '4096 x 2160', '4096*2160'],
}

screen_res_list = re_add(screen_res, dict_new_res)
screen_res_dict = keyw_dict(screen_res_list)
# print(screen_res_dict)
# print(screen_res_list)

defects = {
    'no hdd': -300,

    'no ram': -400,
    # 'без памяти': -400,

    'no memory': -400,
    # 'без диска': -350,

    'no ac': -250,

    'no battery': -600,
    # 'без батареи'

    'no screen': -1500,
    # 'разбит экран': -150,

    'no hinge': -600,
    # 'поломана петля': -600,
    # 'сломана петля': -600,
}

dict_new_defects = {
    'screen': ['display', 'picture', 'image'],
    'battery': ['bat', 'akku', 'aku', 'batery'],
    'ac': ['adapter', 'cord', 'charger', 'power supply'],
    'no': ['without', 'mis', 'missing', 'miss', 'defective', 'cracked', 'broken'],
    'hdd': ['hard drive', 'disk', 'storage', 'drive', 'ssd'],
    # ' ': ['-'],
}

defects_list = re_add(defects, dict_new_defects)
defects_dict = keyw_dict(defects_list)
# print(defects_dict)
# print(defects_list)

graphics = {
    'nvidia 520': 100,
    'nvidia 550': 300,
    'nvidia 555': 400,
    'nvidia 560': 600,
    'nvidia 570': 800,
    'nvidia 580': 1000,

    'nvidia 610': 200,
    'nvidia 620': 300,
    'nvidia 625': 400,
    'nvidia 630': 400,
    'nvidia 640': 500,
    'nvidia 650': 800,
    'nvidia 660': 1200,
    'nvidia 670': 2000,
    'nvidia 680': 2500,

    'nvidia 710': 500,
    'nvidia 720': 700,
    'nvidia 730': 800,
    'nvidia 740': 1200,
    'nvidia 750': 2000,
    'nvidia 760': 2800,
    'nvidia 770': 3500,
    'nvidia 780': 4000,

    'nvidia 820': 700,
    'nvidia 830': 900,
    'nvidia 840': 1500,
    'nvidia 850': 2200,
    'nvidia 860': 3000,
    'nvidia 870': 3700,
    'nvidia 880': 4200,

    'nvidia 910': 700,
    'nvidia 920': 800,
    'nvidia 930': 1000,
    'nvidia 940': 2000,
    'nvidia 950': 2700,
    'nvidia 960': 3200,
    'nvidia 970': 4000,
    'nvidia 980': 4500,

    'nvidia mx 110': 700,
    'nvidia mx 130': 1200,
    'nvidia mx 150': 1500,
    'nvidia mx 230': 1000,
    'nvidia mx 250': 1500,
    'nvidia mx 330': 1000,
    'nvidia mx 350': 1800,
    'nvidia mx 450': 2000,

    'nvidia 1050': 4500,
    'nvidia 1060': 6000,
    'nvidia 1070': 7000,
    'nvidia 1080': 8000,

    'nvidia 1650': 5200,
    'nvidia 1660': 6000,

    'nvidia 2060': 8000,
    'nvidia 2070': 9000,
    'nvidia 2080': 10000,

    'nvidia 3050': 800,
    'nvidia 3060': 10000,
    'nvidia 3070': 12000,
    'nvidia 3080': 15000,
}

dict_new_graph = {
    'nvidia': ['nvidia gtx', 'nvidia gt', 'nvidia geforce', 'нвидиа гтх'],
    ' ': ['', '-']
}

graphics_list = re_add(graphics, dict_new_graph)
graphics_dict = keyw_dict(graphics_list)
print(graphics_dict)
# print(graphics_list)

specs_list = []
specs_list.append(models_list)
specs_list.append(cpu_s_list)
specs_list.append(ram_list)
specs_list.append(hard_drive_list)
specs_list.append(screen_size_list)
specs_list.append(screen_res_list)
specs_list.append(graphics_list)
specs_list.append(defects_list)

arr_fin = []
for elements in specs_list:
    arr_current = []
    for el in elements:
        arr_fin.append(el)

# print(arr_fin)
# print(cpu_s_list)


specs_dict = {}
specs_dict.update(models)
specs_dict.update(cpu_s)
specs_dict.update(memory)
specs_dict.update(hard_drive)
specs_dict.update(screen_size)
specs_dict.update(screen_res)
specs_dict.update(graphics)
specs_dict.update(defects)

specs_dict_list = []
specs_dict_list.append(models_dict)
specs_dict_list.append(cpu_s_dict)
specs_dict_list.append(ram_dict)
specs_dict_list.append(hard_drive_dict)
specs_dict_list.append(screen_size_dict)
specs_dict_list.append(screen_res_dict)
specs_dict_list.append(graphics_dict)
specs_dict_list.append(defects_dict)
# print(specs_dict_list)




# print(specs_dict)


