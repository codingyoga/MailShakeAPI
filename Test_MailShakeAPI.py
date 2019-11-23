import MailShakeAPI as ms

# Below is dummy api key,replace with your api key value.
API_KEY = "995c9c4-54ea-4d4d-80a0-0831fc3b462"


# Just to connect mailshake api and check whether api key is valid
result = ms.test_connect(API_KEY)
print("\nResponse of test_connect:\n", result.content)


# To create campaign
response_campaign = ms.create_campaign(API_KEY, title="Sample Title Test")
# print id of created campaign, this id can be used while adding recipients.
if response_campaign.json().get('id'):
    created_campaign_id = response_campaign.json()['id']
    print("\nCreated campaign id:\n", created_campaign_id)
else:
    print("\nResponse of create_campaign:\n", response_campaign.json())


# To add recipients
# sending email ids as json
json_email = {'john Doe': '<john@gmail.com>', 'greg': '<greg@gmail.com>'}
response_recipients = ms.add_recipients(API_KEY, campaign_id=427368, list_of_emails=json_email, as_new_list='true')
print("\nResponse of add_recipients: \n", response_recipients.json())


# To create push event for replies
response_push_event = ms.create_push_event(API_KEY, target_url="https://mysite.com/some-unique-id", event="Replied")
print("\nResponse of create_push_event: \n", response_push_event.json())
