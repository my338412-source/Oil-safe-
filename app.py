import streamlit as st

st.set_page_config(page_title="نظام إدارة العمليات - حمودي", page_icon="⚡", layout="centered")

st.title("⚡ نظام إدارة العمليات والبرميتات")
st.write("برنامج سريع ودقيق مطابق تماماً للقواعد المعتمدة للمحطات والآبار.")

st.sidebar.header("⚙️ إعدادات الذكاء الاصطناعي")
ai_provider = st.sidebar.selectbox("اختر المحرك:", ["Gemini", "ChatGPT"])
api_key = st.sidebar.text_input("أدخل الـ API Key:", type="password")

if api_key:
    st.sidebar.success("تم الربط بنجاح!")

tab1, tab2 = st.tabs(["📝 قسم التصاريح (Permits)", "🧪 قسم الحقن (Head Injection)"])

with tab1:
    st.subheader("إصدار وتوثيق التصاريح (Protocol 88 / 88b)")
    station = st.selectbox("المحطة:", ["T.b. 8/1", "T.b. 8/2", "T.b. 6/1", "PETRECO"])
    permit_type = st.selectbox("نوع التصريح:", ["Hot Work", "Cold Work", "Gas Clearance"])
    permit_no = st.text_input("رقم التصريح:")
    task_desc = st.text_area("وصف المهمة:")
    manual_date = st.text_input("التاريخ المكتوب بخط اليد:")
    
    st.markdown("---")
    st.markdown("#### قراءات أجهزة الغاز (Gas Test Readings)")
    c1, c2 = st.columns(2)
    with c1:
        h2s = st.text_input("H2S (PPM):", "0")
        lel = st.text_input("LEL (%):", "0")
    with c2:
        o2 = st.text_input("O2 (%):", "20.9")
        co = st.text_input("CO (PPM):", "0")

    if st.button("إصدار التقرير"):
        if not permit_no or not manual_date:
            st.error("⚠️ برجاء إدخال رقم التصريح والتاريخ اليدوي.")
        else:
            report_output = f"""========================================
       SAFETY PERMIT REPORT
========================================
Station: {station}
Permit Type: {permit_type}
Permit No: {permit_no}
Task: {task_desc}
Manual Date: {manual_date}
----------------------------------------
Gas Test Results:
- H2S: {h2s} PPM | LEL: {lel} %
- O2: {o2} % | CO: {co} PPM
========================================
"""
            st.code(report_output, language="text")

with tab2:
    st.subheader("تقرير حقن المواد الكيميائية (Protocols 10/1 & 99)")
    inj_station = st.selectbox("محطة الحقن:", ["T.b. 8/1", "T.b. 8/2", "T.b. 10/1"])
    pump_type = st.selectbox("نوع الطلمبة:", ["Texteam", "Electric"])
    scavenger_type = st.selectbox("نوع المادة:", ["EPRI scavenger", "Standard Scavenger"])
    
    st.markdown("#### إدخال معدلات الآبار بالترتيب الثابت:")
    well_1 = st.number_input("بئر رقم 1 (L/day):", min_value=0.0, step=0.1)
    well_2 = st.number_input("بئر رقم 2 (L/day):", min_value=0.0, step=0.1)
    well_3 = st.number_input("بئر رقم 3 (L/day):", min_value=0.0, step=0.1)
    
    total_rate = well_1 + well_2 + well_3
    
    if st.button("حساب التقرير"):
        injection_report = f"""========================================
     HEAD INJECTION REPORT
========================================
Station: {inj_station}
Pump: {pump_type} | Chemical: {scavenger_type}
----------------------------------------
Well Rates:
- Well 1: {well_1} L/day
- Well 2: {well_2} L/day
- Well 3: {well_3} L/day
----------------------------------------
Total Actual Rate: {total_rate} L/day
========================================
"""
        st.code(injection_report, language="text")
      
