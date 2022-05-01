import json

from comfig import *  # импорт констант (путь к json-файлу и к папке с картинками)
from exceptions import *


def get_posts(path):
    """Функция принимает аргумент, ссылку на json-файл,
     открывает его и возвращает его в виде списока словарей"""
    try:  # проверка на наличие и открытие файла
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def content_for_the_posts(posts, substring):
    """Функция распаковывает словари и выводит
     Картинку и текст по вхождению"""
    posts_list = []
    for post in posts:
        if substring.lower() in post['content'].lower():  # подстрока входит в строку в ниж. регистре
            posts_list.append(post)

    return posts_list


def save_uploaded_picture(picture):
    """Функция принимает аргумент файл, проверяет
     Тип файла и допустимый сохраняет в указанную папку"""
    all_type = ["jmg", "png", "gif", "jpeg"]  # список допустимого формата файла
    picture_type = picture.filename.split('.')[-1]  # разбивает строку на подстроки по точке и берёт последний элемент
    if picture_type not in all_type:  # элемент не входит в перечень списка
        raise WrongImgType(f"Не верный формат файла, допустимые форматы {', '.join(all_type)}")  # вызывает ошибку
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"  # картинка и путь в папку, куда нужно сохранить
    picture.save(picture_path)  # метод save сохраняет картинку в указанную папку

    return picture_path


def add_post(post_list, post):
    """Функция принимает аргумент файл, проверяет
    Тип файла и допустимый сохраняет в указанную папку"""
    post_list.append(post)  # записывает новый пост в список постов
    with open(POST_PATH, 'w', encoding='utf-8') as file:  # открывает файл для записи
        json.dump(post_list, file)
        return
