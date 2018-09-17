if __name__=="__main__":
    import re
    import sys
    import pickle
    import time
    import timeit
    from itertools import product
    from string import ascii_lowercase
    from operator import itemgetter
    from nltk import bigrams
    start_time=time.perf_counter()
    start_cpu=time.process_time()

    unigrams={}
    words=[]
    distinct_words=0
    result=0
    new_words=[]
    actual_words={}
    def unigram_gen(words):
                #unigrams count
        char_count=0
        alphabet_count=0
        for x in words:
            for y in x:
                char_count+=1
                if y in unigrams:
                    unigrams[y]+=1
                else:
                    unigrams[y]=1
                    alphabet_count+=1

    bigram={}
    bigram_list=[]
    def bigram_gen(words):
        list_bigram=[]
        for w in words:
            w="<"+w+">"
            list_bigram=list(bigrams(w))
            for x in list_bigram:
                s=''.join(x)
                if s in bigram:
                    bigram[s]+=1
                else:
                    bigram[s]=1
    def word_frequency_gen(words):
        for y in words:
            if y in actual_words:
                actual_words[y]+=1
            else:
                actual_words[y]=1

    def func(fname):
        with open(fname,'r') as f:
            print("started reading at: %f, cpu_time: %f " %(start_time,start_cpu))
            pattern="AP88....-...."
            records=0
            for line in f:
                records+=1
                for char in line:
                    line=re.sub(pattern,' ',line)
                    line=line.lower()
                    line=re.sub('[^A-Za-z]',' ', line)

                words=line.split(" ")
                words = [elem for elem in words if elem.strip()]



                unigram_gen(words)
                bigram_gen(words)
                word_frequency_gen(words)
            end_time=time.perf_counter()
            end_cpu=time.process_time()

            sort_top10=sorted(actual_words.items(),key=lambda kv: kv[1], reverse=True)
            num_of_words=0
                #loop for counting and printing the words and distinct words
            for a,b in sort_top10:
                temp=int(b)
                num_of_words+=temp

            elapsed_time=end_time-start_time
            elapsed_cpu=end_cpu-start_cpu

            print("finished reading at: %f, cpu_time: %f " %(end_time,end_cpu))
            print("Total elapsed time: %f, cpu_time: %f" %(elapsed_time,elapsed_cpu))
            print("Number of Records: ",records)
            print("Number of Words: ",num_of_words)
            print("Number of unique words:",len(actual_words))
                #loop for printing the sorted list of words
            i=0
            for a,b in sort_top10:
                i+=1
                if i in range(11):
                    print("%-20s %5d" %(a,b))

                #unigrams count
            print("\n unigram counts:")
            sort_alpha=sorted(unigrams.items(), key=itemgetter(0))
            for a,b in sort_alpha:
                print("%-2s %5d" %(a,b))

            print("\n bigram counts:")
            sort_bigram=sorted(bigram.items(), key=itemgetter(0))
            for a,b in sort_bigram:
                print("%-2s %5d" %(a,b))

    func(sys.argv[1])
    final_dicts_list=[]
    final_dicts_list.append(unigrams)
    final_dicts_list.append(bigram)
    final_dicts_list.append(actual_words)
    final_dicts_list.append(len(actual_words))
    class Data(object):
        def __init__(self,data):
            self.data=data
        def mydata(self,data):
            return self.data

    data_object=Data(final_dicts_list)
    mydata=data_object.mydata(final_dicts_list)

    my_file = open("pickled_data2.dat", 'wb')
    pickle.dump(mydata, my_file)
