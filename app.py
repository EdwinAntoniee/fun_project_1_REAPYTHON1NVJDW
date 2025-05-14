import streamlit as st

st.set_page_config(page_title="MBTI Finder", page_icon="🧠", layout="wide")

st.image("https://www.icegif.com/wp-content/uploads/2023/12/icegif-940.gif", width=300)
st.title("MBTI Finder")
st.write("Jawablah pertanyaan berikut untuk mengetahui tipe kepribadian MBTI kamu!")

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

name = st.text_input("Masukkan nama kamu:")

if st.button("Mulai Quiz"):
    if name.strip():
        st.session_state.quiz_started = True
        st.session_state.name = name
        st.success(f"Halo, {name}! Ayo kita cari tahu MBTImu!")
    else:
        st.warning("Nama tidak boleh kosong. Silakan masukkan nama kamu terlebih dahulu!")

# Initialize session state variables
if "sesi" not in st.session_state:
    st.session_state.sesi = 1
if "I" not in st.session_state:
    st.session_state.I = 0
if "E" not in st.session_state:
    st.session_state.E = 0
if "N" not in st.session_state:
    st.session_state.N = 0
if "S" not in st.session_state:
    st.session_state.S = 0
if "T" not in st.session_state:
    st.session_state.T = 0
if "F" not in st.session_state:
    st.session_state.F = 0
if "J" not in st.session_state:
    st.session_state.J = 0
if "P" not in st.session_state:
    st.session_state.P = 0

if st.session_state.sesi == 1 and st.session_state.quiz_started:
    st.subheader("Sesi 1: Introvert vs Ekstrovert")

    q1 = st.radio("Kamu lebih suka:", ["Sendirian", "Bersosialisasi"], key="ie_q1")
    q2 = st.radio("Ketika lelah, kamu ingin:", ["Menyendiri", "Ngobrol dengan orang"], key="ie_q2")
    q3 = st.radio("Kamu lebih nyaman dengan:", ["Lingkungan tenang", "Lingkungan ramai"], key="ie_q3")
    q4 = st.radio("Kamu cenderung:", ["Mendengarkan", "Berbicara"], key="ie_q4")
    q5 = st.radio("Saat bertemu orang baru:", ["Butuh waktu menyesuaikan", "Langsung nyambung"], key="ie_q5")

    if st.button("Submit", key="submit_ie"):
        if q1 == "Sendirian": st.session_state.I += 1
        else: st.session_state.E += 1

        if q2 == "Menyendiri": st.session_state.I += 1
        else: st.session_state.E += 1

        if q3 == "Lingkungan tenang": st.session_state.I += 1
        else: st.session_state.E += 1

        if q4 == "Mendengarkan": st.session_state.I += 1
        else: st.session_state.E += 1

        if q5 == "Butuh waktu menyesuaikan": st.session_state.I += 1
        else: st.session_state.E += 1

        if st.session_state.I > st.session_state.E:
            st.success("Kamu lebih cenderung ke Introvert!")
            st.image("https://media4.giphy.com/media/jUwpNzg9IcyrK/giphy.gif", width=250)
        else:
            st.success("Kamu lebih cenderung ke Ekstrovert!")
            st.image("https://media2.giphy.com/media/l41m16me3v2pDJ3Fu/giphy.gif", width=250)
        
        st.session_state.sesi1_submitted = True 

    if st.session_state.get("sesi1_submitted", False):
        if st.button("Lanjut ke Sesi 2"):
            st.session_state.sesi = 2 

if st.session_state.sesi == 2:
    st.subheader("Sesi 2: Intuition vs Sensing")

    q1 = st.radio("Saat belajar, kamu fokus pada:", ["Gambaran besar", "Fakta detail"], key="ns_q1")
    q2 = st.radio("Kamu lebih suka informasi yang:", ["Abstrak & teoritis", "Konkret & nyata"], key="ns_q2")
    q3 = st.radio("Kamu cenderung percaya pada:", ["Intuisi", "Pengalaman"], key="ns_q3")
    q4 = st.radio("Saat mencerna ide, kamu:", ["Membayangkan kemungkinan", "Mencari bukti nyata"], key="ns_q4")
    q5 = st.radio("Kamu lebih suka tugas yang:", ["Kreatif", "Praktis"], key="ns_q5")

    if st.button("Submit", key="submit_ns"):
        if q1 == "Gambaran besar": st.session_state.N += 1
        else: st.session_state.S += 1

        if q2 == "Abstrak & teoritis": st.session_state.N += 1
        else: st.session_state.S += 1

        if q3 == "Intuisi": st.session_state.N += 1
        else: st.session_state.S += 1

        if q4 == "Membayangkan kemungkinan": st.session_state.N += 1
        else: st.session_state.S += 1

        if q5 == "Kreatif": st.session_state.N += 1
        else: st.session_state.S += 1

        if st.session_state.N > st.session_state.S:
            st.success("Kamu lebih cenderung ke Intuition!")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjA3cDFieHE5dDB5dGRkeDdhaGNjeHdrNTN4azhnNGQ3MXF1dXU0ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SIO00WvNcnbSo/giphy.gif", width=250)
        else:
            st.success("Kamu lebih cenderung ke Sensing!")
            st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGZlMXR2ZTh4NnY0eWVlcXJ4eWV0eWdrODQ1MG9seDI3b3lmYWdyYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lxfXcVFaE42By/giphy.gif", width=250)
    
        st.session_state.sesi2_submitted = True 

    if st.session_state.get("sesi2_submitted", False):
        if st.button("Lanjut ke Sesi 3"):
            st.session_state.sesi = 3  

if st.session_state.sesi == 3:
    st.subheader("Sesi 3: Thinking vs Feeling")

    q1 = st.radio("Saat mengambil keputusan:", ["Logika", "Perasaan"], key="tf_q1")
    q2 = st.radio("Kamu menilai orang dari:", ["Objektivitas", "Empati"], key="tf_q2")
    q3 = st.radio("Kamu lebih suka:", ["Adil", "Baik hati"], key="tf_q3")
    q4 = st.radio("Di konflik, kamu:", ["Langsung ke intinya", "Perhatikan perasaan"], key="tf_q4")
    q5 = st.radio("Kamu lebih percaya pada:", ["Kepala", "Hati"], key="tf_q5")

    if st.button("Submit", key="submit_tf"):
        if q1 == "Logika": st.session_state.T += 1
        else: st.session_state.F += 1

        if q2 == "Objektivitas": st.session_state.T += 1
        else: st.session_state.F += 1

        if q3 == "Adil": st.session_state.T += 1
        else: st.session_state.F += 1

        if q4 == "Langsung ke intinya": st.session_state.T += 1
        else: st.session_state.F += 1

        if q5 == "Kepala": st.session_state.T += 1
        else: st.session_state.F += 1

        if st.session_state.T > st.session_state.F:
            st.success("Kamu lebih cenderung ke Thinking!")
            st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnY1NXViNjhwdzNmNGZmaXMzbWZqZTNqZmRraXNldTZlaG95Z2d6NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/a5viI92PAF89q/giphy.gif", width=250)
        else:
            st.success("Kamu lebih cenderung ke Feeling!")
            st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExanplY21wZ3BjMjhxYTg1endsdmI3ZmRlM3N5MjNsNDQ4MmVsNHhoaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xcX8GBuT1JdY10oPFI/giphy.gif", width=250)    

        st.session_state.sesi3_submitted = True 

    if st.session_state.get("sesi3_submitted", False):
        if st.button("Lanjut ke Sesi 4"):
            st.session_state.sesi = 4  

if st.session_state.sesi == 4:
    st.subheader("Sesi 4: Judging vs Perceiving")

    q1 = st.radio("Kamu lebih suka hidup yang:", ["Terencana", "Fleksibel"], key="jp_q1")
    q2 = st.radio("Dalam kerjaan kamu:", ["Ikuti jadwal", "Ikuti mood"], key="jp_q2")
    q3 = st.radio("Kamu lebih nyaman saat:", ["Semua sudah pasti", "Ada opsi terbuka"], key="jp_q3")
    q4 = st.radio("Saat liburan:", ["Rencana detail", "Go with the flow"], key="jp_q4")
    q5 = st.radio("Kamu menyelesaikan tugas:", ["Tepat waktu", "Sering mepet deadline"], key="jp_q5")

    if st.button("Submit", key="submit_jp"):
        if q1 == "Terencana": st.session_state.J += 1
        else: st.session_state.P += 1

        if q2 == "Ikuti jadwal": st.session_state.J += 1
        else: st.session_state.P += 1

        if q3 == "Semua sudah pasti": st.session_state.J += 1
        else: st.session_state.P += 1

        if q4 == "Rencana detail": st.session_state.J += 1
        else: st.session_state.P += 1

        if q5 == "Tepat waktu": st.session_state.J += 1
        else: st.session_state.P += 1

        if st.session_state.J > st.session_state.P:
            st.success("Kamu lebih cenderung ke Judging!")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW9rY3d0dmtqMGczZ2MydHc3d29xcXYybGx4Mm1kd2hyemN5a21tZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/a5viI92PAF89q/giphy.gif", width=250)
        else:
            st.success("Kamu lebih cenderung ke Perceiving!")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGQ2d3k3Z2ZzYmh5bXY1NWNlN2ZvcGJkcmw0Zzl4bDFxZTN2djloMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PDh7vdu40CnhS/giphy.gif", width=250)

        st.session_state.sesi4_submitted = True

    if st.session_state.get("sesi4_submitted", False):
        if st.button("Lihat Hasil MBTImu!"):
            mbti = (
                ("I" if st.session_state.I > st.session_state.E else "E") +
                ("N" if st.session_state.N > st.session_state.S else "S") +
                ("T" if st.session_state.T > st.session_state.F else "F") +
                ("J" if st.session_state.J > st.session_state.P else "P")
            )

            st.balloons()
            st.header(f"Hasil MBTI Kamu: {mbti}")
