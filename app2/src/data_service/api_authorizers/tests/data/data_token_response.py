import json

# from collections import namedtuple


tests = [
    json.loads(
        """
        {
            "assertion_category": "B2B",
            "swid": "",
            "authenticator": "authz",
            "BLUE": "",
            "RED": "",
            "affiliate_name": "disney",
            "token_ttl": 28780,
            "client_id": "TPR-GUESTPROFILETOOLS-PPD.B2B-STAGE",
            "client_taxonomy_id": 1749,
            "scope": "tpr-ia-roz-ccpa tpr-celia-test"
        }
        """
    ),
    json.loads(
        """
        {
            "assertion_category": "B2B",
            "swid": "",
            "authenticator": "authz",
            "BLUE": "",
            "RED": "",
            "affiliate_name": "disney",
            "token_ttl": 28780,
            "client_id": "TPR-GUESTPROFILETOOLS-PPD.B2B-STAGE",
            "client_taxonomy_id": 1749,
            "scope": "tpr-ia-roz-ccpa"
        }
        """
    ),
    json.loads(
        """
        {
            "assertion_category": "B2B",
            "swid": "",
            "authenticator": "authz",
            "BLUE": "",
            "RED": "",
            "affiliate_name": "disney",
            "token_ttl": 28780,
            "client_id": "TPR-GUESTPROFILETOOLS-PPD.B2B-STAGE",
            "client_taxonomy_id": 1749,
            "scope": ""
        }
        """
    ),
]
