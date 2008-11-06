from authorize import xml, util, base, responses as resp

from authorize.xml import INDIVIDUAL, BUSINESS, ECHECK_CCD, ECHECK_PPD, ECHECK_TEL, ECHECK_WEB
from authorize.xml import BANK, CREDIT_CARD, VALIDATION_NONE, CAPTURE_ONLY, AUTH_CAPTURE
from authorize.xml import VALIDATION_TEST, VALIDATION_LIVE, ACCOUNT_CHECKING, ACCOUNT_SAVINGS
from authorize.xml import ACCOUNT_BUSINESS_CHECKING, AUTH_ONLY

class Api(base.BaseApi):
    """
    Main CIM api object.
    
    It implements the following api calls:
    
    NOTE: Arguments should be passed in as named arguments. Always.
    
        create_profile: create a user's profile
            arguments:
                REQUIRED:
                    customer_id: L{unicode}

                OPTIONAL or CONDITIONAL:
                    payment_profiles: L{list} containing L{dict}:
                        REQUIRED:
                            profile_type: L{CREDIT_CARD} (default) or L{BANK}
                            card_number: L{unicode} or L{int}, required with CREDIT_CARD
                            expiration_date: YYYY-MM, required with CREDIT_CARD
                            routing_number: 9 digits, required with BANK
                            account_number: 5 to 17 digits, required with BANK
                            name_on_account: required with BANK
                            
                        OPTIONAL:
                            customer_type: L{INDIVIDUAL} or L{BUSINESS}
                            bill_first_name:
                            bill_last_name: 
                            bill_company: 
                            bill_address: 
                            bill_city: 
                            bill_state: 
                            bill_zip: 
                            bill_country:
                            bill_phone:
                            bill_fax:
                        all the above arguments can simply be passed
                        as method arguments if you need to create just
                        a single payment profile.

                    description:
                    email:                    
                    account_type: L{ACCOUNT_CHECKING} or L{ACCOUNT_SAVINGS}
                            or L{ACCOUNT_BUSINESS_CHECKING}, only with BANK
                    bank_name:
                    ship_first_name:
                    ship_last_name:
                    ship_company:
                    ship_address:
                    ship_city:
                    ship_state:
                    ship_zip:
                    ship_country:
                    ship_phone:
                    ship_fax:
        
        create_payment_profile: add to a user's profile a new payment profile
            arguments:
                REQUIRED:
                    customer_profile_id: L{unicode} or L{int}
                    all the arguments for payment_profiles (above) should
                        be provided as arguments to this method call
                    validation_mode: L{VALIDATION_TEST}, L{VALIDATION_LIVE}, L{VALIDATION_NONE},
                        the different level of validation will try to run and immediately
                        void 0.01 transactions on live or test environment, L{VALIDATION_NONE}
                        will skip this test. By default it's L{VALIDATION_NONE}

        create_shipping_address: add to a user's profile a new shipping address
            arguments:
                REQUIRED:
                    customer_profile_id: L{unicode} or L{int}
                    all the arguments above starting with 'ship_' can be
                        provided here with the same name.

        create_profile_transaction: create a new transaction in the user's profile
            NOTE: The response doesn't conform exactly to the XML output given
            in the authorize.net documentation. The direct response has been
            translated into a dictionary. The list of keys is in the source.
            arguments:
                REQUIRED:
                    amount: L{float} or L{decimal.Decimal}
                    customer_profile_id: L{unicode} or L{int}
                    customer_payment_profile_id: L{unicode} or L{int}
                    profile_type: L{AUTH_ONLY}, L{CAPTURE_ONLY}, L{AUTH_CAPTURE} (default AUTH_ONLY)
                    approval_code: L{unicode}, 6 chars authorization code of an original transaction (only for CAPTURE_ONLY)
                
                OPTIONAL:
                    tax_amount:
                    tax_name:
                    tax_descr:
                    ship_amount:
                    ship_name:
                    ship_description:
                    duty_amount:
                    duty_name:
                    duty_description:
                    line_items:
                        list of dictionaries with the following arguments:
                            item_id: required
                            name: required
                            description: required
                            quantity: required
                            unit_price: required
                            taxable:
                    customer_address_id:
                    invoice_number:
                    description:
                    purchase_order_number:
                    tax_exempt: L{bool}, default False
                    recurring: L{bool}, default False
                    ccv:


        delete_profile: delete one's profile
            arguments:
                customer_profile_id: required

        delete_payment_profile: delete one of user's payment profiles
            arguments:
                customer_profile_id: required
                customer_payment_profile_id: required
                
        delete_shipping_address: delete one of user's shipping addresses
            arguments:
                customer_profile_id: required
                customer_address_id: required


        get_profile: get a user's profile
            arguments:
                customer_profile_id: required
                
        get_payment_profile: get a user's payment profile
            arguments:
                customer_profile_id: required
                customer_payment_profile_id: required
                
        get_shipping_address: get a user's shipping address
            arguments:
                customer_profile_id: required
                customer_address_id: required

        update_profile: update basic user's information
            arguments:
                customer_id: optional
                description: optional
                email: optional
                customer_profile_id: required
        
        update_payment_profile: update user's payment profile
            arguments:
                customer_profile_id: required
                
                and the same arguments for payment_profiles with the
                addition of an extra argument called
                customer_payment_profile_id added for each payment_profile
                that you intend to change.
                
                
        update_shipping_address: update user's shipping address
            arguments:
                customer_profile_id: required
                
                and the same arguments for shipping_address with the
                addition of an extra argument called
                customer_address_id added for each shipping_address that
                you intend to change.

        validate_payment_profile: validate a user's payment profile
            arguments:
                customer_profile_id: required
                customer_payment_profile_id: required
                customer_address_id: required
                validation_mode: L{VALIDATION_TEST} or L{VALIDATION_LIVE} or L{VALIDATION_NONE}, default L{VALIDATION_NONE}
                
    
    Each of them will return a response dictionary that can vary from:
    
    {'messages': {'message': {'code': {'text_': u'I00001'},
                              'text': {'text_': u'Successful.'}},
                  'result_code': {'text_': u'Ok'}}}
    
    to:

    {'messages': {'message': {'code': {'text_': u'I00001'},
                              'text': {'text_': u'Successful.'}},
                  'result_code': {'text_': u'Ok'}},
     'profile': {'customer_profile_id': {'text_': u'135197'},
                 'merchant_customer_id': {'text_': u'testaccount'},
                 'payment_profiles': {'customer_payment_profile_id': {'text_': u'134101'},
                                      'payment': {'credit_card': {'card_number': {'text_': u'XXXX1111'},
                                                                  'expiration_date': {'text_': u'XXXX'}}}}}}

    with all the possible variations and arguments depending on the
    format specified by Authorize.net at:
    
        http://www.authorize.net/support/CIM_XML_guide.pdf
    
    a field in the response can be accesses by using either dictionary
    access methods:
        
        response['messages']['message']['code']['text_']
    
    or object dot-notation:
    
        response.messages.message.code.text_
    
    There are 2 custom key names in the responses:
        attrib_: a dictionary of the attributes of a tag
        text_: the text contained in the tag
    
    In order to read the corresponding value one has to manually
    access to the special attribute. Sometimes though one just wants
    to pass a dict_accessor to an authorize API call without having to
    worry about the text_ key (and only the text key), in this case
    the XML flattener is smart enough to recognize that you passed
    a dict_accessor with a text_ attribute and will use it for you.
        
        profile = cim.get_customer_profile()
        cim.some_api_call(profile.customer_profile_id)
    
    In the example customer_profile_id would be {'text_': u'12334'} but
    the api_call will extract the text_ content for you.
    """
    responses = resp.cim_map

util.populate(Api, xml, 'cim_')
