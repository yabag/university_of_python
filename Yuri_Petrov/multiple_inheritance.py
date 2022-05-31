class Student:
    def pass_exam(self):
        print("Я сдал экзамен!")


class Worker:
    def work(self):
        print("Работаю...")


class FootballPlayer:
    def score(self):
        print("Забил гол!")


class StudenWorkerAndFootballPlayer(Student, Worker, FootballPlayer):
    pass


if __name__ == "__main__":
    s = StudenWorkerAndFootballPlayer()
    s.pass_exam()  # Я сдал экзамен!
    s.work()       # Работаю...
    s.score()      # Забил гол!
