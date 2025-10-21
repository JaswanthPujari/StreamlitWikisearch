import streamlit as st
import requests

st.title("Wiki Search App in Streamlit")


query = st.text_input("Search Wikipedia")

if st.button("Search"):
    if query:
        try:
            
            url = f"https://apis.ccbp.in/wiki-search?search={query}"
            response = requests.get(url)
            
         
            if response.status_code == 200:
                data = response.json()
                
              
                if data['search_results']:
                    st.subheader("Search Results:")
                    for result in data['search_results']:
                        st.write(result['title'].title())
                        st.write(result['link'])
                        st.write(result['description'])
                        st.write("---")
                else:
                    st.info("No results found")
            else:
                st.error("Failed to fetch data from API")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a search term")
