### agents Folder:
    - Contains python files for agents defined in the langchain_app project. 

### tools: 
    - Tools used in the langchain_app project. 
    - cflogin_tool defines btp_login functionality-> More tools to be added later in the project. 

### prompts: 
    - Instead of creating a .txt file or any other file then import the file into python. I declared a python file and defined prompts as strings; less complexity I feel.  

### BaseAgent.py
    - Acts as the wrapper around the LLM Calls and performs the actual LLM Calls. 
    - Abstraction layer; which is seperate from core logic can be written in seperate file. For now I've written the abstraction layer in the same file. 
