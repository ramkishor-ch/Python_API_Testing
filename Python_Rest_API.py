# CRUD: Create, Read, Update, Delete

# GET : Read 
# POST : Create
# Put : Update, complete set of record has to pass for updating the multiple values
# Delete : Delete
# Patch : Update, only single field/column value then we use patch


import requests

# Get
# url="https://gorest.co.in/public/v2/users"

# 200 response
# response = requests.get(url)
# print(response) # Output : <Response [200]>

# response will be in dictionary format
# status_Code = response.status_code
# result = response.json()
# # print(result)
# Output : [{'id': 230859, 'name': 'Hiranya Mehra Ret.', ....  ,'status': 'inactive'}]




####### Token #######

# Bearer Token: used for Authorization,
# when login into system, token is generated
# using that token used to perform all API authentication operations
# token is encrypted format and it is used every where and
# token contains data, we can see it by decrypting it

url = "https://gorest.co.in/public/v2/users"
headers = {
'Authorization': 'Bearer e22d5f6b7b7f4b69da5e22e21efcfc8084af58b32dbe7cb850b84504e82d127d'
}
response = requests.get(url,headers=headers)
status_code = response.status_code
result = response.json()
print(status_code) # Output : 200 Success, The request was successful.
print(result)      # Output : [{'id':236048, ... ,'status':'inactive'}]


print("\n")



# Post
import requests
import json

url = "https://gorest.co.in/public/v2/posts"

payload = json.dumps({
  "id": 3699,
  "user_id": 235222,
  "title": "ABCDEF",
  "body": "ZYXW"
})
headers = {
  'Authorization': 'Bearer e22d5f6b7b7f4b69da5e22e21efcfc8084af58b32dbe7cb850b84504e82d127d',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text) # Output : {"id":3700,"user_id":235222,"title":"ABCDEF","body":"ZYXW"}

status_code = response.status_code
print(status_code) # Output : 201 Created, The resource was successfully created.



# 404 : Not Found occurs, The requested resource could not be found.
# When you incorrect url, pass data to that url, 404 error occurs

# 400 : Bad Request	
# The input parameters in the request body are either incomplete or in the wrong format. 
# Be sure to include all required parameters in your request.
















# import requests
# payload = {"firstName":"John", "lastName":"Smith"}
# r = requests.post("https://httpbin.org/post",data=payload)
# print(r.text)