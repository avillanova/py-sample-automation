public class TestConfig {
		private WebDriver driver;
		private ExtentReports report;
		private ExtentTest logger;
		
		private DateFormat dateFormat = new SimpleDateFormat("yy-MM-dd HH-mm-ss");
		private Date date = new Date();
		private String testReportsFolder = "./Test_Report/";
		private String reportFolder = testReportsFolder + dateFormat.format(date) + "/";
		
		@Parameters({"ambienteURL", "baseURL","projectKey","user", "pass", "bugResponsable", "sprintId", "sysUser", "sysPass"})
		@BeforeSuite(alwaysRun=true)
		public void beforeSuite(String ambienteURL, String baseURL, String projectKey, String user, String pass, String bugResponsable, String sprintId, String sysUser, String sysPass, ITestContext context) {
			new File(reportFolder).mkdir();
			TestReport.createNewDir();
			setContext(context);
			JiraConnection.setBaseURL(baseURL);
			JiraConnection.setBugResponsable(bugResponsable);
			JiraConnection.setPass(pass);
			JiraConnection.setUser(user);
			JiraConnection.setPROJECT_KEY(projectKey);
			JiraConnection.setAuth(user+":"+pass);
			JiraConnection.setSprint(sprintId);
			LoginVH.setBaseTest(ambienteURL);
			LoginVH.setSysUser(sysUser);
			LoginVH.setSysPass(sysPass);
			
		}
		
		@Parameters({"browser", "ipaddress", "runKey"})
		@BeforeTest(alwaysRun=true)
		public void beforeTest(String browser, @Optional String ipaddress, String runKey, ITestContext context) {
			JiraConnection.setFlag(true);
			JiraConnection.setRunKey(runKey);
			ServerArguments serverArguments = new ServerArguments();
			AppiumServer _appiumServer = new AppiumServer(new File("CaminhoDriverAppium/Drivers/Appium"), serverArguments);
			try {
				DesiredCapabilities caps;
				switch(browser.toLowerCase()){
				/*
				case "chromegrid":
					System.setProperty("webdriver.chrome.driver", "/absolute/path/to/binary/chromedriver");
					caps = new DesiredCapabilities().chrome();
					caps.setBrowserName("chrome");
					driver=new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"),caps);
					break;
				case "edgegrid":
					caps = new DesiredCapabilities().edge();
					caps.setBrowserName("MicrosoftEdge");
					driver=new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"),caps);
					break;
				case "firefoxgrid":
					caps = new DesiredCapabilities().firefox();
					caps.setBrowserName("firefox");
					driver=new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"),caps);
					break;
				case "safarigrid":
					caps = new DesiredCapabilities().safari();
					caps.setBrowserName("Safari");
					caps.setVersion("9.1.3");
					driver=new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"),caps);
					break;
				case "nexus5": 
					caps = new DesiredCapabilities();
					caps.setCapability(MobileCapabilityType.BROWSER_NAME,"Chrome");
					caps.setCapability(MobileCapabilityType.APPIUM_VERSION,"1.4.16.1");
					caps.setCapability(MobileCapabilityType.PLATFORM_VERSION,"6.0.1");
					caps.setCapability(MobileCapabilityType.DEVICE_NAME,"ANDROID");
					caps.setCapability(MobileCapabilityType.PLATFORM_NAME,"ANDROID");
					caps.setCapability(MobileCapabilityType.UDID,"0bb3584a0369db84");
					driver = new AndroidDriver<>(new URL("http://" + ipaddress + "/wd/hub"), caps);
					break;
				case "s6edge": 
					caps = new DesiredCapabilities();
					caps.setCapability(MobileCapabilityType.BROWSER_NAME,"Chrome");
					caps.setCapability(MobileCapabilityType.APPIUM_VERSION,"1.4.16.1");
					caps.setCapability(MobileCapabilityType.PLATFORM_VERSION,"6.0.1");
					caps.setCapability(MobileCapabilityType.DEVICE_NAME,"Galaxy S6 Edge");
					caps.setCapability(MobileCapabilityType.PLATFORM_NAME,"ANDROID");
					caps.setCapability(MobileCapabilityType.UDID,"06157df635074301");
					driver = new AndroidDriver<>(new URL("http://" + ipaddress + "/wd/hub"), caps);
					break;
				case "s7edge":
					caps = new DesiredCapabilities();
					caps.setCapability(MobileCapabilityType.BROWSER_NAME,"Chrome");
					caps.setCapability(MobileCapabilityType.APPIUM_VERSION,"1.4.16.1");
					caps.setCapability(MobileCapabilityType.PLATFORM_VERSION,"6.0.1");
					caps.setCapability(MobileCapabilityType.DEVICE_NAME,"Alice on Edge");
					caps.setCapability(MobileCapabilityType.PLATFORM_NAME,"ANDROID");
					caps.setCapability(MobileCapabilityType.UDID,"ad0816030824a8630f");
					driver = new AndroidDriver<>(new URL("http://" + ipaddress + "/wd/hub"), caps);
					break;
				case "alice6":
					caps = new DesiredCapabilities();
					caps.setCapability(MobileCapabilityType.BROWSER_NAME,"Safari");
					caps.setCapability(MobileCapabilityType.APPIUM_VERSION,"1.6.3");
					caps.setCapability(MobileCapabilityType.PLATFORM_VERSION, "10.2.1");
					caps.setCapability(MobileCapabilityType.DEVICE_NAME,"Alice 6+");
					caps.setCapability(MobileCapabilityType.PLATFORM_NAME, "iOS");
					caps.setCapability(MobileCapabilityType.UDID,"8e12198cbebfc5e6aa84d9f4a2ab3c266a6d36ba");
					caps.setCapability(MobileCapabilityType.APP,"io.appium.SafariLauncher");
//					caps.setCapability("newCommandTimeout", 120);
					caps.setCapability("safariAllowPopups", false);
					caps.setCapability("safariIgnoreFraudWarning", true);
					driver=new RemoteWebDriver(new URL("http://" + ipaddress + "/wd/hub"),caps);
					driver.manage().timeouts().pageLoadTimeout(15, TimeUnit.SECONDS);
					break;
					*/
				case "firefox":
					FirefoxDriverManager.getInstance().setup();
					driver = new FirefoxDriver();
					break;
				case "chrome":
					ChromeDriverManager.getInstance().setup();
					driver = new ChromeDriver();
					break;
			/*	case "internet explorer":
					InternetExplorerDriverManager.getInstance().setup(Architecture.x32);//64 bit driver is very slow
					caps = DesiredCapabilities.internetExplorer();
					caps.setCapability(InternetExplorerDriver.IGNORE_ZOOM_SETTING, true);
					caps.setCapability(InternetExplorerDriver.NATIVE_EVENTS, true);
					driver = new InternetExplorerDriver(caps);	
					driver.manage().timeouts().pageLoadTimeout(3,TimeUnit.MINUTES);
					driver.manage().timeouts().setScriptTimeout(3, TimeUnit.MINUTES);
					break;
					*/
				}
			} catch (Exception e) {
				e.printStackTrace();
				throw new IllegalStateException("Can't start Web Driver", e);
			}
			setContext(context);
		}
		
		@Parameters({"browser", "closeDriver"})
		@AfterTest(alwaysRun=true)
		public void afterTest(ITestContext context, String browser, Boolean closeDriver) {
			if(closeDriver) {
				driver.close();
				driver.quit();
				LoginVH.isLogged = false;
			}
		}
		
		@Parameters({"closeDriver"})
		@AfterSuite(alwaysRun=true)
		public void afterSuite(ITestContext context, Boolean closeDriver) {
			try {
				Thread.sleep(5000);
				if(!closeDriver) {
				//	driver.close();
				//	driver.quit();
					LoginVH.isLogged = false;
				}//Give the last test a chance to finish before launching the next driver
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			//TestReport.close();
//			Tools.zipFolder(testReportsFolder + "Bupa" + testSet + " " +dateFormat.format(date) +".zip", reportFolder);
		}
		
		private void setContext(ITestContext context){
			context.setAttribute("driver", driver);
			context.setAttribute("report", report);
			context.setAttribute("logger", logger);
			context.setAttribute("dateFormat", dateFormat);
			context.setAttribute("date", date);
			context.setAttribute("reportFolder", reportFolder);
			context.setAttribute("testReportsFolder", testReportsFolder);
		}