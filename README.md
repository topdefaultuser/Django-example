# Django-example


Несколько слов о сайте. Данный сайт сделан исключительно для получения практического опыта разработки на фреймворке Django. Все сходства с другими проектами случайность. 

**Описание возможностей сайт:**

При запуске сервера Django и переходе по базовому url-адресу, первое, что увидит пользователь, это форму авторизации.  Для создания заметок, сначала нужно создать свой кабинет, в котором будут храниться задания. Поэтому, кликаем  на ссылку «регистрация» под кнопкой «войти» и указываем имя пользователя, e-main, вводим  пароль и повторяем его. Если вы ввели все верно и такого пользователя еще не существует, вы будете перенаправлены на главную страницу.

**Скриншоты страниц авторизации пользователя:**

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot1.PNG)


**Скриншот главной страницы нового пльзователя:**

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot2.PNG)

**Скриншот главной страницы с заданиями:**

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot3.PNG)

Если по какой-то причине у пользователя отключен javascript, у него будет отображаться предупреждение о том, что нужно включить  javascript для корректной работы сайта. Но сайт полноценно работает и без включенного  javascript. В таком случае  аккордеон будет раскрыт и при любом действии (изменение состояния задачи, удаления комментария, задачи), сервер будет присылать новую страницу.

**Скриншоты страниц добавления задачи и комментария:**

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot4.PNG)

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot5.PNG)

В случае, когда javascript не отключен, скрипт под названием scripts.js будет отправлять ajax запросы на сервер и производить манипуляции с DOM-деревом на стороне клиента, как в SPA (Single Page Application).

**Скриншоты главной страницы с работающем javascript:**
![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot6.PNG)

**Скриншоты модальных окон для  добавления задачи и комментария:**
![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot7.PNG)

![]( https://github.com/topdefaultuser/Django-example/blob/advanced/screenshots/screenshot8.PNG)
