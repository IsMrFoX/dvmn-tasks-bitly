# Обрезка ссылок с помощью Битли

### Как установить


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы с сервисом Bitly вам потребуется персональный ключ – “токен”. Он нужен для взаимодействия с API Bitly.
Его вы сможете получить на [Сервис Bitly](https://app.bitly.com/Bmcg8anPYYX/bitlinks/3W4iikm/details), [Документации Bitly](https://dev.bitly.com/),[Генератор токенов](https://app.bitly.com/settings/integrations/),
***GENERIC ACCESS TOKEN*** — нужный тип токена (пример: 17c09e20ad155405123ac1977542fecf00231da7).

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv), или как в моем случае [pyenv](https://docs.python-guide.org/dev/virtualenvs/)
для изоляции проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
