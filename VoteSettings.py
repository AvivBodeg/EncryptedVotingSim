from QuestionInfo import QuestionInfo


class VoteSettings:
    def __init__(self, question, opt1, opt2, num_voters):
        self.num_voters = num_voters
        self.question_info = QuestionInfo(question, opt1, opt2)
