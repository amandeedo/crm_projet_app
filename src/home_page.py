import streamlit as st

st.set_page_config(
    page_title="Page d'accueil",
    page_icon="👋",
)

st.write("# Bienvenue sur la présentation de notre segmentation RFM ! 👋")

import streamlit as st

st.markdown(
    """
    Bonjour à tous, dans le cadre du projet de CRM analytics, il nous a été demandé de construire un segmentation RFM 
    afin de comprendre le comportement de la clientèle qui nous a été soumise. 
    
    Le site est ainsi composé de   : 
    - La page principale sur laquelle vous vous trouvez actuellement 
    - Une page contenant le dashboard à présenter aux équipes marketings et/ou à la direction générale
    - Une page contenant l'ensemble des visualisations nous ayant permis de caractériser la clientèle du magasin """)


st.markdown (" Bonne visite ! 🎉 ")



tab1, tab2 = st.tabs(["Qu'est ce qu'une segmentation RFM ?", "Résultats de notre segmentation"])


with tab1:
    st.markdown("Qu'est ce qu'une segmentation RFM ?")
    st.markdown("La segmentation RFM est un type de segmentation client basé sur 3 indicateurs :")
    st.markdown("La récence qui fait référence à la notion de dernière activité du client (achats, visites sur le site e-commerce)")
    st.markdown("La fréquence qui fait référence à la notion d'utilisation du service proposé sur une période donnée. Dans le cadre de notre étude, cela ferait référence au nombre de fois que le client ait eu recours à notre site.")
    st.markdown("Le montant qui fait référence à la somme moyenne dépensée sur une période par le client.")

with tab2:
    st.markdown("""### Résultats de notre segmentation
        En ce sens, nos segments sont les suivants : 
    """
    )
    st.image(r'./src/segments.jpeg', caption='Segments RFM')


    st.markdown(" Les segments que vous pouvez apercevoir ci-dessus sont le résultats des analyses effectuées dans les visualisations que vous trouverez sur notre interface web.")
    st.markdown (" Ils peuvent s'interpréter de la façon suivante :")
    st.markdown(""" 
    * Segment 1 : **Les vagues plates**
    
    Ce segment représente les clients qui ne génèrent pas beaucoup de chiffre d'affaires, ne montrent pas beaucoup d'intérêt pour l'entreprise et ne nécessitent pas beaucoup d'attention de la part de l'équipe marketing.
    
    
    * Segment 2 : **Les débutants**
    
    Les clients de ce segment ont acheté il y a longtemps, mais seulement une fois ou deux, et n'ont pas investi une grande somme d'argent.
    
    * Segment 3 : **Les anciens habitués**
    
    Ce segment regroupe les clients qui par le passé ont acheté en quantité auprès de l'entreprise et représentent une part importante de son chiffre d'affaires. Cependant ils n’ont pas une grandes récence
    
    * Segment 4 : **Les surfers égarés**
    
    Les clients de ce segment ont acheté avec un montant faible par le passé, mais ne sont plus actifs depuis un certain temps. Comme les surfeurs qui se sont éloignés de leur spot habituel, l'entreprise doit comprendre pourquoi ils ne sont plus intéressés et essayer de les reconquérir.
    
    * Segment 5 : **Les vagues perdues**
    
    Ce segment représente les clients qui ont acheté assez régulièrement dans le passé, mais dont les achats se sont espacés dans le temps. Comme les surfeurs qui perdent progressivement leur niveau, ces clients sont en train de s'éloigner de l'entreprise et il est important de trouver des moyens de les récupérer.
    
    * Segment 6 : **Les surfeurs prometteurs**
    
    Ce segment regroupe les clients qui ont acheté également dans le passé et dont les achats montrent un certain potentiel en termes de montant. Comme les surfeurs qui ont un bon potentiel mais qui doivent encore s'améliorer, ces clients pourraient devenir de bons clients fidèles s'ils sont bien ciblés.
    
    * Segment 7 : **Les planches stables**
    
    Ce segment représente les clients qui achètent régulièrement, mais dont les achats ne sont pas très importants. Comme les surfeurs qui se contentent de vagues régulières mais pas très hautes, ces clients ont une certaine valeur pour l'entreprise mais n'ont pas un potentiel de croissance très élevé.
    
    * Segment 8 : **Les Barrels**
    
    En surf, un "barrel" est un tube formé par une vague qui se referme sur elle-même. De même, ces clients ont le potentiel de faire des achats répétés, il est donc important de travailler pour les conserver et les faire progresser dans leur relation avec l'entreprise.
    
    * Segment 9 : **Les grosses vagues**
    
    Ce segment regroupe les clients à haute valeur qui ont acheté régulièrement et ont dépensé beaucoup d'argent. Comme les surfeurs qui sont en quête de grosses vagues à dompter, ces clients sont très importants pour l'entreprise et doivent être fidélisés.
    """ )
