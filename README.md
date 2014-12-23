Where The Truck?
================

Where The Truck? helps San Franciscans find the food trucks they love.  

A community powered application, Where The Truck? allows users to update the current location of food trucks in the city using geolocation data taken from their browsers or smartphones.  Users can securely login, vote on whether food trucks are where other users say they are, update a truck’s location, see its Yelp reviews, and get directions to it.  Machine learning algorithms filter out updates by users who gain a reputation for inaccuracy based on community votes—an option users can toggle off in their preferences.  Where The Truck? also emphasizes secure authentication, using password encryption and resetting.

Test it out <a href="http://www.wherethetruck.co/" target="_blank">here</a>.

###Contents
<ul>
	<li><a href="#overview">Overview</a></li>
	<li><a href="#technologies-and-stack">Technologies & Stack</a></li>
	<li><a href="#features">Features</a></li>
	<li><a href="#future-plans">Future plans</a></li>
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