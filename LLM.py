from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
import fitz
# from langchain import TemplateAttachment
from langchain_community.document_loaders import TextLoader

class Langchain:
    def __init__(self) -> None:
        # Callbacks support token-wise streaming
        local_path = ("./models/mistral-7b-instruct-v0.1.Q4_0.gguf")
        
        
        callbacks = [StreamingStdOutCallbackHandler()]

        # Verbose is required to pass to the callback manager
        llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

        # If you want to use a custom model add the backend parameter
        # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
        self.llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)
        
        template = """Question: {question} 
        Answer : Give answer in about 50 words.
        """
        
     
        self.prompt = PromptTemplate.from_template(template)
       
   
            
                
        
        
    def querry(self,message):

        
        chain = LLMChain(prompt=self.prompt, llm=self.llm)
        response = chain.invoke(message)
        # print(response)
        
        return response
        
        
