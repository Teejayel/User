class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("User Info")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age, "yrs old")
        if self.is_rewards_member:
            print("Membership: Active")
        else:
            print("Membership: Inactive")
        print("Membership Points:", self.gold_card_points)
        print()

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Membership is now active!")
            print("200 points have been added to the account.")
        else:
            print("Already enrolled in membership program.")
        print()

    def spend_points(self, amount):
        if not self.is_rewards_member:
            print("Please enroll in membership program to spend points.")
            print()
            return
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print("Points Spent =", amount)
            print("New Point Total =", self.gold_card_points)
        else:
            print("Insufficient Points")
        print()

Ada = User("Ada", "Leg", "Ada.Leg@email.com", "34")
Ada.display_info()
Ada.spend_points(1)
Ada.enroll()
Ada.enroll()
Ada.display_info()
Ada.spend_points(50)
Ada.spend_points(250)

Sam = User("Samwise", "Gamgee", "samgee@email.com", 22)
Sam.display_info()
Sam.enroll()
Sam.spend_points(80)

Frodo = User("Frodo", "Gamgee", "frogee@email.com", 23)
Frodo.display_info()