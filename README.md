### [ **Demo of our application**](https://devpost.com/software/euphoria-vd3178) 

### **Inspiration**
Mental health and depression are some of the most pressing concerns today, especially in teenagers. Consider these alarming facts: Every 100 minutes, a teen takes their own life. 20% of all teens experience depression before adulthood. Only 30% of depressed teens are being treated for it. (Source: Discover Mood & Anxiety)

Meanwhile, the number of mental health services & organizations has been growing rapidly for the past decade. How can we address that increasing gap between mental health services and getting them to those who actually need it?

Teenagers are expressing themselves more than ever before, with 45% of teens saying that they are online almost constantly. (Source: Pew Research Center)

Reddit is one of the most popular outlets for teenage expression today, where over 330 million users share content, comment on discussion forums, and interact with one another. It is a go-to place for many people seeking to find help anonymously. Some popular help-seeking forums include:

r/depression (700k members)
r/anxiety (400k members)
r/mental health (200k members)
r/suicide watch (250k members) Reddit is a support community for individuals, both as a first resort and as a last.
There is an opportunity here to drastically improve mental health services engagement by targeting social media platforms like Reddit to identify those we need professional help.

### **What it does**
Euphoria is an early risk detection tool for mental health organizations that uses ML to analyze the linguistic patterns and sentiments of online content to detect signs of depression or suicidal behaviour. It is a Reddit Bot that acts on behalf of a mental health organization's Reddit account (i.e. Canadian Mental Health Association's Reddit account).

Euphoria screens all new posts on target subreddits (i.e. r/anxiety) that can be pre-set and identifies individuals who may be at-risk from the severe effects of mental health and depression. It then crafts a direct message and automatically sends the at-risk individual with resources via the mental health organization’s Reddit account. If they need someone to talk to, a wellness representative who manages the organization’s Reddit can directly chat with them now live!

We designed a Euphoria web page for users (i.e. Canadian Mental Health Association) as the one go-to control center for the organization’s bot. Upon visiting this web page, users must login with the credentials of their organization before gaining access to all the configurations for their bot. Configuration options include:

Starting and stopping the bot from screening the latest posts
Choosing which subreddits for their bot to be active in
Customize the automated message that is sent to at-risk individuals

### **How We built it**
We utilized the Reddit API to obtain new posts returned as JSON objects from our desired Subreddit. Furthermore, we created endpoints using the Flask framework so a user could send and receive requests from another server independent from the frontend. We used HTML/CSS/Javascript alongside bootstrap templates to deliver a clean user interface for the user where requests were sent and received using Axios on the frontend.

The backend of the application is engineered with NLP, bot, and the server respectively, as we were intrigued by the endless possibilities offered by AI and MI. We were also surprised to find out how capable Google was of analyzing sentiments in texts, enabling us to aggregate more precise data for the auto-messaging feature. Even though we ran into challenges along the way due to the lack of exposure to cloud technologies, we were able to pick it up quickly and connected it with the bot.

To store the configuration data in the user portal, we decided to use Flask as our server, through which we were able to integrate the frontend with the backend and timely configure the bot to better aid individuals.

Finally, using the Reddit API once again, we can craft an automated direct message to the Reddit users that we believe are at-risk.

### **Challenges We ran into**
We were able to get individual components working together. Our challenge lied in connecting components together; frontend to backend, routing and navigation, and adding frontend data persistence to the UI. We ran into many obstacles getting the API calls to communicate between the frontend and backend. In particular, working with requesting the frontend user input and giving it to our backend Reddit bot. We discovered new issues we never knew were possible, but ultimately successfully integrated the two. It was also many of our first time working with the google natural language processor and creating a Reddit bot. That knowledge gap was a challenge at first. However, following the documentation we were able to quickly pick these things up and learned many new technologies during this hackathon.

### **Accomplishments that I'm proud of**
Our team is very proud of our work and hopes that it will be a small step in the right direction to address the gap between mental health organizations and at-risk teens. We hope to reach communities who may not get the support that they need and help to bring more awareness to mental health issues. In terms of skills we’re especially proud of the new technologies that we have been able to learn in such a short amount of time. We were able to create a Reddit bot which gives us base skills we can then use in the future and apply to different platforms such as Discord or Twitter. We tackled the difficult problem of connecting our frontend to our backend and were able to create a streamlined application. We went through many trials and errors, including long debugging sessions, but everything paid off the moment we were able to connect our frontend and backend and see our initial idea come to life.

### **What We learned**
The team’s growth during this project was phenomenal. In these 24 hours, we were able to create a working Reddit bot, interactive UI control console, and used API calls to connect the backend and frontend. Each team member gained invaluable skills working with the google natural language processor and we were able to see the power that it holds in the future. Our team was especially challenged and learned great lengths about APIs and the integration between backend and frontend. Our JavaScript knowledge was stretched as we learned the best ways of taking user input and connecting it with the python backend.

Additionally, our team discovered new ways to increase the effectiveness of online communication, especially with coding. We found new extensions that allowed us to pair-program together, learning and struggling together and we worked to fulfill our user stories. Overall, this hackathon was a tremendous learning experience for us and we gained numerous new skills to add to our toolkit.

### **What's next for Euphoria**
Euphoria has just started on its mission to address the gap between mental health organizations and the teens who need them. We’re excited to learn more about natural language processors and the potential they hold in the future. Furthermore, we’re always on the lookout for new ways to connect with the communities around us. Especially in expanding this model to various different social media platforms such as Twitter, Facebook, Instagram, and even Piazza. We hope to reach out to those individuals who may not get enough support and find the best ways to support them.
