import streamlit as st
from streamlit.components.v1 import html
def nav_page(page_name, timeout_secs=0):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


st.set_page_config(
    page_title="Music Generator",
    page_icon="🎵",
    initial_sidebar_state="collapsed"
)



video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 80%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://cdn.pixabay.com/video/2022/10/16/135068-761273397_large.mp4")>
		  Your browser does not support HTML5 video.
		</video>
        """

st.markdown(video_html, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st1 = st.markdown(
    """
<style>
button {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-right: 20px !important;
    padding-left: 20px !important;
    font-family: Arial, sans-serif;
    font-size: 25px !important;
    font-weight: bold;
    color: ##ff99ff;
    
}
</style>
""",
    unsafe_allow_html=True,
)

def main():
    st.title("Music Generator 🎵")
    PrompttoMusic = st.button("Generate music using a description")
    if PrompttoMusic:
        nav_page("Promtmusicpage")
    Filemusic = st.button("Generate music using a file")
    if Filemusic:
        nav_page("Filemusicpage")
if __name__ == "__main__":
    main()