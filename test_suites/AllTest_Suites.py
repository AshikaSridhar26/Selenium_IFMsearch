import unittest


from HtmlTestRunner import HTMLTestRunner

from HomePageTestCase.HomePgae import HomePageTest
from PricePagetestCase.getpricelist import getPriceTest
from SearchFunc.searchfunction import SearchFunctionTest

loader = unittest.TestLoader()

tc1 = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(getPriceTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SearchFunctionTest)

# FunctionalTestSuite

FunctionalTestSuite = unittest.TestSuite([tc1, tc2, tc3])
runner = HTMLTestRunner(title='Test Report', description='IfmPrice list TestReport', open_in_browser=True)
runner.run(FunctionalTestSuite)


if __name__ == '__main__':

    unittest.main()