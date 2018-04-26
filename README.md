# Python to IFTTT
## A simple interface for triggering IFTTT webhooks
________
## Installation

```bash
pip install py2ifttt
```

## Usage

```python
from py2ifttt import IFTTT

ifttt = IFTTT('your key str', 'event_name')
ifttt.notify('event name', 'value1', 'value2', 'value3')
```