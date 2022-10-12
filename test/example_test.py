import boto3
from src.sns_extended_client.session import SNSExtendedClientSession


SMALL_MSG_BODY = 'small message body'
SMALL_MSG_ATTRIBUTES = {'test attr':{'DataType': 'String', 'StringValue': 'str value'}}\

def test_determine_payload_s3_not_used():
    sns_extended_client = SNSExtendedClientSession().client('sns')
    msg_attrs, msg_body = sns_extended_client._determine_payload('test_topic_name', SMALL_MSG_ATTRIBUTES, SMALL_MSG_BODY, None )

    assert msg_attrs == SMALL_MSG_ATTRIBUTES
    assert msg_body == SMALL_MSG_BODY


def test_always_through_s3():
    sns_extended_client = SNSExtendedClientSession().client('sns')
    sns_extended_client.always_through_s3 = True
    msg_attrs, msg_body = sns_extended_client._determine_payload('test_topic_name', SMALL_MSG_ATTRIBUTES, SMALL_MSG_BODY, None )



def demo():
    sns_extended_client = SNSExtendedClientSession().client('sns', region_name='us-east-1')
    

    sns_extended_client.large_payload_support = 'extended-client-bucket-store'
    sns_extended_client.always_through_s3 = True

    sns_extended_client.publish(TopicArn='arn:aws:sns:us-east-1:569434664987:extended-client-topic', Message='This message should be published to S3')

    sns_extended_client.always_through_s3 = False

    sns_extended_client.publish(TopicArn='arn:aws:sns:us-east-1:569434664987:extended-client-topic', Message='This message should be published.')

    sns_extended_client.message_size_threshold = 32
    sns_extended_client.publish(TopicArn='arn:aws:sns:us-east-1:569434664987:extended-client-topic', Message='This message should be published to S3 as it exceeds the limit of the 32 bytes')


if __name__ == '__main__':
    demo()
