# alertlib
library for sending alerts for various platforms

# examples

## slack

#### simple
```python
from alertlib import send_to_slack

# when sending to user then send_to must start with '@'
# when sending to channel then send_to must start with '#'
send_to_slack(slack_token, send_from, send_to, message)
```

#### or with decorator
```python
from alertlib import create_chat_notificator

chat_notify = create_chat_notificator(TOKEN, return_instance=True)

@chat_notify
method_to_wrap(c, *args, **kwargs):
	pass
```

