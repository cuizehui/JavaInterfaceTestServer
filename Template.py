import time


class Template(object):

    def __init__(self):
        pass

    HTML_TMPL_All = """
    <?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>自动化测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2.1"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    
%(style)s
</head>
<body >
<script language="javascript" type="text/javascript">
output_list = Array();

/*level 调整增加只显示通过用例的分类 --Findyou
0:Summary //all hiddenRow
1:Failed  //pt hiddenRow, ft none
2:Pass    //pt none, ft hiddenRow
3:All     //pt none, ft none
*/
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 2 || level == 0 ) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level < 2) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
    }

    //加入【详细】切换文字变化 --Findyou
    detail_class=document.getElementsByClassName('detail');
	//console.log(detail_class.length)
	if (level == 3) {
		for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="收起"
		}
	}
	else{
			for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="详细"
		}
	}
}

function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        //ID修改 点 为 下划线 -Findyou
        tid0 = 't' + cid.substr(1) + '_' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
            document.getElementById(cid).innerText = "详细"
        }
        else {
            document.getElementById(tid).className = '';
            document.getElementById(cid).innerText = "收起"
        }
    }
}

function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>

%(heading)s
%(report)s
%(ending)s

<div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>

</body>
</html>
"""

    HTML_TMPL_STYLE = """
    <style type="text/css" media="screen">
body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
table       { font-size: 100%; }

/* -- heading ---------------------------------------------------------------------- */
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
</style>
"""

    Html_Report_Generate_Message = """
<div class='heading'>
<h1>自动化测试报告</h1>
<p class='attribute'><strong>测试人员 : </strong> %(author)s </p>
<p class='attribute'><strong>操作系统 : </strong> %(system)s</p>
<p class='attribute'><strong>开始时间 : </strong> %(begin_time)s</p>
<p class='description'></p>
</div>
    """

    Report_Message = ['5', '2', '3', '3']
    Html_Report_Head_Message = """<table id='result_table' class="table table-condensed table-bordered table-hover">
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
    <td>用例集/测试用例</td>
    <td>总计</td>
    <td>通过</td>
    <td>失败</td>
    <td>错误</td>
    <td>详细</td>
</tr>
<!-- 对应数量 -->
<tr class='failClass warning'>
    <td>MyTestCase</td>
    <td class="text-center">""" + Report_Message[0] + """</td>
    <td class="text-center">""" + Report_Message[1] + """</td>
    <td class="text-center">""" + Report_Message[2] + """</td>
    <td class="text-center">""" + Report_Message[3] + """</td>
    <td class="text-center"><a href="javascript:showClassDetail('c1',5)" class="detail" id='c1'>详细</a></td>
</tr>
<!-- 对应数量 -->"""

    Html_Pass_Message = """
<!-- pass条例 -->
<tr id='pt1_1' class='hiddenRow'>
    <td class='passCase'><div class='testcase'>testCase1</div></td>
    <td colspan='5' align='center'><span class="label label-success success">通过</span></td>
</tr>
<!-- pass条例 -->
"""
    Html_Fail_Message = """<!-- fail条例 -->
<tr id='ft1_2' class='none'>
    <td class='failCase'><div class='testcase'>testCase2</div></td>
    <td colspan='5' align='center'>
    <!--默认收起错误信息 -Findyou
    <button id='btn_ft1_2' type="button"  class="btn btn-danger btn-xs collapsed" data-toggle="collapse" data-target='#div_ft1_2'>失败</button>
    <div id='div_ft1_2' class="collapse">  -->

    <!-- 默认展开错误信息 -Findyou -->
    <button id='btn_ft1_2' type="button"  class="btn btn-danger btn-xs" data-toggle="collapse" data-target='#div_ft1_2'>失败</button>
    <div id='div_ft1_2' class="collapse in">
    <pre>
        fail——info
    </pre>
    </div>
    </td>
</tr>
<!-- fail条例 -->
    """

    HTML_TMPL_END = """
    <div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
</body>
</html>
    """


# -------------------- The end of the Template class -------------------

Template.Html_Report_Generate_Message = Template.Html_Report_Generate_Message % dict(
    author="nela",
    system="Mac",
    begin_time=time.localtime()
)

Html = Template.HTML_TMPL_All % dict(
    style=Template.HTML_TMPL_STYLE,
    heading=Template.Html_Report_Generate_Message,
    report=Template.Html_Report_Head_Message,
    ending=Template.Html_Pass_Message,
)

f = open("test.html", mode='w')
f.write(Html)
f.close()
# class resultCreater(object):
#     def __init__(self):
#         self.author = {}
#         self.time = {}
#         self.operate_system = {}
#         self.success_count = 0
#         self.failure_count = 0
#         self.error_count = 0
#
#     # 创建 测试报告
#     def startTest(self):
#         if os.path.exists(os.getcwd() + "/out"):
#             localtime = time.localtime(time.time())
#             times = str(localtime.tm_mon) + '_' + str(localtime.tm_mday) + '_' + str(localtime.tm_hour) + '_' + str(
#                 localtime.tm_min)
#         file = open(os.getcwd() + '/out/' + times + '_report.html', mode='a')
#         file.write()
#
#     def addModle(self, name):
#         pass
#
#     # 结束测试
#     def stopTest(self, test):
#         pass
#
#     #  成功
#     def addSuccess(self, test):
#         pass
#
#     #  失败
#     def addError(self, test, err):
#         pass
#
#     #  跳过
#     def addFailure(self, test, err):
#         pass
