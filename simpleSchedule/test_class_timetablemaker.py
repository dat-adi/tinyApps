class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = {}

    def get_info(self):
        self.in_time = input("Enter time in HHMM format : ")
        self.course_code = input("Enter the course code : ")
        self.links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == 'quit':
                break
            else:
                self.links.append(temp_link)
        self.time_table[self.in_time] = {self.course_code: self.links}


