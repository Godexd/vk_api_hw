import requests

VK_URL = 'https://api.vk.com/method/'
VK_TOKEN = input('Введите ваш ТОКЕН: ')
VK_API_VERSION = 5.126


class VkClient:

    def __init__(self, user_id):
        self.user_id = user_id
        self.loading = {
            'user_id': self.user_id,
            'access_token': VK_TOKEN,
            'v': VK_API_VERSION,
        }

    def get_friends(self):
        method_name = "friends.get"
        response = requests.get(f"{VK_URL}{method_name}", params=self.loading)
        json_dict = response.json()

        return json_dict['response']['items']

    def __and__(self, friend):
        print(f" Получаю список друзей пользователя : '{self.user_id}'....")
        first_user = set(self.get_friends())

        print(f" Получаю список друзей пользователя : '{friend.user_id}'....")
        second_user = set(friend.get_friends())

        print('\nСписок общих друзей:')
        friends = first_user & second_user
        return list(map(VkClient, friends)) or ['Общих друзей - нет!']

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


def get_user_id(user_id):
    users_get = "users.get"
    response = requests.get(f"{VK_URL}{users_get}", params={
        "user_ids": user_id,
        "access_token": VK_TOKEN,
        "v": VK_API_VERSION
    })
    return response.json()['response'][0]['id']


def main():
    first_user_id = input('Введите ID первого пользователя: ')
    first_user_id = get_user_id(first_user_id)

    second_user_id = input('Введите ID второго пользователя: ')
    second_user_id = get_user_id(second_user_id)

    first_user = VkClient(first_user_id)
    second_user = VkClient(second_user_id)

    print(*(first_user & second_user), sep="\n")


if __name__ == '__main__':
    main()