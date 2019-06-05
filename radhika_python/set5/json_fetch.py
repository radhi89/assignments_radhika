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
comm = {}

def Posts():
	return data

def get_post_detail():
	detail = [data[i]['title'] for i in range(0,len(data))]
	return detail

def user_post(x):
	user_post_detail = [data[x-1]['title']]
	return user_post_detail

def comment_detail():
	print(comments)
	

def comments_postid(postid):
	c_detail = [comments[i]['body'] for i in range(0,len(comments))]
	print("Comments :",c_detail)
	comm['postId'] = postid
	for j in range(0,len(comments)):
		c = comments[j]['postId']
		body = comments[j]['body']
		for key,val in comments[j].items():
			if(c == postid):
				c_postid = comments[j]['body']
		print(c_postid)




Posts()
get_post_detail()
x = int(input("Enter user id:"))
postid = int(input("Enter PostId:"))
user_post(x)
comment_detail()
comments_postid(postid)

