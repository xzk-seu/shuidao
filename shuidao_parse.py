import json
import os

if __name__ == '__main__':
    file_name = '水稻.txt'
    path = os.path.join(os.getcwd(), file_name)

    result = dict()
    item = None
    with open(path, 'r') as fr:
        for line in fr.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            words = line.split(' ', 1)
            if len(words) == 1:
                if item:
                    name = item.pop('名称')
                    result[name] = item
                item = dict()
                item['名称'] = words[0]
            else:  # len(words) == 2:
                prop = words[0]
                value = words[1]
                item[prop] = value.strip()

        result[item['名称']] = item

    w_path = os.path.join(os.getcwd(), '水稻.json')
    with open(w_path, 'w') as fw:
        json.dump(result, fw)
