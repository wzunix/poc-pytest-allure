import requests
from pic_core.file import pic_json
from pic_core.utils.log import getMyLogger
import urllib3
log = getMyLogger(__name__)


class APIRequestsSession(object):
    def __init__(self):
        self._session = requests.Session()
        self._response = None
        self._request = None
        self._default_encoding = 'utf-8'
        self._proxy_string = None

    @property
    def response_status_code(self):
        return self._response.status_code

    @property
    def response_headers(self):
        return self._response.headers

    @property
    def response_text(self):
        return self._response.text

    @property
    def response_content(self):
        return self._response.content

    @property
    def response_json(self):
        return self._response.json()

    @property
    def response_encoding(self):
        return self._response.encoding

    @property
    def request_headers(self):
        return self._response.request.headers

    @property
    def request_json_body(self):
        return pic_json.load_json_data(self._response.request.body)

    @property
    def request_body(self):
        return self._response.request.body

    @property
    def session_cookies(self):
        return self._session.cookies.get_dict()

    @property
    def proxies(self):
        return self._session.proxies

    @property
    def session(self):
        return self._session

    def set_encoding(self, ec):
        self._default_encoding = ec

    def request(self, method, url=None, data=None, json=None, headers=None, proxy_string=None, verify=False, cookies=None):
        """
           Warning msg: -  "InsecureRequestWarning: Unverified HTTPS request is being made to host 'x.com'. Adding certificate verification is strongly advised."
           To disable above warning msg with below - 'urllib3.disable_warnings'
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._response = self._session.request(method=method, url=url, data=data, json=json, headers=headers, proxies={"http": proxy_string,"https": proxy_string}, verify=verify, cookies=cookies)
        self._response.encoding = self._default_encoding
        if data and 'password' in data.keys():
            data['password'] = 'password-masked'
        if headers and 'password' in headers.keys():
                headers['password'] = 'password-masked'
        if json and 'password' in json.keys():
                json['password'] = 'password-masked'

        log.info(f"HTTP session request: method={method}, url={url}, data={data}, json={json}, headers={headers}, proxy_string={proxy_string}, verify={verify}")
