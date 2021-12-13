import random
import requests
import json


TOKEN = '5008658974:AAHaCl3LBwDPw2Pp4tZv8nZ3-qjzh8P_zjE'
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
LONG_POLLING_TIMEOUT = 10


def get_anime_by_genre(user_choice):
    anime_dict = {'кодомо': ['Покемон', 'Дораэмон', 'Приключения пчелки Майи'],
                  'сёнен': ['Блич', 'Боец Баки', 'Черный клевер'],
                  'сёдзё': ['Сейлор Мун', 'Рыцарь-вампир'],
                  'сэйнэн': ['Пираты Черной лагуны', 'Берсерк'],
                  'дзёсэй': ['Мёд и клевер', 'Ателье Paradise Kiss']}

    if user_choice in ['кодомо', 'кадомо', 'кодамо', 'кадамо']:
        return random.choice(anime_dict.get('кодомо'))
    elif user_choice in ['сенен', 'сёнен', 'сёнён', 'сенён']:
        return random.choice(anime_dict.get('сёнен'))
    elif user_choice in ['сёдзё', 'седзе', 'сёдзе', 'сёдзе']:
        return random.choice(anime_dict.get('сёдзё'))
    elif user_choice in ['сэйнэн', 'сейнэн', 'сэйнен', 'сейнен']:
        return random.choice(anime_dict.get('сэйнэн'))
    elif user_choice in ['дзёсэй', 'дзесэй', 'дзёсей', 'дзесей']:
        return random.choice(anime_dict.get('дзёсэй'))
    else:
        raise KeyError


def main():
    last_update_id = None
    while True:
        r = requests.get(BASE_URL + 'getUpdates',
                         params={
                             'offset': last_update_id,
                             'timeout': LONG_POLLING_TIMEOUT
                         })
        response_dict = json.loads(r.text)
        print(r.status_code)
        print(r.text)
        for upd in response_dict["result"]:
            last_update_id = upd["update_id"] + 1
            msg = upd["message"]
            chat_id = msg["chat"]["id"]
            if "text" in msg:
                text = msg["text"]
                if text.lower() == 'подобрать аниме':
                    r = requests.post(BASE_URL + 'sendMessage', params={
                        "chat_id": chat_id,
                        "text": '''Пожалуйста, введите жанр аниме в зависимости от целевой аудитории:
1. кодомо - для детей до 12\n2. сёнен - для юношей до 18\n3. сёдзё - для девочек-подростков
4. сэйнэн - для мужчин от 18\n5. дзёсэй - для женщин от 18'''
                    })
                    anime_choice_id = last_update_id
                    recommended_anime = ''
                    while not recommended_anime:
                        r = requests.get(BASE_URL + 'getUpdates',
                                         params={
                                             'offset': last_update_id,
                                             'timeout': LONG_POLLING_TIMEOUT
                                         })
                        response_dict = json.loads(r.text)
                        print(r.status_code)
                        print(r.text)
                        for choice_upd in response_dict["result"]:
                            anime_choice_id = choice_upd["update_id"] + 1
                            msg = choice_upd["message"]
                            chat_id = msg["chat"]["id"]
                            if "text" in msg:
                                text = msg["text"]
                                try:
                                    recommended_anime = get_anime_by_genre(text)
                                    r = requests.post(BASE_URL + 'sendMessage', params={
                                        "chat_id": chat_id,
                                        "text": recommended_anime
                                    })
                                except KeyError:
                                    r = requests.post(BASE_URL + 'sendMessage', params={
                                        "chat_id": chat_id,
                                        "text": 'Ошибочка! Вы неправильно ввели название жанра :('
                                    })
                                    recommended_anime = 'not'
                else:
                    r = requests.post(BASE_URL + 'sendMessage', params={
                        "chat_id": chat_id,
                        "text": '''Извините, я пока вас не понимаю, потому что я в разработке.
Введите, пожалуйста, "подобрать аниме"'''
                     })


if __name__ == "__main__":
    main()
