from authorize import aim as aim_api
from pprint import pprint

LOGIN = u"LOGIN"
KEY = u"TRAN_KEY"

# Setup the aim Api object.
aim = aim_api.Api(LOGIN, KEY, is_test=True)

# Create a transaction against a credit card
result_dict = aim.transaction(
    amount=u"16.00",
    card_num=u"4111111111111111",
    exp_date=u"2009-07")

pprint(result_dict)

trans_id = result_dict.trans_id

# Credit back the transaction passing the transaction_id that they gave us.
result_dict_2 = aim.transaction(
    type=aim_api.CREDIT,
    amount=u"16.00",
    card_num=u"1111",
    exp_date=u"2009-07",
    trans_id=trans_id
)

pprint(result_dict_2)