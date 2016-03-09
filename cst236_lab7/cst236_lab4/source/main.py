from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_object_shape_type_2
from job_story_end import check_current_time
from git_utils import check_valid_path, get_git_file_info, get_file_info, get_repo_branch, get_repo_url, is_file_in_repo

import difflib

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', 'Why', 'Is']
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_object_shape_type_2),
            'What time is it': QA('What time is it', check_current_time()),
            'How many days?': QA('How many days?', 'How many days?'),
            'Is the file path in the repo': QA('Is the  in the repo', is_file_in_repo),
            'What is the status of the file path?'
            : QA('What is the status of the file path', get_git_file_info),
            'What is the deal with the file path'
            : QA('What is the deal with the file path', get_file_info),
            'What branch is file path'
            : QA('What branch is file path?',get_repo_branch),
            'What is the repo url'
            : QA('What is the path file come from?', get_repo_url)


        }
        self.last_question = None

    def ask(self, question=""):

        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                    if keyword[0] == "[" and keyword[-1] == "]":
                        args.append(keyword)

                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= 90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def delete(self):
        self.question_answers = {}
        return "deleted"

    def checkdelete(self):
        if self.question_answers == {}:
            return "deleted"
        else:
            return 1
    def wrapper_ask(self, ask):
        def out_put_to_log():
            outfile = open("log.txt", "w")
            for STR in ask():
                outfile.write(STR)



