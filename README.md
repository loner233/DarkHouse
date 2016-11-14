# Django_Blog

__0__.Python == 2.7

__1__.Mysql == 1.5.6  

__2__.Django == 1.8.2  

__3__.Pillow == 3.4.2  

__4__.MySQL-Python == 1.2.5  



##I recommend using nginx+uwsgi to deployment server; #
##And I have set the dubug false,so staticfile will not correctly load without static server#


**step 1:**  

1.Set the USER and PASSWORD of your Mysql in file Blog_project/settings  
    
2.Set the SITE_URL with your server ip in file Blog_project/settings  
    
3.Set the blog_owner in file Blog_project/settings  
    



**step 2:**
Create the database named 'myblog'


**step 3:**
Run "python manage.py syncdb" to set the admin user


**step 4:**
enjoy it!


