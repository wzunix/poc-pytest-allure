import codecs
import sys

import allure

from pic_core.api.api_requests import APIRequestsSession

# Create a new http request session log.debug("Create a new HTTP request session! ")
apiRequestsSession = APIRequestsSession()
apiRequestsSession.set_encoding('ISO-8859-1')

root_url = 'https://members-api.parliament.uk'

@allure.epic("UK Parliament API Test")
@allure.feature("LordsInterests Staff API")
@allure.story("When a user request LordsInterests staff")
@allure.description("When a user request LordsInterests staff, it should return a list of LordsInterests staff")
def test_api_reference_PolicyInterests():
    with allure.step("Step 1: request"):
        test_url = root_url+'/api/LordsInterests/staff?searchTerm=Morgan'
        headers = {'accept':'text/plain'}
        apiRequestsSession.request('GET', url=test_url, headers=headers)

        expect_status = 200
        actual_status = apiRequestsSession.response_status_code
        allure.attach("expect result:{} \n, actual result:{}".format(expect_status, actual_status), "check response code")
        assert expect_status == actual_status

        expect_total_result = 4
        actual_data = apiRequestsSession.response_json
        actual_total_result = actual_data['totalResults']
        allure.attach("actual response data: {}".format(actual_data), "display response data")
        allure.attach("expect result: {} \n, actual result: {}".format(expect_total_result,actual_total_result), "check response data")
        assert expect_total_result == actual_total_result