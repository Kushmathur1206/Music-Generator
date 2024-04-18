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
    page_icon="👋",
)

st.title("Music Generator")
st.sidebar.success("Select a page above.")


PrompttoMusic = st.button("Generate music using a description")
if PrompttoMusic:
    nav_page("Promtmusicpage")
Filemusic = st.button("Generate music using a file")
if Filemusic:
    nav_page("Promtmusicpage")