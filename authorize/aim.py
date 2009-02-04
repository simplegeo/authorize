import urllib

from authorize import gen_xml as xml, util, base, responses as resp

from authorize.gen_xml import CREDIT_CARD, ECHECK
from authorize.gen_xml import AUTH_CAPTURE, AUTH_ONLY, CAPTURE_ONLY
from authorize.gen_xml import CREDIT, PRIOR_AUTH_CAPTURE, VOID

class Api(base.BaseApi):
    """
    This object is the interface to Authorize.net AIM payment API, the
    following list is a list of all arguments that the spec supports,
    you can pass all of these in the transaction method as keyword
    arguments without adding 'x_' at the beginning of the name. For
    example:
    
        result_dict = aim.transaction(
            amount=10.00,
            card_num=u"4111111111111111",
            exp_date=u"2009-07"
        )
    
    Every string argument must be unicode.
    
    
    Minimum required arguments for a transaction:
        x_login: up to 20 chars
        x_tran_key: 16 chars
        x_type: AUTH_CAPTURE (default), AUTH_ONLY, CAPTURE_ONLY, CREDIT, PRIOR_AUTH_CAPTURE, VOID
        x_amount: up to 15 digits with a decimal point, no dollar symbol, all inclusive (tax, shipping etc)
        x_card_num: between 13 and 16 digits, with x_type == CREDIT only the last 4 digits are required
        x_exp_date: MMYY, MM/YY, MM-YY, MMYYYY, MM/YYYY, MM-YYYY
        x_trans_id: only required for CREDIT, PRIOR_AUTH_CAPTURE, VOID
        x_auth_code: authorization code of an original transaction not authorized on the payment gateway,
                        6 chars only for CAPTURE_ONLY
    
    Protocol related required arguments, you MUST NOT pass these:
        x_version: 3.1
        x_delim_char: char delimitator for the response
        x_delim_data: TRUE (return a transaction response)
        x_encap_char: boh
        x_relay_response: FALSE
    
    Optional arguments or conditional arguments (arguments required only in certain cases):
        x_method: CC (default), ECHECK
        x_recurring_billing: TRUE, FALSE, T, F, YES, NO, Y, N (optional, default F)
        x_card_code: optional
        x_test_request: TRUE, FALSE, T, F, YES, NO, Y, N, 1, 0 (default FALSE)
        x_duplicate_window: avoid multiple transactions submitted. (default 0)
        x_invoice_num: up to 20 chars (optional)
        x_description: up to 255 chars (optional)

        Repeat multiple times for each itemID:
        NOTE: This argument can also be passed using a list of lists with
                the name 'items'.
        x_line_item: ItemID<|>Item name<|>item description<|>itemX quantity<|>item price (unit cost)<|>itemX taxable<|>
                     31 chars, 31 chars, 255 chars        , up to 2 digits >0, up to 2 digits >0     , TRUE, FALSE etc...

        x_first_name: billing name, 50 chars (opt)
        x_last_name: 50 chars (opt)
        x_company: 50 chars (opt)
        x_address: billing address, 60 chars (opt), required with avs
        x_city: 40 chars
        x_state: 40 chars or valid 2 char code
        x_zip: 20 chars required with avs
        x_country: 60 chars
        x_phone: 25 digits (no letters)
        x_fax: 25 digits (no letters)
        x_email: up to 255 chars
        x_email_customer: send an email to the customer: TRUE, FALSE, T, F, YES, NO, Y, N, 1, 0
        x_header_email_receipt: plain text, header of the email receipt
        x_footer_email_receipt: plain text, footer of the email receipt
        x_cust_id: merchant customer id, 20 chars
        x_customer_ip: customer ip address, 15 chars, (Useful for fraud detection)
    
        x_ship_to_first_name: 50 chars
        x_ship_to_last_name: 50 chars
        x_ship_to_company: 50 chars
        x_ship_to_address: 60 chars
        x_ship_to_city: 40 chars
        x_ship_to_state: 40 chars or 2 char state code
        x_ship_to_zip: 20 chars
        x_ship_to_country: 60 chars
    
        x_tax: tax item name<|>tax description<|>tax amount
                name of tax , describe tax     , digits with no $ sign
               x_amount includes this already
        x_freight: freight item name<|>freight description<|>freight amount
                    name of freight  , describe it        , digits with no $ sign
                x_amount includes this already
        x_duty: duty item name<|>duty description<|>duty amount
                item name      , description      , digits with no $ sign
                x_amount includes this already
        x_tax_exempt: TRUE, FALSE, T, F, YES, NO, Y, N, 1, 0
        x_po_num: 25 chars, merchant assigned purchase order number
    
        x_authenticator_indicator: only AUTH_CAPTURE or AUTH_ONLY when processed
                        through cardholder authentication program
        x_cardholder_authentication_value: only AUTH_CAPTURE or AUTH_ONLY when processed
                        through cardholder authentication program
        valid combinations of the fields above:
         VISA:
          indicator - value
          -----------------
            5 - something
            6 - something
            6 - <blank>
            7 - <blank>
            7 - something
            <blank> - <blank>
          MasterCard:
           indicator - value
           -----------------
            0 - <blank>
            2 - something
            1 - Null
            Null - Null
        
    there are also custom fields that will be added to the transaction
    and can be passed to the transaction method using the keyword argument:
        extra_fields of type C{dict}
        
        like:
            
            result_dict = aim.transaction(
                amount=10.00,
                card_num=u"4111111111111111",
                exp_date=u"2009-07",
                extra_fields={u'color': u'blue',
                              u'comment': u'ring twice at the door'}
            )
            
        
    """
    responses = resp.aim_codes
    
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        if not self.is_test:
            self.server = "secure.authorize.net"
        else:
            self.server = "test.authorize.net"

        self.path = "/gateway/transact.dll"
        self.headers = {'Content-Type': 'x-www-url-encoded'}
        self.required_arguments = {
            'x_login': self.login,
            'x_tran_key': self.key,
            'x_delim_char': u'|',
            'x_encap_char': u'',
            'x_delim_data': True,
            'x_relay_response': False,
            'x_version': u'3.1'
        }

    def transaction(self, **kwargs):
        """
        Create a transaction with the service through aim
        """
        extra_fields = kwargs.pop('extra_fields', {})
        argslist = []
        for field, value in kwargs.iteritems():
            if field == "items":
                # these are the items that are bought here.
                field_name = "x_line_item"
                for item in value:
                    argslist.append((field_name, "<|>".join(unicode(item))))
            else:
                if field == "authentication_indicator" or \
                   field == "cardholder_authentication_value":
                    value = unicode(urllib.quote(str(value)))
                field_name = "x_" + field
                if isinstance(value, list):
                    value = u'<|>'.join(value)
                
                argslist.append((field_name, xml.convert(value)))

        for args in [self.required_arguments, extra_fields]:
            for field, value in args.iteritems():
                argslist.append((field, xml.convert(value)))
        body = urllib.urlencode(argslist)
        return self.request(body)

    def parse_response(self, response):
        """
        Parse the response string.
        
        @param response: The response string
        @type response: C{str}
        """
        dict_response =  xml.parse_direct_response(response)
        if dict_response.code != u"1":
            if self.do_raise:
                raise resp.AuthorizeError(dict_response.code,
                                          dict_response.reason_text,
                                          dict_response)
        return dict_response
