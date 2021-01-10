from google.cloud import language_v1

def sentiment_analysis(text_file):
    ## Instantiates a client
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT

    ## language 
    language = "en"
    document = {"content": text_file, "type_": type_, "language": language}

    #encoding type
    encoding_type = language_v1.EncodingType.UTF8

    ## Sends a request and response retrieved
    response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})


    sentiment_score = round(response.document_sentiment.score,2)
    sentiment_magnitude = round(response.document_sentiment.magnitude,2)

    print("Score: {}".format(sentiment_score))
    print("Magnitude: {}".format(sentiment_magnitude))

    sentences = response.sentences

    for sentence in sentences:
        print(round(sentence.sentiment.magnitude,2))
        print(round(sentence.sentiment.score, 2))
    
    return sentiment_score


def send(posts):
    temp_list = []
    for each_post in posts:
        ## calls the sentiment analysis on each post 
        score = sentiment_analysis(each_post['selftext'])
        each_post['wap_score'] =score
        ##setting threshold
        ##severe: <= -0.5
        if score <= -0.5:
            temp_list.append(each_post['submission_id'])
    
    return temp_list, posts
        

# sentiment_analysis("Sorry in advance for the negativity, but I’m so tired and lost and done with everything. I don’t know how to explain this, but it’s as if nothing is ever going to be good enough. I’m such a loser for feeling this way when I know so many people out there have it a lot worse. But I just can’t anymore. I was doing relatively well during the past few months, after a very long time. But it all went downhill very fast and I’ve hit rock bottom. And I can’t get back up.")

# sentiment_analysis("Sometimes I think about how meaningless and insignificant I am, a tiny somewhat functional human, in a sea of millions of other students, in an ocean of billions of people. I'm smaller than a droplet in the ocean. Then, I zoom out even more and see how tiny the earth, solar system are in the galaxy. Then, i see that the milky way galaxy is just a drop in the entity that is the universe. With this reality, why isnt everyone a nihilist? Why does anything matter at all? If I offed myself right now")

# sentiment_analysis("As proof of him being my favorite, take a look at what I made: https://i.imgur.com/S3voiW3.jpg What about you? Who are your favorite profs?")


# sentiment_analysis("Please be kind to yourself. This is a very strange and isolating time for everyone. In the bigger picture, school will just be a chapter in your life. Grades aren’t everything. You will be able to pull through this. You aren’t stupid and you aren’t a coward. I hope you know there are people who care. Your mental and physical health are the most important, so please focus on this as much as you can. If at any point you are feeling like you are at your wits end, please consider reaching out")

# sentiment_analysis("I want to kill myself")

# sentiment_analysis("Hi I'm in 1st year arts and im struggling with impostor syndrome")


# lists, thePosts = send([{
# 'submission_id': 123,
# 'wap_score': 10,
# 'title': "KMS",
# 'author': "linda",
# 'selftext': "I feel depressed, alone, hopeless, and suicidal. I honestly don’t know what to do", 
# 'created_utc': 124343545
# }])

# print (lists)
# print (thePosts)
