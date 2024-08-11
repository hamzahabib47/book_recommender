import numpy as np
import streamlit as st
import pickle

books = pickle.load(open('PKL/books.pkl', 'rb'))
pt = pickle.load(open('PKL/pt.pkl', 'rb'))
similarity_scores = pickle.load(open('PKL/similarity_scores.pkl', 'rb'))

book_names = pt.index.values

def recommend(book_name):
  index = np.where(pt.index == book_name)[0][0]
  similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:7]

  data = []
  for i in similar_items:
    item = []

    temp_df = books[books['Book-Title']  == pt.index[i[0]]]
    item.extend(list(temp_df.drop_duplicates("Book-Title")['Book-Title'].values))
    item.extend(list(temp_df.drop_duplicates("Book-Title")['Book-Author'].values))
    item.extend(list(temp_df.drop_duplicates("Book-Title")['Image-URL-L'].values))

    data.append(item)

  return data

# Streamlit App
st.set_page_config(
    page_title="Book_Recommender",
)

st.title(":green[Book Recommender System]")

st.sidebar.success("Enter the name of your favourite book to see the top 6 similar books rated by the expert readers.")

selected_book_name = st.selectbox(
    label='Enter the book name to see top 6 similar books.', 
    options=book_names, 
    placeholder='Enter the book name...',
    index=None
)

try:
    if st.button('Recommmend'):
        if selected_book_name == None:
            st.header('Please enter the book name to see recommendations...')

        else:
            st.header(f'Six books similar to :green["{selected_book_name}"] are: ')

            book_data = recommend(selected_book_name)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(book_data[0][2])
                st.text(book_data[0][0])

            with col2:
                st.image(book_data[1][2])
                st.text(book_data[1][0])

            with col3:
                st.image(book_data[2][2])
                st.text(book_data[2][0])

            col4, col5, col6 = st.columns(3)

            with col4:
                st.image(book_data[3][2])
                st.text(book_data[3][0])

            with col5:
                st.image(book_data[4][2])
                st.text(book_data[4][0])

            with col6:
                st.image(book_data[5][2])
                st.text(book_data[5][0])

except:
    st.header(':red[An Error Occured!] Please try again or Select another book.')
