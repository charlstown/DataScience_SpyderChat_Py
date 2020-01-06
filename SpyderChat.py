import sys
import re
import os
import pandas as pd
pd.set_option('display.max_columns', 500)
from matplotlib import pyplot as plt
import seaborn as sns
import calendar
from collections import Counter

def start_bot():
    path = 'chat.txt'
    loop = os.path.isfile(path)
    while loop == False:
        path = input('Please type the file to analyze. Ex: chat.txt  >>>')
        if path == 'exit':
            sys.exit()
        loop = os.path.isfile(path)
        if loop == False:
            print('There is no file named like that. Please try again or type exit to close.')
    try:
        os.makedirs('whatsapp')
    except:
        print('Overwritting folder...')
    return path

def opener(p):
    f = open(p, encoding='utf-8')
    text = f.read()
    return text

def extract_time(text):
    date_time = re.findall('\d{1,2}.\d{1,2}.\d{2}.\d{1,2}.\d{1,2}.-.+:', text)
    date = [i.split(' ')[0] for i in date_time]
    time = [i.split(' ')[1] for i in date_time]
    return date, time

def extract_messages(text):
    chat = re.split('\d{1,2}.\d{1,2}.\d{2}.\d{1,2}.\d{1,2}.-.+:', text)[1:]
    users = re.findall('\d{1,2}.\d{1,2}.\d{2}.\d{1,2}.\d{1,2}.-.+:', text)
    users = [i.split(':')[1] for i in users]
    users = [i.split('-')[-1] for i in users]
    users = [i.strip() for i in users]
    return chat, users

def create_table(path):
    whatsapp = opener(path)
    date, time = extract_time(whatsapp)
    messages, users = extract_messages(whatsapp)
    whatsapp_df = pd.DataFrame({'date': date, 'time': time, 'user': users, 'message': messages})
    return(whatsapp_df)

def erase_users(users):
    for us in users:
        df.drop(df[df.user == us].index, axis=0, inplace=True)

def text2words(text):
    def no_accents(txt):
        txt = re.sub('[àáä]','a', txt)
        txt = re.sub('[éëè]','e', txt)
        txt = re.sub('[íïì]','i', txt)
        txt = re.sub('[óöò]','o', txt)
        txt = re.sub('[úüù]','u', txt)
        return txt
    
    text = re.sub('<Multimedia omitido>', '', text)
    text = re.sub('[^\w]', ' ', text)
    text = re.sub('[ \t\n]', ' ', text)
    text = re.sub('[\d]', ' ', text)
    text = re.sub('[ja]{2,10}', '', text)
    text = text.lower()
    text = no_accents(text)
    words = text.split()
    words = [i for i in words if len(i)>2]
    return words
    
def words_rank(df):
    #all words counted
    all_messages = df.groupby('user').message.sum().reset_index()
    #create dataframe
    dfs = []
    for i in list(all_messages.user):
        txt = all_messages[all_messages.user == i].message.reset_index(drop=True)[0]
        user_words = text2words(txt)
        counted = Counter(user_words)
        df_words = pd.DataFrame({'user': [i]*len(list(counted.keys())),'word': list(counted.keys()), 'times_repeated': list(counted.values())})
        dfs.append(df_words)
    df_words_users = pd.concat(dfs).sort_values(by=['times_repeated'], ascending=False)
    return df_words_users

def words_finder(df):
#    selected_names = 'vills charles nach maiks simon juan cesar edu fer dave david saims alvaro'
    selected_words = 'joder tio crack puto puta buen gente coño mierda cabron sara lucia tias fiesta tetas cojones gente'
    selected_words = selected_words.split()
    subset = df[df['word'].isin(selected_words)].sort_values(by=['times_repeated'], ascending=False)
    return subset
    

# =============================================================================
# STARTING THE CODE
# =============================================================================
#insert data
path = start_bot()

#dataframe creation
df = create_table(path)

#data cleanning for this study
users_to_delete = ['César Bernabé Rodríguez', 'Jorge Bravo', 'César Villa']
erase_users(users_to_delete)

#creating new columns
df['months'] = df.date.apply(lambda x: (x.split('/')[1]).zfill(2))
df['years'] = df.date.apply(lambda x: (x.split('/')[2]))

#saving df
df.to_csv('whatsapp/WhatsDataframe.csv', index=False)

#piechart by users
pie = df.groupby(df.user).message.count().reset_index()
pie['percentage'] = pie.message/pie.message.sum()
plt.title('Users conversation percentage')
plt.pie(pie.percentage, labels=pie.user, autopct='%1.1f%%')
plt.savefig('whatsapp/01_ConversationPercentage.png')
plt.close()

#get the months
# plt.figure(1, figsize=(100, 10))
data_month = df.groupby(df.months).message.count().reset_index().sort_values(by=['months'], ascending = True)
data_month['months'] = data_month.months.apply(lambda x: calendar.month_abbr[int(x)])
plt.title('Monthly activity in the chat')
sns.barplot(data_month.months, data_month.message)
plt.savefig('whatsapp/02_MonthlyActivity.png')
plt.close()

#get user monthly chat
group = df.groupby([df.user, df.years]).message.count().reset_index()
g = sns.FacetGrid(group, col = "user")
g.map(plt.plot, 'years', 'message')
plt.savefig('whatsapp/03_TrendActivityByUser.png')
plt.close()

#group activity
total = df.groupby(df.years).message.count().reset_index()
plt.title('Anual Activity')
plt.xlabel('Years')
plt.ylabel('Number of messages')
plt.plot(total.years, total.message)
plt.savefig('whatsapp/04_AnualActivity.png')
plt.close()

#number of messages sent
data_nmsn = df.groupby(df.user).message.count().reset_index()
data_nmsn = data_nmsn.sort_values(by=['message'], ascending=False)
plt.title('Average words by user')
plt.gcf().subplots_adjust(bottom=0.25)
chart01 = sns.barplot(data_nmsn.user, data_nmsn.message)
chart01.set_xticklabels(data_nmsn.user, rotation=45)
chart01.figure.savefig("whatsapp/05_TotalMessagesByUser.png")
plt.close()

#get the average messages length
df['average_words'] = df.message.apply(lambda x: len(x))
plt.title('Average words by user')
plt.gcf().subplots_adjust(bottom=0.20)
chart02 = sns.boxplot(x=df.user, y=df.average_words, data=df, showfliers=False)
#chart02.set_xticklabels(x=df.user, rotation=45)
chart02.figure.savefig("whatsapp/06_AverageWordsByUser.png")
plt.close()

#get the words mostly used
words = words_rank(df)
pd.set_option('display.max_rows', 500)
#print(words[:500])
subset = words_finder(words).pivot("user", "word", "times_repeated")
f, ax = plt.subplots(figsize=(11, 6))
plt.title('Palabras más repetidas por Brothas&Co')
plt.gcf().subplots_adjust(bottom=0.25)
chart_words = sns.heatmap(subset, fmt='g', annot=True, linewidths=.5, ax=ax)
chart_words.figure.savefig("whatsapp/07_Words HeatMap.png")
plt.close()



