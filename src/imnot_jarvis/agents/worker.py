# PEP-8 Standards: Standard inputs, Thirdparties & First parties - Seperated by Blank space. 
import sys

if sys.platform == "win32": 
    import subprocess
    from functools import partial
    import langchain_mcp_adapters.sessions as mcp_sessions
    print("Running")