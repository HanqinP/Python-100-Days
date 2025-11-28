import json
import os

def write_to_json(path, dict_data):
    try:
        with open(path, 'w', encoding='utf-8') as fs:
            json.dump(dict_data, fs)
    except IOError as e:
        print(e)
    print('数据保存完成')


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    current_dir = os.path.dirname(__file__)
    write_to_json(current_dir+r'\jsondemo1.json', mydict)

if __name__ == "__main__":
    main()