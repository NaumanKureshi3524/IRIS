import streamlit as st

st.title("Bar Island")
st.subheader("Welcome To The Bar Island ,Where you can customize your drinks!")

a=st.button('Make a drink')

if a:
    st.success('your drink is being prepared')


b=st.checkbox('Add Egg')
if b:
    st.success('Egg has been added to your drink.')



c=st.selectbox('Select Your Base',['Milk','Alcohol','Coconut Water','Toadi','Soft-drink'])

if c:
    st.write(f'you have selected {c} as your base for the drink')

d=st.slider("Select your base in strengh",30,250,60)
if d:
    st.write(f'YOu have selected {d} as your base for the drink')


e=st.radio('select your flavour',['chocolate','vanila','Tangy','Mint','Lime','Without flavour'])
if e:
    st.success(f'You Have Selected {e} as your flavour for the drink ')

st.number_input('How Many Number Of Spoon Sugar You Want to Add ?',min_value=0,max_value=10,step=1)

f=st.text_input("Enter Your Name ")
if f: 
    st.success(f'Hello {f},Your Order Is Being Prepared.')

g=st.date_input("Select Your Date Of Birth")
if g:
    st.write(f'Your Date Of Birth is: {g}')


st.markdown('## Ww are Planing To introduce two new drinks in the house , please vote for favourite Drinks')

clm1,clm2=st.columns(2)
with clm1:
    st.header("Jamun Chatpata")
    
    v1=st.button("Vote For Jamun Chatpata")

with clm2:
    st.header("Mango Jim-Jam")
    
    v2=st.button("Vote For Mango Jim-Jam")

if v1:
    st.success("You Have Voted For Jamun Chatpata")
else:
     st.success("You Have Voted For Mango Jim-Jam")



st.sidebar.title("Bar Island's Sidebar")

n=st.sidebar.number_input('How Many Drinks Would You LIke To Order !',min_value=1,max_value=15,step=1)

m=st.sidebar.text_input("Enter Your Name")

o=st.sidebar.selectbox("Select Your Favourite Drink",["Mojito","Jamun Chatpata","Mango Jim-Jam"])

st.write(f"Thank YOU {m} for your order of {n} drinks, your favourite drnks is {o} .we will prepared it for you shortly !!!" )

with st.expander("Instuction For Drinks "):
    st.write("1.select my  base drink  as fresh as new")
    st.write("2.Use Falvour as per your choice" )
    st.write("3.Drink should not be to chill and must not be at room temperatures")