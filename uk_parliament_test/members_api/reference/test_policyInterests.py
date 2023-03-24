import codecs
import sys

import allure

from pic_core.api.api_requests import APIRequestsSession

# Create a new http request session log.debug("Create a new HTTP request session! ")
apiRequestsSession = APIRequestsSession()
apiRequestsSession.set_encoding('ISO-8859-1')

root_url = 'https://members-api.parliament.uk'

@allure.epic("UK Parliament API Test")
@allure.feature("Reference PolicyInterests API")
@allure.story("When a user request policy interests")
@allure.description("When a user request policy interests, it should return a list of policy interests")
def test_api_reference_PolicyInterests():
    with allure.step("Step 1: request"):
        test_url = root_url+'/api/Reference/PolicyInterests'
        headers = {'accept':'text/plain'}
        apiRequestsSession.request('GET', url=test_url, headers=headers)

        expect_status = 200
        actual_status = apiRequestsSession.response_status_code
        allure.attach("expect result:{} \n, actual result:{}".format(expect_status, actual_status), "check response code")
        assert expect_status == actual_status

        expect_data_length = 20
        actual_data = apiRequestsSession.response_json
        actual_data_length = len(actual_data)
        allure.attach("actual response data: {}".format(actual_data), "display response data")
        allure.attach("expect result: {} \n, actual result: {}".format(expect_data_length,actual_data_length), "check response data")
        assert expect_data_length == actual_data_length