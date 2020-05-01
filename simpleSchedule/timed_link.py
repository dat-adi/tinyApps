import datetime
import webbrowser as webb
from time import sleep

op = webb.get('opera')

def link_open():
    op.open("https://m.teamlink.co/7706072174?p=83b0953304ad70075faa84c94f63a6fd")

now = datetime.datetime.now()
print(now)
run_at = now + datetime.timedelta(seconds=5)
print(run_at)
delay = (run_at - now).total_seconds()
print(delay)

sleep(delay)
link_open()
