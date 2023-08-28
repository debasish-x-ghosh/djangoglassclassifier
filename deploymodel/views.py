from django.http import HttpResponse
from django.shortcuts import render
import joblib 
import pandas as pd
import os 
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS 
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from django.conf import settings

os.environ["OPENAI_API_KEY"] = "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"
global_docsearch = {}

def home(request):
    return render(request, "home.html")

def classifyglass(request):
    return render(request, "classifyglass.html")

def predictcarprice(request):
    return render(request, "predictcarprice.html")

def lcreadpdf(request):
    return render(request, "lcreadpdf.html")

def loadpdfopnai(request):
    return render(request, "lcreadpdf.html")

def resultlcreadpdf(request):
    input1 = request.GET['iptxt1'] 
    result = llmlc(input1, request)
    return render(request, "lcreadpdf.html", {'question': input1, 'result': result})

def llmlc(ques, request):
    # lanchain code starts here  
   
    print("*****************************************") 
    doc_reader = PdfReader('C:/Users/dgwor/PycharmProjects/jptrnb-ai/lanhchain-2/djlc/appdjlc/media/RespectedNetaji.pdf')
    #print(doc_reader)
    # read data from the file and put them into a variable called raw_text
    raw_text = ''
    for i, page in enumerate(doc_reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    print(len(raw_text))
    #print(raw_text[:100])
    # Splitting up the text into smaller chunks for indexing
    text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200, #striding over the text
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)
    #print(len(texts))
    #print(texts[0])
    #print(texts[1])
    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()
    global_docsearch = FAISS.from_texts(texts, embeddings)

 
    global_docsearch.embedding_function
    query = "who was Netaji's father?"
    docs = global_docsearch.similarity_search(query)
    print(docs)
    print(len(docs))
    print(docs[0])
    chain = load_qa_chain(OpenAI(), 
                      chain_type="stuff") # we are going to stuff all the docs in at once
  
    chain.llm_chain.prompt.template
    query = ques
    docs = global_docsearch.similarity_search(query)
    op = chain.run(input_documents=docs, question=query)
    
    print("---------------------------------------------")
    print(docs)
    print(op)
    # lanchain code ends here
    return op

def resultclassifyglass(request):
    cls = joblib.load('final_model.sav')

    lis=[]
    lis.append(request.GET['RI'])
    lis.append(request.GET['NA'])
    lis.append(request.GET['MG'])
    lis.append(request.GET['AI'])
    lis.append(request.GET['SI'])
    lis.append(request.GET['K'])
    lis.append(request.GET['CA'])
    lis.append(request.GET['BA'])
    lis.append(request.GET['FE'])
    print(lis)

    ans = cls.predict([lis])

    return render(request, "resultclassifyglass.html", {'ans': ans, 'lis': lis})

def resultpredictcarprice(request):
    
    cls2 = joblib.load('car_price_predictor.sav')

    # lis=[]
    # lis.append(request.GET['Present_Price'])
    # lis.append(request.GET['Kms_Driven'])
    # lis.append(request.GET['Fuel_Type'])
    # lis.append(request.GET['Seller_Type'])
    # lis.append(request.GET['Transmission'])
    # lis.append(request.GET['Owner'])
    # lis.append(request.GET['Age'])

    Present_Price = float(request.GET['Present_Price'])
    Kms_Driven = int(request.GET['Kms_Driven'])
    Fuel_Type = int(request.GET['Fuel_Type'])
    Seller_Type = int(request.GET['Seller_Type'])
    Transmission = int(request.GET['Transmission'])
    Owner = int(request.GET['Owner'])
    Age = int(request.GET['Age'])
    data_new = pd.DataFrame([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, Age]],
                            columns = ['Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Age'])
        
    #ar = np.array([5.0,0,0,0,0,0,9],dtype = float)
    ans = cls2.predict(data_new)
    return render(request, "resultpredictcarprice.html",{'ans': ans})