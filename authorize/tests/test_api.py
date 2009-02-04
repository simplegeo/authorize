from unittest import TestCase
from authorize import gen_xml as x, responses, cim, arb, aim

class TestAPIUsage(TestCase):
    def test_aim_calls(self):
        """
        Test that the API calls using AIM are made with the correct parameters.
        """

        api = aim.Api(login=u"ciao", key=u"handsome", do_raise=True)
        assert api.server.startswith("secure")
        
        api = aim.Api(login=u"ciao", key=u"handsome", is_test=True, do_raise=True)
        assert api.server.startswith("test")
        assert api.login == "ciao"
        assert api.key == "handsome"
        assert api.required_arguments[u'x_login'] == api.login
        assert api.required_arguments[u'x_tran_key'] == api.key
        
        request_body = []
        def _fake_request(body):
            request_body.append(body)
            return u'1|1|1|This transaction has been approved.||||||40.00|CC|credit|||||||||||||||||||||||||||||||||||||||||||||||||||||||||true'
        api.request = _fake_request

        result = api.transaction(type=aim.CREDIT, amount=40, card_num=u"2222", exp_date=u"0709", trans_id=u"123456")
        
        body = request_body[0]
        assert body == """\
x_exp_date=0709&x_amount=40&x_card_num=2222&x_type=credit&x_trans_id=123456&x_login=ciao&x_tran_key=handsome&x_encap_char=&x_version=3.1&x_delim_char=%7C&x_relay_response=false&x_delim_data=true"""
    
        result = api.transaction(amount=40, card_num=u"4111111111111111",
                                 exp_date=u"0709", trans_id=u"123456",
                                 items=[[1,2,3,4], [5,6,7,8]],
                                 extra_fields={u"comment": u"on this"},
                                 authentication_indicator=1,
                                 cardholder_authentication_value=4)
        body = request_body[1]
        assert body == """\
x_cardholder_authentication_value=4&x_card_num=4111111111111111&x_line_item=%5B%3C%7C%3E1%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E2%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E3%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E4%3C%7C%3E%5D&x_line_item=%5B%3C%7C%3E5%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E6%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E7%3C%7C%3E%2C%3C%7C%3E+%3C%7C%3E8%3C%7C%3E%5D&x_amount=40&x_exp_date=0709&x_authentication_indicator=1&x_trans_id=123456&x_login=ciao&x_tran_key=handsome&x_encap_char=&x_version=3.1&x_delim_char=%7C&x_relay_response=false&x_delim_data=true&comment=on+this"""
