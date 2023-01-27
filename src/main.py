import os
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def design():
	st.write("""# Covid19 Dashboard 
		This dashboard aims to provide a quick overview of covid19 status. """)
	st.sidebar.title("Home Menu")
	photo = Image.open("Vex.jpg")
	photo.show()
	st.image(photo, use_column_width = True)
	st.markdown('<style>body{background-color: darkblue;}</style', unsafe_allow_html = True)
design()