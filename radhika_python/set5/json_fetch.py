"""Features:
Post
Get posts
Get posts based on the user
Get post detail
Comment
Get comments
Get comments based on the post
Write unittest for minimum two functions
"""
import requests 
import json
import urllib

posts = "http://my-json-server.typicode.com/radhi89/json.db/posts/"
comment = "http://my-json-server.typicode.com/radhi89/json.db/comments/"
r = requests.get(posts)
p = requests.get(comment)
data = r.json()
comments = p.json()

def Posts():
	print("Posts :",data)
	detail = [data[i]['title'] for i in range(0,len(data))]
	print("Post details : ",detail)

def user_post(x):
	if(x<=len(data)):
		print("Post based on User {} : {} ".format(x,data[x]['title']))

def comment_detail(c):
	print(comments)
	c_detail = [comments[i]['body'] for i in range(0,len(comments))]
	print("Comments :",c_detail)
	k = [comments[i]['postId'] for i in range(0,len(comments))]
	
	print(k)





Posts()
x = int(input("enter user id:"))
c = int(input("enter the post id:"))
user_post(x)
comment_detail(c)

