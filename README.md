# Космический Инстаграм

### О проекте
С помощью данного кода вы сможете скачивать фотографии о космосе в ваш инстраграм.
Их можно брать с последних запусков SpaceX или из коллекций телескопа Hubble.
 
### Как установить
1. Создайте файл `.env` и положите ваши пароль и логин от инстаграма в переменные `INSTA_LOGIN` и `INSTA_PASSWORD`. Пример: 
    ```
    INSTA_LOGIN=dvmncool@mail.ru
    INSTA_PASSWORD=12345
    ```

2. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
    ```
    pip install -r requirements.txt
    ```

### Примеры запуска
Если вы уже скачали нужные вам картинки, нужно просто ввести в терминал `python main.py`.

Далее бот выведет такие строчки, если он успешно вошел в инстаграм аккаунт:
   ```
    2021-02-23 20:14:48,818 - INFO - Instabot version: 0.117.0 Started
    2021-02-23 20:14:48,819 - INFO - Not yet logged in starting: PRE-LOGIN FLOW!
    2021-02-23 20:14:52,245 - INFO - Logged-in successfully as 'dvmncool@mail.ru'!
    2021-02-23 20:14:52,246 - INFO - LOGIN FLOW! Just logged-in: True
   ```
Если любая из этих строк будет другой, то что-то пошло не так(может не работать бот или вы ввели не верные файлы о вашем аккаунте).

После этого он будет полряд идти по картинкам в папке:
1. Сначала выведет размер картинки `FOUND: w:1080 h:720 r:1.5`.
2. Затем то, что она загрузилась `Photo 'images/spacex0.jpg' is uploaded.` (Если фото не загрузится, то бот сообщит о ошибке)
.
3. После того, как все фотографии загрузились, бот выведет количество запросов ` Total requests: 33
`
### Дополнительная информация
Узнать о API SpaceX вы можете на [documenter.getpostman.com](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1).

О API Hubble на [hubblesite.org](http://hubblesite.org/api/documentation).

О том как пользоваться instabot на [instagrambot.github.io](https://instagrambot.github.io/docs/en/For_developers.html#photos).

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).