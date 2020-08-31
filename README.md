<img src="https://andeweg-festival-zvl.s3.amazonaws.com/media/FestivalZVL_logo.png" style="margin: 0;">

# Festival-zvl (Festival van Zeeuwsch-Vlaanderen)

For over 30 years the Festival van Zeeuwsch-Vlaanderen has been the biggest festival for classical music in Zeeuwsch-Vlaanderen (Zealand's Flanders). This is the Dutch part of Flanders, disconnected from The Netherlands by the River Scheldt. A quiet, rural, but culturally rich area. This is where different venues form the stage for the festival. 
Over ten years I've had the privilege to create the program brochures, different printed material and the website. However, the ticket sale has always been outsourced to a local theater. This has meant an extra step for the visitor to buy tickets on a secondary website, away from the main site. The festival manager wants one-stop-shop. Having the tools now to build e-commerce sites will make it possible to have all the elements for one-stop-shopping on the main site.

 
## UX
 
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_1.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_2.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_3.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_4.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_5.jpg?raw=true" style="margin: 0;">


## Features

 
### Existing Features

##### Navbar:
Provides the festival logo, and links to the 'concerts', additional 'ticket information', the 'locations' of concerts, 
the 'previous' editions/years of the festival, a page with 'sponsoring' information and 'media' which holds some footage
from previous years, interviews and previews. 
On small screens the navigation collapses into a hamburger menu (MDBootstrap).

##### Selection options:
'Concerts' shows all concerts, under 'locations' you can view the concerts per location (the nature of the festival is that
mostly local people visit and like to see what's the nearest concert available), under 'previous' the concerts per year or
edition can be filtered.

##### Concert presentation:
The results are shown on the concert page as tweaked MDBootstrap cards with, when populated, the fields available for the concert,
edition and location. 

##### Ticket information:
The original website has more information here, since the ticket sales are outsourced, but some information on returning tickets
and buying at the location is given here if someone would wish not to buy online.

##### Locations:
Concerts per location can be shown here.

##### Previous:
We're about to start the 32nd edition of the festival and a lot of digital material and information is still available. So here
the previous editions can be populated to serve as a catalogue and impression of what the festival stands for.

##### Sponsoring:
This years' sponsors are presented and the main sponsor presents an editorial on it's cultural plans and involvement.


### Features Left to Implement
- Locations in the database can be used to implement Google Maps functionality: creating directions and showing the location on the map.
- For more easily populating the database a time/date picker can be implemented.
- 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
