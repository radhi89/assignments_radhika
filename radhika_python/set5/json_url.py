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

posts = "https://jsonplaceholder.typicode.com/posts"
comment = "https://jsonplaceholder.typicode.com/comments"
r = requests.get(posts)
p = requests.get(comment)
data = r.json()
comments = p.json()
comm = {}
def Posts():
	print("Posts :",data)
	detail = [data[i]['title'] for i in range(0,len(data))]
	print("Post details : ",detail)

def user_post(x):
	if(x<=len(data)):
		print("Post based on User {} : {} ".format(x,data[x]['title']))

def comment_detail():
	print(comments)
	c_detail = [comments[i]['body'] for i in range(0,len(comments))]
	print("Comments :",c_detail)

	k = [comments[i]['postId'] for i in range(0,len(comments))]
	for i in k:
		comm[i]=c_detail
	print(" postId : comment = {} ".format(comm))




Posts()
x = int(input("enter user id:"))

user_post(x)
comment_detail()

