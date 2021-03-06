Where The Truck?
================

Where The Truck? helps San Franciscans find the food trucks they love.  

A community powered application, Where The Truck? allows users to update the current location of food trucks in the city using geolocation data taken from their browsers or smartphones.  Users can securely login, vote on whether food trucks are where other users say they are, update a truck’s location, see its Yelp reviews, and get directions to it.  Machine learning algorithms filter out updates by users who gain a reputation for inaccuracy based on community votes—an option users can toggle off in their preferences.  Where The Truck? also emphasizes secure authentication, using password encryption and resetting.

Test it out <a href="http://www.wherethetruck.co/" target="_blank">here</a>.  (You may need to toggle the "Show updates older than 1 day" option.)

###Contents
<ul>
	<li><a href="#overview">Overview</a></li>
	<li><a href="#technologies-and-stack">Technologies & Stack</a></li>
	<li><a href="#features">Features</a></li>
	<li><a href="#future-plans">Future plans</a></li>
	<li><a href="#technical-choices">Technical choices</a></li>
	<li><a href="#screenshots">Screenshots</a></li>
	<ul>
		<li><a href="#user-actions">User actions</a></li>
		<li><a href="#directions">Directions</a></li>
		<li><a href="#responsive-design">Responsive design</a></li>
		<li><a href="#bootstrap-js-elements">Bootstrap JS elements</a></li>
	</ul>
<li><a href="#forking">Forking</a></li>
<li><a href="#about-me">About me</a></li>
</ul>



Overview
----------------

Where The Truck? features an interactive map showing the most recently updated location for each food truck in the database.

<img src="screenshots/homepage.png" width="100%" alt="homepage" title="homepage">

<h4>The map:</h4>
<ul>
	<li>Shows the most recent location of each food truck</li>
	<li>Provides routing and times/distances to food trucks</li>
	<li>Displays Yelp ratings and links to Yelp pages for each truck</li>
	<li>Displays timestamp data for when a truck's location was updated</li>
	<li>Shows upvotes and downvotes on the accuracy of each truck's current location</li>
</ul>

<h4>Users can:</h4>
<ul>
	<li>Sign in/sign out/sign up (create an account)</li>
	<li>Reset their password</li>
	<li>Update the location of a food truck by dragging its icon on the map or by clicking Truck Sighted! to update its location to their current geolocation</li>
	<li>See recent location updates made by other users</li>
	<li>Get directions to food trucks from their current location</li>
	<li>Select which trucks they want to see on the map </li>
	<li>Click on truck names to center the map on that truck's (bounce animated) icon</li>
	<li>Choose to see location updates even if they have bad ratings (or predicted bad ratings)</li>
	<li>Save their preferences</li>
	<li>Vote on the accuracy of location updates made by other users</li>
	<li>Change their existing vote on another user's update</li>
	<li>Read the help section ("?") modal to get answers to common questions.</li>
</ul>

Technologies and stack
------------------------

<h4>Backend:</h4>
Python, Flask, SQLAlchemy, sqlite, passlib (encryption & verification).<br>
Flask extensions: Flask-Mail, Flask-Login, Flask-WTForms, Flask-CORS, 
Flask-SQLAlchemy.<br>
Machine learning: rating location checkins and using those ratings to rate 
users and predict the accuracy of their future checkins.<br>
Testing: doc string and unit tests.

<h4>Frontend:</h4>
JavaScript, jQuery, AJAX, Jinja, jQuery plugins (lightbox_me, timeago).<br>
HTML5, CSS3, Twitter Bootstrap (html/css/js framework), RWD (responsive web design).

<h4>APIs:</h4>
Google Maps Javascript V3, Yelp, Geonames, Twilio.

Features
-------------------


- [X] Get latitude and longitude from user's browser using HTML5 geolocation.
- [X] Store updated location data in a database with associated tables for users, location updates, and food trucks.
- [X] Flask app routes AJAX requests to the database and manages password reset form validation via Flask-WTForms.

#####Voting and user ratings
- [X] Calculate an overall rating for each location update using its upvotes and downvotes in a modified Wilson score interval algorithm.
- [X] Machine learning algorithm predicts if a given user's update will be accurate, based on their averaged update ratings, and hides the update if the user's average rating falls below a certain threshold.


#####Security with passlib encryption and Flask-Login
- [X] Encrypt and verify user passwords using hashes and salts.
- [X] Secure user sessions let users stay logged in.
- [X] Confirm user accounts via email and allow users to reset passwords using secure email links with unique tokens that timeout.

#####APIs and Cross Origin Resource Sharing
- [X] Enable cross origin resource sharing (CORS) by routing insecure API's through the python server.
- [X] Twilio API integration allows users to text the name of a food truck and receive a google maps link to its most recent location.
- [X] Prevent trolling by limiting location updates to within San Francisco, and preventing location updates in the bay using the Geonames Ocean API.


#####Data visualization and interaction
- [X] Dynamically display aging location updates using timeago.js and different icon images.
- [X] Show the last good* location update when a specific option is toggled on/off, causing the current update to be hidden. (*made by a logged in user, who has a user rating above a certain threshold)
- [X] Increase rendering speed when truck locations are updated, or display options are toggled, by using Javascript to manipulate cached data rather than re-requesting data from the server.
- [X] Customize checkbox appearances and interactivity, and site features based on logged in user's data and previous map interactions.
- [X] Foster learned user behavior using Bootstrap's Javascript popovers on voting options for non-users and users who haven't voted yet.
- [X] Create custom responsive web design (RWD) using CSS3.


Future plans
-----------------------
#####Adding more food trucks
Currently, there are only 6 trucks available to choose from.  I limited the number of food trucks I was working with for development purposes, but to be a useful product, I will need to add all the food trucks in San Francisco.

#####Accounting for multiple food trucks with the same name
Some companies have multiple food trucks, meaning there could be two Curry Up Now trucks on the map at any given time.  I plan to use geofencing to assign location updates within a given region to that region's designated truck.

#####Advanced user rating system
The machine learning algorithms used to determine whether a user is considered trusted and reliable rely on the voting system (upvotes and downvotes).  These votes only affect a user's given rating for the first hour after the user made that update (in order to prevent downvotes on older updates from hurting a user's rating).  But what happens if users are more inclined to click "Truck Sighted!" than to verify a truck's position with an upvote?  Depending on user behavior, it may make sense to implement a system in which location updates made within X radius and within X time of a given update count towards the previous update's upvotes, thus improving that update's user's rating.

#####Adjusting bad rating thresholds
Based on user interaction, the numbers chosen for determining a bad update or an untrusted user may need to be altered to be more or less forgiving.  Currently, the "bad update" threshold is set low for demo purposes.

#####Additional security
To prevent brute-force hacking attempts, I will add an increasing time delay after multiple failed login attempts.  I will also specify password length requirements.

#####User stats
Allow users to see their stats on their user pages, e.g. how many updates they have made, what's their user rating, etc.  

#####"Near me"
Besides centering the map on the user's location from the get-go (as long as they are within San Francisco), I may add a "Near me" functionality to refocus the map on the user's current location, and list the food trucks closest to them.

#####Real time updates
Currently, the page must be refreshed to show updated food truck locations.  This should be updated to happen in real-time with server-sent events.

#####SSL Certificate
This app needs to be run on https for security purposes, but is currently deployed on http://www.wherethetruck.co, pending approval of a certificate.  See it's <a href="https://dbyasso-wherethetruck.herokuapp.com/" target="_blank">herokuapp.com</a> page for the secure version.


Technical choices
-----------------------

#####Security
In any login system, security is important.  I wanted to ensure that user passwords couldn't be stolen, especially considering that most people re-use their passwords all over the place (despite warnings against such a practice).  Passlib offers a simple but effective encryption and verification system using hashes and salts, requiring only 3 lines of code: the import line, the encryption line, and the verification line.  

I chose Flask-Login to manage secure user sessions and session cookies to afford users the option of clicking "Remember me" when they login.  This Flask extension is well-known, well-documented, reliable, and offers exactly what I needed to implement that feature.  

Any real user system allows users to reset their passwords when they forget them.  To implement this, I needed to be able to send users emails, for which I chose Flask-Mail, an easy-to-use Flask extension that fit my project needs.  I exlored Flask-Security, a robust extension that builds off of Flask-Login and many other Flask extensions and libraries, but found it was not well-documented, bulky, and not the right choice for the task.  I ended up choosing to use the URLSafeTimedSerializer from itsdangerous to generate unique tokens that timeout to allow users to safely reset their passwords.

#####Flask-WTForms
Partway through the project, I discovered Flask-WTForms, a Flask extension that offers form creation and validation.  I switched to this method for all future forms on the site (password resets and the like) because of its simple and effective form management.

#####Machine learning algorithm
I found <a href="https://possiblywrong.wordpress.com/2011/06/05/reddits-comment-ranking-algorithm/" target="_blank">this article</a> useful when trying to determine the best way to rate updates and users.  Many systems just directly compare upvotes to downvotes, which is flawed.  5 upvotes to 4 downvotes may have the same ratio as 50 upvotes to 40 downvotes, but they are not the same, and shouldn't be treated as such by any system.  The latter has 10 upvotes more, versus just 1, and has many more votes in general.  The Wilson Score Interval accounts for these differences by normalizing the ratio on a 0 to 1 scale.  In this case, 50 upvotes to 40 downvotes will have a higher value than 5 upvotes to 4 downvotes.

However, the suggested algorithm at the end of the article would cause issues for updates with only downvotes.  Since I average all the calculated Wilson Score Intervals from all of a user's updates, having some with values of -5 (for 5 downvotes and 0 upvotes) would negatively impact the system.  As such, I modified the algorithm to instead create a normalized value on a scale of 0 to -1 for updates with only downvotes.

Only upvotes and downvotes made within an hour of an update count towards that updates calculated Wilson Score Interval.  This is to prevent downvoted aging updates, which may have been accurate within the first hour, but are no longer accurate 3 hours later, from damaging a user's rating (which is based on the averages of all their updates' Wilson Score Intervals).

#####Manipulating cached data
At first, every time a user toggled a food truck's visibility on or off, adjusted other display options, or updated the location of a particular food truck, I regenerated the entire map and requested all the food truck location data from my database again.  This was extremely slow, and caused the page to hang at times.  To speed things up and prevent errors, I changed the code so that it now simply manipulates cached data on the frontend for the food trucks, and doesn't need to reload the database info for each.  When a user toggles a display option, everything that happens occurs on the frontend using JavaScript and jQuery; there are no AJAX requests to the server.

#####Data visualization
Originally, if a food truck's most recent update had a bad rating, and the checkbox to "Show updates with bad ratings" was NOT selected, no location marker for that food truck would show.  This was a bad user experience, in my opinion.  I decided to store, along with the most recent location update, the last "good" location update (good meaning it fit specific criteria: it was made by a user, the user was in good standing - aka "trusted", and the update itself did not have a bad rating).  Now, when the most recent update has a bad rating or is made by an untrusted user and those display options are toggled to not show it, the food truck's last good location is shown.  This way, users can always see a location for each truck.

#####Custom CSS
Using CSS3, I customized the checkboxes and select dropdowns.  I didn't like their default appearances, and wanted to change their colors and styles to better match that of the website.

I used Bootstrap for certain things, like button shapes and the nav bar, but found its responsive elements restrictive.  Because of this, I custom coded all the responsive design seen on the site (with the exception of the nav bar).

#####Code structure
When I decided to use Flask-Login for secure user sessions, I had to switch from SQLAlchemy to Flask-SQLAlchemy.  I had to add this line "db = SQLAlchemy(app)" to my model.py file, which meant I needed access to my Flask app, which I implement in my python server's routing.py file.  To prevent a circular import, with model importing app from routing, and routing importing model, I separated the Flask app creation into its own separate file, flaskapp.py.

All my routes are in one file, routing.py, and my table class methods and definitions are in a separate model.py file.  I try to keep similar functions grouped, and put all API-related routes at the bottom of routing.py.

For JavaScript, I separated all the JS needed to manipulate the map and food truck data from the user signup and login JavaScript code.  This code doesn't need to interact, so it made sense to fully separate the two.

On the frontend, rather than recode my nav bar for every web page, I used Jinja templates to simplify the process by extending from a base.html file that contains the nav bar.

Screenshots
-----------------------

######Updating a food truck's location using geolocation data - at the click of a button
<img src="screenshots/updateLocation.png" width="100%" alt="update location" title="update location">


####User actions:

######Login using lightbox_me.js
<p align="center">
	<img src="screenshots/loginLightBox.png" width="50%" title="login lightbox" alt="login lightbox">
</p>

######Password recovery via unique url token sent by email
<img src="screenshots/forgotPassword.png" width="100%" title="forgot password page" alt="forgot password page">
<p align="center">
	<img src="screenshots/resetPassword.png" width="60%" title="reset password page" alt="reset password page">
</p>

######User settings: logged in users can reset their passwords
<p align="center">
	<img src="screenshots/userSettings.png" width="60%" title="user settings page" alt="user settings page">
</p>

####Directions

######Selecting travel type from the dropdown
<p align="center">
	<img src="screenshots/getDirections.png" width="50%" title="get directions" alt="get directions">
</p>

######Responsively displaying map and written directions
<img src="screenshots/directions.png" width="100%" title="display directions" alt="display directions">
<p align="center">
	<img src="screenshots/responsiveDirections.png" width="75%" title="responsive directions container" alt="responsive directions container">
</p>

####Responsive design

######Largest screen
<img src="screenshots/homepage.png" width="100%" alt="largest screen homepage" title="largest screen homepage">

######Large screen
<img src="screenshots/responsive1.png" width="100%" alt="large screen homepage" title="large screen homepaage">

######Medium screen
<p align="center">
	<img src="screenshots/responsive2.png" width="75%" alt="medium screen homepage" title="medium screen homepage">
</p>

######iPad
<p align="center">
	<img src="screenshots/iPad.png" width="75%" alt="iPad homepage" title="iPad homepage">
</p>

######Mobile
<img src="screenshots/mobile.png" width="45%" alt="mobile homepage" title="mobile homepage">
<img src="screenshots/mobileMenu.png" width="45%" alt="mobile menu" title="mobile menu">

####Bootstrap JS elements

######Modal help menu
<img src="screenshots/helpModal.png" width="100%" alt="help modal" title="help modal">

######Voting popovers telling users how to vote on location accuracy for updates
Pictured here for a user who is not logged in
<p align="center">
	<img src="screenshots/votingPopover.png" width="50%" alt="voting instructions popover" title="voting instruction popovers">
</p>


Forking?
-----------------------
You'll need your own API keys for Google Maps, Yelp, and Twilio, and your own username for Geonames.  And don't forget to update the email address and mail password for Flask-Mail in app.config!

	pip install -r requirements.txt

	python routing.py


About me
-----------------------

Check out my <a href="https://www.linkedin.com/in/danielleyasso" target="_blank">LinkedIn</a> profile for more information on my experience, education, and projects.  See some of my starred GitHub projects for other examples of my code.