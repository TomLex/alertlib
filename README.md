# alertlib
library for sending alerts for various platforms

# examples

## email
```python
from alertlib import send_to_email

## mandrill_login = [mandrill_login, mandrill_password]
send_to_email(mandrill_login, email_from='alertlib@skypicker.com', email_to=[], subject='', message='', list_of_files=[])
```

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

chat_notify = create_chat_notificator(slack_token, user='alertlib', send_to='#channel', s_msg=None, e_msg=None, return_instance=True)

# if return_instance is True
@chat_notify
method_to_wrap(c, *args, **kwargs):
	# your code here
	pass

# if return_instance is False
@chat_notify
method_to_wrap(*args, **kwargs):
	# your code here
	pass
```

