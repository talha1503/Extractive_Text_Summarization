# Extractive Text Summarization

Various  unsupervised algorithms for Extractive Summarization. <br />
* [TextRank](Text_Rank_.ipynb)  <br />
* [SumBasic](SumBasic.ipynb) <br />
* [Luhns Summarization](luhn_sum.py)  <br />


## Sample Results

###  **Document :**

```"In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, 'With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow.' The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills."```

### Outputs:

#### TextRank:

```In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, 'With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset."```

#### SumBasic:

``` 
Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public.As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses.
The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry.Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. 
``` 

#### Luhn's Summarization:
```The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, 'With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses.``` 


## Built With

* [nltk](https://www.nltk.org/)
* [numpy](https://numpy.org/)


## Acknowledgments

* Research paper on SumBasic Text Summarization https://www.cs.bgu.ac.il/~elhadad/nlp09/sumbasic.pdf 
* A youtube video which explains PageRank Algorithm https://www.youtube.com/watch?v=P8Kt6Abq_rM
* Research paper on TextRank Algorithm https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
* Masa Nekic's talk on Automatic Text Summarization https://www.youtube.com/watch?v=_d0OXm0dRZ4
