import time

def ask_question(question):
    print(question)
    time.sleep(1)  
    return input("User: ")

def book_appointment():
    time.sleep(2)
    doctor = ask_question("Which doctor would you like to book an appointment with?")
    date = ask_question("When would you like to book the appointment? (e.g., YYYY-MM-DD)")
    time = ask_question("What time would you prefer? (e.g., 10:00 AM)")
    time.sleep(6)
    print("\nAppointment booked successfully with Dr. {} on {} at {}.".format(doctor, date, time))

def main():
    print("WELCOME TO CareAssist!")
    print("I'll ask you a few questions to assist you.")

    name = ask_question("1. What is your full name?")
    age = ask_question("2. How old are you?")
    time.sleep(1)
    age=int(age)
    if age<=0:
        print("INVALID AGE,TYPE AGAIN")
        time.sleep(2)
        ask_question("2. How old are you?")
    gender = ask_question("3. What is your gender?")
    time.sleep(1)
    symptoms = ask_question("4. What symptoms are you experiencing?")
    time.sleep(1)
    duration = ask_question("5. How long have you been experiencing these symptoms (In Days)?")
    time.sleep(1)
    medical_history = ask_question("6. Do you have any existing medical conditions?")
    time.sleep(1)
    allergies = ask_question("7. Are you allergic to any medications?")
    time.sleep(1)
    insurance = ask_question("8. Do you have health insurance?")
    time.sleep(1)
    contact_info = ask_question("9. What is the best way to contact you?")
    time.sleep(1)
    additional_info = ask_question("10. Is there anything else you'd like to share?")
    time.sleep(1)
    if additional_info.lower() == "yes":
        print("\nPlease Contact: 9986075076 For Further Queries")
        time.sleep(5)

    book = ask_question("\nWould you like to book an appointment with a doctor? (yes/no)")
    if book.lower() == "yes":
        book_appointment()
   
    print("\nThank you", name, "for providing the information. We'll get back to you shortly.")


if __name__ == "__main__":
    main()
