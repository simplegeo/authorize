import httplib

from authorize import gen_xml as xml

class BaseApi(object):
    """
    Base Api object.
    """
    responses = None
    def __init__(self, login, key, is_test=False, do_raise=False, async=False):
        """
        @param login: login key given by authorize.net
        @type login: L{unicode}
        
        @param key: transaction key given by authorize.net
        @type key: L{unicode}
        
        @param is_test: Use the test sandbox from authroize.net
        @type is_test: L{bool}
        """
        if is_test:
            self.server = 'apitest.authorize.net'
        else:
            self.server = 'api.authorize.net'
        self.path = "/xml/v1/request.api"
        self.is_test = is_test
        self.login = login
        self.key = key
        self.do_raise = do_raise
        self.async = async
        self.headers = {'Content-Type': 'text/xml'}

    def request(self, body):
        """
        @param body: An XML formatted message for Authorize.net services.
        @type body: L{str}
        """
        if self.async:
            return self.asyncrequest(body)
        conn = httplib.HTTPSConnection(self.server)
        conn.request("POST", self.path, body, headers=self.headers)
        return self.parse_response(conn.getresponse().read())

    def asyncrequest(self, body):
        """
        Runs the request inside twisted matrix in an asynchronous way.

        @param body: An XML formatted message for Authorize.net services.
        @type body: L{str}
        """
        from twisted.web import client
        return client.getPage("https://"+self.server+self.path,
                              method="POST",
                              postdata=body,
                              headers=self.headers
            ).addCallback(self.parse_response)
    
    def parse_response(self, response):
        """
        Parse the response from the web service, check also if we want
        to raise the error as opposed to return an error object.
        """
        return xml.to_dict(response, self.responses, self.do_raise)