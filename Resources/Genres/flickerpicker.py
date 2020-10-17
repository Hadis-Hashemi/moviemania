

import pandas as pd
data_Action = pd.read_csv("Resources/Genres/Action.csv")
data_Action = data_Action[data_Action['description'].notna()]

data_Adventure = pd.read_csv("Resources/Genres/Adventure.csv")
data_Adventure = data_Adventure[data_Adventure['description'].notna()]

data_Biography = pd.read_csv("Resources/Genres/Biography.csv")
data_Biography = data_Biography[data_Biography['description'].notna()]

data_Comedy = pd.read_csv("Resources/Genres/Comedy.csv")
data_Comedy = data_Comedy[data_Comedy['description'].notna()]

data_Crime= pd.read_csv("Resources/Genres/Crime.csv")
data_Crime = data_Crime[data_Crime['description'].notna()]

data_Drama = pd.read_csv("Resources/Genres/Drama.csv")
data_Drama = data_Drama[data_Drama['description'].notna()]

data_Family = pd.read_csv("Resources/Genres/Family.csv")
data_Family = data_Family[data_Family['description'].notna()]

data_Fantasy = pd.read_csv("Resources/Genres/Fantasy.csv")
data_Fantasy = data_Fantasy[data_Fantasy['description'].notna()]

data_Film_Noir = pd.read_csv("Resources/Genres/Film-Noir.csv")
data_Film_Noir = data_Film_Noir[data_Film_Noir['description'].notna()]

data_Horror = pd.read_csv("Resources/Genres/Horror.csv")
data_Horror = data_Horror[data_Horror['description'].notna()]

data_Musical = pd.read_csv("Resources/Genres/Musical.csv")
data_Musical = data_Musical[data_Musical['description'].notna()]

data_Mystery = pd.read_csv("Resources/Genres/Mystery.csv")
data_Mystery = data_Mystery[data_Mystery['description'].notna()]

data_Romance = pd.read_csv("Resources/Genres/Romance.csv")
data_Romance = data_Romance[data_Romance['description'].notna()]

data_Sci_Fi = pd.read_csv("Resources/Genres/Sci-Fi.csv")
data_Sci_Fi = data_Sci_Fi[data_Sci_Fi['description'].notna()]

data_Sport = pd.read_csv("Resources/Genres/Sport.csv")
data_Sport = data_Sport[data_Sport['description'].notna()]

data_Thriller = pd.read_csv("Resources/Genres/Thriller.csv")
data_Thriller = data_Thriller[data_Thriller['description'].notna()]

data_War= pd.read_csv("Resources/Genres/War.csv")
data_War = data_War[data_War['description'].notna()]

data_Western= pd.read_csv("Resources/Genres/Western.csv")
data_Western = data_Western[data_Western['description'].notna()]

from sklearn.feature_extraction.text import CountVectorizer

count_vect_Action = CountVectorizer()
Action_train_counts = count_vect_Action.fit_transform(data_Action['description'])

count_vect_Adventure = CountVectorizer()
Adventure_train_counts = count_vect_Adventure.fit_transform(data_Adventure['description'])

count_vect_Biography = CountVectorizer()
Biography_train_counts = count_vect_Biography.fit_transform(data_Biography['description'])

count_vect_Comedy = CountVectorizer()
Comedy_train_counts = count_vect_Comedy.fit_transform(data_Comedy['description'])

count_vect_Crime = CountVectorizer()
Crime_train_counts = count_vect_Crime.fit_transform(data_Crime['description'])

count_vect_Drama = CountVectorizer()
Drama_train_counts = count_vect_Drama.fit_transform(data_Drama['description'])

count_vect_Family = CountVectorizer()
Family_train_counts = count_vect_Family.fit_transform(data_Family['description'])

count_vect_Fantasy = CountVectorizer()
Fantasy_train_counts = count_vect_Fantasy.fit_transform(data_Fantasy['description'])

count_vect_Film_Noir = CountVectorizer()
Film_Noir_train_counts = count_vect_Film_Noir.fit_transform(data_Film_Noir['description'])

count_vect_Horror = CountVectorizer()
Horror_train_counts = count_vect_Horror.fit_transform(data_Horror['description'])

count_vect_Musical = CountVectorizer()
Musical_train_counts = count_vect_Musical.fit_transform(data_Musical['description'])

count_vect_Mystery = CountVectorizer()
Mystery_train_counts = count_vect_Mystery.fit_transform(data_Mystery['description'])

count_vect_Romance = CountVectorizer()
Romance_train_counts = count_vect_Romance.fit_transform(data_Romance['description'])

count_vect_Sci_Fi = CountVectorizer()
Sci_Fi_train_counts = count_vect_Sci_Fi.fit_transform(data_Sci_Fi['description'])

count_vect_Sport = CountVectorizer()
Sport_train_counts = count_vect_Sport.fit_transform(data_Sport['description'])

count_vect_Thriller = CountVectorizer()
Thriller_train_counts = count_vect_Thriller.fit_transform(data_Thriller['description'])

count_vect_War = CountVectorizer()
War_train_counts = count_vect_War.fit_transform(data_War['description'])

count_vect_Western = CountVectorizer()
Western_train_counts = count_vect_Western.fit_transform(data_Western['description'])

from sklearn.feature_extraction.text import TfidfTransformer

Action_tfidf_transformer = TfidfTransformer()
Action_train_tfidf = Action_tfidf_transformer.fit_transform(Action_train_counts)

Adventure_tfidf_transformer = TfidfTransformer()
Adventure_train_tfidf = Adventure_tfidf_transformer.fit_transform(Adventure_train_counts)

Biography_tfidf_transformer = TfidfTransformer()
Biography_train_tfidf = Biography_tfidf_transformer.fit_transform(Biography_train_counts)

Comedy_tfidf_transformer = TfidfTransformer()
Comedy_train_tfidf = Comedy_tfidf_transformer.fit_transform(Comedy_train_counts)

Crime_tfidf_transformer = TfidfTransformer()
Crime_train_tfidf = Crime_tfidf_transformer.fit_transform(Crime_train_counts)

Drama_tfidf_transformer = TfidfTransformer()
Drama_train_tfidf = Drama_tfidf_transformer.fit_transform(Drama_train_counts)

Family_tfidf_transformer = TfidfTransformer()
Family_train_tfidf = Family_tfidf_transformer.fit_transform(Family_train_counts)

Fantasy_tfidf_transformer = TfidfTransformer()
Fantasy_train_tfidf = Fantasy_tfidf_transformer.fit_transform(Fantasy_train_counts)

Film_Noir_tfidf_transformer = TfidfTransformer()
Film_Noir_train_tfidf = Film_Noir_tfidf_transformer.fit_transform(Film_Noir_train_counts)

Horror_tfidf_transformer = TfidfTransformer()
Horror_train_tfidf = Horror_tfidf_transformer.fit_transform(Horror_train_counts)

Musical_tfidf_transformer = TfidfTransformer()
Musical_train_tfidf = Musical_tfidf_transformer.fit_transform(Musical_train_counts)

Mystery_tfidf_transformer = TfidfTransformer()
Mystery_train_tfidf = Mystery_tfidf_transformer.fit_transform(Mystery_train_counts)

Romance_tfidf_transformer = TfidfTransformer()
Romance_train_tfidf = Romance_tfidf_transformer.fit_transform(Romance_train_counts)

Sci_Fi_tfidf_transformer = TfidfTransformer()
Sci_Fi_train_tfidf = Sci_Fi_tfidf_transformer.fit_transform(Sci_Fi_train_counts)

Sport_tfidf_transformer = TfidfTransformer()
Sport_train_tfidf = Sport_tfidf_transformer.fit_transform(Sport_train_counts)

Thriller_tfidf_transformer = TfidfTransformer()
Thriller_train_tfidf = Thriller_tfidf_transformer.fit_transform(Thriller_train_counts)

War_tfidf_transformer = TfidfTransformer()
War_train_tfidf = War_tfidf_transformer.fit_transform(War_train_counts)

Western_tfidf_transformer = TfidfTransformer()
Western_train_tfidf = Western_tfidf_transformer.fit_transform(Western_train_counts)

from sklearn.naive_bayes import MultinomialNB

ActionTest = MultinomialNB().fit(Action_train_tfidf, data_Action['class'])

AdventureTest = MultinomialNB().fit(Adventure_train_tfidf, data_Adventure['class'])

BiographyTest = MultinomialNB().fit(Biography_train_tfidf, data_Biography['class'])

ComedyTest = MultinomialNB().fit(Comedy_train_tfidf, data_Comedy['class'])

CrimeTest = MultinomialNB().fit(Crime_train_tfidf, data_Crime['class'])

dramaTest = MultinomialNB().fit(Drama_train_tfidf, data_Drama['class'])

FamilyTest = MultinomialNB().fit(Family_train_tfidf, data_Family['class'])

FantasyTest = MultinomialNB().fit(Fantasy_train_tfidf, data_Fantasy['class'])

Film_NoirTest = MultinomialNB().fit(Film_Noir_train_tfidf, data_Film_Noir['class'])

HorrorTest = MultinomialNB().fit(Horror_train_tfidf, data_Horror['class'])

MusicalTest = MultinomialNB().fit(Musical_train_tfidf, data_Musical['class'])

MysteryTest = MultinomialNB().fit(Mystery_train_tfidf, data_Mystery['class'])

RomanceTest = MultinomialNB().fit(Romance_train_tfidf, data_Romance['class'])

Sci_FiTest = MultinomialNB().fit(Sci_Fi_train_tfidf, data_Sci_Fi['class'])

SportTest = MultinomialNB().fit(Sport_train_tfidf, data_Sport['class'])

ThrillerTest = MultinomialNB().fit(Thriller_train_tfidf, data_Thriller['class'])

WarTest = MultinomialNB().fit(War_train_tfidf, data_War['class'])

WesternTest = MultinomialNB().fit(Western_train_tfidf, data_Western['class'])

    ## 'user input html text box, to test change to "<description>"'
    
def flickerpicker(user_input):
    description = [user_input]

    #descrip_counts
    Action_descrip_counts = count_vect_Action.transform(description)
    Adventure_descrip_counts = count_vect_Adventure.transform(description)
    Biography_descrip_counts = count_vect_Biography.transform(description)
    Comedy_descrip_counts = count_vect_Comedy.transform(description)
    Crime_descrip_counts = count_vect_Crime.transform(description)
    Drama_descrip_counts = count_vect_Drama.transform(description)
    Family_descrip_counts = count_vect_Family.transform(description)
    Fantasy_descrip_counts = count_vect_Fantasy.transform(description)
    Film_Noir_descrip_counts = count_vect_Film_Noir.transform(description)
    Horror_descrip_counts = count_vect_Horror.transform(description)
    Musical_descrip_counts = count_vect_Musical.transform(description)
    Mystery_descrip_counts = count_vect_Mystery.transform(description)
    Romance_descrip_counts = count_vect_Romance.transform(description)
    Sci_Fi_descrip_counts = count_vect_Sci_Fi.transform(description)
    Sport_descrip_counts = count_vect_Sport.transform(description)
    Thriller_descrip_counts = count_vect_Thriller.transform(description)
    War_descrip_counts = count_vect_War.transform(description)
    Western_descrip_counts = count_vect_Western.transform(description)


    #descrip_tfidf
    Action_descrip_tfidf = Action_tfidf_transformer.transform(Action_descrip_counts)
    Adventure_descrip_tfidf = Adventure_tfidf_transformer.transform(Adventure_descrip_counts)
    Biography_descrip_tfidf = Biography_tfidf_transformer.transform(Biography_descrip_counts)
    Comedy_descrip_tfidf = Comedy_tfidf_transformer.transform(Comedy_descrip_counts)
    Crime_descrip_tfidf = Crime_tfidf_transformer.transform(Crime_descrip_counts)
    Drama_descrip_tfidf = Drama_tfidf_transformer.transform(Drama_descrip_counts)
    Family_descrip_tfidf = Family_tfidf_transformer.transform(Family_descrip_counts)
    Fantasy_descrip_tfidf = Fantasy_tfidf_transformer.transform(Fantasy_descrip_counts)
    Film_Noir_descrip_tfidf = Film_Noir_tfidf_transformer.transform(Film_Noir_descrip_counts)
    Horror_descrip_tfidf = Horror_tfidf_transformer.transform(Horror_descrip_counts)
    Musical_descrip_tfidf = Musical_tfidf_transformer.transform(Musical_descrip_counts)
    Mystery_descrip_tfidf = Mystery_tfidf_transformer.transform(Mystery_descrip_counts)
    Romance_descrip_tfidf = Romance_tfidf_transformer.transform(Romance_descrip_counts)
    Sci_Fi_descrip_tfidf = Sci_Fi_tfidf_transformer.transform(Sci_Fi_descrip_counts)
    Sport_descrip_tfidf = Sport_tfidf_transformer.transform(Sport_descrip_counts)
    Thriller_descrip_tfidf = Thriller_tfidf_transformer.transform(Thriller_descrip_counts)
    War_descrip_tfidf = War_tfidf_transformer.transform(War_descrip_counts)
    Western_descrip_tfidf = Western_tfidf_transformer.transform(Western_descrip_counts)


    #predicted
    predicted_Action = ActionTest.predict(Action_descrip_tfidf)
    predicted_Adventure = AdventureTest.predict(Adventure_descrip_tfidf)
    predicted_Biography = BiographyTest.predict(Biography_descrip_tfidf)
    predicted_Comedy = ComedyTest.predict(Comedy_descrip_tfidf)
    predicted_Crime = CrimeTest.predict(Crime_descrip_tfidf)
    predicted_Drama = dramaTest.predict(Drama_descrip_tfidf)
    predicted_Family = FamilyTest.predict(Family_descrip_tfidf)
    predicted_Fantasy = FantasyTest.predict(Fantasy_descrip_tfidf)
    predicted_Film_Noir = Film_NoirTest.predict(Film_Noir_descrip_tfidf)
    predicted_Horror = HorrorTest.predict(Horror_descrip_tfidf)
    predicted_Musical = MusicalTest.predict(Musical_descrip_tfidf)
    predicted_Mystery = MysteryTest.predict(Mystery_descrip_tfidf)
    predicted_Romance = RomanceTest.predict(Romance_descrip_tfidf)
    predicted_Sci_Fi = Sci_FiTest.predict(Sci_Fi_descrip_tfidf)
    predicted_Sport = SportTest.predict(Sport_descrip_tfidf)
    predicted_Thriller = ThrillerTest.predict(Thriller_descrip_tfidf)
    predicted_War = WarTest.predict(War_descrip_tfidf)
    predicted_Western = WesternTest.predict(Western_descrip_tfidf)



    movie_type = []

    if predicted_Action[0]==True:
        movie_type.append('Action')

    if predicted_Adventure[0]==True:
        movie_type.append('Adventure')

    if predicted_Biography[0]==True:
        movie_type.append('Biography')

    if predicted_Comedy[0]==True:
        movie_type.append('Comedy')

    if predicted_Crime[0]==True:
        movie_type.append('Crime')

    if predicted_Drama[0]==True:
        movie_type.append('Drama')

    if predicted_Family[0]==True:
        movie_type.append('Family')

    if predicted_Fantasy[0]==True:
        movie_type.append('Fantasy')    

    if predicted_Film_Noir[0]==True:
        movie_type.append('Film Noir')

    if predicted_Horror[0]==True:
        movie_type.append('Horror')    

    if predicted_Musical[0]==True:
        movie_type.append('Musical')   

    if predicted_Mystery[0]==True:
        movie_type.append('Mystery')    

    if predicted_Romance[0]==True:
        movie_type.append('Romance')

    if predicted_Sci_Fi[0]==True:
        movie_type.append('Sci Fi')

    if predicted_Sport[0]==True:
        movie_type.append('Sport')

    if predicted_Thriller[0]==True:
        movie_type.append('Thriller')

    if predicted_War[0]==True:
        movie_type.append('War')

    if predicted_Western[0]==True:
        movie_type.append('Western')   



    query = "SELECT title FROM Movie_imdb2 WHERE"
    if not movie_type:
        return "no movies"
    for genre in movie_type:
        query = query+" genre like '%%"+genre+"%%' AND " 


    query = query[:-4]+ "ORDER BY avg_vote DESC LIMIT 5"


    ## connection engine 
    import sqlalchemy
    from sqlalchemy import create_engine



    engine = create_engine(f'postgresql://postgres:clickflick@moviemania.cuwkcwki24z2.us-east-2.rds.amazonaws.com:5432')
    connection = engine.connect()
    results = connection.execute(str(query))

    return results

print(flickerpicker("An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles. NYPD cop John McClane goes on a Christmas vacation to visit his wife Holly in Los Angeles where she works for the Nakatomi Corporation."))