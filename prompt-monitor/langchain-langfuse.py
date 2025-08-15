from langfuse import get_client, Langfuse
from langfuse.langchain import CallbackHandler
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
 

langfuse = Langfuse(
  secret_key="sk",
  public_key="pk",
  host="url"
)

langfuse_handler = CallbackHandler()

langfuse_chat_prompt = langfuse.get_prompt("测试langfuse")
 
# Manually set the metadata on the langchain_chat_prompt to link it to generations that use it
langchain_chat_prompt = ChatPromptTemplate.from_messages(
    langfuse_chat_prompt.get_langchain_prompt()
)
 
# langchain_chat_prompt.metadata = {"langfuse_prompt": langfuse_chat_prompt}
 
# ## or use the ChatPromptTemplate constructor directly.
# ## Note that using ChatPromptTemplate.from_template led to issues in the past
# ## See: https://github.com/langfuse/langfuse/issues/5374
# langchain_chat_prompt = ChatPromptTemplate(
#     langfuse_chat_prompt.get_langchain_prompt(),
#     metadata={"langfuse_prompt": langfuse_chat_prompt}
# )

 
## Use the chat prompt in a Langchain chain
chat_llm = ChatOpenAI(
    model="model",
    temperature=0.1,
    base_url="base_url",
    api_key= "api_key", #os.environ.get("ARK_API_KEY"),
)
chat_chain = langchain_chat_prompt | chat_llm
 
result = chat_chain.invoke({"occupation": "医生", "position": "主任医师"}, config={"callbacks": [langfuse_handler]})
print("result = ", result)