

import unittest
from sample import PostComment

class PostCommentTest(unittest.TestCase):
    postcomment = PostComment()
   
    def user_post(self,x):
        self.user_post_title = [self.data[x-1]['title']]
        self.user_post_body = [self.data[x-1]['body']]
        self.user_post_detail = dict(zip(self.user_post_title,self.user_post_body))
        return self.user_post_detail
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
        return self.comm

    def test_userpost(self,x):
        self.assertEqual(12, self.postcomment.user_post(1))
        self.assertEqual(13.2, self.calculator.Multiplication(11,1.2))

    def test_divide(self):
        self.assertEqual(3, self.calculator.Division(3,1))
		
if __name__ == "__main__":
	unittest.main() 