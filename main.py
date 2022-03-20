import json
import logging
import os

from app.components.MainComponent import MainComponent

format = '%(asctime)s %(filename)s %(lineno)s : %(message)s'

logging.basicConfig(format=format, level=logging.INFO)

if os.getenv('CLOUD', 'LOCAL') == 'GCP':
    import google.cloud.logging    
    client = google.cloud.logging.Client()    
    handler = client.get_default_handler()        
    handler.setFormatter(logging.Formatter(format))        
    logging.getLogger().addHandler(handler)

def startup(request):        

    queries = request.args.to_dict()    
    
    if 'token' in queries and queries['token'] == '?':   
        request_json = request.get_json()                        
        main = MainComponent()
        return main.process(request_json)
    else:        
        return {

        }
