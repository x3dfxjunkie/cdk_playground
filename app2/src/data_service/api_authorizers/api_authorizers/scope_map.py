"""
This document includes the scope map for the customer API authorizer.
This scope map is simply a configuration file which maps access to API endpoints
to AuthZ scopes.  For example, as per the below, in order to access any resources
in /api/v1/experiences/*, a client would require access to the scope tpr-guest360-experiences
in AuthZ.
"""
SCOPE_MAP = {
    "authorization": [
        {
            "authType": "pattern",
            "urlPattern": "/api/v1/experiences/*",
            "id": 1,
            "authToken": True,
            "gdsEnabled": False,
            "scopes": [
                {
                    "method": "GET",
                    "scopesRequired": [
                        "tpr-guest360-experiences",
                    ],
                }
            ],
        },
        {
            "authType": "pattern",
            "urlPattern": "/api/v1/ownership/*",
            "id": 2,
            "authToken": True,
            "gdsEnabled": False,
            "scopes": [
                {
                    "method": "GET",
                    "scopesRequired": [
                        "tpr-guest360-ownership",
                    ],
                }
            ],
        },
        {
            "authType": "pattern",
            "urlPattern": "/api/v1/profile/*",
            "id": 3,
            "authToken": True,
            "gdsEnabled": False,
            "scopes": [
                {
                    "method": "GET",
                    "scopesRequired": [
                        "tpr-guest360-profile",
                    ],
                }
            ],
        },
    ]
}
