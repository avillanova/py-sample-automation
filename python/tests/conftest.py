import pytest
import os
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        extra.append(pytest_html.extras.html('<h3>'+item.name+'</3>'))
        print os.path
        extra.append(pytest_html.extras.image(os.getcwd()+"/resources/files/output/"+item.name+".png"))
        #if (report.skipped and xfail) or (report.failed and not xfail):
        report.extra = extra
