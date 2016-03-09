from unittest import TestCase
from test.plugins.ReqTracer import story
from source.job_story_end import check_current_time, fiboncci_number, \
    check_n_pi, conversion_func, ask_user, \
    ten_conversions, check_legal_age_to_drive, yellow_book, \
    convert_radian_to_degrees, event_calender, cube
from source.main import Interface, QA


class _TestJobStory(TestCase):
    @story('When I ask "What time is it?" I want to be given '
           'the current date/time so I can stay up to date')
    def test_check_current_time(self):
        """
        func that test for current time
        :rtype: object

        """
        QA('what time is it?', check_current_time())

    @story('When I ask "What is the n digit of fibonacci" I want to receive '
           'the answer so I do not have to figure it\
                out myself')
    def test_check_nDigit_Fiboncci(self):
        """
        func that test for fiboncci digit
        :rtype: object

        """
        QA('What is the 7TH digit of fibonacci', fiboncci_number(num=7))

    @story(
        'When I ask "What is the n digit of pi" I want to receive the answer '
        'so I do not have to figure it out myself')
    def test_check_nDigit_Pi(self):
        """
        func that test for digit of pi
        :rtype: object

        """
        QA('What is the 2ND digit of pi', check_n_pi(2))

    @story(
        'When I ask "Please clear memory" I want the application to '
        'clear user set questions and answers\
         so I can reset the application')
    def test_check_memory_cleared(self):
        """
        func that test for memory cleared
        :rtype: object

        """
        interface = Interface()
        result = interface.delete()
        self.assertEqual(result, interface.checkdelete())
        QA('Please clear memory', interface.checkdelete())

    def test_check_delete(self):
        """
        func that test for deleted data
        :rtype: object

        """
        interface = Interface()
        self.assertEqual(interface.checkdelete(), 1)

    @story('When I say "Open the door hal", '
           'I want the application to say "I m afraid I can not do that <user name> \
    so I know that is not an option')
    def test_ask_buttler(self):
        """
        func that test for a question
        :rtype: object

        """
        QA('Open the door hal', ask_user('john'))

    @story(
        'When I ask "Convert <number> <units> to <units>" I want to '
        'receive the converted value and units so I can\
         know the answer')
    def test_convert_unit(self):
        """
        func that test for unit conversion
        :rtype: object

        """
        QA('What is the conversion of 1 cm to meter?', conversion_func(1, 'cm', 'm'))
        result = conversion_func(1, 'cm', 'm')
        self.assertEqual(result, 0.01)

    @story('When I ask for a numberic conversion I want at least '
           '10 different units I can convert from/to')
    def test_ten_numeric(self):
        """
        func that test for 10 unit conversion
        :rtype: object

        """
        QA('What are 10 conversions of one cm ?',
           ten_conversions(1, 'cm', 'm', 'mm', 'km', 'in', 'ft', 'yd', 'mi',
                           'micron', 'micrometer'))

    def test_legal_age(self):
        """
        func that test for legal age
        :rtype: object

        """
        result = check_legal_age_to_drive('2001-10-21')
        self.assertEqual(result, 'not legal')

    def test_legal_age_invalid(self):
        """
        func that test for invalid age
        :rtype: object

        """
        result = check_legal_age_to_drive('2016-10-21')
        self.assertEqual(result, 'invalid')

    def test_legal_age_legal(self):
        """
        func that test for valid age
        :rtype: object

        """
        result = check_legal_age_to_drive('1978-10-21')
        self.assertEqual(result, 'legal')

    def test_yellow_book(self):
        """
        func that test dictionary
        :rtype: object

        """
        result = yellow_book('Robert')
        self.assertEqual(result, '555-6564612')

    def test_yellow_book_2(self):
        """
        func that test dictionary
        :rtype: object

        """
        result = yellow_book('Joly')
        self.assertEqual(result, '555-7456612')

    def test_yellow_book_3(self):
        """
        func that test dictionary
        :rtype: object

        """
        result = yellow_book('Victor')
        self.assertEqual(result, None)

    def test_yellow_book_4(self):
        """
        func that test dictionary
        :rtype: object

        """
        result = yellow_book(155328)
        self.assertEqual(result, 'Invalid')

    def test_convert_radian_to_degrees(self):
        """
        func that test conversion
        :rtype: object

        """
        result = convert_radian_to_degrees(1)
        self.assertEqual(result, 57.29577951308232)

    def test_convert_radian_to_degrees_invalid(self):
        """
        func that test for invalid conversion
        :rtype: object
        """
        result = convert_radian_to_degrees('a')
        self.assertEqual(result, 'invalid')

    def test_fiboncci_number(self):
        """
        func that test for fiboncci number
        :rtype: object

        """
        result = fiboncci_number(7)
        self.assertEqual(result, 13)

    def test_fiboncci_number_zero(self):
        """
         func that test for fiboncci number
        :rtype: object

        """
        result = fiboncci_number(0)
        self.assertEqual(result, 0)

    def test_fiboncci_number_one(self):
        """
        func that test for fiboncci number
        :rtype: object
        """
        result = fiboncci_number(1)
        self.assertEqual(result, 1)

    def test_conversion_func(self):
        """
        func that test for number conversion
        :rtype: object

        """
        result = conversion_func(1, 'mm', 'km')
        self.assertEqual(result, 1e-07)

    def test_conversion_func_2nd(self):
        """
        func that test for number conversion
        :rtype: object

        """
        result = conversion_func(1, 'in', 'ft')
        self.assertEqual(result, 0.08333333333333333)

    def test_conversion_func_3rd(self):
        """
        func that test for number conversion
        :rtype: object
        """
        result = conversion_func(1, 'yd', 'mi')
        self.assertEqual(result, 0.0005681818181818182)

    def test_event_calender_invalid(self):
        """
        func that test for invalid calender date
        :rtype: object
        """
        result = event_calender(2)
        self.assertEqual(result, 'invalid')

    def test_event_calender_valid(self):
        """
        func that test for invalid calender date
        :rtype: object
        """
        result = event_calender('January 2010')
        self.assertEqual(result, ' project start')

    def test_cube_invalid(self):
        """
        func that test for invalid cube
        :rtype: object
        """
        result = cube('a')
        self.assertEqual(result, 'invalid')

    def test_cube_valid(self):
        """
        func that test for invalid cube
        :rtype: object
        """
        result = cube(3)
        self.assertEqual(result, 27)
