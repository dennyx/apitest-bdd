EMAIL_TEMPLATE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>自动化测试报告</title>
</head>

<body>
    <table width="1000px" align="center" cellspacing="0" cellpadding="0" style='border-collapse: collapse;font-size: 16px; color: #333;font-family:"微软雅黑","sans-serif";'>
        <tr>
            <td>
                <table align="center" border="0" cellspacing="0" cellspadding="0" width="900">
                    <tr>
                        <td colspan="" height="8"></td>
                    </tr>
                    <tr class="email-title">
                        <td valign="middle" height="77px" style="font-size: 30px;line-height: 77px;border-bottom:1px solid #baccd7;padding: 0;">
                            <img src="https://localhost/static/img/qa.f9b3524.jpg" alt="" width="52" height="52">测试结果</td>
                    </tr>
                    <tr>
                        <td colspan="">
                            <table border="0" cellspacing="0" cellpadding="0" width="760" align="center">
                                <tr>
                                    <td width="20"></td>
                                    <td width="205" height="58">执行时间</td>
                                    <td width="514">%s</td>
                                </tr>                                
                                <tr>
                                    <td colspan="3" style="border-bottom:1px dashed #baccd7;"></td>
                                </tr>
                                <tr>
                                    <td width="20"></td>
                                    <td width="205" height="58"> 成功用例</td>
                                    <td width="514">%s</td>
                                </tr>
                                <tr>
                                    <td colspan="3" style="border-bottom:1px dashed #baccd7;"></td>
                                </tr>
                                <tr>
                                    <td width="20"></td>
                                    <td width="205" height="58">
                                        失败用例
                                    </td>
                                    <td width="514" style="color:red;">%s</td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" style="border-bottom:1px dashed #baccd7;"></td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="12"></td>
                                </tr>
                                <tr>
                                    <td width="20"></td>
                                    <td width="205" height="" valign="top" style="line-height: 38px;">跳过用例</td>
                                    <td width="514">%s</td>
                                </tr>
                                <tr>
                                    <td colspan="3" style="border-bottom:1px dashed #baccd7;"></td>
                                </tr>
                                <tr>
                                    <td width="20"></td>
                                    <td width="205" height="" valign="top" style="line-height: 38px;">耗时</td>
                                    <td width="514">%s</td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="35"></td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="35"></td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="35"></td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="35"></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td align="center" height="57" style="color:#555;font-size: 14px;background-color: #b5dff9;">
                邮件为脚本自动发送，请勿回复
            </td>
        </tr>
    </table>
</body>

</html>
"""