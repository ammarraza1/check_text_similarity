from flask import Flask, request, render_template
import re
import pickle
import numpy as np

app = Flask("__name__")

@app.route("/")
def loadPage():
	return render_template('index.html')

@app.route("/", methods=['POST'])
def checkSimilarity():
	###############################################################################################
	################################Read predefined stopwords file#################################
	###############################################################################################
    with open('stopwords.pkl', 'rb') as f:
        stopwords = pickle.load(f)

	###############################################################################################
	###################################Process first input text####################################
	###############################################################################################
    sample_1 = request.form['text_box_1']
    sample_1_cleaned = re.sub(r'[^\w\s]','',sample_1).split(' ')
    sample_1_cleaned_normalized = [i.upper() for i in sample_1_cleaned if i not in stopwords and len(i)>1]
    
    if len(sample_1_cleaned_normalized)<1:
        return render_template('index.html', text_box_1=sample_1, output='Please enter at least one word in first textbox')

    bag_of_words_1={}
    for word in sample_1_cleaned_normalized:
        if word in bag_of_words_1.keys():
            bag_of_words_1[word]+=1
        else:
            bag_of_words_1.update({word:1})

	###############################################################################################
	###################################Process second input text###################################
	###############################################################################################
    sample_2 = request.form['text_box_2']
    sample_2_cleaned = re.sub(r'[^\w\s]','',sample_2).split(' ')
    sample_2_cleaned_normalized = [i.upper() for i in sample_2_cleaned if i not in stopwords and len(i)>1]

    if len(sample_2_cleaned_normalized)<1:
        return render_template('index.html', text_box_1=sample_1, text_box_2=sample_2, output='Please enter at least one word in second textbox')
    
    bag_of_words_2={}
    for word in sample_2_cleaned_normalized:
        if word in bag_of_words_2.keys():
            bag_of_words_2[word]+=1
        else:
            bag_of_words_2.update({word:1})
    
	###############################################################################################
	######################################Calculate match Score####################################
	###############################################################################################
    matchScore = np.sum([1 for wrd in bag_of_words_1 if wrd in bag_of_words_2.keys()])/len(bag_of_words_1)
    output = f"Similarity score between first text and second text is {matchScore:.2f} in the range between 0 and 1"
    
    return render_template('index.html', text_box_1=sample_1, text_box_2=sample_2, output=output)


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000)
