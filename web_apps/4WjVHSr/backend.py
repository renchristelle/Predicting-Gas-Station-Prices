import dataiku
import pandas as pd
import json
import dataiku
from dataiku.scenario import Scenario

SCENARIO_ID = 'RECURSIVEBUILDOFTIMESERIES'
PROJECT_KEY = dataiku.get_custom_variables()["projectKey"]
client = dataiku.api_client()
p = client.get_project(PROJECT_KEY)

@app.route('/update/<path:params>')
def update(params):
    params = json.loads(params)
    variables = p.get_variables()
    variables["standard"] = params
    p.set_variables(variables)
    
    sc = p.get_scenario(SCENARIO_ID)
    try:
        sc.run_and_wait()
        jobSucceed = True
    except:
        jobSucceed = False
        
    return json.dumps({"status": str(jobSucceed)})