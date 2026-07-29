# BTP Cloud Foundry Login Tool. 
from langchain_core.tools import tool


@tool
def btp_login(base_url)->str: 
    """ 
    Description:
        BTP login tool that takes User credentials and allows user to login to BTP. Returns Nothing. 

    Args: 
        base_url: SAP BTP Cloud Foundry URL. 
    """
    return base_url