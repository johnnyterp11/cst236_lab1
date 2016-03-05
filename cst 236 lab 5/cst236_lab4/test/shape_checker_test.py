"""
Test for source.shape_checker
"""

import urlparse
from unittest import TestCase

import os

import mock

from plugins.ReqTracer import requirements
from source.shape_checker import get_object_shape__type, get_triangle_type, get_object_shape_type_2
from source.main import Interface
from mock import patch
from git_utils import get_file_info, get_git_file_info, is_file_in_repo, has_untracked_files


class TestFilePath(TestCase):
    @requirements(['#00100'])
    @patch('subprocess.Popen')
    def test_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = is_file_in_repo("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertTrue(x)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_file_path_false(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = is_file_in_repo("C:\Users\johnny\Desktop\*.docx")
        self.assertFalse(x)
        self.assertTrue(mock_subproc_popen.called)

    @requirements(['#00120'])
    @patch('subprocess.Popen')
    def test_status_of_file(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertEquals(x, 'lab 3 b251.docx is a dirty repo')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_status_of_file_up_to_date(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertEquals(x, 'lab 3 b251.docx is up to date')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_status_of_file_modified(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('C:\\Users\johnny\Desktop\lab 3 b251.docx', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertEquals(x, 'lab 3 b251.docx has been modified locally')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_untracked_files(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('C:\Users\johnny\Desktop\*.docx', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = has_untracked_files("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertTrue(x)
        self.assertTrue(mock_subproc_popen.called)
    @patch('subprocess.Popen')
    def test_absolute_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('lab 3 b251.docx', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = is_file_in_repo("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertTrue(x)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_absolute_file_path(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('C:\Users\johnny\Desktop\*.docx', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        x = get_git_file_info("C:\Users\johnny\Desktop\lab 3 b251.docx")
        self.assertEqual(x, '')
        self.assertTrue(mock_subproc_popen.called)


class TestGetTriangleType(TestCase):
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_isosceles_second(self):
        result = get_triangle_type(2, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_isosceles_third(self):
        result = get_triangle_type(1, 2, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_type_not_list(self):
        result = get_triangle_type((1, 2), 2, 5)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_not_dict(self):
        result = get_triangle_type([1, 2], 2, 5)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_negative_num(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_negative_num_second(self):
        result = get_triangle_type(1, -1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_negative_num_third(self):
        result = get_triangle_type(1, 1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_zero_num(self):
        result = get_triangle_type(0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_zero_num_second(self):
        result = get_triangle_type(1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_zero_num_third(self):
        result = get_triangle_type(1, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_not_char(self):
        result = get_triangle_type('a', 1, 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_not_char_second(self):
        result = get_triangle_type(1, 'a', 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_type_not_char_third(self):
        result = get_triangle_type(1, 1, 'a')
        self.assertEqual(result, 'invalid')


class TestGetObjectType(TestCase):
    def test_get_square_type_square(self):
        result = get_object_shape__type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_square_type_rectangle(self):
        result = get_object_shape__type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_object_shape__type_char(self):
        result = get_object_shape__type('a', 1, 2, 1)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape__type_char_second(self):
        result = get_object_shape__type(1, 'a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape__type_char_third(self):
        result = get_object_shape__type(1, 1, 'a', 1)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape__type_char_fourth(self):
        result = get_object_shape__type(1, 1, 1, 'a')
        self.assertEqual(result, 'invalid')

    def test_get_object_type_dict(self):
        result = get_object_shape__type([1, 2], 1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape__type(self):
        result = get_object_shape__type(1, 7, 9, 10)
        self.assertEqual(result, 'invalid')

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

    def test_get_object_shape_type_2_invalid(self):
        result = get_object_shape_type_2('a', 1, 1, 1, 0, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_2nd(self):
        result = get_object_shape_type_2(1, 'a', 1, 1, 0, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_3rd(self):
        result = get_object_shape_type_2(1, 1, 'a', 1, 0, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_4th(self):
        result = get_object_shape_type_2(1, 1, 1, 'a', 0, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_5th(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 'a', 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_6th(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 90, 'a', 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_7th(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 90, 90, 'a', 90)
        self.assertEqual(result, 'invalid')

    def test_get_object_shape_type_2_invalid_8th(self):
        result = get_object_shape_type_2('a', 1, 1, 1, 90, 90, 90, 'a')
        self.assertEqual(result, 'invalid')


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

    def test_correct_no_question(self):
        x = Interface()
        self.assertEqual(x.correct(answer="Inside the bag"), 'Please ask a question first')

    def test_ask_invalid(self):
        x = Interface()
        with self.assertRaises(Exception) as context:
            x.ask(123)
            self.assertTrue('Not A String!' in context.exception)
