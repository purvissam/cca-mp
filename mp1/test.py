import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
        'ip_address1':  'ec2-18-183-46-248.ap-northeast-1.compute.amazonaws.com:5000', 
        'ip_address2':  'ec2-35-78-97-17.ap-northeast-1.compute.amazonaws.com:5000',
		'load_balancer' :  'MP2-ffc2f978f8089736.elb.ap-northeast-1.amazonaws.com',
		'submitterEmail':  'purvis.sam@gmail.com',
		'secret':  'pRdTAXiwULK0TTGi'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
