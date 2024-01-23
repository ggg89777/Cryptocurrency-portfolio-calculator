The calculator is designed to calculate a cryptocurrency portfolio.
You can add an unlimited number of cryptocurrencies. 
This can be useful if you have many cryptocurrency wallets and are tired of recalculating your portfolio manually.

Калькулятор предназначен для расчета портфеля криптовалют. 
Вы можете добавить неограниченное количество криптовалют. 
Это может быть полезно, если у вас много криптовалютных кошельков и вы устали пересчитывать свой портфель вручную.

First you need to register on the website: pro.coinmarketcap.com/account/
In your personal account you will receive an API KEY.

Для начала вам необходимо зарегистрироваться на сайте: pro.coinmarketcap.com/account/
В личном кабинете вы получите API КЛЮЧ.

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/97d3064f-a5b2-4efc-9299-4d01196457b5)

When you run the program, the API-KEY file does not exist and you are prompted to enter the key in a dialog box. 
Then when you start the program you will not need to enter the key. The key is automatically written to the API-KEY.txt file.

При запуске программы файл API-KEY не существует, и вам будет предложено ввести ключ в диалоговом окне.
Тогда при запуске программы вам не нужно будет вводить ключ. Ключ автоматически записывается в файл API-KEY.txt.

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/7c55b98a-b1bf-4e72-a0cd-db7c974344ee)

This site has a monthly request limit (if you are using the free version). By default, the request limit is set to 5 minutes. 
But you can change this in the settings. By setting the delay value to more than 5 minutes in the settings. 
In the show_delay_entry function of the main file, you can change the minimum delay value in the minvalue parameter.

Этот сайт имеет ежемесячный лимит запросов (если вы используете бесплатную версию). По умолчанию лимит запроса установлен на 5 минут.
Но вы можете изменить это в настройках. Установив в настройках значение задержки более 5 минут.
В функции show_delay_entry основного файла вы можете изменить минимальное значение задержки в параметре minvalue.

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/2c141337-cbb8-40eb-a06a-4917ebf099d5)

The calculator sends queries to coinmarketcap.com to determine the price of the asset by clicking the "Get Coinmarketcap" button. 
You then enter the number of coins, and when you click “Calculate”, your current capitalization in that asset is displayed, as well as your TOTAL CASH.

Калькулятор отправляет запросы на coinmarketcap.com для определения цены актива, нажав кнопку «Получить Coinmarketcap». 
Затем вы вводите количество монет, и когда вы нажимаете «Рассчитать», отображается ваша текущая капитализация в этом активе, а также TOTAL CASH.

The survey can be started automatically (if you have entered all the required fields) using the auto_start button. 
You can stop the countdown using the auto_stop button.

Опрос можно запустить автоматически (если вы ввели все необходимые поля) с помощью кнопки auto_start.
Вы можете остановить обратный отсчет с помощью кнопки auto_stop.

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/90749fe1-e469-46e7-96ab-d8fe5ed72851)

You can add a coin by clicking the "Add Coin" button. You can remove a coin using the del button.

Вы можете добавить монету, нажав кнопку «Добавить монету». Удалить монету можно с помощью кнопки del.

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/fff6b814-b820-42b5-ab29-b188ae471713)

Function descriptions are given in the code. When you click on the “Add Coin” button,
an instance of the CreateTag class is generated, which creates the necessary fields for entering and displaying values. 
All server responses are saved in the dict_price file. The dict_id dictionary is used to store in RAM the positions of the coins in your coin list,
as well as their quantity. This dictionary can be saved by clicking "Save File" in the main menu. 
You can also open a save in the main menu by clicking on the “open file” button.

Описания функций приведены в коде. При нажатии на кнопку «Добавить монету» генерируется экземпляр класса CreateTag,
который создает необходимые поля для ввода и отображения значений. 
Все ответы сервера сохраняются в файле dict_price. 
Словарь dict_id используется для хранения в оперативной памяти позиций монет в вашем списке монет, а также их количества.
Этот словарь можно сохранить, нажав «Сохранить файл» в главном меню. Открыть сохранение также можно в главном меню, нажав на кнопку «открыть файл».

![image](https://github.com/ggg89777/Cryptocurrency-portfolio-calculator/assets/33584533/71390a25-70e7-45ff-8962-00117ea9f78b)
