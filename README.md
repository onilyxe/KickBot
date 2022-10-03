# Kick Bot for Telegram
Bot kicks fans of blue text in telegram

[Try the my bot](https://t.me/sofiarolbot)

About
------------
**Такс. Есть у меня в тг один чатик, в котором мы с пацанами любим байтить ньюфагов на `/kickme` от Розы. Лично мной, было принято решение украсть бота (не смогу указать, забыл где достал) и переделать его под это дело. От оригинала осталось несколько полезных фич, и так же самое главное мной добавлено, аля `"розыгрыши"`. По команде: `/roulet` - бот покажет несколько команд, с помощью которых типо можно выиграть админку и т.д. На самом деле - он просто кикает участника и всё (Если ты админ, то просто пишет что ты уже выиграл, а остальным - попробуй ещё раз) Так же ещё одна замечательная команда: `/bluetext` - думаю многим известно что там. Бот кикает за любой текст с этой херни, а в ответ выдаёт просто "Потыкай". И, вишенка на торте, это команда `/kekmi` - которая тупо кикает и ничего не пишет, так скажем, сайленткик. Ну, на этом вроде всё. Не думаю что вам пригодится этот бот, но а вдруг)**

Installation
------------
```shell
# Clone the repository
$ git clone https://github.com/onilyxe/KickBot.git

# Change the working directory to KickBot
$ cd KickBot
```

Configuring
------------
**Open `config.yaml` configuration file with text editor and set the tokens and your id:**
```ini
TELEGRAM:
    API_KEY: 0000000000:0000000000000000000000000000000000
    LIST_OF_ADMINS:
        - 000000000
        - 000000001
```
* `API_KEY` is token for your Telegram bot. You can get it here: [BotFather](https://t.me/BotFather)
* `LIST_OF_ADMINS` is list id

Running
------------
Using Python
```shell
# Install requirements
$ python3 -m pip install -r requirements.txt

# Run script
$ python3 bot.py
```