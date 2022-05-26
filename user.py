class User:

    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_pass):
        self.password = new_pass

    def change_job_title(self, new_job):
        self.current_job_title = new_job

    def show_info(self):
        print(self.name + " " + self.email)


user = User("dang@yahoo.com", "dang", "pass", "Dev")
user.show_info()
