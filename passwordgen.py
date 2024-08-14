#using streamlit
import streamlit as st
import random

# Your password generation code goes here 

# Define the Streamlit app
def main():
    st.title("Password Generator")

    passlen = st.slider("Select the desired length of the password:", 8, 128, 12)
    capans = st.selectbox("Are CAPITAL Alphabets allowed?", ("Yes", "No"))
    smallans = st.selectbox("Are lowercase Alphabets allowed?", ("Yes", "No"))
    digans = st.selectbox("Are Digits allowed?", ("Yes", "No"))
    spans = st.selectbox("Are Special Characters allowed?", ("Yes", "No"))
    rep = st.selectbox("Select password generation method:", ("Minimal Resource Usage (Way 1)", "More Secure Generation (Way 2)"))

    capans, smallans, digans, spans = capans.title(), smallans.title(), digans.title(), spans.title()

    # Generate the password when the button is clicked
    if st.button("Generate Password"):
        capchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        spchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', ',', '.']
        smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        comblis = []
        if capans == 'Yes':
            if smallans == 'Yes':
                if digans == 'Yes':
                    if spans == 'Yes':
                        comblis = capchar + dig + spchar + smallchar
                    else:
                        comblis = capchar + dig + smallchar
                else:
                    if spans == 'Yes':
                        comblis = capchar + spchar + smallchar
                    else:
                        comblis = capchar + smallchar
            else:
                if digans == 'Yes':
                    if spans == 'Yes':
                        comblis = capchar + dig + spchar
                    else:
                        comblis = capchar + dig
                else:
                    if spans == 'Yes':
                        comblis = capchar + spchar
                    else:
                        comblis = capchar
        else:
            if smallans == 'Yes':
                if digans == 'Yes':
                    if spans == 'Yes':
                        comblis = dig + spchar + smallchar
                    else:
                        comblis = dig + smallchar
                else:
                    if spans == 'Yes':
                        comblis = spchar + smallchar
                    else:
                        comblis = smallchar
            else:
                if digans == 'Yes':
                    if spans == 'Yes':
                        comblis = dig + spchar
                    else:
                        comblis = dig
                else:
                    if spans == 'Yes':
                        comblis = spchar
                    else:
                        st.error("Error, You denied the usage of all possible characters")
                        return

        # Generate the password
        password = ""
        if rep == 'Minimal Resource Usage (Way 1)':
            for i in range(passlen):
                password += comblis[random.randint(0, len(comblis) - 1)]
        else:
            random.shuffle(comblis)
            for i in range(passlen):
                q = random.choice(comblis)
                random.shuffle(comblis)
                password = password + q

        st.success("Generated Password: " + password)

if __name__ == "__main__":
    main()