from datetime import date
import pandas as pd
import google.generativeai as genai
from time import sleep
import copy
import sys
import re
csv_file = "./ubuntu22.csv"
df = pd.read_csv(csv_file)


failed_cases_file = "failed_out.csv"
df_fail = pd.read_csv(failed_cases_file)


# failed_guideline = df_fail.iloc[0][0]
# failed_guideline_output = df_fail.iloc[0][2]

# print(failed_guideline , failed_guideline_output , len(df_fail))


#configuring genai and checking the avilable models
genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
model = genai.GenerativeModel('gemini-pro')

#chat history 
chat = model.start_chat(history=[])
while True :
    a = input("Enter your prompt")
    k = chat.send_message(a)
    print(k.text)


# def remove_markdown(text):
   
#     text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
#     text = re.sub(r'\[.*?\]\(.*?\)', '', text)   # Remove links

#     # Remove emphasis (bold, italics)
#     text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)  # Bold
#     text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)     # Italics

#     # Remove headers
#     text = re.sub(r'#+\s*(.*)', r'\1', text)

#     # Remove inline code
#     text = re.sub(r'`([^`]*)`', r'\1', text)

#     # Remove code blocks for all languages
#     text = re.sub(r'```json[a-z]*\n([\s\S]*?)```', r'\1', text) # Remove any content between triple backticks

#     # Remove blockquotes
#     text = re.sub(r'>\s*(.*)', r'\1', text)

#     # Remove horizontal lines
#     text = re.sub(r'---+', '', text)

#     # Remove lists
#     text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)

#     # Remove extra newlines and spaces
#     text = re.sub(r'\n+', '\n', text).strip()

#     return text





# chat.send_message(f"""You are AutoCIS Guard i.e. you see the guidelines and convert the guidelines into system specific commands 
#                   and check if its complaint with the systen or not.  if its not comliant then you are supposed to make a list of 
#                   commands you have to make the system compliant to it. This is your job""", safety_settings={'HARASSMENT':'block_none'})
# chat.send_message(f"So you will be generating commands and doing some debugging the csv fornat for this data is like this . This is only format of the data{df.head()}")


# for i in range(0, len(df_fail)) :
#       res = model.generate_content(f""" here the guideline is { df_fail.iloc[i][0]} and i got the  output as  {df_fail.iloc[i][2]} , now to make compatiable give me the la list of commands and their expected outcoeme in json format.
#                                   """)
#       rmmk = remove_markdown(res.text)
#       print(res.text)                         
#       print(rmmk)
#       print(" ------------------------------------------------------------------ ")






































# while True :
#     prompt =  input("say : ")
#     while prompt == "" or prompt == " ":
#         prompt = input("say : ")
#     # classifying the prompt for realtimedata or not
#     response = model.generate_content(f"""if the prompt is related to realtime data or current affairs or current news, 
#                                           then say strictly yes and if no say no
#                                           here to make you clear what might be realtime data are '
#                                           if asked about price of something , political learders or current news or ongoing events anywhere or weather or upcoming or releasing movies '
#                                           ,and to make sure you dont say yes to everything ,
#                                           and if  asked to look for something in interet or search for something in internet then return "intquery"
#                                           where the prompt : {prompt} """)
#     print(response.text)
    
#     if response.text.lower() == "yes"  :
#        # converting prompt to query 
#        rep2 = model.generate_content(f"""suppose you are a google search query bot and your work is to omptimise the prompt given by the user in such a way that google can use that 
#                                      search query to get the desired result and you give the a single search query,
#                                      an example for this is  if a prompt is ' hey yo whats the price of silver in my country ' 
#                                      and query is ' silver price today ',
#                                      strictly convert the given prompt to the query well todays date is {date.today()} and my location is {city}
#                                      where the prompt by user is : {prompt} """)
       

 



























            #   with open('mod.txt' ,'a') as f :
            #       f.write(f"---------------------------------------------------------------\n{all_text}\n----------------------------------------------------------")     
            #   if rep3.text.lower() != 'negative' and rep3.text.lower() != "":
            # #  if rep3.text.lower() != 'negative' or rep3.text.lower() != "" ''' or rep4.text.lower() != 'negative ''' :
            #      # if rep3.text.lower() != 'negative'  or rep3.text.lower() != ""  :
            #       k = copy.deepcopy(chat.history[0])
            #       l = copy.deepcopy(chat.history[1])
            #       chat.history.insert(len(chat.history),k)
            #       chat.history[len(chat.history)-1].role = "user"
            #       chat.history[len(chat.history)-1].parts[0].text = f" there are two prompt i.e. prompt 1 ''' {prompt} ''' and prompt 2 ''' {rep2} ''' , they are basically the same question as a prompt and would have the same answer,so according to these prompt try to answer from the text where the text is '''{result}''' well if you didn't find the asnwer in the text just strictky return 'negative' , well if you do find the answer then also try to return its unit , quantity , measurement or rate  if its givven there.   "
            #       chat.history.insert(len(chat.history),l)
            #       chat.history[len(chat.history)-1].role = "model"
            #       chat.history[len(chat.history)-1].parts[0].text = rep3.text
            #       print(rep3.text)
            #      # if rep4.text.lower() != 'negative' :
            #       #    print(rep4.text) 
            #       print(result['link'])
            #       break
            #   elif(rep3.text.lower()=="") :
            #       print("cannot get answer from the source")
            #       pass
            #   else :
            #       print("negetive")
      