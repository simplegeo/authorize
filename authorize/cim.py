from authorize import gen_xml as xml, util, base, responses as resp
from authorize.gen_xml import x, AuthorizeSystemError
from authorize.util import request

from authorize.gen_xml import INDIVIDUAL, BUSINESS, ECHECK_CCD, ECHECK_PPD, ECHECK_TEL, ECHECK_WEB
from authorize.gen_xml import BANK, CREDIT_CARD, VALIDATION_NONE, CAPTURE_ONLY, AUTH_CAPTURE
from authorize.gen_xml import VALIDATION_TEST, VALIDATION_LIVE, ACCOUNT_CHECKING, ACCOUNT_SAVINGS
from authorize.gen_xml import ACCOUNT_BUSINESS_CHECKING, AUTH_ONLY, CREDIT, PRIOR_AUTH_CAPTURE

class Api(base.BaseApi):
    """
    Main CIM api object.

    NOTE: Arguments should be passed in as named arguments. Always.

    Each api call will return a response dictionary that can vary from:

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

    NOTE:
    It's important that you make sure that your Authorize dashboard
    uses the same delimiter and encapsulator that you are using in
    your API objects. If you don't check this it could happen that the
    direct_response cannot be parsed even in those cases where it's
    absolutely necessary, like in the AIM API.
    """
    responses = resp.cim_map

    @request
    def create_profile(**kw):
        """create a user's profile

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
        """
        return 'createCustomerProfileRequest', kw, xml.profile(**kw)

    @request
    def create_payment_profile(**kw):
        """add to a user's profile a new payment profile

        arguments:
            REQUIRED:
                customer_profile_id: L{unicode} or L{int}
                all the arguments for payment_profiles (above) should
                    be provided as arguments to this method call
                validation_mode: L{VALIDATION_TEST}, L{VALIDATION_LIVE}, L{VALIDATION_NONE},
                    the different level of validation will try to run and immediately
                    void 0.01 transactions on live or test environment, L{VALIDATION_NONE}
                    will skip this test. By default it's L{VALIDATION_NONE}
        """
        return ('createCustomerPaymentProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            xml.paymentProfile(**kw),
            x.validationMode(kw.get('validation_mode', VALIDATION_NONE)) # none, testMode, liveMode
        )

    @request
    def create_shipping_address(**kw):
        """add to a user's profile a new shipping address

        arguments:
            REQUIRED:
                customer_profile_id: L{unicode} or L{int}
                all the arguments above starting with 'ship_' can be
                    provided here with the same name.
        """
        return ('createCustomerShippingAddressRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            xml.address_2('ship_', **kw)
        )

    @request
    def create_profile_transaction(**kw):
        """create a new transaction in the user's profile

        NOTE: The response doesn't conform exactly to the XML output given
        in the authorize.net documentation. The direct response has been
        translated into a dictionary. The list of keys is in the source.

        arguments:
            REQUIRED:
                amount: L{float} or L{decimal.Decimal}
                customer_profile_id: L{unicode} or L{int}
                customer_payment_profile_id: L{unicode} or L{int}
                profile_type: L{AUTH_ONLY}, L{CAPTURE_ONLY}, L{AUTH_CAPTURE}, L{PRIOR_AUTH_CAPTURE}, L{CREDIT} (default AUTH_ONLY)
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
        """
        return 'createCustomerProfileTransactionRequest', kw, xml.transaction(**kw)

    @request
    def delete_profile(**kw):
        """delete one's profile

        arguments:
            customer_profile_id: required
        """
        return ('deleteCustomerProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id'])
        )

    @request
    def delete_payment_profile(**kw):
        """delete one of user's payment profiles

        arguments:
            customer_profile_id: required
            customer_payment_profile_id: required
        """
        return ('deleteCustomerPaymentProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            x.customerPaymentProfileId(kw['customer_payment_profile_id'])
        )

    @request
    def delete_shipping_address(**kw):
        """delete one of user's shipping addresses

        arguments:
            customer_profile_id: required
            customer_address_id: required
        """
        return ('deleteCustomerShippingAddressRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            x.customerAddressId(kw['customer_address_id'])
        )

    @request
    def get_profile_ids(**kw):
        """get all users' profiles ids

        arguments:
            Nothing
        """
        return ('getCustomerProfileIdsRequest', kw)

    @request
    def get_profile(**kw):
        """get a user's profile

        arguments:
            customer_profile_id: required
        """
        return ('getCustomerProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id'])
        )

    @request
    def get_payment_profile(**kw):
        """get a user's payment profile

        arguments:
            customer_profile_id: required
            customer_payment_profile_id: required
        """
        return ('getCustomerPaymentProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            x.customerPaymentProfileId(kw['customer_payment_profile_id'])
        )

    @request
    def get_shipping_address(**kw):
        """get a user's shipping address

        arguments:
            customer_profile_id: required
            customer_address_id: required
        """
        return ('getCustomerShippingAddressRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            x.customerAddressId(kw['customer_address_id'])
        )

    @request
    def update_profile(**kw):
        """update basic user's information

        arguments:
            customer_id: optional
            description: optional
            email: optional
            customer_profile_id: required
        """
        return ('updateCustomerProfileRequest', kw,
            x.profile(
                x.merchantCustomerId(kw.get('customer_id')),
                x.description(kw.get('description')),
                x.email(kw.get('email')),
                x.customerProfileId(kw['customer_profile_id'])
            )
        )

    @request
    def update_payment_profile(**kw):
        """update user's payment profile

        arguments:
            customer_profile_id: required

            and the same arguments for payment_profiles with the
            addition of an extra argument called
            customer_payment_profile_id added for each payment_profile
            that you intend to change.
        """
        return ('updateCustomerPaymentProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            xml.update_paymentProfile(**kw)
        )

    @request
    def update_shipping_address(**kw):
        """update user's shipping address

        arguments:
            customer_profile_id: required

            and the same arguments for shipping_address with the
            addition of an extra argument called
            customer_address_id added for each shipping_address that
            you intend to change.
        """
        return ('updateCustomerShippingAddressRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            xml.update_address(**kw)
        )

    @request
    def validate_payment_profile(**kw):
        """validate a user's payment profile

        arguments:
            customer_profile_id: required
            customer_payment_profile_id: required
            customer_address_id: required
            validation_mode: L{VALIDATION_TEST} or L{VALIDATION_LIVE} or L{VALIDATION_NONE}, default L{VALIDATION_NONE}
        """
        return ('validateCustomerPaymentProfileRequest', kw,
            x.customerProfileId(kw['customer_profile_id']),
            x.customerPaymentProfileId(kw['customer_payment_profile_id']),
            x.customerShippingAddressId(kw['customer_address_id']),
            x.validationMode(kw.get('validation_mode', VALIDATION_NONE))
        )
