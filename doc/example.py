from authorize import cim

from pprint import pprint

cim_api = cim.Api(u'LOGIN', u'TRANS_KEY', is_test=True)

tree = cim_api.create_profile(
    card_number=u"4111111111111111",
    expiration_date=u"2008-07",
    customer_id=u"test_account")
profile_id = tree.customer_profile_id.text_

tree = cim_api.get_profile(customer_profile_id=profile_id)
pprint(tree)

resp = cim_api.create_profile_transaction(
    customer_profile_id=profile_id,
    amount=50.0
)
pprint(resp)

pprint(cim_api.delete_profile(customer_profile_id=profile_id))
