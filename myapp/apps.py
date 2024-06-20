from django.apps import AppConfig
from langtrace_python_sdk import langtrace


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        pass  # startup code here

        print("langtrace init darshit")
        langtrace.init(
            api_key='',
            # disable_instrumentations={'all_except': [
            #     'langgraph', 'openai', "langchain", "langchain_community"]}
        )
        print("after langtrace init")
