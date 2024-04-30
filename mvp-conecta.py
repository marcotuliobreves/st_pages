from st_pages import show_pages_from_config, hide_pages
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

show_pages_from_config()

switch_page("Login")

