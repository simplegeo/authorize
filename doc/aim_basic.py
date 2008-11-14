from authorize import aim as aim_api

from pprint import pprint

LOGIN = u"LOGIN"
KEY = u"TRAN_KEY"

aim = aim_api.Api(LOGIN, KEY)


# x_login: up to 20 chars
# x_tran_key: 16 chars
# x_type: AUTH_CAPTURE (default), AUTH_ONLY, CAPTURE_ONLY, CREDIT, PRIOR_AUTH_CAPTURE, VOID
# x_amount: up to 15 digits with a decimal point, no dollar symbol, all inclusive (tax, shipping etc)
# x_card_num: between 13 and 16 digits, with x_type == CREDIT only the last 4 digits are required
# x_exp_date: MMYY, MM/YY, MM-YY, MMYYYY, MM/YYYY, MM-YYYY
# x_trans_id: only required for CREDIT, PRIOR_AUTH_CAPTURE, VOID
# x_auth_code: authorization code of an original transaction not authorized on the payment gateway, 6 chars only for CAPTURE_ONLY

result_dict = aim.transaction(
    amount=u"16.00",
    card_num=u"4111111111111111",
    exp_date=u"2009-07")

pprint(result_dict)

trans_id = result_dict.trans_id

result_dict_2 = aim.transaction(
    type=aim_api.CREDIT,
    amount=u"16.00",
    card_num=u"1111",
    exp_date=u"2009-07",
    trans_id=trans_id
)

pprint(result_dict_2)