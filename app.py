import streamlit as st 
import conversion 
import conversions_rates

st.title("✨Unit Converter✨")

conversion_type = st.selectbox("Select the type of conversion : ",["Lenght","Weight","Area","Time","Speed","Temperature"])

if conversion_type == "Lenght" :
   from_unit = st.selectbox("From",list(conversions_rates.length_conversion.keys()))
   to_unit = st.selectbox("To",list(conversions_rates.length_conversion.keys()))
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.unit_conversion(value,from_unit,to_unit,conversions_rates.length_conversion)
     st.success(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_type == "Weight" :
   from_unit = st.selectbox("From",list(conversions_rates.weight_conversion.keys()))
   to_unit = st.selectbox("To",list(conversions_rates.weight_conversion.keys()))
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.unit_conversion(value,from_unit,to_unit,conversions_rates.weight_conversion)
     st.success(f"{value} {from_unit} = {result} {to_unit}")  

elif conversion_type == "Area" :
   from_unit = st.selectbox("From",list(conversions_rates.area_conversion.keys()))
   to_unit = st.selectbox("To",list(conversions_rates.area_conversion.keys()))
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.unit_conversion(value,from_unit,to_unit,conversions_rates.area_conversion)
     st.success(f"{value} {from_unit} = {result} {to_unit}")  

elif conversion_type == "Time" :
   from_unit = st.selectbox("From",list(conversions_rates.time_conversion.keys()))
   to_unit = st.selectbox("To",list(conversions_rates.time_conversion.keys()))
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.unit_conversion(value,from_unit,to_unit,conversions_rates.time_conversion)
     st.success(f"{value} {from_unit} = {result} {to_unit}")        

elif conversion_type == "Speed" :
   from_unit = st.selectbox("From",list(conversions_rates.speed_conversion.keys()))
   to_unit = st.selectbox("To",list(conversions_rates.speed_conversion.keys()))
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.unit_conversion(value,from_unit,to_unit,conversions_rates.speed_conversion)
     st.success(f"{value} {from_unit} = {result} {to_unit}")        

elif conversion_type == "Temperature" :
   from_unit = st.selectbox("From",["Celsius","Fahrenheit","Kalvin"])
   to_unit = st.selectbox("To",["Celsius","Fahrenheit","Kalvin"])
   value= st.number_input("Enter value",min_value=0.0,format="%.2f")
   if st.button("Convert"):
     result =conversion.convert_temperature(value,from_unit,to_unit)
     st.success(f"{value} {from_unit} = {result} {to_unit}")          

st.write("Created By GIAIC Student : Syed Shurem Ali 🖤")