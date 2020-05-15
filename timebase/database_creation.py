import pandas as pd

class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = pd.DataFrame()

    def get_info(self):
        
        self.in_time = input("Enter time in HH:MM format : ")
        self.links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == 'quit':
                break
            else:
                self.links.append(temp_link)
        self.time_table = pd.DataFrame({'Time' : self.in_time, 'Links' : [self.links]})

    def day_return(self):
        return self.day

    def put_info(self):
        return self.time_table

def make():
    week_timetable = {}
    while True:
            input_day_name = input("Enter the day : ").lower()
            current_day = day_timetable(input_day_name)
            while True:
                if input('Enter the upcoming class?(y/n) : ')[0] == 'y':
                    current_day.get_info()
                    week_timetable[current_day.day_return()] = current_day.put_info()
                else:
                    break
            if input("Do you wish to continue?(y/n) : ")[0] == 'n':
                break
    print(week_timetable)

    with open('schedule.txt', 'w') as f:
        f.write(str(week_timetable))
        f.close()

'''def take_links():
    print("Enter the links you wish to execute.")
    link_list = []
    input_taken = ''
    while True:
        input_taken = input('link>')
        if input_taken == 'quit':
            break
        else:
            link_list.append(input_taken)
    return link_list

df1 = pd.DataFrame({
    'Day' : input("Enter the day : "),
    'Time' : input("Enter the time at which the class is : "),
    'Links' : [take_links()]
})

print(df1)'''

make()