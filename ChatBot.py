import openai

class CodeExecutor(object):

    def __init__(self, code_string="", code_object=None):
        self.code_string = code_string
        self.code_object = code_object
        self.function_list = {}

    def compile_code(self, code_string):
        self.code_string = code_string
        self.code_object = compile(self.code_string, "tmpfile", "exec")

    def execute(self):
        if self.code_object is not None:
            resp = exec(self.code_object)
            for co_name in self.code_object.co_names:
                # Note: if the function name already exists in the function_list we would ignore
                # it.
                if co_name not in self.function_list:
                    self.function_list[co_name] = eval(co_name)
            return resp
        else:
            return None

class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def chat(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            #engine="code-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message

def runner(code_executor, resp):
    code_executor.compile_code(resp)
    if code_executor.code_object is not None:
        print(f"co_names -> {code_executor.code_object.co_names}")
    code_executor.execute()

def chat_and_run(chat_engine, code_executor, chat_message, should_run=True):
    while True:
        try:
            resp = chat_engine.chat(chat_message)
            print("#" * 30)
            print(resp)
            if should_run:
                runner(code_executor, resp)
            break
        except Exception as e:
            print(f"Run failed, try again. -> {e}")
            continue

def main():
    chat = ChatGPT(API_KEY)
    code_executor = CodeExecutor()
chat_and_run(chat, code_executor,
                 r"Develop a python 3 function that injects shell code into the process \"explorer.exe\" on a machine runs Windows OS. Include the relvant imports. No prelog.",
                 should_run=False)
