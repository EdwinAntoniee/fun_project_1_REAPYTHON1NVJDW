import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Mini Quiz App", page_icon="🔍", layout="wide")

# Gambar dan Judul
st.image("https://www.icegif.com/wp-content/uploads/2023/12/icegif-940.gif", width=300)
st.title("Mini Quiz App")
st.write("Penasaran ngga sih tentang profesi yang cocok sama preferensi kamu?")

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

name = st.text_input("Masukkan nama kamu:")

if st.button("Mulai Quiz"):
    if name.strip():
        st.session_state.quiz_started = True
        st.session_state.name = name
        st.success(f"Halo, {name}! Ayo kita cari tahu profesi yang cocok sama kamu!")
    else:
        st.warning("Nama tidak boleh kosong. Silakan masukkan nama kamu terlebih dahulu!")

if st.session_state.quiz_started:
    jawaban1 = st.radio(
        "### Pertanyaan 1: Apa yang paling kamu suka lakukan di waktu luang?",
        ("Coding dong", "Design layout semenarik mungkin", "Analisis data sekaligus tren"),
        key="pertanyaan1"
    )

    jawaban2 = st.radio(
        "### Pertanyaan 2: Device apa nih yang kamu paling suka gunain sehari-hari?",
        ("VS Code", "Figma", "Google Colab"),
        key="pertanyaan2"
    )

    jawaban3 = st.radio(
        "### Pertanyaan 3: Motto hidup kamu?",
        ("Menyelesaikan masalah dengan logika dan efisiensi", "Setiap detail visual punya makna", "Data adalah kunci memahami dunia"),
        key="pertanyaan3"
    )

    if st.button("Kirim", type="primary", key="submit"):
        st.session_state.quiz_submitted = True
        st.session_state.jawaban1 = jawaban1
        st.session_state.jawaban2 = jawaban2
        st.session_state.jawaban3 = jawaban3

if st.session_state.quiz_submitted:
    jawaban1 = st.session_state.jawaban1
    jawaban2 = st.session_state.jawaban2
    jawaban3 = st.session_state.jawaban3

    programmer_score = 0
    designer_score = 0
    datascientist_score = 0

    if jawaban1 == "Coding dong":
        programmer_score += 1
    elif jawaban1 == "Design layout semenarik mungkin":
        designer_score += 1
    elif jawaban1 == "Analisis data sekaligus tren":
        datascientist_score += 1

    if jawaban2 == "VS Code":
        programmer_score += 1
    elif jawaban2 == "Figma":
        designer_score += 1
    elif jawaban2 == "Google Colab":
        datascientist_score += 1

    if jawaban3 == "Menyelesaikan masalah dengan logika dan efisiensi":
        programmer_score += 1
    elif jawaban3 == "Setiap detail visual punya makna":
        designer_score += 1
    elif jawaban3 == "Data adalah kunci memahami dunia":
        datascientist_score += 1

    st.write("### Profesi yang cocok untuk kamu adalah:")

    if programmer_score > designer_score and programmer_score > datascientist_score:
        st.success("Programmer")
        st.write("Programmer adalah orang yang menciptakan perangkat lunak dan aplikasi. Kamu suka memecahkan masalah dengan logika dan efisiensi.")

        follow_up = st.radio(
            "### Pertanyaan lanjutan: Kamu lebih tertarik pada:",
            ("Desain antarmuka yang menarik dan interaktif", "Menjaga operasi website agar tetap lancar dan aman"),
            key="lanjutan_programmer"
        )

        if st.button("Kirim Jawaban Lanjutan", key="jawaban_programmer"):
            st.write("### Kamu sangat cocok menjadi:")
            if follow_up == "Desain antarmuka yang menarik dan interaktif":
                st.success("Front-End Engineer!")
                st.write("Front-End Engineer adalah orang yang fokus pada tampilan dan interaksi aplikasi yang langsung digunakan oleh pengguna. Kamu senang membuat antarmuka yang menarik dan mudah digunakan.")
                st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW5obTUwanE5ZmRxY3QxbHM5dXdkZnc3anZidDNpdWFwMGk5bjgybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bGgsc5mWoryfgKBx1u/giphy.gif", width=300)
            else:
                st.success("Back-End Engineer!")
                st.write("Back-End Engineer bertanggung jawab atas logika dan sistem di balik layar dari sebuah aplikasi. Kamu suka membuat sistem berjalan efisien dan aman.")
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGR6bWNmaXI2OHV2eHViNTk3dDZkdjF0bGc3OGw0MHM3amtnMG9ocCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/78XCFBGOlS6keY1Bil/giphy.gif", width=300)

    elif designer_score > programmer_score and designer_score > datascientist_score:
        st.success("Designer")
        st.write("Designer adalah orang yang menciptakan tampilan visual yang menarik. Kamu percaya bahwa setiap detail visual punya makna.")

        follow_up = st.radio(
            "### Pertanyaan lanjutan: Kamu lebih tertarik pada:",
            ("Desain UI/UX untuk aplikasi dan website", "Branding visual seperti poster dan logo"),
            key="lanjutan_designer"
        )

        if st.button("Kirim Jawaban Lanjutan", key="jawaban_designer"):
            st.write("### Kamu sangat cocok menjadi:")
            if follow_up == "Desain UI/UX untuk aplikasi dan website":
                st.success("UI/UX Designer!")
                st.write("UI/UX Designer merancang pengalaman pengguna dan tampilan antarmuka yang intuitif. Kamu senang menciptakan desain yang tidak hanya estetis, tapi juga fungsional.")
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTc5eGhmOWR5cmIxejVscjM5cW96aWpleWRieHh2czMzems0bjZmbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1k889fiqiZV19HO2sx/giphy.gif", width=300)
            else:
                st.success("Graphic Designer!")
                st.write("Graphic Designer menciptakan elemen visual seperti poster, logo, dan ilustrasi. Kamu memiliki kreativitas tinggi dan mampu mengomunikasikan ide lewat desain visual.")
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTJuaXQ3bm4xNGFyMW5rajk0Nmtxcnd3cTBhY2RuZW5ub252N2cyNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/am8pxddtatQoq3iHhr/giphy.gif", width=300)

    elif datascientist_score > programmer_score and datascientist_score > designer_score:
        st.success("Data Scientist")
        st.write("Data Scientist adalah orang yang menganalisis data untuk menemukan pola dan tren. Kamu percaya bahwa data adalah kunci memahami dunia.")

        follow_up = st.radio(
            "### Pertanyaan lanjutan: Kamu lebih tertarik pada:",
            ("Membuat model prediksi dari data besar", "Menyampaikan insight lewat visualisasi data yang jelas"),
            key="lanjutan_datascientist"
        )

        if st.button("Kirim Jawaban Lanjutan", key="jawaban_datascientist"):
            st.write("### Kamu sangat cocok menjadi:")
            if follow_up == "Membuat model prediksi dari data besar":
                st.success("Machine Learning Engineer!")
                st.write("Machine Learning Engineer membangun sistem cerdas yang bisa belajar dari data. Kamu tertarik pada algoritma dan otomatisasi pengambilan keputusan.")
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZoYWdpbWJnY2hzN2NhNGRrYjAxZHVhZDNwNmV2OG55aWQzemMwYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/iPj5oRtJzQGxwzuCKV/giphy.gif", width=300)
            else:
                st.success("Data Analyst!")
                st.write("Data Analyst bertugas mengolah data dan menyajikannya dalam bentuk yang mudah dimengerti. Kamu suka mencari pola dan insight yang bisa digunakan untuk membuat keputusan.")
                st.image("https://media.giphy.com/media/AXorq76Tg3Vte/giphy.gif?cid=ecf05e47uphc60lrrnx0hryrx50hw3137dt2p3opxn6yfm8k&ep=v1_gifs_search&rid=giphy.gif&ct=g")
    else:
        st.info("Kamu punya minat seimbang di beberapa bidang!")
        st.write("Cobalah eksplorasi lebih dalam untuk menemukan yang paling kamu sukai!")

