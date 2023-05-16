def main():
    class Welcome:
        welcome = "Welcome new user"

    class Question:
        def question(self):
            self.question_one = int(input("Write in number between 1 and 1000: "))
            if self.question_one > 1000:
                pass
                while self.question_one >= 1001:
                    print()
                    self.question_one = int(input("Write in number between 1 and 1000: "))
            else:
                self.operation = self.question_one % 2
                if self.operation == 0:
                    print()
                    print("The number " + str(self.question_one) + " is even")
                else:
                    print()
                    print("The number " + str(self.question_one) + " is odd")


    welcome_one = Welcome()
    question_one_master = Question()

    print(welcome_one.welcome)
    print()
    question_one_master.question()



if __name__ == '__main__':
    main()