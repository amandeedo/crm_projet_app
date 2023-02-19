import streamlit as st

st.set_page_config(
    page_title="Page d'accueil",
    page_icon="👋",
)

st.write("# Bienvenue sur la présentation de notre segmentation RFM ! 👋")


st.markdown(
    """
    Bonjour à tous, dans le cadre du projet de CRM analytics, il nous a été demandé de construire un segmentation RFM 
    afin de comprendre le comportement de la clientèle qui nous a été soumise. 
    
     ### Qu'est ce qu'une segmentation RFM ? 
    La segmentation RFM est un type de segmentation client basée sur 3 indicateurs : 
    *  La récence qui fait référence à la notion de dernière activité du client (achats, visites sur le site e-commerce)
    * La fréquence qui fait référence à la notion d'utilisation du service proposé sur une période donnée. Dans le cadre de notre étude, cela ferait référence au nombre de fois que le client ait eu recours à notre site.
    * Le montant qui fait référence à la somme moyenne dépensée sur une période par le client.
    
    ### Résultats de notre segmentation
    En ce sens, nos segments sont les suivants : 
"""
)
st.image('./crm_projet_app/src/segments.jpeg', caption='Segments RFM')


st.markdown(" Les segments que vous pouvez apercevoir ci-dessus sont le résultats des analyses effectuées dans les visualisations que vous trouverez sur notre interface web.")



st.markdown (" Bonne visite ! 🎉 ")
