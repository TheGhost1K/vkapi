import sys
import requests

if __name__ == '__main__':
    id = sys.argv[1]
    token = "your token"
    try:
        json_res = requests.get(
            f'https://api.vk.com/method/users.get?user_ids={id}&fields=city, bdate'
            f' counters&access_token={token}&v=5.107').json()

        friends = requests.get(
            f'https://api.vk.com/method/friends.get?user_id={id}&fields=nickname, city, bdate'
            f' &access_token={token}&v=5.107').json()
    except requests.ConnectionError as e:
        print("Ошибка соединения.")
        sys.exit(1)

    print("Name: " + json_res["response"][0]["first_name"] + " " + json_res["response"][0][
        "last_name"] + "\n")

    f = friends["response"]["items"]
    c = int(friends["response"]["count"])
    print("Count of friends: ", c, "\n")
    print("Friends list: ")
    for i in range(c):
        friend = f[i]
        print(friend['first_name'], friend["last_name"])
