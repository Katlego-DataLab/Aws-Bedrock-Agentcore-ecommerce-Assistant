import config, boto3
c = boto3.client("bedrock-agent", region_name="us-east-1")
r = c.list_knowledge_bases()
for k in r["knowledgeBaseSummaries"]:
    print(k["name"], k["knowledgeBaseId"], k["status"])