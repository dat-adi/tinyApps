import pickle
import webbrowser as webb
'''
entry = {
    1100:{
        'STS1007':[
           'https://m.teamlink.co/7706072174?p=83b0953304ad70075faa84c94f63a6fd'
        ]
    },
    1200:{
        'CHY1004':[
            'https://m.teamlink.co/1559268139'
        ]
    }
}
'''
sunday_table = {}

while True:
    print("1. Add entry for sunday.\n2. Exit")
    selection_of_entrys = int(input())
    if selection_of_entrys == 1:
        in_time = input("Enter time in HHMM format : ")
        course_code = input("Enter the course code : ")
        links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == 'quit':
                break
            else:
                links.append(temp_link)
        sunday_table[in_time] = {course_code: links}
    elif selection_of_entrys == 2:
        break
    else:
        print("You kinda made an error there. Retry?")

print(sunday_table)

#pickle.dump(entry, open('timetable', 'wb'))