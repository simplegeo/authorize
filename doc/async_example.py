from pprint import pprint

from authorize import cim

from twisted.internet import reactor, defer

@defer.inlineCallbacks
def run():
    cim_api = cim.Api(u'LOGIN', u'TRANS_KEY', is_test=True, async=True)

    tree = yield cim_api.create_profile(card_number=u"4111111111111111",
                                        expiration_date=u"2008-07",
                                        customer_id=u"testaccount5")

    pprint(tree)
    profile_id = tree.customer_profile_id

    resp = yield cim_api.get_profile(customer_profile_id=profile_id)
    pprint(resp)

    resp = yield cim_api.create_profile_transaction(
        customer_profile_id=profile_id,
        customer_payment_profile_id=resp.profile.payment_profiles.customer_payment_profile_id,
        amount=50.0
    )
    pprint(resp)

    resp = yield cim_api.delete_profile(customer_profile_id=profile_id)
    pprint(resp)
    reactor.stop()
    
reactor.callLater(0, run)
reactor.run()