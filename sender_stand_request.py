import requests
import configuration
import data


# Создание пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


# Токен авторизации
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")


# Создание набора для пользователя
def post_new_client_kit(kit_body):
    data.headers["Authorization"] += get_new_user_token()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
                         json=kit_body,
                         headers=data.headers)
