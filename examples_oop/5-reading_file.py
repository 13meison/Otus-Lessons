from csv import DictReader
import json
from itertools import cycle

with open('../files_for_lessons/result.json', 'w') as f_result:
    json_data = []

    with open('../files_for_lessons/users.json', 'r') as f_users:
        users = json.loads(f_users.read())
        for user in users:
            new_user = {
                "name": user['name'],
                "gender": user['gender'],
                "address": user['address'],
                "age": user['age'],
                "books": []
            }
            json_data.append(new_user)

    with open('../files_for_lessons/books.csv', newline='') as f_books:
        reader = DictReader(f_books)
        book_list = []

        for row in reader:
            book_list.append(row)

        gen_list = [i for i in range(len(json_data))]
        print('!!!!!!!!!!!!!!!!!!!!!!!')
        print(gen_list)


        for cnt, i in enumerate(cycle(gen_list)):
            if cnt >= len(book_list):
                print('!!!')
                print(cnt)
                break
            json_data[i]['books'].append(book_list[cnt])
            print(i)
            cnt += 1

    json.dump(json_data, f_result)

# with open('../files_for_lessons/result.json', 'r') as f:
#     json = json.loads(f.read())
#     print(json)

print(enumerate(cycle(gen_list)))
