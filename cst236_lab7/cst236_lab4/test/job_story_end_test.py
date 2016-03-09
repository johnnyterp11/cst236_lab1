from unittest import TestCase
from plugins.ReqTracer import story
from source.job_story_end import check_current_time, fiboncci_number, check_n_pi, conversion_func, ask_user, \
    ten_conversions, check_legal_age_to_drive, yellow_book, convert_radian_to_degrees, event_calender, cube
from source.main import Interface, QA




class TestJobStory(TestCase):
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_check_current_time(self):
        QA('what time is it?', check_current_time())

    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I do not have to figure it\
                out myself')
    def test_check_nDigit_Fiboncci(self):
        QA('What is the 7TH digit of fibonacci', fiboncci_number(n=7))

    @story(
        'When I ask "What is the n digit of pi" I want to receive the answer so I do not have to figure it out myself')
    def test_check_nDigit_Pi(self):
        QA('What is the 2ND digit of pi', check_n_pi(2))

    @story(
        'When I ask "Please clear memory" I want the application to clear user set questions and answers\
         so I can reset the application')
    def test_check_memory_cleared(self):
        x = Interface()
        result = x.delete()
        self.assertEqual(result, x.checkdelete())
        QA('Please clear memory', x.checkdelete())

    def test_check_delete(self):
        x = Interface()
        self.assertEqual(x.checkdelete(), 1)

    @story('When I say "Open the door hal", I want the application to say "I m afraid I can not do that <user name> \
    so I know that is not an option')
    def test_ask_buttler(self):
        QA('Open the door hal', ask_user('john'))

    @story(
        'When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can\
         know the answer')
    def test_convert_unit(self):
        QA('What is the conversion of 1 cm to meter?', conversion_func(1, 'cm', 'm'))
        result = conversion_func(1, 'cm', 'm')
        self.assertEqual(result, 0.01)

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_ten_numeric(self):
        QA('What are 10 conversions of one cm ?', ten_conversions(1, 'cm', 'm', 'mm', 'km', 'in', 'ft', 'yd', 'mi',
                                                                  'micron', 'micrometer'))

    def test_legal_age(self):
        result = check_legal_age_to_drive('2001-10-21')
        self.assertEqual(result, 'not legal')

    def test_legal_age_invalid(self):
        result = check_legal_age_to_drive('2016-10-21')
        self.assertEqual(result, 'invalid')

    def test_legal_age_legal(self):
        result = check_legal_age_to_drive('1978-10-21')
        self.assertEqual(result, 'legal')

    def test_yellow_book(self):
        result = yellow_book('Robert')
        self.assertEqual(result, '555-6564612')

    def test_yellow_book_2(self):
        result = yellow_book('Joly')
        self.assertEqual(result, '555-7456612')

    def test_yellow_book_3(self):
        result = yellow_book('Victor')
        self.assertEqual(result, None)

    def test_yellow_book_4(self):
        result = yellow_book(155328)
        self.assertEqual(result, 'Invalid')

    def test_convert_radian_to_degrees(self):
        result = convert_radian_to_degrees(1)
        self.assertEqual(result, 57.29577951308232)

    def test_convert_radian_to_degrees_invalid(self):
        result = convert_radian_to_degrees('a')
        self.assertEqual(result, 'invalid')

    def test_fiboncci_number(self):
        result = fiboncci_number(7)
        self.assertEqual(result, 13)

    def test_fiboncci_number_zero(self):
        result = fiboncci_number(0)
        self.assertEqual(result, 0)

    def test_fiboncci_number_one(self):
        result = fiboncci_number(1)
        self.assertEqual(result, 1)

    def test_conversion_func(self):
        result = conversion_func(1, 'mm', 'km')
        self.assertEqual(result, 1e-07)

    def test_conversion_func_2nd(self):
        result = conversion_func(1, 'in', 'ft')
        self.assertEqual(result, 0.08333333333333333)

    def test_conversion_func_3rd(self):
        result = conversion_func(1, 'yd', 'mi')
        self.assertEqual(result, 0.0005681818181818182)

    def test_event_calender_invalid(self):
        result = event_calender(2)
        self.assertEqual(result, 'invalid')

    def test_event_calender_valid(self):
        result = event_calender('January 2010')
        self.assertEqual(result, ' project start')

    def test_cube_invalid(self):
        result = cube('a')
        self.assertEqual(result, 'invalid')

    def test_cube_valid(self):
        result = cube(3)
        self.assertEqual(result, 27)
