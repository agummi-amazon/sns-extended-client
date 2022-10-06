from xml.dom.minidom import Attr
import boto3
from sqs_extended_client import SQSExtendedClientSession
from sns_extended_client.session import SNSExtendedClientSession

session = SNSExtendedClientSession()
sns = session.client('sns')

sesh = SQSExtendedClientSession()

sqs = sesh.client('sqs')

sns.large_payload_support = 'some-gibberish-to-work-now-agummi123'
sns.always_through_s3 = True

sns.publish(TopicArn='arn:aws:sns:us-east-1:569434664987:extended-client-topic', Message='Hello World!')

recv = sqs.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/569434664987/extended-client-queue', MessageAttributeNames=['All'])

print(recv)
