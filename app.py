import streamlit as st

st.title("Hello World")
st.header("Welcome to my Milk Tea Shop!")

icelevel = st.selectbox(
    'How much ice do you want in your order?',
    ('100%', '50%', 'không đá'))
st.write('You selected:', icelevel)

sugaramount = st.selectbox(
    'How much sugar do you want in your order?',
    ('100%', '70%', '50%'))
st.write('You selected:', sugaramount)

st.subheader("Choose a topping:")
blackboba = st.checkbox('Black boba (7K)')
whiteboba = st.checkbox('White boba (5K)')  
cheesejelly = st.checkbox('Cheese jelly (5K)')

baseprice = 20000


if blackboba:
    b_bobaprice = 7000
else:
    b_bobaprice = 0
if whiteboba:
    w_bobaprice = 5000
else:
     w_bobaprice = 0
if cheesejelly:
    jellyprice = 5000
else:
    jellyprice = 0

toppingprice = b_bobaprice + w_bobaprice + jellyprice
total = baseprice + toppingprice

if st.button("Order"):
    st.write(f'Your bill is {total} VNĐ')