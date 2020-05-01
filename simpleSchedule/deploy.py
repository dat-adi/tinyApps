import os
import pickle

apps = []

if os.path.isfile('timetable'):
    temp_apps = open('timetable', 'rb')
    oneday = pickle.load(temp_apps)

for '1100' in oneday.items():
    apps.append(oneday[1100['STS1007']])
print(apps)