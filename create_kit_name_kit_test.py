import sender_stand_request
import data


# Данные для поля name
kit_body_511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
kit_body_512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


# эта функция меняет содержимое в теле запроса
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data
    current_kit_body = data.kit_body.copy()
    # изменение значения в поле name
    current_kit_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_kit_body


# функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body_positive = get_kit_body(name)

    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response_positive = sender_stand_request.post_new_client_kit(kit_body_positive)
    # Проверяем, что в ответе есть поле authToken
    assert kit_response_positive.json()["name"] == name
    # Проверяем, что код равен 201
    assert kit_response_positive.status_code == 201


# функция для негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body_negative = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response_negative = sender_stand_request.post_new_client_kit(kit_body_negative)

    # Проверяем, что код равен 400
    assert kit_response_negative.status_code == 400


# функция для негативной проверки "Параметр не передан в запросе"
def negative_assert_no_name(kit_body):
    kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response_negative_no_name.status_code == 400


# Позитивные тесты
# Тест 1. Успешное создание пользователя
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание пользователя
# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(kit_body_511)


# Тест 5. Успешное создание пользователя
# Параметр name состоит из английских букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание пользователя
# Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание пользователя
# Параметр name состоит из спецсимволов
def test_create_kit_has_special_simbol_in_name_get_success_response():
    positive_assert("№%@")


# Тест 8. Успешное создание пользователя
# Параметр name состоит из символов с пробелами
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание пользователя
# Параметр name состоит из цифр
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# Негативные тесты
# Тест 3. Ошибка
# Параметр name состоит из 0 символов (меньше допустимого)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")


# Тест 3. Ошибка
# Параметр name состоит из 512 символов (больше допустимого)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(kit_body_512)


# Тест 10. Ошибка
# Параметр name не передан в запросе
def test_create_kit_no_name_get_error_response():
    current_kit_body_negative_no_name = data.kit_body.copy()
    current_kit_body_negative_no_name.pop("name")
    negative_assert_no_name(current_kit_body_negative_no_name)


# Тест 11. Ошибка
# Передан другой тип параметра (число)
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(123)
