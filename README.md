# tgtqdm

<p align="center">
    <img src="images/banner.png" alt="tgtqdm banner" width="50%" />
</p>

who needs work-life balance when you can watch your logs on the phone?

I made this because I wanted to watch my scripts go brr while I'm away from my computer

```bash
pip install tgtqdm
```

Replace your `tqdm` bar with this:

```python
import time
from tgtqdm import tgtqdm

for i in tgtqdm(
    range(33),
    json_filename="telegram_info.json",
    desc="running something"
):
    ## do something
    time.sleep(1)
```


The json file should look like this:
```json
{
    "api_token": "TOKEN",
    "chat_id": 123456789
}
```

**How do I get an API token and a chat ID?**

- For your own API token, go to [t.me/botfather](https://t.me/botfather) in telegram and create a new bot
- For your chat id, go to [t.me/userinfobot](https://t.me/userinfobot) in telegram


You can also manually log messages like this:

```python
from telegram_logger import TelegramLogger

logger = TelegramLogger(
    api_token="...",
    chat_id=123
)

## when you log for the first time, it will send a message
logger.log(message="Lettuce begin", timestamp=False)

## when you log again, it will update the existing message
logger.log(message="Legume resume", timestamp=False)
```

Alternatively, you can also safely store your api token and chat ID in a json and initialize your logger from the filename. This is usually safer for dummies

```python
logger = TelegramLogger.from_json(
    filename="telegram_info.json"
)
```
