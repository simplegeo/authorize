import httplib

from authorize import xml

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

    def request(self, body):
        """
        @param body: An XML formatted message for Authorize.net services.
        @type body: L{str}
        """
        if self.async:
            return self.asyncrequest(body)
        conn = httplib.HTTPSConnection(self.server)
        conn.request("POST", self.path, body, headers={'Content-Type': 'text/xml'})
        return xml.to_dict(conn.getresponse().read(), self.responses, do_raise=self.do_raise)

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
                              headers={'Content-Type': 'text/xml'}
            ).addCallback(xml.to_dict, self.responses, do_raise=self.do_raise)