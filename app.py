import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Occupational Health & Pain Guide", page_icon="🩺", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🩺 Physio Ergonomics Blog")
st.sidebar.caption("Evidence-based self-care for desk workers")

selected_topic = st.sidebar.radio(
    "Select Topic:",
    ["Workplace Ergonomics 101", "Shoulder Impingement", "Wrist Pain & Carpal Tunnel", "Finger Strain & Tendonitis"]
)

# 3. Dynamic Blog Content
if selected_topic == "Workplace Ergonomics 101":
    st.title("🖥️ Desk Setup & Posture Basics")
    st.write("Prevent occupational musculoskeletal disorders before chronic pain sets in.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ideal Ergonomic Checklist")
        st.markdown("""
        * **Monitor Height:** Top third of screen at eye level, arm's length away.
        * **Elbow Angle:** Supported at 90°–100° relative to desk height.
        * **Foot Placement:** Flat on floor or on an angled footrest.
        """)
    with col2:
        st.subheader("Interactive Risk Check")
        time_spent = st.slider("Hours spent typing per day:", 0, 12, 6)
        if time_spent >= 6:
            st.warning("⚠️ High Ergonomic Risk Zone: Take 2-minute upper limb mobility breaks every hour.")
        else:
            st.info("💡 Follow the 20-20-20 rule to reduce eye and neck fatigue.")

elif selected_topic == "Shoulder Impingement":
    st.title("🦴 Desk Worker Shoulder Impingement")
    st.write(
        "Forward-head posture and rounded shoulders reduce the subacromial space, irritating rotator cuff tendons.")

    tab1, tab2 = st.tabs(["Physio Mechanism", "Targeted Exercises"])
    with tab1:
        st.markdown("""
        * **Primary Symptoms:** Pain when reaching overhead or reaching behind the back.
        * **Pathology:** Overactive Pec Minor pulls the scapula forward, inhibiting the Lower Trapezius and Serratus Anterior.
        """)
    with tab2:
        st.success("**Exercise 1:** Scapular Retraction / Wall Slides (3 sets x 10 reps)")
        st.success("**Exercise 2:** Doorway Pectoral Stretch (Hold 30s x 3 reps)")

elif selected_topic == "Wrist Pain & Carpal Tunnel":
    st.title("🖐️ Wrist Pain & Median Nerve Compression")
    st.write("Repetitive wrist extension while typing increases pressure inside the carpal tunnel.")

    st.subheader("Symptom Self-Check")
    s1 = st.checkbox("Numbness/tingling in thumb, index, or middle finger")
    s2 = st.checkbox("Pain worsening at night or upon waking")

    if s1 or s2:
        st.error(
            "Possible Median Nerve Irritation: Consider switching to a vertical ergonomic mouse and maintaining neutral wrist angles.")

    st.subheader("Nerve Gliding Protocol")
    st.markdown("""
    1. Extend elbow and wrist gently with fingers pointing downward.
    2. Hold for 5 seconds; repeat 5 times daily to restore median nerve mobility.
    """)

elif selected_topic == "Finger Strain & Tendonitis":
    st.title("✍️ Finger Joint Strain & Scroll Tendonitis")
    st.write("Continuous mouse clicking and smartphone scrolling overload the flexor tendons of the hand.")

    st.subheader("Hand Care Checklist")
    st.checkbox("Use a vertical mouse to eliminate forearm pronation tension.")
    st.checkbox("Perform tendon glides (straight hand -> claw fist -> full fist).")
    st.checkbox("Apply a warm compress for 10 minutes post-work to relax intrinsic hand muscles.")
