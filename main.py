from browser_use.llm import ChatGroq
from browser_use import Agent
import asyncio

llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")

async def main():
    agent = Agent(
        task="tell me about KamKalima",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())