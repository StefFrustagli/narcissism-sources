# Narcissistic Personality Disorder: Social Resources

Developer: Stefania Frustagli

## Website Overview

The purpose of this website is to provide a centralized repository of resources from social media related to understanding narcissistic and violent behaviors. By incorporating reels from platforms, like Instagram and YouTube, this project aims to shed light on subtle and recurrent abuse patterns.
My goal is to raise awareness about these patterns, empowering individuals to recognize and protect themselves from toxic influences, ultimately leading to a better quality of life.

#### Why Narcissism awareness?

This is a very personal project. I wanted to share all the material I found helpful during the years as a 'survivor'.
I strongly believe in the importance of education: narcissistic abuse, or violent behaviours in general, can be insidious and difficult to identify, so it's crucial to have prevention and recovery plans. Through this project, I hope to facilitate discussions and provide valuable insights into narcissistic behaviors, helping individuals understand and navigate their experiences more effectively.

View the live project [here](https://narcissism-website-8191a44972de.herokuapp.com/).

Responsive Mockup: ![Responsive Mockup]() AGGIUNGI MOCKUP

## Table of Contents DA MODIFICARE

- [Website Overview](#website-overview)
- [Project background & User Experience](#project-background--user-experience)
  - [Agile Development](#agile-development)
  - [Problem Statement](#problem-statement)
  - [The Design Process](#the-design-process-thinking-through-it)
  - [Colour Palettes](#colour-palettes)
  - [Wireframes](#wireframes)
  - [Data Model](#data-model)
  - [Ideal Users](#ideal-users)
  - [User Stories](#user-stories-site-accessibility--functionality)
- [Features and functionalities](#features-and-functionalities)
  - [Current Features](#current-features)
  - [Future Features](#future-features-and-general-aspects-left-to-implement)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Project background

### Agile Development

The development process for this project followed Agile methodology, emphasizing continuous improvement throughout the development lifecycle.

**Project Management**: I utilised GitHub Project boards to manage tasks, user stories, and project progression effectively.

**User Stories**: User stories were categorized into EPICs A, B, C, D, E, and F based on user types and content specificity. I prioritized these user stories using the MoSCoW method, which categorizes requirements into Must have, Should have, Could have, and Won't have categories based on their importance and urgency.

**Continuous Improvement**: Despite working solo on this project, I actively sought ways to enhance development processes and product quality. Regular retrospectives allowed me to reflect on past work, pinpoint areas for improvement, and brainstorm solutions.

[Link to the GitHub Project board](https://github.com/users/StefFrustagli/projects/2/views/1)

### Problem Statement

In the past few years, I have liked a large number of reels and videos about narcissism on Instagram and YouTube. These videos played a crucial role in my awareness journey - I believe they were pivotal to my recovery. But this material was somehow 'hidden' or lost in a sea of information on social apps, and I felt it was chaotic. I wanted to make this helpful material organised in one place and easily accessible to those who could benefit from it. It might have helped someone else as well.

**Proposed solution**: What can I do to accomplish that? My answer was this website. The primary intent was to create a site, easy to navigate and interactive, containing all the material (or at least some of it) that could be as helpful to others as much as it was tor me.

### The design process: thinking through it

It was important to me to create a simple and intuitive website where the viewers would be able to focus on the contents.

Originally, I planned to use a purple color palette since it felt neutral (the colour also reminded me of vampires, and this creature would be perfectly associated with the theme).

However, as I was building the site and researching images, I wasn't sure about the colour anymore. My interest was piqued by an illustration with a red background, a black silhouette of a hand, and white strings. 
The colour red conveys danger vibes and it would fit perfectly - but it was too 'strong', so I reverted to purple.

In my mind, purple appears calm, yet mysterious and enigmatic, so it still evokes the feeling of alert I wanted to reproduce. And as I said, it reminds me of vampires. The appropriate analogy with vampires and narcissism will be used at some point.

At the same time, purple seems associated with healing, and healing from narcissistic abuse is the ultimate hope for my ideal users and the reason why I'm building this site.

In my original plan for the homepage, some squares would serve as topics to click on. For simplicity, I have stuck with that, but I plan to add illustrations in the future to replace the purple squares - this is why the squares are added as images.

### Fonts
Fonts used are Roboto and Lato. They were imported using Google fonts.

### Colour palettes

![Colour Palette](https://i.ibb.co/Rg9f3bt/my-screenshots-2024-03-18-at-07-53-23.png)

#### Variations:

![Colour square #7e3594](https://i.ibb.co/rtyKWVp/my-screenshots-2024-03-20-at-10-48-09.png) ![Colour square #ffffff](https://i.ibb.co/HxX3pSW/my-screenshots-2024-03-20-at-10-50-23.png) ![Colour square #594275](https://i.ibb.co/cD9SjV2/my-screenshots-2024-03-19-at-12-48-21.png)

#7e3594, #ffffff, #594275

### Wireframes

Draft project plan:

![Wireframe created using Figma](https://i.ibb.co/HNTL86J/frame.png)

Homepage [Desktop and mobile]:

![Wireframe created using Balsamiq - Homepage](https://i.ibb.co/gdnFy5q/Homepage.png)

About page [Desktop and mobile]:

![Wireframe created using Balsamiq - About page](https://i.ibb.co/rxFKB1X/About-Page.png)

Register page [Desktop and mobile]:

![Wireframe created using Balsamiq - Register](https://i.ibb.co/tXQ79jS/Register.png)

Login page [Desktop and mobile]:

![Wireframe created using Balsamiq - Login](https://i.ibb.co/MCDhRzp/Login.png)

Topic page template [Desktop and mobile]:

![Wireframe created using Balsamiq - Topic template](https://i.ibb.co/mcj6PmK/Topic-template.png)

Topic page example [Desktop and mobile]:

![Wireframe created using Balsamiq - Topic example](https://i.ibb.co/JrFm6hp/Topic-example.png)

Community page [Desktop and mobile]:

![Wireframe created using Balsamiq - Community Page](https://i.ibb.co/vPq1gvF/Community-page.png)

### Data Model
The structure of our database was illustrated using an Entity-Relationship Diagram (ERD). This diagram shows how different entities within the system are related to each other and helps in understanding the data flow. The second version is currently the most accurate.

ERD - first draft version:

![ERD](https://i.ibb.co/c1XywtS/ERD-first-version.png)

ERD - second version:

![ERD second version](https://i.ibb.co/WWsS9Qv/my-screenshots-2024-03-23-at-14-14-37.png)

Draft flowchart for apps organisation:
![draft flowchart to organise apps](https://i.ibb.co/rZNXCF7/draft-apps-planning.png)

The **applications** used are:

- **homepage**: 
  Responsible for managing core functionalities of the website, including category displays on the homepage and topic pages.

- **about_page**:
  Manages content related to the About section, including the form for collaborators.

- **content_management**:
  Manages third-party content, specifically social media resources, ensuring their seamless integration and display throughout the website.

- **comments**:
  Designed to facilitate user interactions and community features. Although not currently implemented at this stage, this app is present for future development. 

## User Experience

#### Ideal users:

- Someone who has experienced or is experiencing Narcissistic abuse;
- Someone who is interested in understanding more about Narcissism.

#### As a developer, I expect:

- The user to have easy navigation of all the content in the website;
- The user to find the website appealing and informative in a different way than a search engine;
- The user to find the content helpful and find support during their awareness journey or/and recovery process.

### User Stories: Site accessibility & functionality

#### [EPIC A] Simple viewers (users not logged in)

1 - As a simple viewer of the site (not registered or logged in), I expect to have access to all the information and sources available on the website, so that I can explore and gain insights about the site.

2 - As a simple site viewer, I want to have the ability to register or log into the website, so that I can access the exclusive content in the community page and engage more actively with the site's features.

3 - As a site viewer, I want to be able to log in and contribute by posting and editing my comments on community and topic pages, fostering a sense of participation and collaboration within the website community.

#### [EPIC A] Potential Collaborators (users not logged in)

4 - As a potential collaborator, I seek a straightforward contact form on the About page, so that I can have a convenient means to submit collaboration requests to the site creator, without having to set up an account.

#### [EPIC B] Registered users

1 - As a logged-in user, I require access to the comment functionality, so that I can post, edit, and update my comments to engage and discuss within the website community.

2 - As a logged-in user, I expect to be able to read all approved comments, so that I can fully utilise the interactive features of the site and stay informed about contributions from other users.

3 - As a logged-in user, I can access the community page's content, so that I can participate in discussions, share insights, and connect with other users.

4 - As a logged-in user, I appreciate the ability to reset my password, so that I can regain access to the website in the event that I forget my login details.

5 - As a logged-in user, I can log out so that I can protect my account's security and privacy by securely ending my session and preventing unauthorized access to my account.

#### [EPIC C] Admin Users

1 - As a site administrator, I need the capability to select and add sources to the website, so that I can keep the content updated and relevant, enhancing the overall quality and value of the site to users.

2 - As a site administrator, I require the ability to update and edit website content, so that I can manage and maintain the accuracy, clarity, and relevance of the information presented to users.

3 - As a site administrator, I can approve or disapprove comments, ensuring that objectionable content is filtered out and the website maintains a respectful and constructive environment for all users.

### User Stories: Content specificity

#### [EPIC D] Casual visitor

1 - As a casual visitor, I can look at different material about narcissistic personality disorder so that I can gain insight into the subject.

2 - As a casual visitor, I want to be able to browse through different materials about narcissistic personality disorder so that I can gain insight into the subject without feeling overwhelmed or lost.

3 - As a casual visitor, I expect to understand the topic and scope of the website clearly so that I can make an informed decision about whether to explore it further or not.

4 - As a casual visitor, I expect an intuitive and user-friendly navigation system on the website so that I can effortlessly explore all sections and find relevant information without frustration.

#### [EPIC E] Someone interested in Narcissism

1 - As someone interested in narcissism, I expect to have convenient access to a diverse range of sources gathered in one place, providing me with insights and perspectives not readily available through mainstream search engines like Google.

2 - As someone interested in narcissism, I expect the website to offer a community forum or discussion board where like-minded individuals can share experiences, exchange insights, and support each other in coping with narcissistic relationships or behaviours.

#### [EPIC F] Potential victim of Narcissistic abuse

1 - As a potential victim of narcissistic behaviour, I seek resources and information on the website that can help me recognise and understand the signs of narcissistic abuse, empowering me to take necessary steps to protect myself and seek support if needed.

2 - As a potential victim of narcissistic abuse, I seek practical resources on the website, such as checklists for identifying red flags, coping strategies for dealing with manipulation tactics, and links to support groups or helplines for seeking assistance and guidance.

3 - As a potential victim of narcissistic abuse, I would appreciate the inclusion of personal narratives or testimonials from survivors who have overcome narcissistic relationships, inspiring hope and resilience among those currently struggling with similar challenges.

## Features and functionalities

### Current Features
As previously mentioned, this is an ongoing project that I aim to develop further once I complete my Code Institute diploma.
At the current stage, the website is structured and functions as follows:

#### Navbar
The navbar on every page contains the website name, navigation links, and auxiliary text.
On smaller screens, navigation links and auxiliary text are displayed by clicking the hamburger icon. On larger screens they appear on the same line as the website name.

![Website name](https://i.ibb.co/JdDbNpY/my-screenshots-2024-03-29-at-19-39-01.png)

The navigation links are: 
- Home
- About
- Register (for non-logged-in users)
- Login (for non-logged-in users)
- Logout (for authorised users)

Navigation links for non-logged-in users:

![Navigation links for non-logged-in users](https://i.ibb.co/xsyNNKJ/my-screenshots-2024-03-29-at-19-39-52.png)

Navigation links for authorised users:

![Navigation links for logged-in users](https://i.ibb.co/51XG6wM/my-screenshots-2024-03-29-at-19-39-09.png)

#### Authentication and notification messages
Users can see their log status below the navigation bar. The following message will appear to the right of the acreen if users are logged in:

"You are logged in as [username]" 

Otherwise, a message stating they are not logged in will apprear, with a link:

"You are not logged in.
Log *here*."

Below the navigation bar will also appear other notifications, such as sign out, edits and deletions of comments.

Example:
![Sign out confirmation message](https://i.ibb.co/FHh8NZj/Sign-out-notification.png)

#### Footer
On every page, the footer displays copyright information.
![Footer with copyright information](https://i.ibb.co/pWSrrjN/my-screenshots-2024-03-29-at-17-01-21.png)

#### Homepage
There are currently six categories/topics displayed on the homepage, each with a brief description. 
Topic titles are listed below a square. By clicking the topic title or square, users can access the relevant page. Whenever the square is hovered over and clicked, it simulates a button being pushed. This is a temporary effect, as I plan to add illustrations.

#### Topic page and content
The number of items on a page is kept to a minimum in order not to overburden the loading time and disorient the user.
"Prev" and "Next" buttons allow users to navigate between pages.

!['Prev' and 'Next' buttons](https://i.ibb.co/4tHWmw8/my-screenshots-2024-03-29-at-19-41-17.png)

A title at the top of the content provides users with a quick way to identify the topic. Example:

![Example of content in a topic](https://i.ibb.co/1sQvYWf/Example-of-content.png)

The content area will be implemented in the future, since I plan to include a small description below the content.

#### Comments section
A section at the bottom of the topic page allows authenticated users to leave and view comments. Authenticated users have CRUD capabilities, so they can create, read, update and delete comments.

The comment will need to be authorised by an Admin user to be visible on the website:
![Form to leave a comment](https://i.ibb.co/gj9S3zR/my-screenshots-2024-03-29-at-20-59-53.png)

Form to leave a comment:
![Form to leave a comment](https://i.ibb.co/vmsjCqj/my-screenshots-2024-03-29-at-20-51-20.png)

Once submitted, the user will be able to edit or delete it thorugh the buttons below the comment.

If the user needs to edit the comment, the text will reappear in the body field with an 'update' button:
![Form to update comment](https://i.ibb.co/Fqzv0Y2/my-screenshots-2024-03-29-at-21-00-10.png)

In case of deletion, the user will be asked to confirm their choice. They will also have the option to cancel the action by clicking on "Close":

![Delete comment confirmation](https://i.ibb.co/sHx3dw8/my-screenshots-2024-03-29-at-20-59-44.png)

Users will see a notification when their comments are submitted and awaiting approval: 
![Notification "Comment updated"](https://i.ibb.co/DWdDjfs/my-screenshots-2024-03-29-at-21-01-59.png)

The same applies when users delete a comment:

![Notification "Comment deleted"](https://i.ibb.co/xjSFKmS/my-screenshots-2024-03-29-at-21-08-04.png)


A comment count, located above the comments section, is visible to everyone (see image below). **Users who are not authenticated cannot access this section**. Instead, they will see a link to log in:

![Message for not authenticated users](https://i.ibb.co/WFCtK5J/my-screenshots-2024-03-29-at-19-40-59.png)

#### Register page
The Register page, which is visible to non-logged-in users, presents a registration form. The mandatory fields are 'Username' and 'Password' (to be entered twice), while the optional field is 'Email' address.

![Register page](https://i.ibb.co/6X7qPDX/my-screenshots-2024-03-30-at-11-21-11.png)
In addition, it contains a link that leads to the Login page, if the user has already created an account.

#### Sign in page
The Sign in page allows registered users to sign into their account by entering their username and password. It also contains a link to the Register page, if the user hasn't created an account yet.
![Sign-in form](https://i.ibb.co/2htJsWd/my-screenshots-2024-03-30-at-11-21-19.png)

Also, users have the option of having their login information remembered, so they don't have to re-enter their login information each time they visit the website.

#### Logout page
The logout page allows users to log out of their accounts. The user must confirm their choice. The user can also cancel the action and return to the homepage.

![Log out form](https://i.ibb.co/wrqnYDk/my-screenshots-2024-03-30-at-10-57-15.png)


#### About page
This page outlines the purpose of the website and my role as a creator. The purpose of my short presentation is to establish trust with the viewer and to explain the current state of the website in a clear and concise manner.

Below the About section there is a collaboration/feedback form that I invite the viewer to use.

#### Collaboration form
![Collaboration/feedback form](https://i.ibb.co/9sQGFQb/my-screenshots-2024-03-30-at-09-48-35.png)

The form on the About page is accessible to everyone. If casual viewers did not want to register, I wanted them to be able to send me messages directly. 
A brief text invites the user to contact me.
The fields required are 'Name', 'Email' and 'Message'.

Once submitted, the collaboration request will be visible to admin users on the Django admin board.

![Collaboration forms visible in the Admin board](https://i.ibb.co/tK6yZNV/my-screenshots-2024-03-29-at-23-19-59.png)

From there, it will then be possible for admin users to acknowledge the message as read or simply delete it.

![Delete option in the Django admin board](https://i.ibb.co/kMqyRBk/my-screenshots-2024-03-29-at-23-20-25.png)

#### Django admin board
The admin board allows administrators to control the website. They can add topics and contents, edit the About section and authorise comments to be published.

![Django Administrator Board](https://i.ibb.co/NW7VpRC/my-screenshots-2024-03-30-at-10-50-46.png)

In the admin board, it is also possible to control users' permissions, deactivate their accounts or make them admin users.

The functionalities are still basic and will be improved in the future.

#### Favicon
This website's favicon is a purple square with the first capital letters of the website's subject: NPD.

![Favicon: NPD in a purple square](https://i.ibb.co/Ykpf4gs/my-screenshots-2024-03-29-at-23-01-13.png)

#### Error pages
The error pages simply provide the user with a link back to the homepage and inform them what type of error they encountered.

### Future Features and general aspects left to implement

I have a big project in mind, and this is just the first version. The following are some of the future aspects that still need to be implemented:

- **Graphics & content organisation**:
  In order to make the website professional and appealing, the graphic needs to be improved. I'm considering two approaches for enhancing the homepage: I may hire an illustrator to design topic images or, alternatively, creating these images myself.
  Additionally, I would like to improve the navigation with tags and organize the content more attractively.

- **User account**:
  One of the plans is to expand the functionalities available to users, aiming to streamline their experience. This would involve creating a dedicated user account page where users can manage their account settings and comments conveniently. Additionally, they will have options to delete their account and reset their password for added control over their personal information.

- **Community page & comment app (or 'why did you create a Comments app?')**:
  I've included a comments app because I was laying the groundwork for a future community page. Even though its relevance may not be immediately apparent at the current state of the website, this is important in the future direction of the platform. Sharing is a crucial aspect of the healing process, and having a platform for users to interact will be integral to the site's purpose. The comments app will serve as an essential feature to manage user interactions and foster community engagement. This decision was made to establish a foundation for future features and enhance the overall user experience.

- **Collaborations & courses**:
  My primary objective is to better the site's visibility by focusing on aesthetic improvements. Once these enhancements are in place, I intend to promote the site on relevant channels and platforms where discussions related to the subject take place. My plan is to contact professionals to collaborate on content and offer courses tailored to users' interests and needs.

- **Error pages** are present in the website but the design is left to implement.

## Technologies used

### Programming Languages

- Programming languages used in this project are **HTML5**, **CSS3**, **JavaSctipt** and **Python**.

### Frameworks and Libraries

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages;
- [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images;
- [Django:](https://www.djangoproject.com/) Main Python framework used in the development;
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration;
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [Gunicorn:](https://gunicorn.org/) Python HTTP server, used as the Web Server to run Django on Heroku;
- [Jest:](https://jestjs.io/) A delightful JavaScript Testing Framework, used for automated tests;
- [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.

### Software and Web Applications

- [Code Institute Postgres database](https://dbs.ci-dbs.net) was the Database used for this application.
- [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze
- [PEP8](http://pep8online.com/) was used to check the code for PEP8 requirements.
- [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
- [JSHint:](https://jshint.com/) Check code for JavaScript validation.
- [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
- [Code Beautify - Python Beautifier](https://codebeautify.org/python-formatter-beautifier) was used to format the code.
- [Heroku: Cloud Application Platform](https://dashboard.heroku.com/apps) was used for the deployment.
- [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used as the repository for the project after being pushed from Git.
- [VSCode](https://code.visualstudio.com/) was used as the primary local Integrated Development Environment (IDE) for coding and development.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create a draft flowchart during the planning process.
- [ImgBB](https://imgbb.com/) was used to upload images and extract the source code.
- [Am I Responsive?](http://ami.responsivedesign.is) was used to generate the mockup of the website.
- [Table Convert](https://tableconvert.com/) was used to generate tables for the TESTING.md file.
- [ChatGPT](https://chat.openai.com/) was used as helpful tool during the debugging process.

## Modules imported

- **django.contrib**: Django modules for various functionalities like admin.
- **django.urls**: Django module for URL routing.
- **pathlib**: Module for working with file paths.
- **os**: Module for interacting with the operating system.
- **sys**: Module providing access to some variables used or maintained by the Python interpreter.
- **dj_database_url**: Module for parsing database connection URLs.
- **django.shortcuts**: Django module for shortcuts to common actions.
- **django.core.paginator**: Django module for pagination.
- **django.contrib.auth.decorators**: Django module for authentication-related decorators.
- **django.views.generic**: Django module for generic views.
- **django.contrib.messages**: Django module for displaying messages to users.
- **comments.models**: Custom module for comment models.
- **content_management.models**: Custom module for content models.
- **django.forms**: Django module for form handling.
- **django.contrib.auth.models**: Django module for authentication-related models.
- **django.utils**: Django module with various utility functions.
- **django.test**: Django module for testing utilities.
- **cloudinary.models**: Module for integrating Cloudinary with Django models.
- **django_summernote.admin.SummernoteModelAdmin**: Module for integrating Summernote with Django admin for model forms.
- **django.shortcuts.render**: Django module for rendering templates.
- **.models.About**: Custom module for About model.
- **.forms.CollaborateForm**: Custom module for CollaborateForm.
- **django.test.TestCase**: Django module for creating test cases.
- **.models.CollaborateRequest**: Custom module for CollaborateRequest model.

## Testing

Testing information can be found in [TESTING.md file](TESTING.md).

## Deployment

Heroku was used to deploy the site. Here are the steps to deploy:

1. Log in to Heroku.
2. Click "Create a new app".
3. Choose the app name and region.
4. Click "Create app".
5. Navigate to the "settings" tab.
6. "Click "Reveal Config Vars".
7. Add a configuration variable to Heroku's Settings. The key is PORT and the value is 8000
8. Scroll down to "Buildpacks".
9. Click "Add Buildpack".
10. First, add "python" and click save.
11. Second, add "nodejs" and click save.

The live site can be found here: [Narcissistic Website](https://narcissism-website-8191a44972de.herokuapp.com/) 

### Cloning:

1. Click the "Code" button in the GitHub repository.
2. Choose "HTTPS" and copy the URL.
3. Open the Terminam (in macOS) or Git Bash (in Windows) and navigate to the repository where you would like to locate the cloned repository.
4. Type "git clone" followed by the copied URL.
5. Press enter to create the clone.

### Forking

You can fork this project and make a copy of the original repository in your own GitHub account. In this case, you can view or make changes without affecting the original. To do so:

- log into GitHub and locate the GitHub Repository;
- at the top right of the screen, click the Fork button.

It should be noted that all changes pushed to the main branch are automatically reflected on the site.

## Database creation
The database used is PostgreSQL.

### How to get started:
1. Go to https://dbs.ci-dbs.net/
2. Input email address and click Submit;
3. The Database will be created and the details emailed;
4. You will need the DATABASE_URL to connect the database to your project.

### How to connect the database to the project:
1. Create a file named **env.py** at the top level of the project;
2. Open the **.gitignore** file and add **env.py** to prevent the secret data you will add to it from being pushed to GitHub.
3. In the **env.py** file, import Python's operating system module and use it to set the value of the **DATABASE_URL** constant to the URL copied from the details emailed to you - see below:
```
import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>")
```
4. Pip install the two packages required to connect to your PostgreSQL database. Then add them to the requirements file:
```
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 freeze --local > requirements.txt
```
5. In **settings.py** import the appropriate packages and connect the **settings.py** file to the **env.py** file:
```
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
6. In the **settings.py** file, comment out the local sqlite3 database connection set up by default.

7. In the **settings.py** file, connect to the environment variable **DATABASE_URL** you previously added to the **env.py** file:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
8. Your project is now connected to the database and you can create database tables with Django's **migrate** command.

## Credits

### Content

DA AGGIUNGERE

### Code

The code was mainly based on Code Institute's walkthrough in the Django module. This is my first time using technologies such as Django and Bootstrap, so it has been challenging, but my goal is to keep working on this project going forward and improve the code.

### Acknowledgment

I am grateful to my mentor Brian Macharia for his suggestions and to my classmate Niclas for his precious support. A special thanks goes to the amazing tool that is ChatGPT: it helped me with the debugging process and whenever I got stuck.
