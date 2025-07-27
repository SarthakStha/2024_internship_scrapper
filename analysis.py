import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import os

def get_data(path):
    df = pd.read_csv(path)
    roles = df['role'].astype(str).tolist()
    return roles

def filter_data(data_list):
    removed_words = ['intern', 'summer', 'engineering', 'engineer']
    filtered_list = []

    for data in data_list:
        data = re.sub(r'[^A-Za-z\s]', '', data)
        data = data.lower()

        for word in removed_words:
            data = data.replace(word, '').strip()

        filtered_list.append(data)
    
    return filtered_list

def make_cloud(data, save_dir):
    text = ' '.join(word for word in data)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  
    plt.title("Most frequently appearing words in intership roles")

    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, 'word_frequency.png')
    plt.savefig(file_path)
    plt.show()

def main():
    file_path = './test.csv'
    roles = get_data(file_path)
    filtered_data = filter_data(roles)

    save_dir = './visuals'
    make_cloud(filtered_data, save_dir)


if __name__=="__main__":
    main()