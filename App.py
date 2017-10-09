#coding: utf-8
import boto3
from contextlib import closing

client = boto3.client('polly',aws_access_key_id="XXXXXXXXXXXX",
    aws_secret_access_key="XXXXXXXXXXXXXXXXXX")

response = client.synthesize_speech(
    LexiconNames=[
    ],
    OutputFormat='mp3',
    SampleRate='8000',
    Text='Bom dia! Tudo bem com você?',
    TextType='text',
    VoiceId='Ricardo',
)


with closing(response["AudioStream"]) as stream:
    data = stream.read()
    fo = open("pollytest.mp3", "w+")
    fo.write( data )
    fo.close()
