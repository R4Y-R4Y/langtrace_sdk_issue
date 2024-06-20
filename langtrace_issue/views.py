from django.http import JsonResponse
# Create your views here.
from langtrace_python_sdk import langtrace
from langtrace_python_sdk.utils.with_root_span import with_langtrace_root_span
from openai import OpenAI


@with_langtrace_root_span()
def member1(request):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "How many states of matter are there?"
            }
        ],
    )
    print(response.choices[0].message.content)
    print("members view called ...admin")
    return JsonResponse({'foo': f'bar {response.choices[0].message.content}'})
