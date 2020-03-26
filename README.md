# ApplicationAPI

## Установка 
скачайте проект через команду git clone.

- далее зайдите в папку ```project```

- потом перейдите в папку проекта и потом создайте virtual env командой ```python -m venv venv```

- активируйте venv командой source venv/bin/activate и установите необходимые пакеты командой ```pip install -r requirements.txt```

- проведите необходимые миграции ```python manage.py migrate```
 - запустите проект локально следующей командой:
``` python manage.py runserver ```

 - для того чтобы зарегистрировать нового пользовтеля пройдите по ссылке:
 ```http://127.0.0.1:8000/api/rest-auth/registration/```.
 Заполните все необходимые поля и нажмите POST. Вам будут выслан токен.
 
 - Далее в правом верхнем углу нажимаем на кнопку Log in и вводим данные, которые только, что зарегистрировали.
 
- После этого вы можете пользоваться веб приложением по адресу 
 
 ```http://127.0.0.1:8000/api/applications```
 
 - создание новой связки <br/> method: POST <br/> endpoint: ```http://127.0.0.1:8000/api/applications```
 <br/> required fields: ```name```
 
 - читать все существующие связки <br/> method: GET <br/> endpoint: ```http://127.0.0.1:8000/api/applications```

- просматривать одну связку <br/> method: GET <br/> endpoint: ```http://127.0.0.1:8000/api/applications/{id}``` где {id} является id модельки Application

- обновить одну связку <br/> method: PUT <br/> endpoint: ```http://127.0.0.1:8000/api/applications/{id}``` где {id} является id модельки Application
<br/> updatable fields: ```name```

- удалить одну связку <br/> method: DELETE <br/> endpoint: ```http://127.0.0.1:8000/api/applications/{id}``` где {id} является id модельки Application
 ### При этом при создании новой связки можно заполнять только поле ```name```, остальные поля заполняются сами
