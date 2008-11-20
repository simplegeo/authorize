from authorize import cim

from pprint import pprint

cim_api = cim.Api(u'LOGIN', u'TRANS_KEY', is_test=True)

# We create a profile for one of our users.
tree = cim_api.create_profile(
    card_number=u"4111111111111111",
    expiration_date=u"2008-07",
    customer_id=u"test_account")

# Store the profile id somewhere so that we can later retrieve it.
# CIM doesn't have a listing or search functionality so you'll
# have to keep this somewhere safe and associated with the user.
profile_id = tree.customer_profile_id.text_

# Retrieve again the profile we just created using the profile_id
tree = cim_api.get_profile(customer_profile_id=profile_id)
pprint(tree)

# And let's now try to create a transaction on that profile.
resp = cim_api.create_profile_transaction(
    customer_profile_id=profile_id,
    amount=50.0
)
pprint(resp)

# We did what we needed, we can remove the profile for this example.
pprint(cim_api.delete_profile(customer_profile_id=profile_id))
