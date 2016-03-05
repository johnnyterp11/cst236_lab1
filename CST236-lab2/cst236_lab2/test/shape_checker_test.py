"""
Test for source.shape_checker
"""

from unittest import TestCase
from plugins.ReqTracer import requirements
from source.shape_checker import get_object_shape__type, get_triangle_type, get_object_shape_type_2
from source.question_answer import QA
from source.main import Interface


class TestGetTriangleType(TestCase):
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')


class TestGetObjectType(TestCase):
    def test_get_square_type_square(self):
        result = get_object_shape__type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_square_type_rectangle(self):
        result = get_object_shape__type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_square_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_rectangle_type_2(self):
        result = get_object_shape_type_2(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_rhombus_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 35, 145, 35, 145)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_disconnected_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 0, 90, 90, 90)
        self.assertEqual(result, 'disconnected')


class TestQuestionnairre(TestCase):
    @requirements(['#0006'])
    def test_question_answer_string_type(self):
        x = Interface()
        self.assertEqual(x.ask(question="How are you doing?"), "I don't know, please provide the answer")
        self.assertEqual(x.correct(answer=" fine thank you "), None)

    @requirements(['#0007'])
    def test_questions_keywords(self):
        x = Interface()
        self.assertEqual(x.ask(question="How ?"), "I don't know, please provide the answer")
        self.assertEqual(x.ask(question="How ?"), "I don't know, please provide the answer")
        self.assertEqual(x.ask(question="Where ?"), "I don't know, please provide the answer")
        self.assertEqual(x.ask(question="Who ?"), "I don't know, please provide the answer")
        self.assertEqual(x.ask(question="Why ?"), "I don't know, please provide the answer")

    @requirements(['#0008'])
    def test_invalid_keyword(self):
        x = Interface()
        self.assertEqual(x.ask(question="Whaaat ?"), 'Was that a question?')

    @requirements(['#0009'])
    def test_question_string_type(self):
        x = Interface()
        self.assertEqual(x.ask(question="How many days in a year"), 'Was that a question?')

    @requirements(['#0010', '#0014'])
    def test_break_question_into_words(self):
        x = Interface()
        self.assertEqual(x.ask(question="Whattypeoftriangleisthis?"), 'Was that a question?')
        self.assertEqual(x.ask(question="How are you living these days?"), "I don't know, please provide the answer")

    @requirements(['#0011'])
    def test_match_question_answer(self):
        x = Interface()

    @requirements(['#0012'])
    def test_exclude_numbers(self):
        x = Interface()
        x.ask(question="How old are you?")
        self.assertEqual(x.correct(answer=12), None)

    @requirements(['#0013'])
    def test_valid_match(self):
        x = Interface()
        x.ask(question="Where is the library?")
        if x.correct(answer="across the street") == "across the street":
            self.assertEqual(x.ask(question="Where is the library?"), "across the street")

    @requirements(['#0014'])
    def test_non_valid_match(self):
        x = Interface()
        x.ask(question="Where is the library?")
        if x.teach(answer="across the street") != "across the valley":
            self.assertEqual(x.ask(question="Where is the library?"), "I don't know, please provide the answer")

    @requirements(['#0015'])
    def test_provide_means_to_answer(self):
        x = Interface()
        self.assertEqual(x.ask(question="How many days till the examine?"), "I don't know, please provide the answer")

    @requirements(['#0017', '#0021'])
    def test_correct_keyword_answer(self):
        x = Interface()
        self.assertEqual(x.teach(answer="twenty one "), 'Please ask a question first')

    @requirements(['#0018'])
    def test_teach_different_answer(self):
        x = Interface()
        x.ask(question="Where is the library?")
        x.teach(answer="across the street")
        self.assertEqual(x.teach(answer="across the valley"), 'I don\'t know about that. I was taught differently')

    @requirements(['#0019'])
    def test_system_update(self):
        x = Interface()
        x.ask(question="Where is the library?")
        x.teach(answer="across the street")
        x.correct("across the river")


