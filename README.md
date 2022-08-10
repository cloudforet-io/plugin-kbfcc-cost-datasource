# plugin-kbfcc-cost-datasource
Plugin for collecting KB-FCC data

---

## Secret Data
*Schema*
* client_id (str): HyperBilling login ID 
* secret (str): Credentials for authentication
* endpoint (str): AWS HyperBilling service endpoint 

*Example*
<pre>
<code>
{
    "client_id": "*****",
    "client_secret": "*****",
    "endpoint": "https://{url}
}
</code>
</pre>

## Options
*Schema*
* accounts (list): List of AWS Account IDs
* policy (dict): Cost Distribution Policy

*Example*
<pre>
<code>
{
    "accounts": [
        "1111",
        "2222",
        "3333"
    ],
    "policy": {
        "PBX": {
            "ORG-A": 30,
            "ORG-B": 40,
            "ORG-C": 30
        },
        "SBC": {
            "ORG-A": 20,
            "ORG-B": 30,
            "ORG-C": 50
        },
        ...
    }
}
</code>
</pre>