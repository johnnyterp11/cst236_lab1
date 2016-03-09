"""
Test for source.shape_checker
"""

from unittest import TestCase
import mock
from test.plugins.ReqTracer import requirements
from source.shape_checker import get_object_shape__type, get_triangle_type, get_object_shape_type_2
from source.job_story_end import cube, event_calender, yellow_book, check_legal_age_to_drive
from source.main import Interface
from mock import patch
from git_utils import get_file_info, get_git_file_info
from git_utils import is_file_in_repo, has_untracked_files, get_repo_url, \
    get_repo_branch
import time


class _TestPerformance(TestCase):
    @requirements(['#0051'])
    def test_question(self):
        """"
        func: test question performance
        :param  self
        :return performance time of ask method
        """
        interface = Interface()
        start = time.clock()
        val = interface.ask("Why are you like this?")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_question2(self):
        """
        func test question performance with error condition
        no question mark
        :param self
        :return:
        """
        interface = Interface()
        start = time.clock()
        val = interface.ask("Why are you like this")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_question3(self):
        """
        func test question performance with error condition
        no key word
        :param self
        :return: performance time of ask method
        """
        interface = Interface()
        start = time.clock()
        val = interface.ask("are you like this?")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_question4(self):
        """
        func test question performance with error condition
        string input
        :param self
        :return: performance time of ask method
        """
        interface = Interface()
        start = time.clock()
        val = interface.ask("1236")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_question5(self):
        """
        func test question performance with error condition
        triple question marks
        :param self
        :return: performance time of ask method
        """
        interface = Interface()
        start = time.clock()
        val = interface.ask("Why are you like this???")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    @requirements(['#0051'])
    def test_answer(self):
        """
        func test answer performance
        :param self
        :return: performance time of correct method
        """
        interface = Interface()
        start = time.clock()
        val = interface.correct("No respond")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_teach(self):
        """
        func test answer performance
        string input
        :param self
        :return: performance time of teach method
        """
        interface = Interface()
        start = time.clock()
        val = interface.teach("No respond")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_performance_cube(self):
        """
        func test cube method performance
        :param self
        :return: performance time of cube method
        """
        start = time.clock()
        val = cube(12)
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 3)

    def test_performance_cube2(self):
        """
        func test cube method performance
        with large number
        :param self
        :return: performance time of cube method
        """
        start = time.clock()
        val = cube(5551552355555555555555555555555555555555555555)
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 3)

    def test_calender(self):
        """
        func test event_calender method performance
        :param self
        :return: performance event_calender method
        """
        start = time.clock()
        val = event_calender("January 2010")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_calender2(self):
        """
        func test event_calender method performance
        :param self
        :return: performance event_calender method
        """
        start = time.clock()
        val = event_calender("February 2010")
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_calender3(self):
        """
        func test event_calender method performance with error condition
        input string
        :param self
        :return: performance event_calender method
        """
        start = time.clock()
        val = event_calender(2105656)
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_yellow_book(self):
        """
        func test yellow_book method performance
        :param self
        :return: performance yellow_book method
        """
        start = time.clock()
        val = yellow_book('Robert')
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_yellow_book2(self):
        """
        func test yellow_book method performance
        :param self
        :return: performance yellow_book method
        """
        start = time.clock()
        val = yellow_book('Joly')
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_yellow_book3(self):
        """
        func test yellow_book method performance with error condition
        int input instead of string
        :param self
        :return: performance yellow_book method
        """
        start = time.clock()
        val = yellow_book(151896)
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_check_legal_age_to_drive(self):
        """
        func test check_legal_age_to_drive method performance
        :param self
        :return: performance check_legal_age_to_drive method
        """
        start = time.clock()
        val = check_legal_age_to_drive('1990-10-12')
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)

    def test_check_legal_age_to_drive2(self):
        """
        func test check_legal_age_to_drive method performance with error condition
        age older than existing date
        :param self
        :return: performance check_legal_age_to_drive method
        """
        start = time.clock()
        val = check_legal_age_to_drive('2016-10-21')
        proc_time = time.clock() - start
        self.assertTrue(val)
        self.assertLessEqual(proc_time, 0.5)


class _TestFilePath(TestCase):
    @requirements(['#00100'])
    @patch('subprocess.Popen')
    def test_file_path(self, mock_subproc_popen):
        """
        test func using mock to test the file path
        :param mock_subproc_popen:
        :return: valid if the path exists
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = is_file_in_repo \
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_file_path_false(self, mock_subproc_popen):
        """
        test func using mock to test the file path
        :param mock_subproc_popen:
        :return: valid if the file does not exists
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            'C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = is_file_in_repo\
            ("'C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertEquals(value, 'No')
        self.assertFalse(mock_subproc_popen.called)

    @requirements(['#00120'])
    @patch('subprocess.Popen')
    def test_status_of_file(self, mock_subproc_popen):
        """
        test func using mock to test the file status
        :param mock_subproc_popen:
        :return: valid if the file is in dirty repo
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_git_file_info\
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertEquals(value, 'projectRequirements.txt is a dirty repo')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_status_of_file_up_to_date(self, mock_subproc_popen):
        """
        test func using mock to test the file status
        :param mock_subproc_popen:
        :return: valid if the file is up to date
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_git_file_info\
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertEquals(value, 'projectRequirements.txt is up to date')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_status_of_file_modified(self, mock_subproc_popen):
        """
        test func using mock to test the file status
        :param mock_subproc_popen:
        :return: valid if the file been modified locally
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_git_file_info\
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertEquals(value, 'projectRequirements.txt has been modified locally')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_is_file_in_repo(self, mock_subproc_popen):
        """
        test func using mock to test the file repo
        :param mock_subproc_popen:
        :return: valid if the file is in the repo
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = is_file_in_repo("projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_untracked_file(self, mock_subproc_popen):
        """
        test func using mock to test the un-tracked files
        :param mock_subproc_popen:
        :return: valid if the path is in dirty repo
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\*.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = has_untracked_files\
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_get_abs_path(self, mock_subproc_popen):
        """
        test func using mock to test the absolute file path
        :param mock_subproc_popen:
        :return: valid if the path is absolute
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_git_file_info("projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_get_file_up_to_date(self, mock_subproc_popen):
        """
        test func using mock to test the file is up to date
        :param mock_subproc_popen:
        :return: valid if the file is up to date
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_git_file_info\
            ("C:\\Users\\Zed\\Desktop\\cst 236 lab 7\\cst236_lab4\\projectRequirements.txt")
        self.assertEqual(value, 'projectRequirements.txt is up to date')
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_get_git_file_exce(self, mock_subproc_popen):
        """
        test func using mock to test the file git path
        :param mock_subproc_popen:
        :return: valid if the path does not exist
        """
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = "c"
        self.assertRaisesRegexp(Exception,
                                'Path c does not exist cannot get git file', get_git_file_info, value)

    @requirements(['#00140'])
    @patch('subprocess.Popen')
    def test_get_repo_url(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_repo_url("projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @patch('subprocess.Popen')
    def test_get_file_info(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_file_info("projectRequirements.txt")
        self.assertTrue(value)
        self.assertTrue(mock_subproc_popen.called)

    @requirements(['#00130'])
    @patch('subprocess.Popen')
    def test_get_repo_branch(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (
            "projectRequirements.txt", '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        value = get_repo_branch("projectRequirements.txt")
        self.assertTrue(value)
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
        self.assertEqual(
            x.ask(question="How are you doing?"),
            "I don't know, please provide the answer")
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
        self.assertEqual(x.ask(question="How many days in a year"),
                         'Was that a question?')

    @requirements(['#0010', '#0014'])
    def test_break_question_into_words(self):
        x = Interface()
        self.assertEqual(x.ask(question="Whattypeoftriangleisthis?"),
                         'Was that a question?')
        self.assertEqual(x.ask
                         (question="How are you living these days?"),
                         "I don't know, please provide the answer")

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
            self.assertEqual(x.ask(question="Where is the library?"),
                             "I don't know, please provide the answer")

    @requirements(['#0015'])
    def test_provide_means_to_answer(self):
        x = Interface()
        self.assertEqual(x.ask(question="How many days till the examine?"),
                         "I don't know, please provide the answer")

    @requirements(['#0017', '#0021'])
    def test_correct_keyword_answer(self):
        x = Interface()
        self.assertEqual(x.teach(answer="twenty one "), 'Please ask a question first')

    @requirements(['#0018'])
    def test_teach_different_answer(self):
        x = Interface()
        x.ask(question="Where is the library?")
        x.teach(answer="across the street")
        self.assertEqual(x.teach(answer="across the valley"),
                         'I don\'t know about that. I was taught differently')

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
