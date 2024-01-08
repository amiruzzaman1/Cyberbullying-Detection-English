import streamlit as st
import pickle

# Load the trained model
model_filename = 'trained_model.sav'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TF-IDF vectorizer
vectorizer_filename = 'tfidf_vectorizer.sav'
with open(vectorizer_filename, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a function to predict cyberbullying and filter bad words
def predict_cyberbullying_and_filter_bad_words(text):
    text = text.lower()
    # Vectorize the input text using the loaded vectorizer
    text_tfidf = vectorizer.transform([text])
    
    # Use the trained model to make a prediction
    prediction = model.predict(text_tfidf)
    
    # Initialize variables to store the filtered text and bad words
    filtered_text = text
    bad_words = []
    
    # List of cyberbullying words
    cyberbullying_words = ["bitch", "fuck", "asshole", "shitty", "ass", "slut", "cunt", "motherfucker", "wanker", "dick", "shit", "bastard",
                       "pissed off", "arse", "bugger", "bloody", "whore", "anal", "anus", "arse", "arrse", "assbag", "assbandit", 
                       "assbanger", "assbite", "assclown", "asscock", "asscracker", "asses", "assface", "assfuck", "assfucker",
                       "assfukka", "assgoblin", "asshat", "asshead", "asshole", "assholes", "asshopper", "assjacker", "asslick", 
                       "asslicker", "assmonkey", "assmunch", "assmuncher", "assnigger", "asspirate", "assshit", "assshole", "asssucker", 
                       "asswad", "asswhole", "asswipe", "auto erotic", "autoerotic", "asswound", "boobs", "bitch", "b1tch", "ballbag", 
                       "balls", "ballsack", "bampot", "bangbros", "bareback", "barely legal", "barenaked", "bastard", "bastardo", "bastinado", 
                       "bbw", "bdsm", "bitches", "bitchin", "bitching", "bitchtits", "bitchy", "blowjob", "boob", "boobs", "booobs", "boooobs",
                       "booooobs", "booooooobs", "brotherfucker", "bumblefuck", "bung hole", "buttcheeks", "buttfucka", 
                       "buttfucker", "butthole", "buttmuch", "buttplug", "cock", "cocksucker", "camgirl", "camslut", 
                       "camwhore", "circlejerk", "clit", "cleveland steamer", "clit", "clitface", "clitfuck", "clitoris", 
                       "clits", "clover clamps", "clusterfuck", "cockass", "cockbite", "cockburger", "cockeye", "cockface",
                       "cockfucker", "cockhead", "cockjockey", "cockknoker", "cocklump", "cockmaster", "cockmongler",
                       "cockmongruel", "cockmonkey", "cockmunch", "cockmuncher", "cocknose", "cocknugget", "cocks",
                       "cockshit", "cocksmith", "cocksmoke", "cocksmoker", "cocksniffer", "cocksuck", "cocksucked", 
                       "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cockwaffle", "cok", "cokmuncher",
                       "coons", "cooter", "coprolagnia", "coprophilia", "cornhole", "creampie", "crotte", "cum", "cumbubble",
                       "cumdumpster", "cumguzzler", "cumjockey", "cummer", "cumming", "cums", "cumshot", "cumslut", "cumtart",
                       "cunilingus", "cunillingus", "cunnie", "cunnilingus", "cunt", "cuntass", "cuntface", "cunthole", 
                       "cuntlick", "cuntlicker", "cuntlicking", "cuntrag", "cunts", "cuntslut", "cyalis", "cyberfuc",
                       "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "darkie", 
                       "date rape", "daterape", "deep throat", "deepthroat", "deggo", "dendrophilia", "dick", "dickbag", 
                       "dickbeaters", "dickface", "dickfuck", "dickfucker", "dickhead", "dickhole", "dickjuice", "dickmilk ", 
                       "dickmonger", "dicks", "dickslap", "dicksucker", "dicksucking", "dicktickler", "dickwad", 
                       "dickweasel", "dickweed", "dickwod", "dike", "dildo", "dildos", "doggystyle ","donkeyribber", 
                       "doochbag", "double dong", "penetration", "doublelift", "douche", "douchebag", "dumbass",
                       "dumbcunt", "dumbfuck", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings",
                       "ejaculation", "ejakulate", "erotism", "eunuch", "f u c k", "fagfucker", "fagging", "faggit",
                       "faggitt", "faggot", "faggotcock", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fuck", 
                       "fucker", "fucking", "fecal", "feck", "fecker", "felch", "felching", "fellate", "fellatio", "feltch",
                       "female squirting", "femdom", "figging", "fingerbang", "fingerfuck", "fingerfucked", "fingerfucker",
                       "fingerfuckers", "fingerfucking", "fingerfucks", "fingering", "fistfuck", "fistfucked", "fistfucker", 
                       "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "fisting", 
                       "footjob", "frotting", "fuckass", "fuckbag", "fuckboy", "fuckbrain", "fuckbutt",
                       "fuckersucker", "fuckface", "fuckhead", "fuckheads", "fuckhole", "fuckin", "fucking",
                       "fuckings", "fucking shit motherfucker", "fuckme", "fucknut", "fucknutt", "fuckoff", "fucks",
                       "fuckstick", "fucktard", "fucktards", "fucktart", "fucktwat", "fuckup", "fuckwad", "fuckwhit", 
                       "fuckwit", "fuckwitt", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", 
                       "fukwhit", "fukwit", "futanari", "fux", "fuxor", "g-spot", "gangbang", "gangbanged", "gangbangs",
                       "gayass", "gaybob", "gaydo", "gayfuck", "gayfuckist", "goregasm", "handjob", "hard core", "hardcore",
                       "hardcoresex", "hooker", "arse", "ass fuck", "ass hole", "assfucker", "asshole", "assshole", "bastard",
                       "fucking bitch", "cock", "bloody hell", "boong", "cockfucker", "cocksuck", "coon", "cyberfuck",
                       "erection", "erotic", "faggot fuck", "fuck off", "fuck you", "fuckass", "fuckhole", "hardcore", 
                       "lesbian", "lesbians", "motherfuck", "negro", "nigger", "orgasim", "orgasm", "penis", "penisfucker", 
                       "piss", "piss off", "pussy", "sexy shit", "sexy slut", "son of a bitch", "suck tits", "xxx", 
                       "kill yourself", "fuck yourself", "beheading", "terrorist"]
    
    # Check for and filter out bad words from the text
    for word in cyberbullying_words:
        if word.lower() in text:
            filtered_text = filtered_text.replace(word, '*' * len(word))
            bad_words.append(word)
    
    # Map the prediction to a human-readable label
   
    return prediction[0], filtered_text, bad_words

# Create a Streamlit app
st.title("Cyberbullying Detection App (English)")

# Add a text input field
user_input = st.text_area("Enter text:", "")

# Predict when a button is clicked
if st.button("Predict"):
    if user_input:
        prediction, filtered_text, bad_words = predict_cyberbullying_and_filter_bad_words(user_input)
        if prediction != "not_cyberbullying":
            st.write("Prediction: Cyberbullying")
            st.write(f"Cyberbullying Type: {prediction}")
        else:
            st.write("Prediction: Not Cyberbullying")
        if bad_words:
            st.write(f"Bad Words: {', '.join(bad_words)}")
        else:
            st.write("<span style='color:cyan;'>No bad words found.</span>", unsafe_allow_html=True)
        if bad_words:
            st.write("Filtered Text:")
            st.write(f"<span style='color:red; font-weight:bold'>{filtered_text}</span>", unsafe_allow_html=True) 
        else:
            st.write("Original Text:")
            st.write(f"{filtered_text}", unsafe_allow_html=True)


st.header("Sample Texts")
st.write("It's always the filthy " + "<span style='color:red; font-weight:bold'>bitch</span> that creates problem between us", unsafe_allow_html=True)
st.write("Do you believe it is appropriate to refer to a Muslim as a " + "<span style='color:red; font-weight:bold'>terrorist</span>?", unsafe_allow_html=True)
st.write("I hope you're doing well and having a great day. Let's catch up soon! 😊")
st.write("The team's score is disgraceful.")

