# CRUD: Create, Read, Update, Delete

# GET : Read 
# POST : Create
# Put : Update, complete set of record has to pass for updating the MULTIPLE VALUES
# Delete : Delete
# Patch : Update, only SINGLE field/column of single VALUE then we use patch.



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
# token contains data, to see data we can decrypt it.

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





# 400 : Bad Request	
# The input parameters in the request body are either incomplete or in the wrong format. 
# Be sure to include all required parameters in your request.


# 404 : Not Found occurs, The requested resource could not be found.
# When you incorrect url, pass data to that url, 404 error occurs

# 405 : Method Not Allowed






# PATCH
# Update, only SINGLE field/column of single VALUE then we use patch.
import requests
import json

url = "https://gorest.co.in/public/v2/users/267697"

payload = json.dumps([
  {
    "name": "WXYZ"
  }
])
headers = {
  'Authorization': 'Bearer e22d5f6b7b7f4b69da5e22e21efcfc8084af58b32dbe7cb850b84504e82d127d',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
# Output : user id 267697 updating the name field from "Daya" to "WXYZ"







# PUT
# We can update the multiple values or multiple fields at once or single value can be used to update the rest api

import requests
import json

url = "https://gorest.co.in/public/v2/users/267697"

payload = json.dumps([
  {
    "name": "ABCDEF",
    "gender": "male"
  }
])
headers = {
  'Authorization': 'Bearer e22d5f6b7b7f4b69da5e22e21efcfc8084af58b32dbe7cb850b84504e82d127d',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
# Output : user id 267697 updating the name field from "Daya" to "ABCDEF", "female" to "male"



# We can RESTRICT the developer or tester to use PATCH, that if they want to update only single FIELD of VALUE.
# We can use PUT request for single FIELD of value for updation, but here there is a chance of misuse or
# updating uncessary FIELDS to update the values.

# If there is only SINGLE FIELD of value need to be update then use : PATCH
# If there is MULTIPLE FIELDS of values needs to be update the use : PUT


# Delete
# DELETE request deletes a resource already present in the server,
# after deleting it, it is capable of updating data on the server.
import requests

url = "https://gorest.co.in/public/v2/todos/3051"

payload = ""
headers = {
  'Authorization': 'Bearer e22d5f6b7b7f4b69da5e22e21efcfc8084af58b32dbe7cb850b84504e82d127d'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text) 
# Output : https://gorest.co.in/public/v2/todos/3051
# based on the user ID : 3051 was deleted from the database

# For Information :
# The fields cannot be deleted because firstly the developer has to make the changes
# then only from delete rest api we can delete it


# 204	: No Content, The request was successful. No response body is provided.











# import requests
# payload = {"firstName":"John", "lastName":"Smith"}
# r = requests.post("https://httpbin.org/post",data=payload)
# print(r.text)