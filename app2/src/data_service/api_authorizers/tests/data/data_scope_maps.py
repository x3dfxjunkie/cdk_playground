import json
from collections import namedtuple

ScopeMap = namedtuple("ScopeMap", ["scopemap", "scopes", "policy"])

tests = [
    ScopeMap(
        json.loads(
            """
            {
              "authorization": [
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite1/*",
                  "id": 1,
                  "authToken": true,
                  "gdsEnabled": false,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite2/*",
                  "id": 2,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-celia-other"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite3/*",
                  "id": 3,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test"
                      ]
                    }
                  ]
                }
              ]
            }
            """
        ),
        ("tpr-celia-test"),
        json.loads(
            """
            {
              "principalId": "myfakeprincipal",
              "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite3/*"
                    ]
                  },
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite1/*",
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite2/*"
                    ]
                  }
                ]
              }
            }
            """
        ),
    ),
    ScopeMap(
        json.loads(
            """
            {
              "authorization": [
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite1/*",
                  "id": 1,
                  "authToken": true,
                  "gdsEnabled": false,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite2/*",
                  "id": 2,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-celia-other"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite3/*",
                  "id": 3,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test"
                      ]
                    }
                  ]
                }
              ]
            }
            """
        ),
        ("tpr-celia-test", "tpr-ia-roz-ccpa"),
        json.loads(
            """
            {
              "principalId": "myfakeprincipal",
              "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite1/*",
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite3/*"
                    ]
                  },
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite2/*"
                    ]
                  }
                ]
              }
            }
            """
        ),
    ),
    ScopeMap(
        json.loads(
            """
            {
              "authorization": [
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite1/*",
                  "id": 1,
                  "authToken": true,
                  "gdsEnabled": false,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite2/*",
                  "id": 2,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-celia-other"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite3/*",
                  "id": 3,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test"
                      ]
                    }
                  ]
                }
              ]
            }
            """
        ),
        ("tpr-celia-test", "tpr-celia-other"),
        json.loads(
            """
            {
              "principalId": "myfakeprincipal",
              "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite2/*",
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite3/*"
                    ]
                  },
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite1/*"
                    ]
                  }
                ]
              }
            }
            """
        ),
    ),
    ScopeMap(
        json.loads(
            """
            {
              "authorization": [
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite1/*",
                  "id": 1,
                  "authToken": true,
                  "gdsEnabled": false,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite2/*",
                  "id": 2,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-celia-other"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite3/*",
                  "id": 3,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test"
                      ]
                    }
                  ]
                }
              ]
            }
            """
        ),
        (),
        json.loads(
            """
            {
              "principalId": "myfakeprincipal",
              "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": [
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite1/*",
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite2/*",
                      "arn:aws:execute-api:*:myfakeaccountid:myfakerestapiid/*/GET/minisite3/*"
                    ]
                  }
                ]
              }
            }
            """
        ),
    ),
]
