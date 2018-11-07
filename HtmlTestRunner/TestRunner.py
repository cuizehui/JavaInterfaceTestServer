import time

from HtmlTestRunner import Template


class TestRunner(object):

    def __init__(self):
        self.html_report = ""
        self.html_generate_massage = ""
        self.html_test_tables = {}
        self.test_module = {}

    # 添加报告基本信息
    def generateReport(self, author, system):
        self.html_generate_massage = Template.Html_Report_Generate_Message % dict(
            author=author,
            system=system,
            begin_time=time.asctime(time.localtime(time.time()))
        )

    def addTestCase(self, module, case_name, result):

        # 获取此模块的数据
        module_message = self.test_module.get(str(module))
        test_table = self.html_test_tables.get(str(module))
        if module_message:
            pass_account = module_message.get("pass_account")
            fail_account = module_message.get("fail_account")
            test_cases = module_message.get("test_cases")

        else:
            module_message = {'pass_account': 0, 'fail_account': 0, 'test_cases': "", 'all_account': 0,
                              'error_account': 0}
            pass_account = 0
            fail_account = 0
            test_cases = ""
            #
            self.test_module.setdefault(str(module), module_message)
            # 添加table模版
            self.html_test_tables.setdefault(str(module), "")
        if result:
            test_cases += Template.Html_TR_Pass_Message % dict(testCaseName=str(case_name))
            pass_account += 1
        else:
            test_cases += Template.Html_TR_Fail_Message % dict(testCaseName=str(case_name))
            fail_account += 1
        all_account = pass_account + fail_account
        test_table = Template.Html_Table_Message % dict(
            testModule=module,
            all_account=all_account,
            pass_account=pass_account,
            fail_account=fail_account,
            error_account='0',
            # 添加测试结果
            testCase=test_cases
        )
        # 更新此模块测试数据
        module_message['pass_account'] = pass_account
        module_message['fail_account'] = fail_account
        module_message['test_cases'] = test_cases
        module_message['all_account'] = all_account
        self.test_module[str(module)] = module_message
        self.html_test_tables[str(module)] = test_table
        # 生成模块测试Table

    # 生成报告
    def makeReport(self):
        html_tables = ""
        for table in self.html_test_tables.values():
            html_tables += table

        self.html_report = Template.HTML_TMPL_All % dict(
            style=Template.HTML_TMPL_STYLE,
            # 报告基本信息
            heading=self.html_generate_massage,
            # 模块统计信息
            report=html_tables
        )
        return self.html_report
