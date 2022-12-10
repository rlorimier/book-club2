# BOOK CLUB 2

For my Project Portifolio #4 on Code Institute's Diploma in Software Developement course I have created a blog, called Book Club. The blog is used to post reviews about books. All users can read the preview of the reviews on the main page and then be redirected to another page with the full review clicking on the 'Read more' button. If the user is registered and currently logged in, he can have access to leave a comment or like/dislike a post.

This is my second time submiting my PP4. The first attempt was failed because the deployment on Heroku was not done correctly, causing the live link to crash. With this new project I was able to fix some past issues and improve a few small things that did not look right or that was not working properly on the first time.


You can check the blog page clicking [HERE](https://book-club2.herokuapp.com/)


![HOME-PHOTO](media/images/all-devices-black.png)








## Technologies used


### Languages

* [Python3](https://www.python.org/)
* HTML5
* CSS
* [JavaScript](https://www.javascript.com/)


### Frameworks, Libraries and other programs

* [Django](https://www.djangoproject.com/) framework (from Python)
* Django [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) and [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/#) libraries
* [Gitpod](https://www.gitpod.io/) as IDE
* [GitHub](https://github.com/) to storage files
* [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) for CSS package
* [Cloudinary](https://cloudinary.com/) to storage media
* [Heroku](https://www.heroku.com) for deployment
* Postgres as database (from Heroku)
* [Favicon](https://favicon.io/) for favicon
* [Pexels](https://www.pexels.com/) for background image




## Resources


* [Code Institute](https://codeinstitute.net/ie/) - course materials, Slack community and tutor/mentor support
* [Boostrap docs](https://getbootstrap.com/) - for material support
* [Django central](https://djangocentral.com/) - for inspiration and material support
* [Codemy.com](https://www.youtube.com/c/Codemycom) - youtube channel for material support
* [W3 Schools](https://www.w3schools.com/) - for material support




## Credits


### Content

* Book reviews from [Goodreads](https://www.goodreads.com/) website.
* Book cover images from [Google](http://www.google.com)



## Features


### Code features

* Created in Django using Gitpod.
* Deployed in Heroku for online interaction.


### User features

* Home button, on the navigation bar at the top left, bringing the user back to the home page.
* About button, on the navigation bar at the top left, leading the user to a new page containing information about how the blog was created.
* Option to register/sign in on the blog clicking on the respective button from the navigation bar on the top left.
![Navbar-Login](media/images/navbar-login.png)

* Option to log out by clicking on the respective button from the navigation bar on the top left.
![Navbar-Logout](media/images/navbar-logout.png)

* Once registered/logged in, user can interact with the blog, leaving a new comment or like/dislike posts on the post page.
![Comments-field](media/images/comments-field.png)

* Warning message is shown when user log in/out or leave a comment.
![Warning-msg](media/images/warning-msg.png)

* Read more button, on botton of every post, giving the user the possibility of reading the full review.
![Readmore-btn](media/images/readmore-btn.png)




## User Stories


### Agile Planning

The project was developed using agile methodologies, by delivering small features divided in 3 sprints - To do, In progress, Done.

Every card was labeled under User Stories, divided in User and Admin.

The board was created using Github projects and can be located [HERE](https://github.com/users/rlorimier/projects/3/views/1) to have access to more information on the project cards.

![AGILE-PLANNING](media/images/agile-book.png)


#### As Visitor:

* I want to be able to navigate through the website

* I want to know how the blog was created so I can learn more about the blog

* I want to read the book reviews so I can decide to read the book or not

* I want to be able to register so I can interact with the blog


#### As Registered User:

* I want to be able to login/out so I can interact with the blog

* I want to leave comments on the posts so I can leave my personal opnion

* I want to like the posts so I can tell other users that I like it


#### As Admin

* I want to write a new blog post so I can keep the blog updated

* I want to delete a blog post so I can remove unwanted posts

* I want to edit a blog post so I can amend it








## Testing


### Manual Testing

* Manual tests done as admin user, regular user and visitant. In all scenarios the blog funcionalities worked without showing any issues.
* I also send the live link to friends and family members for testing and feedback.

Manual testing result:

![Manual-Testing](media/images/manual-testing.png)


### Code Testing

* Python - [PythonChecker](https://www.pythonchecker.com/)

All .py files were individualy tested, with the exception of settings.py, as some of the lines are longer than 79 characters but they are required for functionality of the website.

![Python-testing](media/images/python-testing.png)

* HTML - [W3C](https://validator.w3.org/nu/)

W3C Validator shows one error on the HTML, however it cannot be fixed. The closing div tag mentioned is the one after the endblock content on base.html and if removed the css classes will not be applied.

![HTML-testing](media/images/html-testing.png)

* CSS - [Jigsaw](https://jigsaw.w3.org/css-validator/)

![CSS-testing](media/images/css-testing.png)

* JavaScript - [JSHint](https://jshint.com/)

![JSHint-testing](media/images/jshint-testing.png)



### Accessibility Testing

* Tested using [Accessibility Test](https://accessibilitytest.org/). <br>You can check the full test result clicking [HERE](https://accessibilitytest.org/results/YTL9u9vvs41X).
![Accessibility-test](media/images/accessibility-test.png)



### Browser Testing

The site was tested and worked without any issues, using:
* Internet Explorer
* Google Chrome
* Microsoft Edge
* Firefox
* Samsung Internet




## Bugs/Issues *(from 1st repository)*


* Gitignore

When setting up all files and folders I forgot to include the .gitignore. So, when at some stage on my commitments I received and warning email from GitHub about my keys being exposed. <br>
*To Fix: No support needed - I just created a new file, added the necessary content on it and then commit/push to Github.*


* Login on Django Admin

When setting the supper user I was having trouble to access the Django Admin page. The url was returning an error message. <br>
*To Fix: Needed support from Tutor - The server was not running. I was told to run the server and use the url https://8000-rlorimier-bookclub-fa25pzry77q.ws-eu63.gitpod.io/admin/.*


* Hyperlinks not working

The pages were not extending the 'base.html' <br>
*To Fix: Needed support from Tutor - I was told to include on the top of every page 'load static' and it worked*


* New comment does not show

When adding a new comment (logged in and/or out), the page is reloaded and redirected correctly with no error messages, however the comment is not saved and does not appear on the website neither on the blog admin server. <br>
*To Fix: No support needed (although I tried to discuss this issue with my mentor but the time was not enough) - This is the issue that took longer to be solved. I searched on web for different tutorials but any of them seemed to be helpfull. After a while, I just needed to add 'data' on views.py, line 55*


* New post show error message

When adding a new post (only logged users), it shows and error message <br>
*To Fix: No support needed - I was using the same function for both, edit and create a new post. I decided to make it individualy and then it starts to work*


* GET /favicon.ico HTTP/1.1" 404 179

The terminal keeps showing this error from time to time and I can not find a solution or even where is comming from, as I did not add any favicon on the blog. <br> *BUG NOT FIXED*


* Push failed on Heroku

When pushing my gitpod project to Heroku, following the instructions for: DEBUG=False and excluding DISABLE_COLLECTSTATIC=1, an error message is shown. I tried help from my mentor and from the tutor support but none of them were able to help me to find a solution for it. So, I left the DEBUG as False on my code and added again the DISABLE_COLLECTSTATIC=1 and tried to puch my code again. The push worked this time, however the css file is not being loaded. All funcionalities seems to work fine on the manual tests, but the css. <br> *BUG NOT FIXED*




## Bugs/Issues *(from 2nd repository)*


* Error 500 when registering using an email

When the user is registering into the blog, if he adds his email and clicks on 'Register', the site returns the Error 500.<br>
*To Fix: Tutor help was needed. They instructed me to add two lines on settings.py. It creates a default email so if the user adds and nonexistent email or type it wrongly, the user will be registered anyway and redirected to the home page, with no errors.*

![Error500](media/images/signup-error500.png)



## Creating a Repository and Deploying

* To create a new repository:

Logged in my GitHub page and accessed Code Institute GitHub page. 

Selected python-essencials-template and clicked in Use This Template. 

Created a new repository from the one mentioned above and choose the option 'Gitpod'. Once the repository is open on Gitpod it is just start to code. I chose the option to save automatically. 

After every significant amount of coding is time for local commits: On Gitpot, go to Source Control, type in a message and click Commit. After a work day, the last local commit is done and then click in Push to commit all local commits to GitHub repository. 


* To Deploy:

The project was deployed using Heroku. The process is as follows:

Once you have signed up to Heroku, on the top right of the dashboard there is a button labelled 'New'. This will open a dropdown; please select 'Create new app'. On the next page you can choose your region and a name for the project. Then click 'Create app'.

On the next page there is a menu along the top. Navigate to 'Settings', where you will find the config vars. Scroll down to the section named 'Config vars' and click on the button labelled 'Reveal config vars'. Cloudinary and Postgres will both need config vars as per your own details. You will also need to set a secret key. Once the config vars are saved, back in Gitpod save them in an env.py file. Make sure to add env.py to your .gitignore list so that your config vars do not become publically available on Github.

If you scroll back to the top of the page you will find the 'Deploy' tab, which has multiple options for deployment. As I am using Github for this project, I selected it and a bar came up to search for the repo I wish to connect to.

Once you have connected, you have the option to deploy automatically (the app will update every time you push) or manually (update only when you choose). I chose automatic but you can do what suits you.

After the first push/update, your app will be ready to go!