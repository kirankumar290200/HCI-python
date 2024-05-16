import tkinter as tk
from tkinter import messagebox

class DrivingSchoolApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Driving School App")
        self.users = {}
        self.courses = {
            1: {"name": "Basic Driving Course", "instructor": "John Doe", "duration": "10 hours", "price": "$200"},
            2: {"name": "Advanced Driving Course", "instructor": "Jane Smith", "duration": "20 hours", "price": "$400"},
        }
        self.bookings = {} 

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Welcome to Driving School App")
        self.label.pack()

        self.button_register = tk.Button(self.frame, text="Register", command=self.register)
        self.button_register.pack()

        self.button_login = tk.Button(self.frame, text="Login", command=self.login)
        self.button_login.pack()

        self.button_exit = tk.Button(self.frame, text="Exit", command=self.master.quit)
        self.button_exit.pack()

    def register(self):
        register_window = tk.Toplevel(self.master)
        register_window.title("Register")

        tk.Label(register_window, text="Enter your name:").pack()
        self.name_entry = tk.Entry(register_window)
        self.name_entry.pack()

        tk.Label(register_window, text="Enter your email:").pack()
        self.email_entry = tk.Entry(register_window)
        self.email_entry.pack()

        tk.Button(register_window, text="Submit", command=self.save_user).pack()

    def save_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        self.users[email] = {"name": name, "email": email}
        messagebox.showinfo("Success", "Registration successful!")
        self.master.focus_set()

    def login(self):
        login_window = tk.Toplevel(self.master)
        login_window.title("Login")

        tk.Label(login_window, text="Enter your email:").pack()
        self.email_entry = tk.Entry(login_window)
        self.email_entry.pack()

        tk.Button(login_window, text="Submit", command=self.check_login).pack()

    def check_login(self):
        email = self.email_entry.get()
        if email in self.users:
            messagebox.showinfo("Success", f"Welcome back, {self.users[email]['name']}!")
            self.show_courses()
        else:
            messagebox.showerror("Error", "User not found. Please register.")
        self.master.focus_set()

    def show_courses(self):
        courses_window = tk.Toplevel(self.master)
        courses_window.title("Available Courses")

        for course_id, course_info in self.courses.items():
            tk.Label(courses_window, text=f"Course ID: {course_id}").pack()
            tk.Label(courses_window, text=f"Name: {course_info['name']}").pack()
            tk.Label(courses_window, text=f"Instructor: {course_info['instructor']}").pack()
            tk.Label(courses_window, text=f"Duration: {course_info['duration']}").pack()
            tk.Label(courses_window, text=f"Price: {course_info['price']}").pack()
            tk.Button(courses_window, text="Book Now", command=lambda id=course_id: self.book_course(id)).pack()
            tk.Label(courses_window, text="-----------------------------").pack()

    def book_course(self, course_id):
        course_info = self.courses[course_id]
        email = self.email_entry.get()
        if email in self.users:
            self.bookings[email] = {"course_id": course_id, "course_info": course_info}
            messagebox.showinfo("Success", f"Booking confirmed for {course_info['name']}!")
        else:
            messagebox.showerror("Error", "User not found. Please register or login.")
        self.master.focus_set()

def main():
    root = tk.Tk()
    app = DrivingSchoolApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
