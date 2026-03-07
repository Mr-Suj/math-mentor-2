import subprocess
import time
import streamlit.web.cli as stcli
import sys

# start backend
subprocess.Popen(["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"])

time.sleep(5)

# run streamlit
sys.argv = ["streamlit", "run", "frontend/app.py", "--server.port=7860", "--server.address=0.0.0.0"]
sys.exit(stcli.main())