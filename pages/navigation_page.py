import time
from utilities import custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.nav = NavigationPage(driver)

    def demoSpeed(self):
        time.sleep(0)

    # Locators

    # 1. CSS:
    _signIn = "div.hsCY-menu-item-icon.hsCY-icon-with-badge"
    _signInImg = "div.magicLinkLoginImage.unified-login"
    _flightBtn = "div.hsCY-menu-item-title.hsCY-active"
    _staysBtn = "a[aria-label='Search for hotels']"
    _carrentalBtn = "a[aria-label='Search for cars']"
    _carTrainsBusesBtn = "a[aria-label='Search for trains']"
    _packageBtn = "[aria-label='Search for packages']"
    _exploreBtn = "[aria-label='Go to Explore']"
    _travelRestrictionsBtn = "[aria-label='Find out where you can travel']"
    _tripsBtn = 'div[class=UVLb] [href="/trips"]'
    _closeSignInBtn = ".dDYU-closeIcon.dDYU-mod-theme-default"

    # 2. Xpath:
    _flights_title = "//h2[contains(.,'Find and compare cheap flights')]"
    _stays_title = "//h2[contains(.,'Find and compare hotel deals')]"
    _carrental_title = "//h2[contains(.,'Find and compare the best car rental deals')]"
    _carTrainsBuses_title = "//h2[contains(.,'Find and compare cheap trains')]"
    _package_title = "//h1[contains(.,'Search and compare vacation packages')]"
    _explore_title = "//div[contains(@id,'header-title')]"
    _travelRestrictions_title = "//h1[contains(.,'Travel restrictions worldwide')]"
    _trips_title = "//h1[contains(.,'An easier way to manage your trips')]"

    # Navigations:
    # def clickBurgerMenu(self):
    #     self.elementClick(self.LOCATOR, locatorType="css")      # we may need it for mobile
    #     time.sleep(1)

    def clickSignIn(self):
        self.elementClick(self._signIn, locatorType="css")
        # time.sleep(1)
        self.demoSpeed()

    def clickFlightBtn(self):
        self.elementClick(self._flightBtn, locatorType="css")
        self.demoSpeed()

    def clickStays(self):
        self.elementClick(self._staysBtn, locatorType="css")
        self.demoSpeed()

    def clickCarRental(self):
        self.elementClick(self._carrentalBtn, locatorType="css")
        self.demoSpeed()

    def clickCarTrainsBuses(self):
        self.elementClick(self._carTrainsBusesBtn, locatorType="css")
        self.demoSpeed()

    def clickPackages(self):
        self.elementClick(self._packageBtn, locatorType="css")
        self.demoSpeed()

    def clickExplore(self):
        self.elementClick(self._exploreBtn, locatorType="css")
        self.demoSpeed()

    def clickTravelRestrictions(self):
        self.elementClick(self._travelRestrictionsBtn, locatorType="css")
        self.demoSpeed()

    def clickTrips(self):
        self.elementClick(self._tripsBtn, locatorType="css")
        self.demoSpeed()

    # Assertions:
    def verifySignIn_page(self):
        result = self.isElementPresent(self._signInImg, locatorType="css")
        self.elementClick(self._closeSignInBtn, locatorType="css")
        if result is not None:
            return True

    def verifyFlights_page(self):
        result = self.isElementPresent(self._flights_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyStays_page(self):
        result = self.isElementPresent(self._stays_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyStays_page(self):
        result = self.isElementPresent(self._stays_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyCarRental_page(self):
        result = self.isElementPresent(self._carrental_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyCarTrainBuses_page(self):
        result = self.isElementPresent(self._carTrainsBuses_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyPackage_page(self):
        result = self.isElementPresent(self._package_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyExplore_page(self):
        time.sleep(1)
        result = self.isElementPresent(self._explore_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyTravelRestrictions_page(self):
        result = self.isElementPresent(self._travelRestrictions_title, locatorType="xpath")
        if result is not None:
            return True

    def verifyTrips_page(self):
        result = self.isElementPresent(self._trips_title, locatorType="xpath")
        if result is not None:
            return True
