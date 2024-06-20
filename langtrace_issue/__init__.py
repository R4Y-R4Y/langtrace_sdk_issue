import sys
from langtrace_python_sdk import langtrace
# print("before langtrace init")
# if "uvicorn" in sys.argv[0] or "daphne" in sys.argv[0] or "db_init.py" in sys.argv[0]:
print("langtrace init")
langtrace.init(
    api_key='',
    api_host=f"http://tyrhjuf:3000/api/trace",
    disable_instrumentations={'all_except':['langgraph', 'openai', "langchain", "langchain_community"]}
)
print("after langtrace init")