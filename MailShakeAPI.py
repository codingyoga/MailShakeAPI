import requests


def test_connect(api_key):
    """ Function to test connection with api.mailshake.com
    and it can be used to check whether API KEY is valid """

    url = "https://api.mailshake.com/2017-04-01/me"
    payload = {'apiKey': api_key}
    response = requests.post(url, data=payload)
    return response


def create_campaign(api_key, title=None, sender_id=None):
    """ Function to create campaign title and sender_id
    parameters are optional"""

    url = "https://api.mailshake.com/2017-04-01/campaigns/create"

    if title and sender_id:
        payload = {'apiKey': api_key, 'title': title, 'senderID': sender_id}
    elif title:
        payload = {'apiKey': api_key, 'title': title}
    elif sender_id:
        payload = {'apiKey': api_key, 'senderID': sender_id}
    else:
        payload = {'apiKey': api_key}

    response = requests.post(url, data=payload)
    return response


def add_recipients(api_key, campaign_id, list_of_emails, as_new_list='false'):
    """ Function to add new recipients to particular campaign id
    campaign_id and list_of_emails are mandatory parameters"""

    url = "https://api.mailshake.com/2017-04-01/recipients/add"

    emails = ""
    for email in list_of_emails:
        if emails:
            emails = emails + ',' + email + ' ' + list_of_emails[email]
        else:
            emails = email + ' ' + list_of_emails[email]

    payload = {'apiKey': api_key, 'campaignID': campaign_id, 'listOfEmails': emails, 'addAsNewList': as_new_list}
    response = requests.post(url, data=payload)
    return response


def create_push_event(api_key, target_url, event="Replied"):
    """ Function to create push event for replies"""

    url = "https://api.mailshake.com/2017-04-01/push/create"
    payload = {'apiKey': api_key, 'event': event, 'targetUrl': target_url}
    response = requests.post(url, data=payload)
    return response


if __name__ == '__main__':
    print("Please refer Test_MailShakeAPI.py for API usage")


