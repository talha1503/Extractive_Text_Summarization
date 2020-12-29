from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
import re


word_limit = 300


def get_content(topic):
	base_url = "https://en.wikipedia.org/wiki/"+topic
	page = requests.get(base_url)
	soup = BeautifulSoup(page.content , 'html.parser')
	paragraphs = soup.find_all('p')
	content = ""
	for para in paragraphs:
		content+=para.text
	return content


def clean(article):
	lem = WordNetLemmatizer()
	article =  re.sub(r'\[[^\]]*\]','',article)
	article = sent_tokenize(article)
	cleaned_list=[]
	for sent in article:
		sent  = sent.lower()
		word_list = []
		words = word_tokenize(sent)
		for word in words:
			word_list.append(lem.lemmatize(word.lower()))
		cleaned_list.append(' '.join(word_list))
	return cleaned_list

def get_frequency_dictionary(content):
	frequency = {}
	for sentence in content:
		word_list = word_tokenize(sentence)
		for word in word_list:
			if word not in set(stopwords.words('english')).union({',','.',';','%',')','(','``'}):
				if frequency.get(word) is None:
					frequency[word]=1
				else:
					frequency[word]+=1
	return frequency

def get_score(content,frequency_dictionary):
	sentence_score={}
	for sentence in content:
		score=0
		word_list = word_tokenize(sentence)
		start_idx,end_idx = -1,len(word_list)+1
		index_list=[]
		for word in word_list:
			if word not in set(stopwords.words('english')).union({',','.',';','%',')','(','``'}) and word in frequency_dictionary.keys():
				index_list.append(word_list.index(word))
		if index_list:
			score = len(index_list)**2/(max(index_list) - min(index_list))
		sentence_score[content.index(sentence)] = score
	return sentence_score


def get_summary(sentence_scores,content,threshold):
	summary = ""
	sentence_indexes = sorted(sentence_scores,key=sentence_scores.get,reverse=True)[:threshold-1]
	for index in sentence_indexes:
		summary+=content[index]+" " 
	return summary

def main():
	topic_name = input("Enter the topic name for wikipedia article")
	content = get_content(topic_name)
	cleaned_content = clean(content)
	threshold = len(cleaned_content)//40
	frequency_dictionary = get_frequency_dictionary(cleaned_content)
	sorted_dictionary = {key: frequency_dictionary[key] for key in sorted(frequency_dictionary,key=frequency_dictionary.get,reverse=True)[:word_limit]}
	sentence_scores = get_score(cleaned_content,sorted_dictionary)
	summary = get_summary(sentence_scores,sent_tokenize(content),threshold)
	print(summary)

if __name__ == "__main__":
	main()
