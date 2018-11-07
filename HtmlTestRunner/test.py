from HtmlTestRunner.TestRunner import TestRunner

test_runner = TestRunner()
test_runner.generateReport("nela", "mac")
test_runner.addTestCase('JCcall', 'call', True)
test_runner.addTestCase('JCcall', 'term', False)

test_runner.addTestCase('JCclent', 'login', True)
html = test_runner.makeReport()

f = open("test.html", mode='w')
f.write(html)
f.close()
