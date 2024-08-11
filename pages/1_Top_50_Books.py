import streamlit as st
import pickle

popular_df = pickle.load(open('PKL/popular.pkl', 'rb'))

book_name = popular_df['Book-Title'].values
author = popular_df['Book-Author'].values
image = popular_df['Image-URL-L'].values
votes = popular_df['Num_Ratings'].values
rating = popular_df['Avg_Rating'].values

# main app
st.title(":green[Top 50 Books]")

st.sidebar.success("Here are the top 50 books rated by the expert readers.")

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[0])
  st.write(book_name[0])
  st.write('Rating : ', rating[0].round(2))

with col2:
  st.image(image[1])
  st.write(book_name[1])
  st.write('Rating : ', rating[1].round(2))

with col3:
  st.image(image[2])
  st.write(book_name[2])
  st.write('Rating : ', rating[2].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[3])
  st.write(book_name[3])
  st.write('Rating : ', rating[3].round(2))

with col2:
  st.image(image[4])
  st.write(book_name[4])
  st.write('Rating : ', rating[4].round(2))

with col3:
  st.image(image[5])
  st.write(book_name[5])
  st.write('Rating : ', rating[5].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[6])
  st.write(book_name[6])
  st.write('Rating : ', rating[6].round(2))

with col2:
  st.image(image[7])
  st.write(book_name[7])
  st.write('Rating : ', rating[7].round(2))

with col3:
  st.image(image[8])
  st.write(book_name[8])
  st.write('Rating : ', rating[8].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[9])
  st.write(book_name[9])
  st.write('Rating : ', rating[9].round(2))

with col2:
  st.image(image[10])
  st.write(book_name[10])
  st.write('Rating : ', rating[10].round(2))

with col3:
  st.image(image[11])
  st.write(book_name[11])
  st.write('Rating : ', rating[11].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[12])
  st.write(book_name[12])
  st.write('Rating : ', rating[12].round(2))

with col2:
  st.image(image[13])
  st.write(book_name[13])
  st.write('Rating : ', rating[13].round(2))

with col3:
  st.image(image[14])
  st.write(book_name[14])
  st.write('Rating : ', rating[14].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[15])
  st.write(book_name[15])
  st.write('Rating : ', rating[15].round(2))

with col2:
  st.image(image[16])
  st.write(book_name[16])
  st.write('Rating : ', rating[16].round(2))

with col3:
  st.image(image[17])
  st.write(book_name[17])
  st.write('Rating : ', rating[17].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[18])
  st.write(book_name[18])
  st.write('Rating : ', rating[18].round(2))

with col2:
  st.image(image[19])
  st.write(book_name[19])
  st.write('Rating : ', rating[19].round(2))

with col3:
  st.image(image[20])
  st.write(book_name[20])
  st.write('Rating : ', rating[20].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[21])
  st.write(book_name[21])
  st.write('Rating : ', rating[21].round(2))

with col2:
  st.image(image[22])
  st.write(book_name[22])
  st.write('Rating : ', rating[22].round(2))

with col3:
  st.image(image[23])
  st.write(book_name[23])
  st.write('Rating : ', rating[23].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[24])
  st.write(book_name[24])
  st.write('Rating : ', rating[24].round(2))

with col2:
  st.image(image[25])
  st.write(book_name[25])
  st.write('Rating : ', rating[25].round(2))

with col3:
  st.image(image[26])
  st.write(book_name[26])
  st.write('Rating : ', rating[26].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[27])
  st.write(book_name[27])
  st.write('Rating : ', rating[27].round(2))

with col2:
  st.image(image[28])
  st.write(book_name[28])
  st.write('Rating : ', rating[28].round(2))

with col3:
  st.image(image[29])
  st.write(book_name[29])
  st.write('Rating : ', rating[29].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[30])
  st.write(book_name[30])
  st.write('Rating : ', rating[30].round(2))

with col2:
  st.image(image[31])
  st.write(book_name[31])
  st.write('Rating : ', rating[31].round(2))

with col3:
  st.image(image[32])
  st.write(book_name[32])
  st.write('Rating : ', rating[32].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[33])
  st.write(book_name[33])
  st.write('Rating : ', rating[33].round(2))

with col2:
  st.image(image[34])
  st.write(book_name[34])
  st.write('Rating : ', rating[34].round(2))

with col3:
  st.image(image[35])
  st.write(book_name[35])
  st.write('Rating : ', rating[35].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[36])
  st.write(book_name[36])
  st.write('Rating : ', rating[36].round(2))

with col2:
  st.image(image[37])
  st.write(book_name[37])
  st.write('Rating : ', rating[37].round(2))

with col3:
  st.image(image[38])
  st.write(book_name[38])
  st.write('Rating : ', rating[38].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[39])
  st.write(book_name[39])
  st.write('Rating : ', rating[39].round(2))

with col2:
  st.image(image[40])
  st.write(book_name[40])
  st.write('Rating : ', rating[40].round(2))

with col3:
  st.image(image[41])
  st.write(book_name[41])
  st.write('Rating : ', rating[41].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[42])
  st.write(book_name[42])
  st.write('Rating : ', rating[42].round(2))

with col2:
  st.image(image[43])
  st.write(book_name[43])
  st.write('Rating : ', rating[43].round(2))

with col3:
  st.image(image[44])
  st.write(book_name[44])
  st.write('Rating : ', rating[44].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[45])
  st.write(book_name[45])
  st.write('Rating : ', rating[45].round(2))

with col2:
  st.image(image[46])
  st.write(book_name[46])
  st.write('Rating : ', rating[46].round(2))

with col3:
  st.image(image[47])
  st.write(book_name[47])
  st.write('Rating : ', rating[47].round(2))

col1, col2, col3 = st.columns(3)

with col1:
  st.image(image[48])
  st.write(book_name[48])
  st.write('Rating : ', rating[48].round(2))

with col2:
  st.image(image[49])
  st.write(book_name[49])
  st.write('Rating : ', rating[49].round(2))




