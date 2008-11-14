import urllib

from authorize import xml, util, base, responses as resp

from authorize.xml import BANK, CREDIT_CARD, ECHECK
from authorize.xml import AUTH_CAPTURE, AUTH_ONLY, CAPTURE_ONLY
from authorize.xml import CREDIT, PRIOR_AUTH_CAPTURE, VOID

class Api(base.BaseApi):
    """
    x_login: up to 20 chars
    x_tran_key: 16 chars
    x_type: AUTH_CAPTURE (default), AUTH_ONLY, CAPTURE_ONLY, CREDIT, PRIOR_AUTH_CAPTURE, VOID
    x_amount: up to 15 digits with a decimal point, no dollar symbol, all inclusive (tax, shipping etc)
    x_card_num: between 13 and 16 digits, with x_type == CREDIT only the last 4 digits are required
    x_exp_date: MMYY, MM/YY, MM-YY, MMYYYY, MM/YYYY, MM-YYYY
    x_trans_id: only required for CREDIT, PRIOR_AUTH_CAPTURE, VOID
    x_auth_code: authorization code of an original transaction not authorized on the payment gateway, 6 chars only for CAPTURE_ONLY

    x_delim_char: char delimitator for the response
    x_delim_data: TRUE (return a transaction response)
    x_encap_char: boh
    x_relay_response: FALSE

    submit to:
    https://secure.authorize.net/gateway/transact.dll
    
    tests:
    https://test.authorize.net/gateway/transact.dll
    
    x_version: 3.1
    x_method: CC (default), ECHECK
    x_recurring_billing: TRUE, FALSE, T, F, YES, NO, Y, N (optional, default F)
    x_card_code: optional
    x_test_request: TRUE, FALSE, T, F, YES, NO, Y, N, 1, 0 (default FALSE)
    x_duplicate_window: avoid multiple transactions submitted. (default 0)
    x_invoice_num: up to 20 chars (optional)
    x_description: up to 255 chars (optional)

    Repeat multiple times for each itemID:
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
    x_customer_ip: customer ip address, 15 chars
    
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
        
    there are also custom fields.
        
    """
    responses = responses.aim_codes
    
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        if self.is_test:
            self.server = "secure.authorize.net"
        else:
            self.server = "test.authorize.net"

        self.path = "/gateway/transact.dll"
        self.headers = {'Content-Type': 'x-www-url-encoded'}
        self.required_arguments = {
            'login': self.login,
            'tran_key': self.key,
            'delim_char': u'|',
            'encap_char': u';',
            'delim_data': True,
            'relay_response': False,
            'version': u'3.1'
        }

    def send_transact(self, **kwargs):
        extra_fields = kwargs.pop('extra_fields', {})
        argslist = []
        for field, value in kwargs.iteritems():
            if field == "items":
                # these are the items that are bought here.
                field_name = "x_line_item"
                for item in value:
                    argslist.append((field_name, "<|>".join(item)))
            else:
                if field == "authentication_indicator" or \
                   field == "cardholder_authentication_value":
                    value = urllib.quote(value)
                field_name = "x_" + field
                if isinstance(value, list):
                    value = u'<|>'.join(value)
                
                argslist.append((field_name, xml.convert(value)))

        for args in [self.required_arguments, extra_fields]:
            for field, value in args.iteritems():
                argslist.append(field, xml.convert(value))
        
        return self.request(urllib.urlencode(argslist))

    def parse_response(self, response):
        """
        Parse the response string.
        
        @param response: The response string
        @type response: C{str}
        """
        return xml.parse_direct_response(response)
