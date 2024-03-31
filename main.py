import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3


class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        # Set default size of the window
        self.root.geometry("800x600")  # Adjust the dimensions as needed

        # Load background image
        self.bg_image = Image.open("image.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a Canvas widget to place the background image
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create tabs
        self.tab_control = ttk.Notebook(self.canvas)
        self.patient_tab = ttk.Frame(self.tab_control)
        self.appointment_tab = ttk.Frame(self.tab_control)
        self.doctor_tab = ttk.Frame(self.tab_control)  # Added Doctor Tab
        self.tab_control.add(self.patient_tab, text='Patients')
        self.tab_control.add(self.appointment_tab, text='Appointments')
        self.tab_control.add(self.doctor_tab, text='Doctors')  # Added Doctor Tab
        self.tab_control.pack(expand=1, fill='both')

        # Create widgets for the Patients tab
        self.patient_label = ttk.Label(self.patient_tab, text='Patient Management')
        self.patient_label.grid(row=0, column=0, padx=10, pady=10)

        # Patient Credentials Form
        self.patient_name_label = ttk.Label(self.patient_tab, text="Name:")
        self.patient_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.patient_name_entry = ttk.Entry(self.patient_tab)
        self.patient_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.patient_age_label = ttk.Label(self.patient_tab, text="Age:")
        self.patient_age_label.grid(row=2, column=0, padx=10, pady=5)
        self.patient_age_entry = ttk.Entry(self.patient_tab)
        self.patient_age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.patient_gender_label = ttk.Label(self.patient_tab, text="Gender:")
        self.patient_gender_label.grid(row=3, column=0, padx=10, pady=5)
        self.patient_gender_entry = ttk.Entry(self.patient_tab)
        self.patient_gender_entry.grid(row=3, column=1, padx=10, pady=5)

        self.patient_contact_label = ttk.Label(self.patient_tab, text="Contact:")
        self.patient_contact_label.grid(row=4, column=0, padx=10, pady=5)
        self.patient_contact_entry = ttk.Entry(self.patient_tab)
        self.patient_contact_entry.grid(row=4, column=1, padx=10, pady=5)

        self.submit_patient_button = ttk.Button(self.patient_tab, text="Submit", command=self.submit_patient)
        self.submit_patient_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Create widgets for the Appointments tab
        self.appointment_label = ttk.Label(self.appointment_tab, text='Appointment Management')
        self.appointment_label.grid(row=0, column=0, padx=10, pady=10)

        # Appointment Credentials Form
        self.patient_name_label_appointment = ttk.Label(self.appointment_tab, text="Patient Name:")
        self.patient_name_label_appointment.grid(row=1, column=0, padx=10, pady=5)
        self.patient_name_entry_appointment = ttk.Entry(self.appointment_tab)
        self.patient_name_entry_appointment.grid(row=1, column=1, padx=10, pady=5)

        self.doctor_name_label_appointment = ttk.Label(self.appointment_tab, text="Doctor Name:")
        self.doctor_name_label_appointment.grid(row=2, column=0, padx=10, pady=5)
        self.doctor_name_entry_appointment = ttk.Entry(self.appointment_tab)
        self.doctor_name_entry_appointment.grid(row=2, column=1, padx=10, pady=5)

        self.appointment_date_label = ttk.Label(self.appointment_tab, text="Appointment Date:")
        self.appointment_date_label.grid(row=3, column=0, padx=10, pady=5)
        self.appointment_date_entry = ttk.Entry(self.appointment_tab)
        self.appointment_date_entry.grid(row=3, column=1, padx=10, pady=5)

        self.appointment_time_label = ttk.Label(self.appointment_tab, text="Appointment Time:")
        self.appointment_time_label.grid(row=4, column=0, padx=10, pady=5)
        self.appointment_time_entry = ttk.Entry(self.appointment_tab)
        self.appointment_time_entry.grid(row=4, column=1, padx=10, pady=5)

        self.submit_appointment_button = ttk.Button(self.appointment_tab, text="Submit",
                                                    command=self.submit_appointment)
        self.submit_appointment_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Create widgets for the Doctors tab
        self.doctor_label = ttk.Label(self.doctor_tab, text='Doctor Management')
        self.doctor_label.grid(row=0, column=0, padx=10, pady=10)

        # Doctor Credentials Form
        self.doctor_name_label = ttk.Label(self.doctor_tab, text="Name:")
        self.doctor_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.doctor_name_entry = ttk.Entry(self.doctor_tab)
        self.doctor_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.doctor_experience_label = ttk.Label(self.doctor_tab, text="Experience:")
        self.doctor_experience_label.grid(row=2, column=0, padx=10, pady=5)
        self.doctor_experience_entry = ttk.Entry(self.doctor_tab)
        self.doctor_experience_entry.grid(row=2, column=1, padx=10, pady=5)

        self.doctor_skills_label = ttk.Label(self.doctor_tab, text="Skills:")
        self.doctor_skills_label.grid(row=3, column=0, padx=10, pady=5)
        self.doctor_skills_entry = ttk.Entry(self.doctor_tab)
        self.doctor_skills_entry.grid(row=3, column=1, padx=10, pady=5)

        self.doctor_graduation_label = ttk.Label(self.doctor_tab, text="Graduation:")
        self.doctor_graduation_label.grid(row=4, column=0, padx=10, pady=5)
        self.doctor_graduation_entry = ttk.Entry(self.doctor_tab)
        self.doctor_graduation_entry.grid(row=4, column=1, padx=10, pady=5)

        self.doctor_university_label = ttk.Label(self.doctor_tab, text="University:")
        self.doctor_university_label.grid(row=5, column=0, padx=10, pady=5)
        self.doctor_university_entry = ttk.Entry(self.doctor_tab)
        self.doctor_university_entry.grid(row=5, column=1, padx=10, pady=5)

        self.doctor_expertise_label = ttk.Label(self.doctor_tab, text="Expertise:")
        self.doctor_expertise_label.grid(row=6, column=0, padx=10, pady=5)
        self.doctor_expertise_entry = ttk.Entry(self.doctor_tab)
        self.doctor_expertise_entry.grid(row=6, column=1, padx=10, pady=5)

        self.submit_doctor_button = ttk.Button(self.doctor_tab, text="Submit", command=self.submit_doctor)
        self.submit_doctor_button.grid(row=7, columnspan=2, padx=10, pady=10)

        # Database Connection
        self.conn = sqlite3.connect('hospital.db')
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create patient, appointment, and doctor tables if they don't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS patients
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          age INTEGER,
                          gender TEXT,
                          contact TEXT)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS appointments
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          patient_name TEXT,
                          doctor_name TEXT,
                          appointment_date TEXT,
                          appointment_time TEXT)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS doctors
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          experience INTEGER,
                          skills TEXT,
                          graduation TEXT,
                          university TEXT,
                          expertise TEXT)''')

        self.conn.commit()

    def submit_patient(self):
        name = self.patient_name_entry.get()
        age = self.patient_age_entry.get()
        gender = self.patient_gender_entry.get()
        contact = self.patient_contact_entry.get()

        # Insert patient data into database
        self.c.execute('''INSERT INTO patients (name, age, gender, contact)
                           VALUES (?, ?, ?, ?)''', (name, age, gender, contact))
        self.conn.commit()

        print("Patient Details Submitted and Saved to Database:")
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)
        print("Contact:", contact)

    def submit_appointment(self):
        patient_name = self.patient_name_entry_appointment.get()
        doctor_name = self.doctor_name_entry_appointment.get()
        appointment_date = self.appointment_date_entry.get()
        appointment_time = self.appointment_time_entry.get()

        # Insert appointment data into database
        self.c.execute('''INSERT INTO appointments (patient_name, doctor_name, appointment_date, appointment_time)
                           VALUES (?, ?, ?, ?)''', (patient_name, doctor_name, appointment_date, appointment_time))
        self.conn.commit()

        print("Appointment Details Submitted and Saved to Database:")
        print("Patient Name:", patient_name)
        print("Doctor Name:", doctor_name)
        print("Appointment Date:", appointment_date)
        print("Appointment Time:", appointment_time)

    def submit_doctor(self):
        name = self.doctor_name_entry.get()
        experience = self.doctor_experience_entry.get()
        skills = self.doctor_skills_entry.get()
        graduation = self.doctor_graduation_entry.get()
        university = self.doctor_university_entry.get()
        expertise = self.doctor_expertise_entry.get()

        # Insert doctor data into database
        self.c.execute('''INSERT INTO doctors (name, experience, skills, graduation, university, expertise)
                           VALUES (?, ?, ?, ?, ?, ?)''', (name, experience, skills, graduation, university, expertise))
        self.conn.commit()

        print("Doctor Details Submitted and Saved to Database:")
        print("Name:", name)
        print("Experience:", experience)
        print("Skills:", skills)
        print("Graduation:", graduation)
        print("University:", university)
        print("Expertise:", expertise)


def main():
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
