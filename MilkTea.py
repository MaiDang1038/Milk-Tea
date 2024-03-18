import streamlit as st
st.title("Trà Sữa")

radio = st.radio('Kích cỡ', ('Nhỏ (30k)', 'Vừa (40K)', 'Lớn (50K)'), horizontal = True)
if radio == 'Nhỏ (30k)':
    size = "Cỡ Nhỏ"
    baseprice = 30
elif radio == 'Vừa (40K)':
    size = "Cỡ Vừa"
    baseprice = 40
else: 
    size = "Cỡ Lớn"
    baseprice = 50

st.text("Thêm")
col1, col2, col3, col4 = st.columns(4)
with col1:
    check1 = st.checkbox('Sữa (5K)')
with col2:
    check2 = st.checkbox('Cà phê (8K)')
with col3:
    check3 = st.checkbox('Kem (10K)')
with col4:
    check4 = st.checkbox('Trứng (15K)')
added = ""
if check1:
    added = "Sữa"
    addedprice = 5
if check2:
    if added != "":
        added += ', Cà phê'
        addedprice += 8
    else:
        added = 'Cà phê'
        addedprice = 8
if check3:
    if added != "":
        added += ', Kem'
        addedprice += 10
    else:
        added = "Kem"
        addedprice = 10
if check4:
    if added != "":
        added += ', Trứng'
        addedprice += 15
    else:
        added = "Trứng"
        addedprice = 15

options = st.multiselect('Topping', ['Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau cau (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'])
topping = ""
for i in options:
    if topping != "":
        topping += ", "+ i
        toppingprice += int(i.split("(")[-1].split("K")[0]) #Lấy giá tiền trong chuỗi
    else:
        topping = i 
        toppingprice = int(i.split("(")[-1].split("K")[0]) #Lấy giá tiền trong chuỗi

amount = st.number_input('Số lượng', value = 1)
textarea = st.text_area('Ghi chú')

order = st.button("Đặt hàng")
if order:
    total = (baseprice + addedprice + toppingprice)*amount
    st.success(f"{size}\n\nThêm: {added}\n\nTopping: {topping}\n\n{textarea}\n\nSố lượng: {amount}\n\nThành tiền: {str(total)}K")

    