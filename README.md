# Text Summarization

This is Extraction type of text summarization. It take text file of paragraph as input and give output as summary of given paragraph.

Basically this is NLP project. 
* First used sentence and word tokenizer for split data into words. 
* Then it generates similarity matrix by using cosine distance between two sentence vectors. 
* In last, it’ll give top n sentence from the ranked sentence. 

For use this project, just change sample.txt file and then run Python file. You can change number of lines in summary by change one parameter `top_n` in code.
