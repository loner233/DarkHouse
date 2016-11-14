# Django_Blog


__1__.Mysql == 1.5.6
__2__.Django == 1.8.2
__3__.Pillow == 3.4.2
__4__.MySQL-Python == 1.2.5


#I recommend using nginx+uwsgi to deployment server; #
#and I have set the dubug false,so staticfile will not correctly load without static server#


**step 1:**
    __1__.Set the USER and PASSWORD of your Mysql in file Blog_project/settings
    __2__.Set the blog_owner in file Blog_project/settings



**step 2:**
Create the database named 'myblog'


**step 3:**
Run "python manage.py syncdb" to set the admin


**step 4:**
enjoy it!

