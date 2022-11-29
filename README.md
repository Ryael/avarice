# Avarice

### A website for a CLI horror-themed text adventure.

[Avarice - Live Website](https://avarice-txt.herokuapp.com/)

![Stars - Badge](https://badgen.net/github/stars/Ryael/avarice) ![Watchers - Badge](https://badgen.net/github/watchers/Ryael/avarice) ![Issues - Badge](https://badgen.net/github/issues/Ryael/avarice)

![Avarice - Animation](docs/screenshots/memoria-animation-1.gif)

Everyone plays games in this day and age. Consoles and gaming PCs are more common than ever, and one can't forget about the advent of mobile phones gaming. It's a fun little distraction (and sometimes not-so-little) to immerse yourself in a different world and universe. You can be somebody else, living a different life, with different problems. It works well as both escapism and as a means of self-realisation, as games can sometimes be more than just fun experiences depending on their thematic principles and any lessons those might carry. Additionally, text-heavy games can enhance user comprehension and volcabulary as it's not that different from reading a book. After all, what is a text adventure if not an interactive novel?

I wanted to pay homage to the video games of the 1980s, which paved the way forward for action, adventure, and even horror games! The likes of "Zork" and "Spunky Spelunky" are what really inspired me to create a text adventure of my own. However, I wanted to create a horror themed text adventure inspired by the likes of the "Resident Evil", "Evil Within", and especially "Alien: Isolation". The idea was to have a potent adversary pursuing the player throughout the game as the player attempts to accomplish their objective. This becomes innately more difficult due to the lack of both visual and audio components, leading to the entire focus being shifted to the, well, the text! By that I mean the writing and its ability to establish a scene and create a forboding atmosphere that lasts throughout the course of the game.

![AmIResponsive Mock-up Image](docs/screenshots/responsive.png)

This is my third milestone project as part of Code Institute's Diploma in <strong>Software Development (E-commerce Applications)</strong>.

For this project, I decided to create a horror-themed text adventure game using Python. The key concept for this project is greed and this is wholly reflected in the game's title: "Avarice". The chosen monster is loosely based on a Wendigo from Algonquian-speaking First Nations in North America. Wendigos, amongst all mythical creatures, are the ones that best embody greed and gluttony. This is precisely why this game will explore the concept of greed and especially excessive and destructive greed in multiple aspects throughout.

This application is accessed by the player using the command line interface (CLI). It's hosted on Heroku and is displayed via the provided template JavaScript and HTML, which has not been altered in any way. There's no save-game function as this text adventure is intended to be played from start to finish in a single sitting or two, being easily finishable within 30 minutes or so. There multiple endings available, however, once the player figures out how to deal with what the game throws at them, replaying the game for the other endings will not be difficult or time consuming at all.

My vision for this game was for the player to have complete freedom within the game's world, and this is accomplished by four actions.

1. "Move"
2. "Examine"
3. "Hide"
4. "Recall" 

The "Move" function is what truly frees the player up, as it allows them to choose which cardinal direction to move in and let's them explore the world on their own terms. They are, of course, limited by the map and any obstructions it may have. "Examine" allows the player to examine certain objects within each room to learn more about the room, and maybe even find items. The "Hide" action is the key method in how the player deals with the monster: by hiding. Each room has predetermined objects and locations to use to hide themselves. Of course, not all of these locations are good, and as such, they aren't recommended to the player. Lastly, "Recall" allows the player to recall what they remember of the room upon entering it for the first time. This allows for the player to not be bombarded by information upon revisiting a prior room.

## Table of Contents

1. [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
3. [User Interface](#user-interface)
    - [Design Philosophy](#design-philosophy)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
4. [Features](#features)
5. [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
6. [Testing](#testing)
    - [Responsiveness](#responsiveness)
    - [Accessibility](#accessibility)
    - [Performance](#performance)
    - [Device Testing](#device-testing)
    - [Browser Compatibility](#browser-compatability)
    - [Testing User Stories](#testing-user-stories)
7. [Bugs](#bugs)
8. [Future Updates](#future-updates)
9. [Deployment](#deployment)
10. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks-&-tools)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals

The aim of this project is:
- To demonstrate my knowledge of Python, to document my experiences, difficulties, and solutions developed. No other languages or frameworks were used in the development of this project.

### User Goals

- Find a text adventure to play
- Find a suspenseful game that establishes a foreboding and threatening atmosphere
- Find a game that will help improve user comprehension, information retention, and volcabulary
- Explore horror tropes regarding mythical monsters and a ruined facility
- Have total freedom in how to explore the game
- Interact with the environment to learn more about the game world
- Have control in how to deal with the monster
- Read the displayed text at a comfortable speed
- Experience multiple endings depending on choices made
- Be provided feedback on performance after acquiring one of the main endings

### Site Owner Goals

- Provide a text adventure game to play for fans of this type of game
- Provide a suspenseful horror game that focuses on creating a threat that pertsists throughout the game
- Present horror trophes in a unique and engaging manner
- Give the user freedom by providing them with actions to roam the world and interact with objects within it
- Provide a clear explanation of the game rules and difficulty
- Provide links to the developer's social media should players discover any bugs

[Back to Top &uarr;](#avarice)
<hr>

## User Experience 

### Target Audience

- People who are looking of a suspenseful albeit enjoyable experience
- People who are looking for a quick break in an otherwise hectic lifestyle
- People who are looking for a mini-game that's simple enough for children
- Fans of memory card games
- Fans of traditional fantasy concepts
- People who are looking for a mini-game with an escalating level of difficulty

### User Stories

#### First Time Visitors

1. As a first-time visitor, I want to easily understand the main purpose of the game.
2. As a first-time visitor, I want to easily navigate the menus without getting lost.
3. As a first-time visitor, I want to learn about the developer.
4. As a first-time visitor, I want to learn where the images were sourced.
5. As a first-time visitor, I want to learn what the game rules are.
6. As a first-time visitor, I want to know what difficulties are available to me.
7. As a first-time visitor, I want to feel engaged when playing the game.
8. As a first-time visitor, I want to be provided visual feedback upon beating a round.

#### Returning Visitors

9. As a returning visitor, I want to quickly check if any new difficulties or game modes have been added.
10. As a returning visitor, I want to progress through the difficulty levels to strengthen my memorisation.

#### Site Owner

11. As the site owner, I want to clearly showcase the memory game.
12. As the site owner, I want users to be able to navigate the menus smoothly and easily.
13. As the site owner, I want to adhere to a specific vision and provide users with a very engaging game via its design and imagery.
14. As the site owner, I want to provide a clear explanation of the game-rules and the different difficulties.
15. As the site owner, I want to provide my social media contacts should users need to report a bug.
16. As the site owner, I want to provide attribution links to the source of the image.
17. As the site owner, I want to provide players a fun and beneficial game that can be enjoyed by players of all ages.

[Back to Top &uarr;](#avarice)
<hr>

## User Interface

### Design Philosophy

The design of this website began with a simple vision: I wanted to craft a clean and simple SPA with that was based on the old predominately [blue PS3 home theme](docs/screenshots/ps-theme.webp). With this as my core inspiration, the overall design of the website began to take form in my mind's eye. My idea was to find and use an image as the background that had a smooth and subtle light-blue to dark-blue gradient. After much searching I found [this lovely specimen on Freepik](https://www.freepik.com/free-vector/gradient-particles-background_4298560.htm#query=gradient%20particle%20background&position=0&from_view=search&track=sph). It has that exact colour scheme and wave-like particles that I had in mind, and after some manipulation I arrived at the current [background image](assets/images/background/main.png). This, combined with some simple and sleek visual menu elements is what makes the foundation of this project. I had hoped for the end result to be a combination of flashy and clean, which is a difficult balance to achieve but I think I was mostly successful and I am quite happy with the visual end result overall.

All sections of the website follow a similar structure with the "Memoria" title at the top of the page, the footer with the social icons at the bottom, and all interactive elements have similar hover/focus effects wherein they fade-in on mouse-over/interaction and fade-out gently on mouse-leave. This is done to establish a consistency throughout the website such that users become familiar with how interactive elements respond. The Rules & Difficulty, Leaderboards, and Credits section have a white with a slight hexagonal pattern as their main element as they contain text elements. Otherwise, the game portions of the website all possess complementary elements to the rest of the site, creating a sense of flow familiarity for new users.

On smaller viewports, the content expands to 80-100% of the width to reduce user scrolling burden and to allow for easier viewing. The exception to this is the memory game itself. On the easy and normal difficulties, the game board always keep to a square ratio. However, on the hard difficulty, the game board takes the shape of rectangle to best use as much of the available vertical space. This is intentional, as otherwise the cards become far too small on smaller resolutions to interact with and would be an accessibility nightmare.

You can find the images used for all the backgrounds below:

<details>
    <summary>Website Background</summary>
    <img src="assets/images/background/main.png" alt="Background image used for website">
</details>

<details>
    <summary>Game Background</summary>
    <img src="assets/images/background/game.webp" alt="Background image used for the game-board">
</details>

<details>
    <summary>Settings Background</summary>
    <img src="assets/images/background/settings.webp" alt="Background image used for the settings windows">
</details>

### Colours 

No pre-set colour palettes were used in the designing of this website. My vision was to have the site feel simple, clean, but also fancy and packing a bit of a flavourful punch. I wanted to focus on primarily three colours: blue, white, and purple. Shades of blue are used to establish structures and give form to the most important structures in the background, the game itself, and the game background. White is mainly used as the font and the buttons. Purple is used as an accent to the blue, often being used as the link and highlight colour. [Color-Name](https://www.color-name.com/) was used to find slightly lighter and darker shade variations of the colours used for this project. The text content is primarily dark-blue on a white background with darker titles. Buttons and their text elements are either entirely white that transition to purple or vice versa.

### Fonts

The fonts I chose for this project are Jost and Fredoka. Fredoka is the font for the general content, whereas Jost is used for title content. Prior to Jost, I had chosen and used Josefin Sans as my title font of choice. I saw it used [as a title here](https://elementor.com/blog/font-pairing/) and decided it was that geometric and retro look I wanted to introduce the user to the website. However, it unfortunately had uneven padding on its top and bottom, which is simply just how the font was designed. This made it very difficult to creative even padding areas. As such, I ended up looking for a similar font and fortunately Jost is visually very similar, and in fact, the shape of the capital "M" is even more visually appealing than what Josefin Sans had to offer. 

Fredoka was chosen because of it's round edges and overall bold and daring appearance. It epitomises "fun" and I figured this was perfect for text content on a browser game website. They complement each other well although I hadn't found any pairings that used these two before. I think this is a fairly specific case that works which otherwise wouldn't work if the design philosophy was more minimalistic.

Font-weights of 300, 400, and 600 were chosen for Jost and font-weights of 400 and 500. 400 was used as the default for both. 600 was used for a bit more weight and clarity, primarily in titles and especially the "Memoria" page title.

### Wireframes

The conceptualisation of the layout used in this project began with simple pen and paper sketches, which were then transformed into wireframes via Balsamiq. Everything shown here is a rough beta of the layout, some of which has changed during development.

This is the prototype of the project, which changes over the course of project development.

<details>
    <summary>Main Menu</summary>
    <img src="docs/wireframes/main.png" alt="Wireframe of the Main Menu">
</details>
<details>
    <summary>Settings Window</summary>
    <img src="docs/wireframes/settings.png" alt="Wireframe of the Settings Window">
</details>
<details>
    <summary>Game Board</summary>
    <img src="docs/wireframes/game.png" alt="Wireframe of the Game Board">
</details>

[Back to top &uarr;](#avarice)
<hr>

## Features

### Title

![Title](docs/features/header-title.png)

The Title is the first things users will see when loading the page and its geometric and retro look is here to make an impact. It's bold and assertive with its heavy font-weight and contrasting white on blue, and establishes the sort of design philosophy the rest of the website will adhere to. Upon mouse-over and focus, it plays [a subtle animation](docs/features/header-title-animation.gif) and converts the user's cursor to that of a pointer to indicate that it's an interactable element. Upon interaction it plays a script that reloads the page, effectively bringing the user to the Main Menu. As such, no matter what part of the game the user has navigated to, they are always a simple click or tap away from going back to the Main Menu. The name "Memoria" is simply a play on the word "memory" and has no other significant meaning aside from aesthetic preference.

### Main Menu

![Main-Menu](docs/features/main-menu.png)

The Main Menu is fundamentally the navigation menu for the website and also doubles up as the landing page. Upon loading into the page, the user is greeted by a subtle fade-in transition, which is used throughout the entirety of Memoria. It keeps people who prefer reduced motion in mind and is quick and simple on the eyes. From the Main Menu, the user has the option to: a) start a game, b) view the Leaderboards, or c) read the credits. All the [buttons have animations](docs/features/main-menu-animation.gif) that play upon hover/focus. A smooth fade in, and smooth fade out. Upon interaction, a script runs that hides the Main Menu and displays the relevant area instead. For example, clicking on Start Game will hide the Main Menu and instead display the Rules & Difficulty section alongside the return button, which can bring the user back to the Main Menu.

### Rules & Difficulty

![Rules & Difficulty](docs/features/rules-difficulty.png)

The Rules & Difficulty section introduces the rules of the game and the overall objective of the game. It also provides three buttons that allow the user to select their difficulty of choice. The difficulty level itself is explained within the name, where easy is 2x2, normal is 4x4, and hard is 6x6. From a single glance it is clear exactly what each button accomplishes. Their colour palettes are inverted due to the white background but [a similar animation](docs/features/rules-difficulty-animation.gif) plays upon hover/focus. Similar to Main Menu's script, upon interacting with any of the difficulties, the Rules & Difficulty section will be hidden and the game-board will be generated based on which difficulty was selected. 

### Memory Game - Easy

![Memory Game - Easy](docs/features/game-easy.png)

Here is where the magic happens! This is the core functionality of the website that displays a 4-card grid upon the Easy mode button being interacted with. The previous menu is hidden but the game itself is written such that the timer doesn't start counting until the user clicks on a card. There's nothing worse than games that have their timers begin counting before the user is even able to take an action. The emoji are randomised each time using a shuffle method but they are always pulled from the same list of emoji. The emoji approach is quite novel as it allows the website to not have to load images everytime as every device has their own version of emojis built in. 

The game board also has a simple border animation that runs around the edges, drawing the user's focus towards the game board. Upon selecting a card, they flip upwards. Upon selecting two non-matching cards, they both briefly shake to provide the user with visual feedback that there hasn't been a match before flipping back down. However, upon selecting two matching cards, the cards remain flipped. Once all the cards have been flipped, the board itself flips. At this point two things occur simultaneously: 1) the user is presented with their amount of flips and the time elapsed in minutes and second, and 2) a confetti script is run to give the user a reason to celebrate their victory. [Here is the example](docs/features/border-animation.gif) of the animated border and the win screen with the confetti. This is perfect for younger kids as it's flashy enough to keep them invested and to get a taste of what memory games are like before diving into the higher difficulties.

### Memory Game - Normal

![Memory Game - Normal](docs/features/game-normal.png)

Normal mode is pretty much identical to what is described up above except that the game board generates a 16-card grid. This is pretty much the ideal difficulty to play as it strikes the sweet spot between easy and normal, and is commonly what one would see when looking at other memory card games. It doesn't take too long but still tests the user's short-term memory. It's a nice and relaxing difficulty mode. Both the easy and normal modes retain their square ratio across all resolutions.

### Memory Game - Hard

![Memory Game - Hard](docs/features/game-hard.png)

Hard mode is very similar to the other two difficulties but the key difference is that it generates a 36 card grid. Playing on hard mode is significantly more time consuming and can take as much time as two full normal mode games, however, this game mode is here for those who are really trying to push their abilities and test their memory. Completing the game to have the board flip and seeing the confetti is extremely satisfying considering the time and effort needed to be put in, but I'd like to believe that it's all worth it! If the user is looking for a challenge, then they need look no further. Hard mode maintains a square ratio for most viewports except the very small and narrow ones, at which point it flex-wraps into a column. This is to make the best use of the vertical space, ensure that the cards themselves aren't too small, and prevent the game-board from overflowing entirely.

### Return Button

![Return Button](docs/features/return-button.png)

The Return to the Main Menu button is present on every section but the Main Menu. Its purpose is to bring the user back to the Main Menu as it simply plays the same reload script as the Title does, resetting the page to its default state: the Main Menu. It has the exact same animation as the other Main Menu buttons and is even styled the same to ensure consistency and familiarity. 

### Leaderboards

![Leaderboards](docs/features/leaderboards.png)

The Leaderboards section is unfortunately not finished. It was intended to be a section where players could select one of the three corresponding difficulties to display the top 10 times for each. Due to no backend knowledge, the intention was to use a service like [Parse Platform](https://parseplatform.org/). However, I ended up running out of time and didn't want to rush and ultimately fail properly implementing this, hence this feature will be implemented in the future.

### Credits

![Credits](docs/features/credits.png)

The Credits section is very similar to both the Rules & Difficulty and Leaderboards sections, both in how it displays and hides the other content and how it looks. Here the user can find my details and information on how to best contact me in the event of a bug. It also attributes the images used from FreePik.

### Footer

![Footer](docs/features/footer-icons.png)

The Footer of Memoria displays three social icons which are created via Font Awesome. These are links to my GitHub, LinkedIn, and E-mail. No more were added as the intention was to keep this strictly professional. The Footer is present in all sections, providing the user with easy and direct methods to contact me to report bugs or any other reason. They also have [a unique animation](docs/features/footer-icons-animated.png) that fades in and out, similarly to the buttons.

### Favicon

![Favicon](docs/features/favicon.png)

As with all websites, this one also has a Favicon that is displayed beside the Title of the page. A user can quickly and easily discern if they have Memoria open amongst many different tabs by looking for the capital "M" icon, which is rendered in the same font as the Title text, Jost.

[Back to top &uarr;](#avarice)
<hr>

## Validation

### HTML Validation

[W3C Markup Validation Service](https://validator.w3.org/nu/) was used to validate HTML code. No errors were found. 

![HTML Validation](docs/validation/html-validation.png)

### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. No errors were found. 

![CSS Validation](docs/validation/css-validation.png)

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate JavaScript code. It detected two undefined variables; however, they are from a library, which is where they're defined. It also detected seven unused variables are called from the DOM and hence JSHint is unable to detect that they are used. There were no errors found otherwise.

![JavaScript Validation](docs/validation/js-validation.png)

[Back to top &uarr;](#avarice)
<hr>

## Testing

### Responsiveness

[Website Responsive Test Online](https://websiteresponsivetest.com/) was used to extensively test the responsiveness of Memoria. All screen sizes and viewports are now accounted for, including even extremely small screen-widths like 240 px.

### Accessibility

[WAVE WebAIM](https://wave.webaim.org/report#/https://ryael.github.io/memoria/) was used to check for accessibility and no errors were found.

![WAVE WebAIM](docs/testing/wave-webaim.png)

### Performance

Google Lighthouse was used to assess the performance of this website. All tests were performed in incognito mode to avoid interference from any other sources. Tests were carried out on each section but the same result was returned every time. This was the same case for mobile, and as such, only one result will be provided. Performance could be improved yet again but I made a choice to not convert the main background due to the colours becoming [visibly distorted](docs/testing/background-issue.png). 

![Lighthouse](docs/testing/lighthouse.png)

### Device Testing

The website was tested on many different devices, such as:

- Samsung Galaxy S10
- Samsung Galaxy S21
- Samsung Galaxy Note 8
- MSI GE72 6QF Apache Pro
- iPhone 8
- iPhone 10
- iPhone 11
- iPhone 11 Pro
- iPhone 12
- iPhone 14 Pro Max
- iPad Mini (Landscape and Portrait)
- iPad (Landscape and Portrait)
- Vivo S1 Pro
- LG v60
- Huawei P40 Pro
- Google Pixel 6

### Browser Compatibility

- Mozilla Firefox
- Google Chrome
- Opera
- Safari
- Microsoft Edge

I tested the website extensively on Mozilla Firefox, Google Chrome, and Microsoft Edge. For the remaining two, I asked friends and family to test the website on my behalf while overlooking it to ensure cross-compatibility. No issues or bugs were reported.

### Testing User Stories

1. As a first-time visitor, I want to easily understand the main purpose of the game.
    - Upon navigating to the website, the user is automatically greeted with a clean and easily readable Main Menu that allows them to go to their page of choice. The Start Game button will bring them to the Rules & Difficulty section, where they can read about the rules and objective of the game.
    - At this point, users can then select a difficulty to start a game and see first-hand what the purpose of the game is.
    - In addition to this, they may navigate to the GitHub via the Footer and/or the Credits section, where they can read the introduction of the readme in order to ascertain the purpose.

2. As a first-time visitor, I want to easily navigate the menus without getting lost.
    - The website was designed to be easy to navigate and fluid. The top of each section has a Title which doubles as a back button alongside the actual Return Button, with clearly described descriptions so the user has an idea of where they'll end up upon interaction.
    - Every section always has a clear means of moving forwards or backwards, ensuring the user is never lost or overwhelmed.

3. As a first-time visitor, I want to learn about the developer.
    - Navigating to the Credits section is the best and most simple way to learn more about the developer, as it contains a short blurb, a means to report bugs, and attribution links for the images used throughout the project.
    - Additionally, the icons in the Footer allow the user to visit the developer's GitHub or LinkedIn, where they may learn additional information.

4. As a first-time visitor, I want to learn where the images were sourced.
    - The Credits section will hold the answer to this, as it contains full attribution links to the images, their source, and who they were designed by.

5. As a first-time visitor, I want to learn what the game rules are.
    - Simply pressing Start Game will bring the user to the Rules & Difficulty section, which clearly lays out the rule of the game, the objective, and how the difficulties differ.

6. As a first-time visitor, I want to know what difficulties are available to me.
    - Navigating to the Rules & Difficulty section by interacting with Start Game will bring the user where the difficulties are displayed via buttons alongside a clear descriptor of how they differ from each other.
    - To add to this, they can click on each difficulty before returning to the Main Menu and clicking on the others to see the difference for themselves.

7. As a first-time visitor, I want to feel engaged when playing the game.
    - Upon starting the game via any of the difficulty buttons, the board is faded in as it generates with a subtle yet fitting background and an additional animation that runs around the border of the board.
    - Additionally, feedback is provided to the user via the cards shaking upon an incorrect match being made. 
    - Further yet, the game-controls area shows the amount of flips they've made and the amount of time that has elapsed, allowing them to keep track of their moves and become more invested.

8. As a first-time visitor, I want to be provided visual feedback upon beating a round.
    - Upon the completion of the game on any difficulty, an animation is played where the board flips and confetti starts firing, increasing the user's engagement with the game by providing visual feedback of their accomplishment. 

9. As a returning visitor, I want to quickly check if any new difficulties or game modes have been added.
    - If the UI remains the same and there isn't any additional element that informs the user of an update, then they could check the GitHub to see if any updates have been made to the game.
    - Ultimately, they could also visit the Rules & Difficult section of the application to see whether or not new games modes or extra difficulties have been added as of yet.

10. As a returning visitor, I want to progress through the difficulty levels to strengthen my memorisation.
    - This is easily accomplished by starting with whichever difficulty the user may have left off on and work their way up the ladder that ends with the hardest difficulty.
    - At this point the user should attempt the fastest clear time possible without any means of cheating to hone their memorisation.

11. As the site owner, I want to clearly showcase the memory game.
    - The application is designed with the game at the forefront; the menus are sleek and easy to navigate, the semantic structure suggests that there is a game available here, and the clear labelling of buttons will bring the user to the game within seconds.

12. As the site owner, I want users to be able to navigate the menus smoothly and easily.
    - The website has a very clear Main Menu, with easily seen text due to the contrast of the background and the colour of the links. This allows for a smooth navigation experience.
    - Each section is built to be fluidic and flow in a coherent manner where the user learns relevant information as they go through each section of each page.

13. As the site owner, I want to adhere to a specific vision and provide users with a very engaging game via its design and imagery.
    - The consistency of the effects and colours used provide an experience that succeeds bringing many separate parts together to form something that's more than the sum of its parts.
    - All the backgrounds used are primarily blue with some purple hues to create a colour synergy and the application never deviates from its theme.
    - The game portion of the application itself is designed to provide as much feedback to user as possible, hopefully providing them with a highly engaging experience.

14. As the site owner, I want to provide a clear explanation of the game-rules and the different difficulties.
    - Users can find the explanation of the rules, objective, and different difficulties in the Rules & Difficulty section, which covers them succintly. 

15. As the site owner, I want to provide my social media contacts if users need to report a bug.
    - The Credits section links to the issues page on the relevant GitHub page and explains that this is the ideal place to report bugs.
    - Additionally, users may navigate to the Footer of the application and further navigate to the GitHub via that or send an e-mail altogether.

16. As the site owner, I want to provide attribution links to the website where I sourced images from.
    - The attribution links, where the images were found, and who they were designed and uploaded by can all be found within the Credits section, which contains clearly laid-out and high-lighted links.

17. As the site owner, I want to provide players a fun and beneficial game that can be enjoyed by players of all ages.
    - Due to the different difficulties available, especially easy, and the fun and flashy design direction of the application, it's something even younger kids can pick up and learn to enjoy. The concepts don't take much learning and the confetti upon winning will be all the encouragement they'll need.

[Back to top &uarr;](#avarice)
<hr>

## Bugs

1.  **Intended Outcome:** Background images covers the entire available viewport.
    * **Issue:** Background image only covers a certain amount of the vertical viewport, before being cropped and displaying white space.
    * **Cause:** The background image had a square ratio and was quite small in terms of size.
    * **Solution:** Replace the old image with a new image that's a higher resolution and a wider ratio. [Commit](https://github.com/Ryael/memoria/commit/36d73075c269e5c6e902a1075212808940ee9e61).

2.  **Intended Outcome:** H1 title is created such that there is an even amount of space above and below it.
    * **Issue:** [H1 title is unevenly spaced](docs/bugs/bug-2.png).
    * **Cause:** H1 title is created such that there is excess space below the it.
    * **Solution:** Replace the old font with a new font, Jost, that has an even amount of space above and below it. [Commit](https://github.com/Ryael/memoria/commit/7f15638933dd2b3692a467dd0eb7296c9fa39fad).

3.  **Intended Outcome:** After using Return/Back button, all the previously displayed containers should be hidden.
    * **Issue:** After using Return/Back button, all the previously displayed containers were still being displayed.
    * **Cause:** After using Return/Back button, all the previously displayed containers didn't have their display changed to "display: none".
    * **Solution:** Hide the containers when the Return/Back is clicked. This was then later changed to be a reload script, which accomplishes the same thing. [Commit](https://github.com/Ryael/memoria/commit/6340e47c37d8cdf294e879975b10f71dc296abfb).

4.  **Intended Outcome:** All emoji should be rendered once the game board is generated.
    * **Issue:** Some emoji weren't being being rendered.
    * **Cause:** The emoji that weren't being rendered simply weren't compatible with being displayed as icons.
    * **Solution:** Replace the emoji that weren't being properly rendered with ones that are. [Commit](https://github.com/Ryael/memoria/commit/309ec88eb40360d0ef139a6481b6cc65214dd82e).

5.  **Intended Outcome:** The win state is only displayed after a round is over.
    * **Issue:** A part of the win state is being displayed and no text is visible after the board flips.
    * **Cause:** The memory game had a white colour covering it, which is what made the text disappear. Additionally, "win" had a class selector instead of a id selector.
    * **Solution:** Remove the white background and update "win" from a class selector to a id selector. [Commit](https://github.com/Ryael/memoria/commit/a3dd7769ce25eeaac6482b322984772099935f10).

6.  **Intended Outcome:** Game controls is displayed above the game area.
    * **Issue:** Game controls is not visible at all.
    * **Cause:** The game controls section was being placed beside the game area. It also wasn't being hidden upon the user navigating away from the game.
    * **Solution:** Moving the container up a level/div and adding a script to the easyGameMode script that allows the game stats to be displayed from a none-display state. Fix the typo in the constant selectors (no # for idSelector) [Commit](https://github.com/Ryael/memoria/commit/b8693edf9777f0abc5d7eeda75e6975fc3ab1829).

7.  **Intended Outcome:** Upon interacting with the Back/Return buttons, elements on the page fade in normally.
    * **Issue:** Interacting with the Back/Return button would display the Main Menu briefly before the reload and the transitional effects that follow.
    * **Cause:** The page reload would play the transitional effects once and then the show/hide scripts would play the effects again.
    * **Solution:** Remove hide/show scripts in favour of location.reload script. [Commit](https://github.com/Ryael/memoria/commit/6340e47c37d8cdf294e879975b10f71dc296abfb).

8.  **Intended Outcome:** Interacting with the H1 title allows the user to return to the Main Menu.
    * **Issue:** Interacting with the entire section that houses the H1 title causes the user to return to the Main Menu.
    * **Cause:** The function returnButton() was attached to the div that houses the H1 title.
    * **Solution:** Move returnButton() to the H1 instead. [Commit](https://github.com/Ryael/memoria/commit/faab9a6d22a7dbc62ea460199e791247234c1c07).

9. **Intended Outcome:** Memory game works as intended with the "matched" and "shakes" class being added to matching cards when two matched cards are flipped.
    * **Issue:** Too many rapid inputs break the game.
    * **Cause:** The event listener breaks and stops adding the "flipped" and "matched" classes making it impossible to progress the game.
    * **Solution:** Add timeOutRef which adds a delay to shake and flip. [Commit](https://github.com/Ryael/memoria/commit/76eeaa0eb1cf5c14d4e58206d43badc00b12897f).

10. **Intended Outcome:** Border animation stops playing after the game board is flipped and the win state is displayed.
    * **Issue:** [Border animation continues playing on the flipped game board when the win state is displayed](docs/bugs/bug-11.png). This was only present on Google Chrome.
    * **Cause:** Google Chrome handles this animation differently from other browsers and the animation persists despite the element technically being out of view.
    * **Solution:** Add "display: none;" to the animated borders (spans) on flip. [Commit](https://github.com/Ryael/memoria/commit/fa7763928db3b5d77a2695a6389867115fde44fa).

11. **Intended Outcome:** All difficulty levels of the game should be responsive.
    * **Issue:** [After hard mode was made responsive, easy and normal modes broke](docs/bugs/bug-12.png).
    * **Cause:** Easy, normal, and hard all share one ID selector, which was changed via media query to make the game responsive on hard.
    * **Solution:** Adjust generateGame script with the inclusion of template literals to create 3 different boards (board-2, board-4, board-6) to better manipulate all with separate media queries. [Commit](https://github.com/Ryael/memoria/commit/9a7121533e56761c93745c4e5da2b222b11a912b).

12. **Intended Outcome:** Animated border around the game area should remain around the game area.
    * **Issue:** Animated border appears far off to the right side on the smallest media query.
    * **Cause:** The left and right part of animated border are displaced due to the smallest media query causing the hard game board to vertically fill up the screen.
    * **Solution:** Add "overflow: hidden;" to #board-container to hide it. [Commit](https://github.com/Ryael/memoria/commit/f8894fa2842cb0066b707c647ff59ed9d6bde6e1). 

13. **Intended Outcome:** Flip counter only counts the flips made on the game board.
    * **Issue:** Flip counter adds extra flips if the user rapidly interacted with the game board, even if a card was already mid-flip.
    * **Cause:** There was no if statement to ensure there are less than two total flips existing at any time.
    * **Solution:** Moving state.TotalFlips++ into the if statement where there has to be less than 2 total flips existing at any time. [Commit](https://github.com/Ryael/memoria/commit/553351075921cacf2eb57d01241111674ef56b47).  

[Back to top &uarr;](#avarice)
<hr>

## Future Updates

1. Leaderboards - Unfortunately this was part of the original scope, it proved to be too difficult to incorporate in time. The idea is top display the top ten users for every difficulty. After winning a round, a the win state would allow the user to input their name and assign it their clear time, which would then be ranked against other players who input their name.

2. Restart Button - This would allow users to restart a game without having to return to the Main Menu, effectively saving them a lot of extra clicks. 

3. UI Update - I'd like to update the UI, namely the settings menus such that they feel even more visually and thematically fitting.

4. Extra Difficulties - For people that would really like to push their memorisation to the max. Namely 8 x 8 card grids and 10 x 10 card grids.

5. More Emoji - Add more emoji that fit the criteria of traditional fantasy role playing game concepts. This would allow for an even wider pool of emoji to be pulled from, creating a much more varied pool.

I'd like to revisit this project in the future after having learned more about JavaScript in order to push this application to become as good as it can possibly be.

## Deployment

This project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the repository: [Memoria](https://github.com/Ryael/memoria).
2. Locate the Settings button, and then click it.
3. Scroll down to the Pages section, which is found under "Code and automation".
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will then automatically refresh.
6. Scroll back to the top of the page to locate the now published website link.

It can also be forked via the following steps:

1. Log in to GitHub and locate the repository again, as described above.
2. At the top right corner of the repository, you will see a "Fork" button. Click on it.
3. You will then be asked where you want to save it, so choose a location.
4. You now should have a copy of this repository in your own GitHub account.

[Back to top &uarr;](#avarice)
<hr>

## Technologies Used

### Languages

- HTML 5
- CSS 3
- JavaScript

### Frameworks & Tools

- [GitPod](https://gitpod.io) - IDE used to code and build this project.
- [GitHub](https://github.com/) - The repository was created here, is currently stored here, and was deployed via the GitHub Pages features.
- [Balsamiq](https://balsamiq.com) - Used to create wireframes.
- [Obsidian](https://obsidian.md/) - Used to take notes and create to-do lists.
- [Adope Photoshop](https://www.adobe.com/products/photoshop.html) - Used to crop, resize, and edit images.
- [Adope Illustrator](https://www.adobe.com/products/illustrator.html) - Used to manipulate background images from FreePik.
- [W3C HTML Validator](https://validator.w3.org/) - Used to validate HTML code.
- [W3C JigSaw Validator](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS code.
- [JSHint](https://jshint.com/) - Used to validate JS code.
- [WAVE WebAIM](https://wave.webaim.org/) - Used to check accessibility.
- [Google Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - Used to check performance, SEO, accessibility, and best practices.
- [Mozilla Firefox Developer Tools](https://www.mozilla.org/en-US/firefox/new/) - Used to check and test the project.
- [AmIResponsive](https://ui.dev/amiresponsive) - Used to create the Am I Responsive image mock-up.
- [FreeConvert](https://www.freeconvert.com/jpg-to-webp) - Used to convert .PNG to .WEBP.
- [TinyPNG](https://tinypng.com/) - Used to compress images.
- [Google Fonts](https://fonts.google.com/) - Fonts were imported from here.
- [Font Awesome](https://fontawesome.com/) - Icons are used from here.
- [Favicon.io](https://favicon.io/) - Used to create a favicon.
- [ShareX](https://getsharex.com/) - Used to take screenshots and gifs.
- [Color-Name](https://www.color-name.com/) - Used to find complementary shades of colours used.
- [Elementor](https://elementor.com/blog/font-pairing/) - Used to find Google Font combinations.
- [Canvas Confetti](https://www.kirilv.com/canvas-confetti/) - Library of confetti scripts, which were used.
- [FreePik](https://www.freepik.com/) - Used to find background images.
- [Badgen](https://badgen.net/) - Used to generate live badge icons.
- [Website Responsive Test Online](https://websiteresponsivetest.com/) - Used to test the responsiveness of the website.

## Credits

1. [WebTips - Memory Game Tutorial](https://www.webtips.dev/memory-game-in-javascript) - The code presented and explained here was what my project was based on. I heavily modified it and commented every single step of the way to demonstrate my understanding of the complete functionality and concepts employed throughout. It served as a frame of reference with regard to how certain aspects of the memory game worked and gaps with bridging this approach to my own vision were filled by my own solutions and ideas.
1. [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) - This project was first based off the repository created by Code Institute. This template made it very easy to work with in GitPod.
3. [Codepen - Swarup Kumar Kuila](https://codepen.io/uiswarup/pen/RBByzW) - This codepen is where the idea for the animated border came from and helped me understand the use of nth-child elements in creating a uniquely animated four part border such as this.
4. [Stack Overflow](https://stackoverflow.com/) & [W3Schools](https://www.w3schools.com/) - These two website were instrumental in me furthering my understanding of HTML 
5. [Code Institute](https://codeinstitute.net/ie/) - Last but certainly not least, this project wouldn't have been possible without the course and material presented there.

## Acknowledgements 

- [Akshat Garg](https://github.com/akshatnitd) - Akshat is an absolutely amazing mentor that's friendly, knowledgeable, and helpful. He's been super helpful in providing me with suggestions and advice.
- [Simon Waldron](https://github.com/saikez) - One of my closest friends and the very person who introduced me to the world of programming! He has been supporting me throughout my reskilling journey and is an absolute wonder of a human being. He has taken time out of his day again to help break down the more complicated JavaScript concepts and I honestly wouldn't have been able to complete this project to a satisfactory level without him.
- My family and friends, who have been incredibly supportive and have been instrumental in keeping me motivated throughout this project. Thank you all so much! All of you who helped proofread, test, provide feedback on the UI, code, and etc... I couldn't have done it without you all!
- The Code Institute community on Slack - Easy, straightforward, and always willing to help and provide advice.
- Love Running - Ultimately, it wasn't until we went through this project that I realised that this was something I could do. A lot of the website is loosely based on it, too.

[Back to top &uarr;](#avarice)
<hr>
