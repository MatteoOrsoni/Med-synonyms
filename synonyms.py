import streamlit as st
import numpy as np 
import pandas as pd

st.set_page_config(page_title = 'Cerca il tuo Sinonimo')
st.markdown("<h1 style='text-align: center; color: black;'>🩺 Med Synonyms 💉</h1>", unsafe_allow_html=True)

caricamento_dati = st.file_uploader("Carica i tuoi dati in xlsx")

if caricamento_dati is not None:
      data = pd.read_excel(caricamento_dati)
      st.markdown("<h2 style='text-align: center; color: black;'>Grazie!! Ora li puoi vedere visualizzati proprio qui</h2>", unsafe_allow_html=True)
      edited_df = st.data_editor(data,num_rows="dynamic", use_container_width=True)
      list_name = list(data['Nome'])
      st.markdown("<h2 style='text-align: center; color: black;'>Qui puoi cercare i sinonimi inserendo la parola chiave nella barra di ricerca</h2>", unsafe_allow_html=True)
      output = st.selectbox('Cerca qui il tuo sinonimo', list_name)

      select_prod = data.loc[data['Nome'] == output]
      label = int(select_prod['Gruppo'])
      st.write('il gruppo selezionato è il:', label)

      selected = data.loc[data['Gruppo'] == label]

      st.markdown("<h2 style='text-align: center; color: black;'>Qui sotto troverai la lista dei sinonimi collegati alla parola che hai cercato</h2>", unsafe_allow_html=True)
      st.write(selected['Nome'], use_container_width=True)


      ##SIDEBAR##

      st.sidebar.header('Filtra qui i tuoi dati per gruppo')
      macro = st.sidebar.multiselect(
        "Seleziona il gruppo:",
        options = data['Macro'].unique(),
        default = data['Macro'].unique()
      )



      data_selection = data.query (
        "Macro == @macro"
      )
      st.markdown("<h2 style='text-align: center; color: black;'>Qui invece trovi la lista dei sinonimi filtrati per macro categoria</h2>", unsafe_allow_html=True)
      st.dataframe(data_selection,  use_container_width=True)

else:
       st.markdown("<h2 style='text-align: center; color: black;'>Sto aspettando i tuoi dati</h2>", unsafe_allow_html=True)









    
