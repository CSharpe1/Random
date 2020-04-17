# some project ideas to build up;

* Found on a youtube video "Kalle Hallden"
* Web scraper
* Build an Api
* Build a Snake game
* Create a basic web server
* Create a Chip-8 emulator


__
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
Concepts to keep in mind:

Random
Integer
Print
While Loops


A good project for beginners, this project will help establish a solid foundation for basic concepts. And if you already have programming experience, chances are that the concepts used in this project aren’t completely foreign to you. Print, for example, is similar to Javascript’s console.log.

2. Guess the Number
The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements


Jumping off the first project, this project continues to build up the base knowledge and introduces user-inputted data at its very simplest. With user input, we start to get into a little bit of variability.

3. Mad Libs Generator
The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. The program will first prompt the user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then, once all the information has been inputted, the program will take that data and place them into a premade story template. You’ll need prompts for user input, and to then print out the full story at the end with the input included.
Concepts to keep in mind:

Strings
Variables
Concatenation
Print


A pretty fun beginning project that gets you thinking about how to manipulate userinputted data. Compared to the prior projects, this project focuses far more on strings and concatenating. Have some fun coming up with some wacky stories for this!

4. TextBased Adventure Game
The Goal: Remember Adventure? Well, we’re going to build a more basic version of that. A complete text game, the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
Concepts to keep in mind:

Strings
Variables
Input/Output
If/Else Statements
Print
List
Integers


The tricky parts here will involve setting up the directions and keeping track of just how far the user has “walked” in the game. I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most. This project also continues to build on using userinputted data. It can be a relatively basic game, but if you want to build this into a vast, complex word, the coding will get substantially harder, especially if you want your user to start interacting with actual objects within the game. That complexity could be great, if you’d like to make this into a longterm project. *Hint hint.

5. Hangman
The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.
Concepts to keep in mind:

Random
Variables
Boolean
Input and Output
Integer
Char
String
Length
Print


1. Maze Generation Software




There are many different algorithms that you could implement when programming a maze generator (like a lot). So, if you want a list on the different algorithms you could possibly implement, check out this article.
2. Rubik’s Cube Solver




This is probably the hardest project idea on this entire list – in terms of the actual implementation. Creating AI that can actually learn how to solve the Rubik’s cube is very, very difficult.

The good news however, is that I don’t think examiners will expect you to create AI that learns how to solve the Rubik’s cube entirely by itself. Therefore, if you do choose this idea, I highly recommend that you program your AI around one of the many pre-existing algorithms that have been created to solve Rubik’s cubes.

In my opinion, this is the best algorithm for you to base your AI around.
3. Bird Migration Pattern Predictor




If you actually pull this one off, I would eat my foot if you didn’t get top marks (an A*).

For this project, you will need to analyze how birds have migrated across the globe in the past. Then you will need to try and find correlations between migration patterns and geographic weather conditions. From this data, your program could predict future migration patterns depending on different climate changes.

I think a great start for this idea is to read into what web-scraping is and how to do it.
4. Nuclear Power Plant Meltdown Simulation




While programming this project, you would have simulate real world conditions. After you have created this Earth-like environment, you can model the effects that a nuclear power plant meltdown would have on said environment.

You could even add cities to see the affects that radiation would have on them too.
5. Supermarket Stock Management System




Supermarket’s not only need to manage stock, but also staff – both of which, they have lots of. This means that there is most definitely an opportunity for you to make a complex system that could aide a supermarket.

If you do choose this, make sure you read up on how a supermarket actually operates, so the system is suitable. There’s a great document here that should tell you all you need to know about managing a supermarket (and a lot more).
6. Restaurant Point Of Sale (POS) System




A point of sale system is very different to a stock management system (as you would find in a supermarket). The difference is that a point of sale system is used (guess what) at the “point of sale”, meaning staff will use the system at restaurant tables when taking food orders.

Therefore, you must make sure your POS system has an extremely friendly user interface, as customers don’t like waiting around!
7. Chess Playing AI




I don’t think I need to tell you that this is going to be challenging… Therefore, if done right, this could lead to a well earned A* for your NEA.

There are so many resources to help you develop this particular project idea online. So, whenever you get stuck, you will never be far away from help.
8. Image Recognition AI




I reckon this is probably equally as difficult as the Rubik’s cube one – AKA very, very hard.

This idea should be screaming at you: “machine learning and neural networks”. If it’s not, there might be something wrong with you…

Neural Networks + Machine Learning = High Marks

There are loads of free online resources that will help you a ton. However, I highly recommend that you get this book off Amazon.co.uk, it is the best book on getting started with neural networks that I have ever read – just going to have to trust me on this one.
9. Evolution Simulator




This project has the potential to be seriously complicated, however, you could also make it quite simple. It all depends on what’s evolving.

If you are going to simulate how animated stick figures get better at running over many generations, your program is going to be very complex. However, if you are going to simulate how a single-muscled slug can get better traveling between points as quickly as possible then it could be quite simple.

If you’re even considering this project, then you should definitely check out this YouTube playlist (it’s strangely satisfying watching his imaginary creatures evolve).
10. Voice Recognition AI




This project is (obviously) very similar to the image recognition project that was aforementioned. Therefore, this project too, should be screaming “machine learning and neural networks” at you.

I’ve never really programmed a voice recognition AI before, therefore, I can’t really recommend any specific books for you to get (as I can’t be certain of their quality). However, I have done a quick google search and within 5 minutes I can tell that there is shed loads of information on this topic, so on that front – don’t worry.
11. Sales Order Processing System (SOP)




An SOP system should, as the name suggests, manage sales. This means it should control the majority of communications between the warehouse, sales team and the client.

Below are things that a typical SOP system could do:

    Store Order History
    Generate Invoices
    Generate Reports
    Generate Delivery Notes
    Send Reminder Emails

You are tied down a bit with this project, as you do have to make sure a factory could actually use this software. However, there are still many different avenue’s for you take with the types of functionality you decide to implement.
12. Poker Game




For you to do this project, you would have to be fairly confident with networking. This game would allow multiple devices to join a “table” and start playing poker with each other.

Depending on how complex you want your program to be, you could add so many extra features. I think a great extra feature for this project would be to calculate the odds of someone winning per hand. Furthermore, you could also add a computer poker player (where you could definitely implement some AI).
13. DJ Software (Can Mix Music)




This one is definitely a fun project for those of you who have an affection for music. This project would clearly require you to learn a shed load about manipulating audio files, however, if you can pull it off I think you could really make a project that is A* worthy.

You could also build a control system which could implement the software. This might cost a bit of money, but once again, it’s going to make you like you really know what you’re doing.
14. Interactive Circuit Builder




If you want to know what I’m on about, get the free trial of Logicly or just go on YouTube and look at a video of someone else using Logicly.

Assuming you have done that, you will know what I mean by an “interactive circuit builder”. I would say that the most important aspect of this project would have to be the UI. Without a good user interface, the software would not be fit for purpose and you would definitely lose marks.
15. Quiz App




You could either make an offline quiz app or you make a much more complex client-server quiz style app. There is definitely much more opportunity to get an A* with the latter of those options.

If you decide to do a client-server model, I think a real time quiz app would work great – something (even remotely) similar to Kahoot would really stand out.
16. Software for Calculating The Big O of an Algorithm




Examiners will absolutely love this one, but why?

Because in doing this project, you would be making a computer science theory topic actually come to life. Therefore, if you do this project, you are showing to the examiner that you can get a concept off paper and actually make use of it in a real situation.

Besides that, this project is amazingly complex and will certainly provide you with plenty of opportunity’s for you to incorporate A* level concepts into your program.

If you have forgotten what Big O is, don’t worry (you should worry a bit actually) and just go give this a read.
17. Tracking And Monitoring Global Shipping Routes




This project is going to require you to get comfortable with web-scraping and API’s. You will need to be able to gather information about the global whereabouts of cargo ships frequently.

Once you have mastered the back-end tracking, you will need to think of a nice way to present the data. Maybe you could use certain programming libraries to make route representations on a global map?
18. Implementation of Machine Learning To Maximize Profits At An Airport




This could be my favorite project idea on here.

The lengths that airport companies go to when designing the layout of a particular airport is crazy. Everything is where it is for a reason: the route you take to board a plane, where you wait to board and the even where the security is. If you want more information about how airports maximize profits, check this out.

If you choose this project, I think you should do a simulation where people are represented by a particular sprite, shape or whatever you choose, and then they you follow them through the airport. After each day you could track the profits that the airport made.

Now this is where machine learning comes in… you could implement an algorithm that changes the layout of the airport each day and see if profits increase or decrease. Then the program would learn accordingly.
19. 3D First Person Shooter Game




Although many people choose to program a 2D game for their NEA, I think that programming a 3D game is just… better. Programming in 3D makes it so much easier for you to implement A* level programming techniques.
20. Implementation of AI To Model The Effects of Global Warming




Global warming is becoming an ever increasing issue in today’s world – so this project certainly checks the box “assists with a real world problem”.

Anyway, designing a program (using AI) that can attempt to predict what the effects of climate change are going to be on the planet is a great idea. It’s complicated enough, time-consuming enough and definitely “real worldy” enough.

A great place to start with this project is to check out the currently predicted effects of climate change, which you can find here.
21. Encrypted Instant Messaging App




An instant messaging app is one thing, but an encrypted instant messaging app is a whole different thing. This project is great because it just ticks so many boxes. You will be covering encryption and client-server networking in the same project!

Before you start this project, make sure you take out the different types of encryption methods (you can find some here).
22. E-Commerce Web App




Almost every single large company out there now has an online e-commerce website. Therefore, there is going to be plenty of helpful resources out there for you to learn from.

This project will also require some encryption as you will be dealing with payment methods such as debit and credit cards, which are VERY much confidential information.
23. Fitness Monitoring App




Programming a fitness app will allow you to actually interact with the hardware that is on the phone. For example, you could have a fitness app that tracks footsteps, in which case you would need to directly communicate with the phones pedometer.
24. Virtual Flashcard App




This can be a great project, if done right.

You’re going to have to get very good at databases if you do this project as a virtual flashcard app would require crap loads of them. A great example of a virtual flashcard app is Quizlet (I’m sure you have head of it already).

A simple virtual flashcard app should allow a user to:

    Create Folders For Different Subjects
    Create Flashcards Sets For Particular Modules
    Revise Flashcard Sets Effectively.

25. Public Transport Timetable App




Now, I don’t mean just display a PDF image of a pre-existing bus timetable and say “finished!”…

This app should be able to perform web-scraping on live bus and train timetables and display the information is a user friendly way.

Your program could even take two postal codes and calculate the quickest way to get there using a mixture of public transport and walking. It could also return the current price for that specific journey. An example of how this can be implemented is on the Stagecoaches “Plan A Journey” page.
26. Social Networking Platform




You all know what a social networking platform is. I don’t think I need to explain this one to you…
27. Physics Projectile Modelling Tool




If you are a fan of mechanics, this is your project. One of the many reasons this project is so good is because when programming it, you are forced to simulate a real world environment – in the sense that you program in gravity, terrain, air resistance etc.

Furthermore, if you were so inclined, you could very easily transform this project into a game, where you try to hit particular objects using a projectile. Angry birds is a great example of what I mean.
28. Nuclear Power Plant Management System




There’s more to managing a nuclear power plant than you think. Therefore, a nuclear power plant management system can either be super simple or extremely complex depending on what you choose to implement into the system.

I highly recommend you check out this link, it tells you all about the parts of a nuclear power station and you will get a feel for what your system will be managing very quickly.
29. Weather Forecasting Software




There are many paths you could take with this particular project, so it’s really down to what you decide. However, the fundamental core of this project is that you need to at least make an attempt at predicting what the weather will be like tomorrow, the day after or perhaps even a week from now.

You could implement some kind of machine learning algorithm that could compare what your weather prediction was and what the weather actually turned out to be like. From here, the algorithm could adjust the factors that went into making the prediction accordingly.
30. Air Traffic Controller AI




Air traffic controllers are essential to ensure that planes aren’t going to collide when coming in or going out of an airport. However, humans tend to make mistakes – fairly regularly. Maybe an AI would always get it right?

For this project, you would have to create a model of an airport and simulate planes coming in and leaving. Your, AI would ensure that no planes crash… hopefully.
31. Interpreter For Chosen Programming Language




Interpreters convert high level language code into machine code that can be directly processed by the CPU. Furthermore, interpreters normally translate code per line, not all at once.

Although this programming project is challenging, you might struggle to incorporate some of the A* level programming concepts in your code. All I’m saying is that make sure you keep an eye on the marking criteria and don’t forget why you’re doing this project – to get the grades!
32. Internet Speed Tester




There’s more that goes into getting an accurate assessment of your internet bandwidth than you think. Therefore, making an internet speed test is definitely complex enough.

For this project, you will need to add feature to bulk it up. You could maybe try different methods of testing internet speed then compare how accurate each of them are.
33. Secure FTP Server




FTP stands for File Transfer Protocol. So this project would basically be making software that allows devices to easily transfer files between each other. I know I’ve said this a lot, but, once again, this project is going to be as complex as you make it.

If you choose this project, make sure you don’t just use an FTP library that does everything for you! Try and do as much as possible by yourself.
34. Software To Find The Best Online Deals




For this project, you’re going to need to “scrape” all of the current prices for a particular product off their respective websites. That’s the hard part. Next, you will have to present all of your various comparisons to the user in an easy-to-understand way (and give a conclusion containing where they can find the cheapest price).

A great example of this type of software is the website Trivago.
35. AI Chat Bot




This project would entail you creating a program that can talk to humans as if it was a human too. If there was such thing as a perfect AI chat bot, you shouldn’t be able to distinguish it from a human.

When programming this, you are going to need to be able to program in some sort of artificial intelligence that can learn from previous conversations it had with real people.

Two examples of chat bots that I have seen before are CleverBot and Eviee
36. Search Engine




Examples of search engines are: Google, Bing and Yahoo. There role is to receive a query from a user and index webpages in accordance with how relevant they are to the particular query. So if you googled “what is a pineapple?”, the idea is that a webpage containing information about pineapples would come up first before information about bananas.

There are many factors to consider when ranking webpages. Possible ranking factors for your SE could be:

    Keyword Frequency
    Title
    Image ALT Tags
    How Users Have Interacted With Page Previously.

37. AI Spam Filter



If you’ve ever been directly (or even indirectly) involved in front-end website development or survey development, you will know how big of a problem spam is. Spam messages can take many forms and with each passing year, it is getting more and more difficult to decypher what messages are genuine and which are spam.

This means that for your A-Level Computer Science NEA project, an idea could be to build a spam filter that could be run on an email server, implementing AI and Machine Learning. There is huge potential with this project idea and it is certainly not an easy one to develop!
38. Music Suggestion Tool



We’ve all used and heard of the famous YouTube recommendation service… Every time you go on YouTube, they have an algorithm running that recommends videos based on what they think you’ll like. Why not make your own version but just for music?

You could even tailor the recommendations to what mood the person is in by analysing music videos for particular themes e.g. sad, happy or exiting. If you did decide to go down this route with your NEA project, there is huge potential with this idea for machine learning implantation which would be designed around user feedback (user specifies whether or not the recommendation was good).

There is a great video on how the YouTube recommendation algorithm works here.
39. Graph Plotting Software



If you’re currently studying A-Level Maths or A-Level Further Maths, you will know the importance of graph plotting software is very high. So, there’s demand, why not provide the supply in the form of an NEA computer science project?

Your project could receive a polynomial expression as an input, and output (plot) a visual graphic of that graph… There are many examples of these types of software out there, one that you should check out is GeoGebra.
40. Foreign Language Teacher



This project idea could be made extremely basic, or extremely advanced. However, the fundamental building blocks of this project idea will always be the same; it will assist users in learning a foreign language. I don’t think I need to say too much about this idea, but I would recommend you checkout examples of this type of software such as Babbel or Duolingo.
41. Sat Nav



This NEA project could potentially consist of both web-scrapping and Dijkstra’s algorithm. That is a seriously nice combination!

What is not immediately obvious about this project idea is how much graphical work there is to it – there’s a lot. All I’m saying is that if you do decide to choose a project idea similar to this one, be sure that your graphical skills are very strong!


Python Projects (geeksforgeeks):

    Make Notepad using Tkinter
    Color game using Tkinter in Python
    Python | Message Encode-Decode using Tkinter
    XML parsing in Python
    Desktop Notifier in Python
    Hangman Game in Python
    Junk File Organizer in Python
    Browser Automation Using Selenium
    Tracking bird migration using Python-3
    Twitter Sentiment Analysis using Python
    Image Classifier using CNN
    Implementing Photomosaics
    Working with Images in Python
    OpenCV Python Program to blur an image
    Opencv Python program for Face Detection
    Cartooning an Image using OpenCV – Python
    OpenCV Python Program to analyze an image using Histogram
    OpenCV Python program for Vehicle detection in a Video frame
    DNA to Protein in Python 3
    Viruses – From Newbie to pro
    Handling Ajax request in Django
    Working with zip files in Python
    Morse Code Translator In Python
    Simple Chat Room using Python
    Creating a Proxy Webserver in Python | Set 1
    Creating a Proxy Webserver in Python | Set 2
    Project Idea | Audio to Sign Language Translator
    Understanding Code Reuse and Modularity in Python 3
    Multi-Messenger : A python project, messaging via Terminal
    Movie recommendation based on emotion in Python
    Implementing Web Scraping in Python with BeautifulSoup
    Computer Vision module application for finding a target in a live camera

