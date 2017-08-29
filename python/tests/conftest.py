import pytest

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
        extra.append(pytest_html.extras.image("C:/Users/alex.villanova.ext/Documents/develop/automacao/python/Projeto2/resources/files/output/"+item.name+".png"))
        #if (report.skipped and xfail) or (report.failed and not xfail):
        report.extra = extra
