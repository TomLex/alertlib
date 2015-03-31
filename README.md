# alertlib
library for sending alerts for various platforms

# usage

## email
```python
from alertlib import send_to_email

## mandrill_login = [mandrill_login, mandrill_password]
send_to_email(mandrill_login, email_from='alertlib@skypicker.com', email_to=['some.mail@host.com'], subject='alert', message='', list_of_files=[])
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

## pager duty
#### simple
```python
from alertlib import send_to_pagerduty

# when sending to user then send_to must start with '@'
# when sending to channel then send_to must start with '#'
send_to_pagerduty(api_key, service_key, description, details=None, client=None, client_url=None)
```

#### or with decorator
```python
from alertlib import create_pagerduty_notificator

pagerduty_notify = create_pager_notificator(api_key)

@pagerduty_notify
method_to_wrap(pager, *args, **kwargs):
	# ...
	pager.trigger_incident(service_key, alert_description, details=None, client=None, client_url=None)
	# ...
```

# installation

	pip install -e git+https://github.com/TomLex/alertlib.git#egg=alertlib
