import os
import numpy as np
from sklearn import svm 
from sklearn.metrics import accuracy_score
from collections import Counter

def make_Dictionary(root_dir):

    """[summary]
    
    Arguments:
        root_dir {string} -- directory of emails
    
    Returns:
        dic -- dictinary of most 3000 comon words and their count repetition
    """
   
    all_words = []
    emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for email in emails:
        with open(email) as m:
            for line in m:
                words = line.split()
                all_words += words

    dictionary = Counter(all_words)
    list_to_remove = list(dictionary)

    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]

    dictionary = dictionary.most_common(3000)

    return dictionary


def extract_feature(mail_dir):
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeroes((len(files),3000))
    train_labels = np.zeroes(len(files))
    count = 0
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i,line in enumerate(fi):
                if i ==2:
                    words = line.split()
                    for word in word:
                        wordID = 0
                        for i,d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID,wordID] = words.count(word)
            
            train_labels[docID] = 0
            filepathTokens = fil.split('/')
            lastToken = filepathTokens[len(filepathTokens) - 1]
            if lastToken.startswith("spmsg"):
                train_labels[docID] = 1
                count += 1
            docID += 1
    return features_matrix, train_labels


TRAIN_DIR = "../Data/train-mails"
TEST_DIR  = "../Data/test-mails"

