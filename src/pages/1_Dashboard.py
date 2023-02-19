import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Segmentation RFM", layout="wide")

def main():
    html_temp = """<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/segmentationrfm/views/Analysedesegmentationdelaclientelle/DashboardSegmentation' width='1625' height='1008' hide-tabs toolbar='bottom' ></tableau-viz>"""
    components.html(html_temp, width=1625, height=1008)
if __name__ == "__main__":    
    main()