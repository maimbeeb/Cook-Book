# Cook-Book

	Mariam'S Munch – Third milestone project
		
		Mariam'S Munch as the name reflects is a cooking website that is designed for people who love cooking and would like to share their experience of cooking in the form cooking recipes to all the food lovers of the world. 
		Food Lovers and chef can stay connected to the website by contributing, accessing, storing, editing and deleting their cooking experience online anytime they want to by adding the cooking recipes to the database.
		This website has provision to add more functionalities along the way to provide better experience to the Users.
			
		So now on No need to buy any more magazines or cook books!. This website provide enormous options so Food lovers don't have to eat brocolli and boiled chickcen every day.
		If you have an awesome recipe you want to share? Please dont hesitate to add it to the repository! you can share as many recipes with the world as you please.
		If you want to explore a classic dish with a twist or something never seen before, Just click a search button in the website.
		
	UX
	
		The munch online cookbook takes on a modern design by implementing features from the Materialize.css framework. A fixed navbar remains a constant theme throughout, with orange being the dominant colour throughout each of the templates (e.g. form input underlines). The application was designed to work just as well on devices with small screens as those with larger ones.

		A sidenav consisting of the munch logo, as well as options to filter and sort has been implemented (detail of which can be found in the Features section below).



		All of the recipes on the home page are displayed on Materialize cards, each showing a photo of the recipe, the recipe title and it's difficulty. Users can also see how many views that particular recipe has attracted as well as likes. By pressing the thumb button on the homepage, the user can like a recipe at a glance.

		Add Recipe


		The user is redirected to this page when they would like to add a recipe of their own. On this page are a number of inputs that the user must fill in. Each follows the colour scheme and theme of the project, and carefully guides the user through the form with intelligent labels and icons.

		The user can be as detailed or as simplistic as they like when entering recipe ingredients and amounts. The user has the option to add as many ingredients (with respective amounts) as they'd like. Functionality to detect if required fields do not have a value has also been implemented.

		Similarly, the user can add as many steps in the method as they'd like to describe how to prepare and cook the recipe.

		A dropdown for the cuisine chooser, a slider for the number of people served by the recipe, and radio buttons to determine the difficulty of the recipe result in uniform data output by the form, and a pleasant user experience.

		Edit Recipe
		This page mimics many of the properties of the add recipe page, to help the user identify which fields they would like to update faster.

		If the user wants to save the changes, or discard them, familiar green (for success) and red (for warning) buttons are displayed at the bottom of the page respectively.

		Delete Recipe


		The user also has the option to delete a recipe from the page. To prevent users accidentally deleting recipes, a modal flashes up asking the user to confirm their decision before the recipe is permanently deleted from the database.
		
	FEATURES
	
		Existing features
		
			Register page - will allow new user to register to get access to the application

			Login page - will allow user to login before using the application

			'COOK-BOOK' - logo - when clicked it will always bring the user to the home page

			Navbar - created to navigate particular list: (recipes, categories or cusines). Across the navbar the are links with names of the lists. When hoover over the link color will change. For smaller devices the navbar collapse into burger icon.

			'Add New Recipe' - button - when clicked, it will allows the user to add new recipe

			'Search By Category' - button - when clicked, it will allows user to search recipes by particular category

			'View' - button - when clicked, will bring to individual recipe page

			'Edit Recipe' - button - allows user to edit particular recipe and make changes

			'Remove' - button - allows user to remove particualar recipe

		Features left to implement

			Feature that will allow user remove or edit(make changes) only its own recipes - but not others users recipes.
	
	Technologies Used
	
		HTML
			This project uses HTML to build the foundation of the web application and includes links to Materialize, Materialize JS, CSS, and Font Awesome.
		CSS
			This project uses CSS to style the features of the web application, including the header, footer and each page of the cookbook.
		JavaScript
			This project uses JavaScript for interactive functionality of the application.
		Python
			This project uses Python to provide the backend functionality of the cookbook, including functions to add, edit or delete a recipe.	
		PyMongo
			This project uses PyMongo which is a MongoDB driver for Python, used to access the MongoDB database.
		JSON
			This project uses JSON within mLab to provide the core data for the cookbook, including recipes, users, categories, etc.
		mLab
			This project uses mLab to host the database for the application.
		Flask
			This project uses the Flask microframework to bring the frontend and backend of the application together.
		jQuery
			This project uses jQuery which is included with Materialize to initialise many of the Materialize components used within the application (script found in base.html).
		MongoDB
			This project uses MongoDB which is used to contain the database collections.
		Font Awesome
			This project uses Font Awesome to provide icons for the application.
		Google Fonts
			This project uses Google Fonts to provide fonts for the headings of the web application.
			
	TECHNOLOGIES USED
		Git - used command line to for regular commits and to push my project to github
		Github - used to remotely store project code and allow public to see my website
		Bootstrap 3.3.7 - https://getbootstrap.com/docs/3.3/ bootstrap 3.3.7 used for responsive navbar, grid layout of the page;
		JQuery 3.3.1 - to assist the bootsrap
		Materialize 1.0.0 - https://materializecss.com/text-inputs.html used for imput fields
		Material Design Icons - https://material.io/resources/icons/?style=baseline used to add icons to the input fields
		Heroku - this application is hosted via heroku
		Front-End Technologies
		HTML - to create basic structure
		CSS - to add styles to the websites
		Back-End Technologies
		Flask 1.1.1 - to construct and render templates
		Python 3.6.8 - used as the backend programming language
		MongoDB Atlas - database used to storewebsite backend data
		PyMongo 3.8.0 - used for interacting with MongoDB database from Python
		Jinja - to display back-end data to the front-end
		BSON ObjectId - allows you to create and parse ObjectIDs without a reference to the MongoDB or bson modules
			
	Testing

		Manual Tests
		This web application has been manually tested with different scenarios that the user may experience.

		Sign In

		Click on 'Sign In' in the header or in the welcome card and be directed to 'signin.html'.
		Sign in with username 'USER1' and password 'user1'.
		Click on 'Sign In' and be directed back to the homepage.
		Check the user is logged in by seeing if 'Add Recipe' and 'My Recipes' are available in the navigation.
		Register

		Click on 'Register' in the header or in the welcome card and be directed to 'register.html'.
		Choose a username and password of your choice.
		Click on 'Register' and be redirected to 'home.html'.
		Check the user is logged in by seeing if 'Add Recipe' and 'My Recipe' are available in the navigation.
		Homepage

		Click on the brand logo in the top-left corner of the page or click on 'Home' in the navigation bar.
		Be directed to 'home.html'.
		Recipes by...

		Choose to filter by category, difficulty or ingredient and select an option from the dropdown.
		Be directed to appropriate page depending on whichever filter has been chosen.
		Recipes By Cuisine

		From the homepage, choose a cuisine and be shown cuisine description and a button to view all recipes by chosen cuisine.
		All Recipes

		Choose 'All Recipes' in the navigation bar and be directed to 'allrecipes.html'.
		Be shown all recipes in the database on one page.
		Be shown recipe description and details when card is clicked on.
		View Recipe

		Click on 'View Recipe'
		Be directed to the get_recipe page and be shown all details of the recipe, including the ingredients, method and image.
		Add Recipe

		If username is in session, be directed to 'addrecipe.html'.
		Fill in all details in the form and click 'Add Recipe'.
		Be redirected to the homepage.
		Edit Recipe

		On 'My Recipes', click on 'Edit Recipe' when viewing a recipe card.
		Edit any details within the form.
		Click on 'Update Recipe' and be redirected to 'home.html'.
		Delete Recipe

		On 'My Recipes', click on 'Delete Recipe' when viewing a recipe card.
		Be redirected to 'My Recipes' and see if the recipe has been deleted from the database.
		Return To Homepage

		Click on 'Return To Homepage' and be redirected to 'home.html'.
		Sign Out

		Click on Sign Out and be directed to the message page with options to sign back in or return to homepage.
		Responsiveness Testing
		This application has been tested on all mobile, tablet and desktop screen sizes with the Firefox Mozilla Developer Tools and Google Chrome Developer Tools. From these tests, all issues have been resolved.

		Code Validation
		The HTML, CSS and JavaScript code for this application has been run through and validated by The W3C Markup Validation Service and JSHint, with the exception of the validation service seeing the Flask/Jinja markup as errors.

		Bugs
		In the 'Edit Recipe' form, the 'Category' and 'Allergens' dropdown list will not have preselected values.

		Register functionality bug - this function was missing a key line of code which did not allow the user to successfully register into the application and therefore threw a "Method Not Allowed" Exception. This has been corrected and re-tested.
		
	Testing Procedure
			
		Programatical Testing
		Created a simple unit test in tests.py which initially failed.
		These tests made a range of assertions which can be seen in the comments of each test in that file.
		Once a full range of tests were created, I then created utils.py with utility functions that related to each test.
		These functions are explained in the comments within utils.py
		When the functions were complete, all tests were then correctly passing, and I ensured they continued to pass while developing further code.
		Manual Testing
		used Developer Tools in browser to test smaller view-ports and mobile responsiveness
		Try to create a new recipe and select an existing Author Name
		Try to created a new Author Name via the Add Recipe page
		Try to create a new recipe
		Check if the user is correctly redirect to Add Recipe upon saving the new Author
		Check if the success message will be displayed (on All Recipes) updon saving a new recipe
		Try to edit/update an existing recipe
		Try to delete an existing recipe


	Deployment
	
		The source code for this application can be found on Github and the application itself has been deployed onto Heroku. There is no difference between the GitHub code and the code in the live application.

		It can be installed with the following steps:

		Download the git repository
		Sign up/login to Heroku.com
		From the dashboard click Create New App
		Enter a unique name and your region and click Create
		From your command line, enter heroku to ensure heroku is installed (if not installed this can be done with sudo snap install --classic heroku)
		heroku login
		Enter your credentials for heroku.com
		sudo pip3 install Flask
		sudo pip3 install pymongo
		sudo pip3 freeze --local > requirements.txt
		echo web: python run.py > Procfile
		git add .
		git commit -m "initial commit"
		git push -u heroku master
		heroku ps:scale web=1
		Make sure to set debug to True.
		From heroku.com app settings: set config vars to IP : 0.0.0.0, PORT : 5000 and MONGO_URI :mongodb://[username]:[password]@ds129914.mlab.com:29914/online_cookbook, ensuring that you update the username and password accordingly.
		Click More > Restart all Dynos
		Application is live at https://your-app-name.herokuapp.com/
		This application's source code has been modified since the initial deployment - this was to fix a major bug regarding the register functionality, and to also tidy up the indentation of the HTML templates.
	
	Credits
	
		Many times i refered to the python documentation
		During the project i refered to the flask docs as well which have been a huge help
		A big thank you to my mentor for planning and helping with the projects
		A big thanks to tutor support for helping me out with many difficult issues.
		A tutorial has been taken for learning how to use context varibles and sessions on Youtube
		Many more resources have been consulted online for advice and python syntax (stackoverflow, pyhton pep8, blogs, etc) so thank you to all the authors!
	
	Credits

	
	All recipes on this website are credited to the author accordingly. Most are from the bbc.com food website with some coming from recipe books. All details are indicated where necessary.

	Media
		All images are from free image websites including www.freeimages.com, www.shutterstock.com and https://pxhere.com. The favicon is from https://www.freefavicon.com

		Acknowledgements
		This project was based on a brief written by Code Institute to fulfil requirements of their Data Centric Development module (part of the Full Stack Web Developer course).

		I found the Pretty Printed YouTube channel a huge help in learning about Flask sessions and error handling.

		Many thanks also to Chris Zielinski who is my Code Institute mentor, for offering ideas and solutions to various issues throughout the project, as well as endless patience and understanding!
