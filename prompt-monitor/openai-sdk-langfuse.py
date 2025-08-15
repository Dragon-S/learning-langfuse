# from langfuse.openai import openai
from langfuse.openai import OpenAI, AsyncOpenAI, AzureOpenAI, AsyncAzureOpenAI
from langfuse import Langfuse
 
langfuse = Langfuse(
  secret_key="sk",
  public_key="pk",
  host="url"
)
 
prompt = langfuse.get_prompt("prompt名字")

client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="base_url",
    # 从环境变量中获取您的 API Key
    api_key= "api_key", #os.environ.get("ARK_API_KEY"),
)

print("prompt = ", prompt.compile(occupation="医生", position="主任医师"))
 
result = client.chat.completions.create(
    model="model",
    messages=[
        {"role": "system", "content": prompt.compile(occupation="医生", position="主任医师")[0]["content"]},
        # {"role": "user", "content": "1 + 1 = "}
    ]
)

print("result = ", result)