from LLM import Langchain
from scrapper import Scrapping

# scrap = Scrapping()
# response = scrap.scrape_projects(url="https://www.ci.richmond.ca.us/viaverdiproject")

# print(response)
# with open("Web.text","w") as file:
#     file.writelines([""""question": "Give summary of project \n"""])
    # file.write(str(response))
    
with open("Web.text", "r") as file:
    contents = file.read()
    
chain = Langchain()
response = chain.querry(message=contents)

with open("Response.text","w") as file:
    file.write(response['text'])