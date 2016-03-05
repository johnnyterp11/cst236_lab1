import time
from decimal import *
from unittest import TestCase
from plugins.ReqTracer import story
from source.job_story_end import check_current_time, fiboncci_number, check_n_pi


class TestJobStory(TestCase):
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_check_current_time(self):
        result = check_current_time()
        self.assertEqual(result, time.strftime("%a,%b"))

    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I do not have to figure it out myself')
    def test_check_nDigit_Fabrnoci(self):
        result = fiboncci_number(7)
        self.assertEqual(result, 13)
    @story('When I ask "What is the n digit of pi" I want to receive the answer so I do not have to figure it out myself')
    def test_check_nDigit_Pi(self):
        result = check_n_pi(2)
        self.assertEquals(result,Decimal('3.1417') )

#    @story('When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')

        # --    @story('When I say "Open the door hal", I want the application to say "I m afraid I can not do that <user name> so I know that is not an option')

        # --    @story('When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer')

        # --   @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
