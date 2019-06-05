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


class PostComment():
	"""docstring for ClassName"""

	
	def __init__(self):
		self.posts = "https://jsonplaceholder.typicode.com/posts"
		self.comment = "https://jsonplaceholder.typicode.com/comments"
		self.r = requests.get(self.posts)
		self.p = requests.get(self.comment)
		self.data = self.r.json()
		self.comments = self.p.json()
		self.comm = {}
		
		
	def Posts(self):
		self.data1 = [self.data[x] for x in range(0,5)]
		print("All Posts : ",self.data1)
		print('\n')

	def get_post_detail(self):
		self.title = [self.data[i]['title'] for i in range(0,len(self.data))]
		self.detail = [self.data[i]['body'] for i in range(0,len(self.data))]
		self.post_detail=dict(zip(self.title,self.detail))
		for i,j in self.post_detail.items():
			print("post details=> 'title:body' = {}:{}".format(i,j))
			print('\n')

	def user_post(self,x):
		self.user_post_title = [self.data[x-1]['title']]
		self.user_post_body = [self.data[x-1]['body']]
		self.user_post_detail = dict(zip(self.user_post_title,self.user_post_body))
		print("Post Detail for user {}: {}".format(x,self.user_post_detail))
		print('\n')

	def comment_detail(self):
		self.comments1 = [self.comments[x] for x in range(0,5)]
		print("Comment detail ",self.comments1)
		print('\n')
	

	def comments_postid(self,postid):
		for i in range(0,len(self.comments)):
			if(postid == self.comments[i]['postId']):
				self.c_user = self.comments[i]['id']
				self.c = self.comments[i]['body']
				self.c_name = self.comments[i]['name']
				self.c_email = self.comments[i]['email']
				self.comm['id'] = self.c_user
				self.comm['name'] = self.c_name
				self.comm['email'] = self.c_email
				self.comm['body'] = self.c
				print("Comment detail for postId: {} {}".format(postid,self.comm))
				print('\n')


x = int(input("Enter user id:"))
postid = int(input("Enter PostId:"))
call = PostComment()

call.Posts()
call.get_post_detail()
call.user_post(x)
call.comment_detail()
call.comments_postid(postid)

