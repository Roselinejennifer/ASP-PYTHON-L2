class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()

    def display(self):
        raise NotImplementedError("Subclasses should implement this method")

class MultipleChoiceQuestion(Question):
    def __init__(self, text, choices, correct_answer):
        super().__init__(text, correct_answer)
        self.choices = choices

    def display(self):
        print(self.text)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, answer):
        try:
            answer_index = int(answer) - 1
            return self.choices[answer_index].lower() == self.correct_answer.lower()
        except (ValueError, IndexError):
            return False

class TrueFalseQuestion(Question):
    def __init__(self, text, correct_answer):
        super().__init__(text, correct_answer)

    def display(self):
        print(self.text)
        print("1. True")
        print("2. False")

    def check_answer(self, answer):
        answer_text = "true" if answer == "1" else "false"
        return answer_text.lower() == self.correct_answer.lower()

class OpenEndedQuestion(Question):
    def __init__(self, text, correct_answer):
        super().__init__(text, correct_answer)

    def display(self):
        print(self.text)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for question in self.questions:
            question.display()
            answer = input("Your answer: ")
            if question.check_answer(answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question.correct_answer}\n")
        self.display_score()

    def display_score(self):
        print(f"Your final score is: {self.score} out of {len(self.questions)}")


questions = [
    MultipleChoiceQuestion("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris"),
    TrueFalseQuestion("The earth is flat.", "False"),
    OpenEndedQuestion("Who wrote '1984'?", "George Orwell")
]

quiz = Quiz(questions)
quiz.start()
