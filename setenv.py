import config, boto3
g = boto3.client("bedrock", region_name="us-east-1").list_guardrails()["guardrails"][0]
r = boto3.client("bedrock-agentcore-control", region_name="us-east-1").list_agent_runtimes()["agentRuntimes"][0]
f = open(".env", "a")
f.write("\nGUARDRAIL_ID=" + g["id"] + "\n")
f.write("GUARDRAIL_VERSION=1\n")
f.write("AGENTCORE_RUNTIME_ARN=" + r["agentRuntimeArn"] + "\n")
f.close()