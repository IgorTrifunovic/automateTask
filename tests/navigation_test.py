from pages.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NavigationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.np = NavigationPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_Navigation_Menu(self):
        self.np.clickSignIn()
        assert self.np.verifySignIn_page()

        self.np.clickFlightBtn()
        assert self.np.verifyFlights_page()

        self.np.clickStays()
        assert self.np.verifyStays_page()

        self.np.clickCarRental()
        assert self.np.verifyCarRental_page()

        self.np.clickCarTrainsBuses()
        assert self.np.verifyCarTrainBuses_page()

        self.np.clickPackages()
        assert self.np.verifyPackage_page()

        self.np.clickExplore()
        assert self.np.verifyExplore_page()

        self.np.clickTrips()
        assert self.np.verifyTrips_page()

        self.np.clickTravelRestrictions()
        assert self.np.verifyTravelRestrictions_page()



