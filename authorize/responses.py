# -*- encoding: utf-8 -*-

_cim_response_codes = [
    ['I00001', 'Successful', 'The request was processed successfully.'],
    ['I00003', 'The record has already been deleted.', 'The record has already been deleted.'],
    ['E00001', 'An error occurred during processing. Please try again.', 'An unexpected system error occurred while processing this request.'],
    ['E00002', 'The content-type specified is not supported.', 'The only supported content-types are text/xml and application/xml.'],
    ['E00003', 'An error occurred while parsing the XML request.', 'This is the result of an XML parser error.'],
    ['E00004', 'The name of the requested API method is invalid.', 'The name of the root node of the XML request is the API method being called. It is not valid.'],
    ['E00005', 'The merchantAuthentication.transactionKey is invalid or not present.', 'Merchant authentication requires a valid value for transaction key.'],
    ['E00006', 'The merchantAuthentication.name is invalid or not present.', 'Merchant authentication requires a valid value for name.'],
    ['E00007', 'User authentication failed due to invalid authentication values.', 'The name/and or transaction key is invalid.'],
    ['E00008', 'User authentication failed. The payment gateway account or user is inactive.', 'The payment gateway or user account is not currently active.'],
    ['E00009', 'The payment gateway account is in Test Mode. The request cannot be processed.', 'The requested API method cannot be executed while the payment gateway account is in Test Mode.'],
    ['E00010', 'User authentication failed. You do not have the appropriate permissions.', 'The user does not have permission to call the API.'],
    ['E00011', 'Access denied. You do not have the appropriate permissions.', 'The user does not have permission to call the API method.'],
    ['E00013', 'The field is invalid.', 'One of the field values is not valid.'],
    ['E00014', 'A required field is not present.', 'One of the required fields was not present.'],
    ['E00015', 'The field length is invalid.', 'One of the fields has an invalid length.'],
    ['E00016', 'The field type is invalid.', 'The field type is not valid.'],
    ['E00019', 'The customer taxId or driversLicense information is required.', 'The customer tax ID or driver\'s license information (driver\'s license number, driver\'s license state, driver\'s license DOB) is required for the subscription.'],
    ['E00027', 'The transaction was unsuccessful.', 'An approval was not returned for the transaction.'],
    ['E00029', 'Payment information is required.', 'Payment information is required when creating a subscription or payment profile.'],
    ['E00039', 'A duplicate record already exists.', 'A duplicate of the customer profile, customer payment profile, or customer address was already submitted.'],
    ['E00040', 'The record cannot be found.', 'The profileID, paymentProfileId, or shippingAddressId for this request is not valid for this merchant.'],
    ['E00041', 'One or more fields must contain a value.', 'All of the fields were empty or missing.'],
    ['E00042', 'The maximum number of payment profiles allowed for the customer profile is {0}.', 'The maximum number of payment profiles for the customer profile has been reached.'],
    ['E00043', 'The maximum number of shipping addresses allowed for the customer profile is {0}.', 'The maximum number of shipping addresses for the customer profile has been reached.'],
    ['E00044', 'Customer Information Manager is not enabled.', 'The payment gateway account is not enabled for Customer Information Manager (CIM).']
]

_arb_response_codes = [
    ['E00001', 'An error occurred during processing. Please try again.', 'An unexpected system error occurred while processing this request.'],
    ['E00002', 'The content-type specified is not supported.', 'The only supported content-types are text/xml and application/xml.'],
    ['E00003', 'An error occurred while parsing the XML request.', 'This is the result of an XML parser error.'],
    ['E00004', 'The name of the requested API method is invalid.', 'The name of the root node of the XML request is the API method being called. It is not valid.'],
    ['E00005', 'The merchantAuthentication.transactionKey is invalid or not present.', 'Merchant authentication requires a valid value for transaction key.'],
    ['E00006', 'The merchantAuthentication.name is invalid or not present.', 'Merchant authentication requires a valid value for name.'],
    ['E00007', 'User authentication failed due to invalid authentication values.', 'The name/and or transaction key is invalid.'],
    ['E00008', 'User authentication failed. The payment gateway account or user is inactive.', 'The payment gateway or user account is not currently active.'],
    ['E00009', 'The payment gateway account is in Test Mode. The request cannot be processed.', 'The requested API method cannot be executed while the payment gateway account is in Test Mode.'],
    ['E00010', 'User authentication failed. You do not have the appropriate permissions.', 'The user does not have permission to call the API.'],
    ['E00011', 'Access denied. You do not have the appropriate permissions.', 'The user does not have permission to call the API method.'],
    ['E00012', 'A duplicate subscription already exists.', 'A duplicate of the subscription was already submitted. The duplicate check looks at several fields including payment information, billing information and, specifically for subscriptions, Start Date, Interval and Unit.'],
    ['E00013', 'The field is invalid.', 'One of the field values is not valid.'],
    ['E00014', 'A required field is not present.', 'One of the required fields was not present.'],
    ['E00015', 'The field length is invalid.', 'One of the fields has an invalid length.'],
    ['E00016', 'The field type is invalid.', 'The field type is not valid.'],
    ['E00017', 'The startDate cannot occur in the past.', 'The subscription start date cannot occur before the subscription submission date.'],
    ['E00018', 'The credit card expires before the subscription startDate.', 'The credit card is not valid as of the start date of the subscription.'],
    ['E00019', 'The customer taxId or driversLicense information is required.', 'The customer tax ID or driver’s license information (driver’s license number, driver’s license state, driver’s license DOB) is required for the subscription.'],
    ['E00020', 'The payment gateway account is not enabled for eCheck.Net subscriptions.', 'This payment gateway account is not set up to process eCheck.Net subscriptions.'],
    ['E00021', 'The payment gateway account is not enabled for credit card subscriptions.', 'This payment gateway account is not set up to process credit card subscriptions.'],
    ['E00022', 'The interval length cannot exceed 365 days or 12 months.', 'The interval length must be 7 to 365 days or 1 to 12 months.'],
    ['E00024', 'The trialOccurrences is required when trialAmount is specified.', 'The number of trial occurrences cannot be zero if a valid trial amount is submitted.'],
    ['E00025', 'Automated Recurring Billing is not enabled.', 'The payment gateway account is not enabled for Automated Recurring Billing.'],
    ['E00026', 'Both trialAmount and trialOccurrences are required.', 'If either a trial amount or number of trial occurrences is specified then values for both must be submitted.'],
    ['E00027', 'The test transaction was unsuccessful.', 'An approval was not returned for the test transaction.'],
    ['E00028', 'The trialOccurrences must be less than totalOccurrences.', 'The number of trial occurrences specified must be less than the number of total occurrences specified.'],
    ['E00029', 'Payment information is required.', 'Payment information is required when creating a subscription.'],
    ['E00030', 'A paymentSchedule is required.', 'A payment schedule is required when creating a subscription.'],
    ['E00031', 'The amount is required.', 'The subscription amount is required when creating a subscription.'],
    ['E00032', 'The startDate is required.', 'The subscription start date is required to create a subscription.'],
    ['E00033', 'The subscription Start Date cannot be changed.', 'Once a subscription is created the Start Date cannot be changed.'],
    ['E00034', 'The interval information cannot be changed.', 'Once a subscription is created the subscription interval cannot be changed.'],
    ['E00035', 'The subscription cannot be found.', 'The subscription ID for this request is not valid for this merchant.'],
    ['E00036', 'The payment type cannot be changed.', 'Changing the subscription payment type between credit card and eCheck.Net is not currently supported.'],
    ['E00037', 'The subscription cannot be updated.', 'Subscriptions that are expired, canceled or terminated cannot be updated.'],
    ['E00038', 'The subscription cannot be canceled.', 'Subscriptions that are expired or terminated cannot be canceled.']
]

class AuthorizeError(Exception):
    def __init__(self, *args):
        self.args = args
    
    def __str__(self):
        return "Code %s: %s, %s" % self.args
    
    def __repr__(self):
        return "AuthorizeError(%r, %r, %r)" % self.args

cim_map = {}
arb_map = {}

def populate(map, from_):
    for code, text, description in from_:
        if code.startswith("I"):
            continue # it's useless to have successful response codes in this _errors_ map
        else:
            map[code] = AuthorizeError(code, text, description)

populate(cim_map, _cim_response_codes)
populate(arb_map, _arb_response_codes)

aim_codes = {
    '1': 'Approved',
    '2': 'Declined',
    '3': 'Error',
    '4': 'Held for Review'
}

avs_codes = {
    'A': 'Address (Street) matches, ZIP does not',
    'B': 'Address information not provided for AVS check',
    'E': 'AVS error',
    'G': 'Non-U.S. Card Issuing Bank',
    'N': 'No Match on Address (Street) or ZIP',
    'P': 'AVS not applicable for this transaction',
    'R': 'Retry – System unavailable or timed out',
    'S': 'Service not supported by issuer',
    'U': 'Address information is unavailable',
    'W': 'Nine digit ZIP matches, Address (Street) does not',
    'X': 'Address (Street) and nine digit ZIP match',
    'Y': 'Address (Street) and five digit ZIP match',
    'Z': 'Five digit ZIP matches, Address (Street) does not'
}

ccv_codes = {
    'M': 'Match',
    'N': 'No Match',
    'P': 'Not Processed',
    'S': 'Should have been present',
    'U': 'Issuer unable to process request'
}

holder_verification_codes = {
    '': 'CAVV not validated',
    None: 'CAVV not validated',
    '0': 'CAVV not validated because erroneous data was submitted',
    '1': 'CAVV failed validation',
    '2': 'CAVV passed validation',
    '3': 'CAVV validation could not be performed; issuer attempt incomplete',
    '4': 'CAVV validation could not be performed; issuer system error',
    '5': 'Reserved for future use',
    '6': 'Reserved for future use',
    '7': 'CAVV attempt – failed validation – issuer available (U.S.-issued card/non-U.S acquirer)',
    '8': 'CAVV attempt – passed validation – issuer available (U.S.-issued card/non-U.S. acquirer)',
    '9': 'CAVV attempt – failed validation – issuer unavailable (U.S.-issued card/non-U.S. acquirer)',
    'A': 'CAVV attempt – passed validation – issuer unavailable (U.S.-issued card/non-U.S. acquirer)',
    'B': 'CAVV passed validation, information only, no liability shift'
}