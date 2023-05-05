import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import pandas as pd

st.title("📸Ooshot Data Analysis")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    st.error("Pour commencer la visualisation, veuillez choisir le ficher CSV correspondant à l'étude")
#data = pd.read_csv(r'C:\Users\Riviere\OneDrive\Bureau\exercice_ooshot\Export exercice Ingénieur data et process.csv')


# Plot top 10 countries
st.markdown('Pays regroupant le plus les talents - TOP10')
plt.figure(figsize=(12, 4))
top10 = data['CODE PAYS'].value_counts().sort_values().tail(10)
ax = top10.plot.barh(edgecolor='black', grid=True, fontsize=12)

for p in ax.patches:
    width = p.get_width()
    ax.text(width+1, p.get_y(), int(width), ha='left', va='bottom', fontsize=11)

sns.despine()
st.pyplot(plt)

st.write('Dans cette première partie nous avons un appercu du nombre de talent dans chaque pays en utilisant la fonction group by. Pour plus de visibilité j''ai choisi de garder les dix nations ayants les plus de talents dans la base données.Idem, cette reprsétentation grapfique va nous aider à batir via la fonction group by, le nombre de professionnel à travers le monde, en rassemblant les variables ''1- Informations Générales - Compétences' 'et ''CODE PAYS' 'Par la suite la fonction ''sum' 'va nous aider à comptabiliser l''ensemble de grouby')

grouped_data3 = data.groupby(['1- Informations Générales - Compétences', 'CODE PAYS']).size().reset_index(name='count')

# Plot top 10 
st.markdown('Top des professions')
plt.figure(figsize=(12, 4))
top10 = grouped_data3['1- Informations Générales - Compétences'].value_counts().sort_values().tail(10)
ax = top10.plot.barh(edgecolor='black', grid=True, fontsize=12)

for p in ax.patches:
    width = p.get_width()
    ax.text(width+1, p.get_y(), int(width), ha='left', va='bottom', fontsize=12)

sns.despine()
st.pyplot(plt)

total_professionals = grouped_data3['count'].sum()
st.write(f"Total des professionnels dans le monde: {total_professionals}")
st.write('La reprsentation ci dessus, n''est pas forcément des plus comunicante. Pour cela, j''ai essayé de rendre le données plus intéractive. J''ai donc opté pour la librairie ''plotly''qui se veut interactive. Ici notre sunburst permet de "zommer" sur les pays et ainsi avoir une meilleure perspective des talents.')
# Sunburst plot
fig = px.sunburst(grouped_data3, path=['CODE PAYS', '1- Informations Générales - Compétences'], values='count')
st.plotly_chart(fig)


# Class selection
selected_class = st.selectbox('Choisir une option', options=['Classique', 'Premium', 'Luxe'])

# Specialties selection
specialties = ["5 - Graphisme - Spécialité", "7- Spécialité - Voitures", "7- Spécialité - Visite virtuelle", "7- Spécialité - Tourisme", "7- Spécialité - Sports", "7- Spécialité - Retail", "7- Spécialité - Reproduction d'oeuvres d'art", "7- Spécialité - Publicité", "7- Spécialité - Portraits", "7- Spécialité - Paysages"]
selected_specialty = st.selectbox('Choisir une spécialité', options=specialties)

# Country selection
selected_country = st.selectbox('Choisir un pays', options=data['CODE PAYS'].unique())

# Filter data
filtered_data = data[data[selected_specialty] == selected_class]
filtered_data = filtered_data[filtered_data['CODE PAYS'] == selected_country]

# Display filtered data
st.write(filtered_data[['id sellsy', selected_specialty]])

