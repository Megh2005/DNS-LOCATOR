import dns.resolver
import streamlit as st

# Set up the Streamlit app layout and title
st.set_page_config(page_title="DNS Record Tracker", layout="centered", page_icon="🔍")
st.markdown(
    "<style>"
    "h1 { color: #4B4B4B; font-family: 'Arial', sans-serif; }"
    "h2 { color: #2B7A78; font-family: 'Arial', sans-serif; margin-top: 1em; }"
    ".stTextInput input { border-radius: 8px; padding: 10px; font-size: 16px; }"
    ".stButton button { border-radius: 8px; font-weight: bold; padding: 0.5em 1em; }"
    ".error { color: #D72323; font-weight: bold; }"
    "</style>",
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("🔍 DNS Record Tracker")
st.write(
    "A quick way to check and retrieve DNS records for any domain. Enter a domain name below and select the type of DNS records you want to explore."
)

# User input for the domain
domain = st.text_input("Enter Domain Name", "")

# Record types to lookup
record_types = ["A", "AAAA", "NS", "CNAME", "MX", "PTR", "SOA", "TXT"]

# When the user clicks the button, perform the DNS lookup
if st.button("Lookup DNS Records"):
    if not domain:
        st.error("Please enter a domain name.")
    else:
        st.write(f"### Results for: **{domain}**")

        # Go through each record type and attempt to retrieve DNS information
        for record_type in record_types:
            try:
                answer = dns.resolver.resolve(domain, record_type)

                # Collapsible section for each record type
                with st.expander(f"🔹 {record_type} Records"):
                    for server in answer:
                        st.markdown(
                            f"<p style='color: #444; font-size: 1em;'>{server.to_text()}</p>",
                            unsafe_allow_html=True,
                        )

            except dns.resolver.NoAnswer:
                st.warning(f"No {record_type} records found for {domain}.")
            except dns.resolver.NXDOMAIN:
                st.error(f"{domain} does not exist. Please check the domain name.")
                break
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
                break

# Footer with additional resources
st.markdown(
    "<hr style='margin-top: 2em;'>"
    "<p style='text-align: center; color: #888;'>Built With 💗 By Megh</p>"
    "<p style='text-align: center; color: #888;'>"
    "Need help understanding DNS records? Check out these resources:<br>"
    "<a href='https://en.wikipedia.org/wiki/List_of_DNS_record_types' target='_blank'>List of DNS Record Types</a> | "
    "<a href='https://github.com/Megh2005' target='_blank'>My GitHub</a>"
    "</p>",
    unsafe_allow_html=True,
)
