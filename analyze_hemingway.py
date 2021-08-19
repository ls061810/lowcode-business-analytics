import boto3


client = boto3.client("comprehend")

text = '''
Robert Cohn was a member, through his father, of one of the richest Jewish families in New York, and through his mother of one of the oldest. At the military school where he prepped for Princeton, and played a very good end on the football team, no one had made him race-conscious. No one had ever made him feel he was a Jew, and hence any different from anybody else, until he went to Princeton. He was a nice boy, a friendly boy, and very shy, and it made him bitter. He took it out in boxing, and he came out of Princeton with painful self-consciousness and the flattened nose, and was married by the first girl who was nice to him. He was married five years, had three children, lost most of the fifty thousand dollars his father left him, the balance of the estate having gone to his mother, hardened into a rather unattractive mould under domestic unhappiness with a rich wife; and just when he had made up his mind to leave his wife she left him and went off with a miniature-painter. As he had been thinking for months about leaving his wife and had not done it because it would be too cruel to deprive her of himself, her departure was a very healthful shock.
'''

response = client.batch_detect_key_phrases(
    TextList=[
        text,
    ],
    LanguageCode='en'
)
print(response)
