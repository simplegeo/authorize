# -*- encoding: utf-8 -*-
import re
import decimal

from xml.etree.cElementTree import fromstring, tostring
from xml.etree.cElementTree import Element, iselement

from authorize import responses

API_SCHEMA = 'https://api.authorize.net/xml/v1/schema/AnetApiSchema.xsd'
API_SCHEMA_NS = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"
PREFIX = "{AnetApi/xml/v1/schema/AnetApiSchema.xsd}"

INDIVIDUAL = u"individual"
BUSINESS = u"business"

ECHECK_CCD = u"CCD"
ECHECK_PPD = u"PPD"
ECHECK_TEL = u"TEL"
ECHECK_WEB = u"WEB"

BANK = u"bank"
CREDIT_CARD = u"cc"
ECHECK = u"echeck"

DAYS_INTERVAL = u"days"
MONTHS_INTERVAL = u"months"

VALIDATION_NONE = u"none"
VALIDATION_TEST = u"testMode"
VALIDATION_LIVE = u"liveMode"

ACCOUNT_CHECKING = u"checking"
ACCOUNT_SAVINGS = u"savings"
ACCOUNT_BUSINESS_CHECKING = u"businessChecking"

AUTH_ONLY = u"auth_only"
CAPTURE_ONLY = u"capture_only"
AUTH_CAPTURE = u"auth_capture"
CREDIT = u"credit"
PRIOR_AUTH_CAPTURE = u"prior_auth_capture"
VOID = u"void"

c = re.compile(r'([A-Z]+[a-z_]+)')

def convert(arg):
    """
    Convert an object to its xml representation
    """
    if iselement(arg):
        return arg # the element
    if isinstance(arg, dict_accessor):
        try:
            return arg.text_
        except:
            raise Exception("Cannot serialize %s, missing text_ attribute" % (arg,))
    if isinstance(arg, dict):
        return arg # attributes of the element
    if isinstance(arg, unicode):
        return arg
    if isinstance(arg, decimal.Decimal):
        return unicode(arg)
    if arg is True:
        return 'true'
    if arg is False:
        return 'false'
    if isinstance(arg, float):
        return unicode(round(arg, 2)) # there's nothing less than cents anyway
    if isinstance(arg, (int, long)):
        return unicode(arg)
    if isinstance(arg, str):
        raise Exception("'%s' not unicode: can only accept unicode strings" % (arg,))
    raise Exception("Cannot convert %s of type %s" % (arg, type(arg)))

class XMLBuilder(object):
    """
    XMLBuilder tries to be slightly clever in order to be easier for
    the programmer. If you try to add arguments that are None they
    won't be added to the output because empty XML tags are not worth
    the bandwidth and actually mean something different than None.
    """
    def __getattr__(self, key):
        def _wrapper_func(*args):
            converted = [convert(arg) for arg in args if arg is not None]
            if not converted:
                return None
            el = Element(key)
            settext = False
            setatts = False
            for arg in converted:
                if iselement(arg):
                    el.append(arg)
                elif isinstance(arg, basestring):
                    assert not settext, "cannot set text twice"
                    el.text = arg
                    settext = True
                elif isinstance(arg, dict):
                    assert not setatts, "cannot set attributes twice"
                    for k, v in arg.iteritems():
                        el.set(k, v)
                    setatts = True
                else:
                    raise TypeError("unhandled argument type: %s" % type(arg))
            return el
        return _wrapper_func
x = XMLBuilder()

def flatten(tree):
    """
    Return a flattened tree in string format encoded in utf-8
    """
    return tostring(tree, "utf-8")

def purify(s):
    """
    s is an etree.tag and contains also information on the namespace,
    if that information is present try to remove it, then convert the
    camelCaseTags to underscore_notation_more_python_friendly.
    """
    if s.startswith(PREFIX):
        s = s[len(PREFIX):]
    return '_'.join(atom.lower() for atom in c.split(s) if atom)

class dict_accessor(dict):
    """
    Allow accessing a dictionary content also using dot-notation.
    """
    def __getattr__(self, attr):
        return super(dict_accessor, self).__getitem__(attr)

    def __setattr__(self, attr, value):
        super(dict_accessor, self).__setitem__(attr, value)

def parse_node(node):
    """
    Return a dict_accessor representation of the node.
    """
    new = dict_accessor({})
    if node.text and node.text.strip():
        t = node.text
        if isinstance(t, unicode):
            new['text_'] = t
        else:
            new['text_'] = t.decode('utf-8', "replace")
    if node.attrib:
        new['attrib_'] = dict_accessor(node.attrib)

    for child in node.getchildren():
        tag = purify(child.tag)
        child = parse_node(child)

        if tag not in new:
            new[tag] = child
        else:
            old = new[tag]
            if not isinstance(old, list):
                new[tag] = [old]
            new[tag].append(child)
    return new

def to_dict(s, error_codes, do_raise=True):
    """
    Return a dict_accessor representation of the given string, if raise_
    is True an exception is raised when an error code is present.
    """
    t = fromstring(s)
    parsed = dict_accessor(parse_node(t)) # discard the root node which is useless
    try:
        if isinstance(parsed.messages.message, list): # there's more than a child
            return parsed
        code = parsed.messages.message.code.text_
    except KeyError:
        return parsed
    if code in error_codes:
        if do_raise:
            raise error_codes[code]
    if parsed.get('direct_response') is not None:
        parsed.direct_response = parse_direct_response(parsed.direct_response.text_)
    return parsed


m = ['code', 'subcode', 'reason_code', 'reason_text', 'auth_code',
     'avs', 'trans_id', 'invoice_number', 'description', 'amount', 'method',
     'trans_type', 'customer_id', 'first_name', 'last_name', 'company',
     'address', 'city', 'state', 'zip', 'country', 'phone', 'fax', 'email',
     'ship_first_name', 'ship_last_name', 'ship_company', 'ship_address',
     'ship_city', 'ship_state', 'ship_zip', 'ship_country', 'tax', 'duty',
     'freight', 'tax_exempt', 'po_number', 'md5_hash', 'ccv',
     'holder_verification']

def parse_direct_response(s):
    """
    Very simple format but made of many fields, the most complex ones
    have the following meanings:
    
        code: 
            see L{responses.aim_codes} for all the codes
            
        avs:
            see L{responses.avs_codes} for all the codes

        method: CC or ECHECK

        trans_type:
            AUTH_CAPTURE
            AUTH_ONLY
            CAPTURE_ONLY
            CREDIT
            PRIOR_AUTH_CAPTURE
            VOID
        
        tax_exempt: true, false, T, F, YES, NO, Y, N, 1, 0
        
        ccv:
            see L{responses.ccv_codes} for all the codes

        holder_verification:
            see L{responses.holder_verification_codes} for all the codes
    """
    if not isinstance(s, unicode):
        s = s.decode('utf-8', 'replace')
        
    v = s.split(u',')
    if not len(v) >= len(m):
        v = s.split(u'|')

    d = dict_accessor(dict(zip(m, v)))
    d.original = s
    return d

def macro(action, login, key, *body):
    """
    Main XML structure re-used by every request.
    """
    return getattr(x, action)(
        {'xmlns': API_SCHEMA_NS},
        x.merchantAuthentication(
            x.name(login),
            x.transactionKey(key)
        ),
        *body
    )

def _address(pre='', kw={}, *extra):
    """
    Basic address components with extension capability.
    """
    return [
        x.firstName(kw.get(pre+'first_name')), # optional
        x.lastName(kw.get(pre+'last_name')), # optional
        x.company(kw.get(pre+'company')), # optional
        x.address(kw.get(pre+'address')), # optional
        x.city(kw.get(pre+'city')), # optional
        x.state(kw.get(pre+'state')), # optional
        x.zip(kw.get(pre+'zip')), # optional
        x.country(kw.get(pre+'country')) # optional
        
    ] + list(extra)

def address(pre='', **kw):
    """
    Simple address with prefixing possibility
    """
    return x.address(
        *_address(pre, kw)
    )

def address_2(pre='', **kw):
    """
    Extended address with phoneNumber and faxNumber in the same tag
    """
    return x.address(
        *_address(pre, kw,
             x.phoneNumber(kw.get(pre+'phone')),
             x.faxNumber(kw.get(pre+'fax'))
        )
    )

def update_address(**kw):
    return x.address(
        *_address('ship_', kw,
             x.phoneNumber(kw.get('ship_phone')),
             x.faxNumber(kw.get('ship_fax')),
             x.customerAddressId(kw['customer_address_id'])
        )
    )

def billTo(**kw):
    return x.billTo(
        *_address('bill_', kw,
            x.phoneNumber(kw.get('bill_phone')), # optional
            x.faxNumber(kw.get('bill_fax')) # optional
        )# optional
    )

def arbBillTo(**kw):
    return x.billTo(
        *_address('bill_', kw)
    )

def _shipTo(**kw):
    return _address('ship_', kw,
        x.phoneNumber(kw.get('ship_phone')),
        x.faxNumber(kw.get('ship_fax'))
    )

def shipToList(**kw):
    return x.shipToList(
        *_shipTo(**kw)
    )

def shipTo(**kw):
    return x.shipTo(
        *_shipTo(**kw)
    )

def payment(**kw):
    profile_type = kw.get('profile_type', CREDIT_CARD)
    if profile_type == CREDIT_CARD:
        return x.payment(
            x.creditCard(
                x.cardNumber(kw['card_number']),
                x.expirationDate(kw['expiration_date']) # YYYY-MM
            )
        )
    elif profile_type == BANK:
        return x.payment(
            x.bankAccount(
                x.accountType(kw.get('account_type')), # optional: checking, savings, businessChecking
                x.routingNumber(kw['routing_number']), # 9 digits
                x.accountNumber(kw['account_number']), # 5 to 17 digits
                x.nameOnAccount(kw['name_on_account']),
                x.echeckType(kw.get('echeck_type')), # optional: CCD, PPD, TEL, WEB
                x.bankName(kw.get('bank_name')) # optional
            )
        )

def transaction(**kw):
    assert len(kw.get('line_items', [])) <= 30
    content = [
        x.amount(kw['amount']),
        x.tax(
            x.amount(kw.get('tax_amount')),
            x.name(kw.get('tax_name')),
            x.description(kw.get('tax_descr'))
        ),
        x.shipping(
            x.amount(kw.get('ship_amount')),
            x.name(kw.get('ship_name')),
            x.name(kw.get('ship_description'))
        ),
        x.duty(
            x.amount(kw.get('duty_amount')),
            x.name(kw.get('duty_name')),
            x.description(kw.get('duty_description'))
        )
    ] + list(
            x.lineItems(
                x.itemId(line.get('item_id')),
                x.name(line['name']),
                x.description(line.get('description')),
                x.quantity(line.get('quantity')),
                x.unitPrice(line.get('unit_price')),
                x.taxable(line.get('taxable'))
            )
          for line in kw.get('line_items', [])
    ) + [
        x.customerProfileId(kw['customer_profile_id']),
        x.customerPaymentProfileId(kw['customer_payment_profile_id']),
        x.customerAddressId(kw.get('customer_address_id')),
        x.order(
            x.invoiceNumber(kw.get('invoice_number')),
            x.description(kw.get('description')),
            x.purchaseOrderNumber(kw.get('purchase_order_number'))
        ),
        x.taxExempt(kw.get('tax_exempt', False)),
        x.recurringBilling(kw.get('recurring', False)),
        x.cardCode(kw.get('ccv'))
    ]
    
    ptype = kw.get('profile_type', AUTH_ONLY)
    if ptype == AUTH_ONLY:
        profile_type = x.profileTransAuthOnly(
            *content
        )
    elif ptype == CAPTURE_ONLY:
        profile_type = x.profileTransCaptureOnly(
            *(content + [x.approvalCode(kw['approval_code'])])
        )
    elif ptype == AUTH_CAPTURE:
        profile_type = x.profileTransAuthCapture(
            *content
        )
    return x.transaction(profile_type)
    
def paymentProfiles(**kw):
    return x.paymentProfiles(
        x.customerType(kw.get('customer_type')), # optional: individual, business
        billTo(**kw),
        payment(**kw)
    )

def update_paymentProfile(**kw):
    return x.paymentProfile(
        x.customerType(kw.get('customer_type')), # optional
        billTo(**kw),
        payment(**kw),
        x.customerPaymentProfileId(kw['customer_payment_profile_id'])
    )

def paymentProfile(**kw):
    return x.paymentProfile(
        x.customerType(kw.get('customer_type')), # optional
        billTo(**kw),
        payment(**kw)
    )

def profile(**kw):
    content = [
        x.merchantCustomerId(kw['customer_id']),
        x.description(kw.get('description')),
        x.email(kw.get('email'))
    ]
    
    payment_profiles = kw.get('payment_profiles', None)
    if payment_profiles is not None:
        content = content + list(
            paymentProfiles(**prof)
            for prof in payment_profiles
        )
    else:
        if kw.get('card_number') or kw.get("routing_number"):
            content = content + [paymentProfiles(**kw)]
    return x.profile(
        *(content + [shipToList(**kw)])
    )

def subscription(**kw):
    trial_occurrences = kw.get('trial_occurrences')
    trial_amount = None
    if trial_occurrences is not None:
        trial_amount = kw['trial_amount']
    return x.subscription(
        x.name(kw.get('subscription_name')),
        x.paymentSchedule(
            x.interval(
                x.length(kw['interval_length']), # up to 3 digits, 1-12 for months, 7-365 days
                x.unit(kw['interval_unit']) # days or months
            ),
            x.startDate(kw['start_date']), # YYYY-MM-DD
            x.totalOccurrences(kw.get('total_occurrences', 9999)),
            x.trialOccurrences(trial_occurrences)
        ),
        x.amount(kw['amount']),
        x.trialAmount(trial_amount),
        payment(**kw),
        x.order(
            x.invoiceNumber(kw.get('invoice_number')),
            x.description(kw.get('description'))
        ),
        x.customer(
            x.type(kw.get('customer_type')), # individual, business
            x.id(kw.get('customer_id')),
            x.email(kw.get('customer_email')),
            x.phoneNumber(kw.get('phone')),
            x.faxNumber(kw.get('fax')),
            x.driversLicense(
                x.number(kw.get('driver_number')),
                x.state(kw.get('driver_state')),
                x.dateOfBirth(kw.get('driver_birth'))
            ),
            x.taxId(kw.get('tax_id'))
        ),
        arbBillTo(**kw),
        shipTo(**kw)
    )

def base(action, login, key, kw, *main):
    return flatten(
        macro(action, login, key,
            x.refId(kw.get('ref_id')),
            *main
        )
    )


__doc__ = """\
Please refer to http://www.authorize.net/support/CIM_XML_guide.pdf
for documentation on the XML protocol implemented here.
"""
