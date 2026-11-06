import html

import streamlit as st


st.set_page_config(page_title="나를 소개합니다", page_icon="🌈", layout="wide")

PROFILE = {
    "name": "구세현",
    "headline": "반가워요! 저를 소개합니다.",
    "intro": "좋아하는 것과 새로운 도전을 차곡차곡 쌓아가는 사람입니다.\n이 문장을 나를 가장 잘 표현하는 소개로 바꿔보세요.",
    "affiliation": "학교 · 학과 · 동아리 또는 직장을 입력하세요",
    "affiliation_detail": "현재 어떤 곳에서 무엇을 하고 있는지 적어보세요.",
    "dream": "나의 꿈을 입력하세요",
    "dream_detail": "그 꿈을 꾸게 된 이유나 앞으로의 목표를 적어보세요.",
    "courses": [
        ("기억에 남는 수업", "무엇을 배우고 어떤 점이 재미있었나요?"),
        ("새롭게 배운 것", "수업이나 활동에서 익힌 기술을 적어보세요."),
        ("다음에 도전할 수업", "앞으로 배우고 싶은 주제를 적어보세요."),
    ],
    "hometown": "고향을 입력하세요",
    "family_home": "본가가 있는 곳을 입력하세요",
    "home_detail": "고향이나 본가에서 좋아하는 풍경, 음식, 추억을 적어보세요.",
    "ideal_type": "나의 이상형을 입력하세요",
    "ideal_detail": "외모보다 성격, 가치관, 함께하고 싶은 순간을 적어도 좋아요.",
    "trips": [
        ("여행지 01", "어디를 여행했는지", "그곳에서 가장 기억에 남는 순간"),
        ("여행지 02", "또 다른 여행지를 입력하세요", "사진처럼 남아 있는 장면을 적어보세요."),
        ("다음 여행", "가보고 싶은 곳", "그곳에서 해보고 싶은 일을 적어보세요."),
    ],
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=Gowun+Dodum&family=Jua&display=swap');

    :root {
        --ink: #27152a;
        --pink: #ff4f98;
        --yellow: #ffe34f;
        --mint: #72dfc1;
        --blue: #70c8ff;
    }

    .stApp {
        color: var(--ink);
        background:
            repeating-linear-gradient(135deg, rgba(255,255,255,.2) 0 2px, transparent 2px 18px),
            linear-gradient(125deg, #fff18a 0%, #fff8ed 42%, #ffc0dc 100%);
        font-family: 'DM Sans', 'Gowun Dodum', sans-serif;
    }
    .block-container { max-width: 1080px; padding-top: 2.8rem; padding-bottom: 4rem; }
    [data-testid="stHeader"] { background: transparent; }
    #MainMenu, footer { visibility: hidden; }
    h1, h2, h3 { color: var(--ink); }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 3.2rem 3.4rem;
        border: 2px solid rgba(39, 21, 42, .12);
        border-radius: 8px;
        background: linear-gradient(112deg, #ffe34f 0%, #ff8db8 52%, #8de9ce 100%);
        box-shadow: 9px 10px 0 rgba(255, 79, 152, .2);
        animation: arrive .7s ease-out both;
    }
    .hero:after {
        content: '';
        position: absolute;
        width: 42%;
        height: 100%;
        top: 0;
        right: 0;
        opacity: .35;
        background: repeating-linear-gradient(135deg, transparent 0 14px, #fff 14px 18px);
        pointer-events: none;
    }
    .eyebrow, .section-kicker {
        font-family: 'DM Sans', sans-serif;
        font-size: .76rem;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
    }
    .hero h1 {
        position: relative;
        z-index: 1;
        margin: .55rem 0 .4rem;
        font-family: 'Jua', 'Gowun Dodum', sans-serif;
        font-size: 3.2rem;
        line-height: 1.18;
    }
    .hero .headline { position: relative; z-index: 1; margin: 0; font-size: 1.16rem; font-weight: 700; }
    .hero .intro { position: relative; z-index: 1; max-width: 650px; margin: 1.1rem 0 0; line-height: 1.85; white-space: pre-line; }
    .hero .name-tag { position: relative; z-index: 1; display: inline-block; margin-top: 1.4rem; padding: .45rem .8rem; border: 1px solid rgba(39,21,42,.35); border-radius: 4px; background: rgba(255,255,255,.48); font-size: .84rem; font-weight: 700; }

    .section-title { margin: 2.5rem 0 1.1rem; }
    .section-title .section-kicker { color: #a52b68; }
    .section-title h2 { margin: .18rem 0 0; font-family: 'Jua', 'Gowun Dodum', sans-serif; font-size: 1.8rem; }
    .info-card, .course-card {
        min-height: 158px;
        padding: 1.25rem 1.35rem;
        border: 1.5px solid rgba(39, 21, 42, .14);
        border-radius: 8px;
        background: rgba(255, 255, 255, .76);
        box-shadow: 4px 5px 0 rgba(39, 21, 42, .07);
        animation: arrive .55s ease-out both;
    }
    .info-card h3, .course-card h3 { margin: .3rem 0 .55rem; font-family: 'Jua', 'Gowun Dodum', sans-serif; font-size: 1.27rem; }
    .info-card p, .course-card p { margin: 0; line-height: 1.75; white-space: pre-line; }
    .info-card .section-kicker, .course-card .section-kicker { color: #a52b68; }
    .accent-yellow { background: linear-gradient(135deg, #fff8bd, rgba(255,255,255,.84)); }
    .accent-pink { background: linear-gradient(135deg, #ffd1e3, rgba(255,255,255,.84)); }
    .accent-mint { background: linear-gradient(135deg, #c8f5e8, rgba(255,255,255,.84)); }
    .course-card { min-height: 175px; border-top: 5px solid var(--pink); }
    .course-card:nth-child(2) { border-top-color: #efbd16; }
    .course-card:nth-child(3) { border-top-color: #31b991; }
    .home-line { margin: .5rem 0; font-weight: 700; }
    .trip-row { display: grid; grid-template-columns: 150px 1fr; gap: 1rem; align-items: center; padding: 1rem 1.2rem; border-bottom: 1px solid rgba(39,21,42,.14); background: rgba(255,255,255,.58); }
    .trip-row:first-of-type { border-radius: 8px 8px 0 0; }
    .trip-row:last-of-type { border-bottom: 0; border-radius: 0 0 8px 8px; }
    .trip-index { color: #a52b68; font-size: .75rem; font-weight: 800; }
    .trip-place { margin: .15rem 0 0; font-family: 'Jua', 'Gowun Dodum', sans-serif; font-size: 1.2rem; }
    .trip-memory { margin: 0; line-height: 1.7; }
    .footer-note { margin-top: 2.5rem; padding: 1rem 0; border-top: 2px solid rgba(39,21,42,.18); font-size: .86rem; font-weight: 700; }
    @keyframes arrive { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 650px) {
        .block-container { padding-top: 1.2rem; }
        .hero { padding: 2rem 1.35rem; }
        .hero h1 { font-size: 2.35rem; }
        .trip-row { grid-template-columns: 1fr; gap: .35rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def safe(value):
    return html.escape(str(value)).replace("\n", "<br>")


def render_card(kicker, title, detail, color):
    st.markdown(
        f"""
        <section class="info-card {color}">
            <div class="section-kicker">{safe(kicker)}</div>
            <h3>{safe(title)}</h3>
            <p>{safe(detail)}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    f"""
    <section class="hero">
        <div class="eyebrow">A LITTLE BIT OF ME · 나의 이야기</div>
        <h1>안녕하세요,<br>{safe(PROFILE['name'])}입니다!</h1>
        <p class="headline">{safe(PROFILE['headline'])}</p>
        <p class="intro">{safe(PROFILE['intro'])}</p>
        <span class="name-tag">🌈 TODAY, I AM GROWING</span>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title"><div class="section-kicker">MY NOW & NEXT</div><h2>지금의 나, 그리고 앞으로</h2></div>',
    unsafe_allow_html=True,
)
affiliation_column, dream_column = st.columns(2, gap="medium")
with affiliation_column:
    render_card("MY PLACE", "나의 소속", PROFILE["affiliation_detail"], "accent-yellow")
with dream_column:
    render_card("MY DREAM", PROFILE["dream"], PROFILE["dream_detail"], "accent-pink")

st.markdown(
    '<div class="section-title"><div class="section-kicker">WHAT I LEARNED</div><h2>내가 들었던 수업</h2></div>',
    unsafe_allow_html=True,
)
course_columns = st.columns(3, gap="medium")
for column, (course_title, course_detail) in zip(course_columns, PROFILE["courses"]):
    with column:
        st.markdown(
            f"""
            <section class="course-card">
                <div class="section-kicker">CLASS NOTE</div>
                <h3>{safe(course_title)}</h3>
                <p>{safe(course_detail)}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="section-title"><div class="section-kicker">ROOTS & HEART</div><h2>나를 이루는 이야기</h2></div>',
    unsafe_allow_html=True,
)
home_column, ideal_column = st.columns(2, gap="medium")
with home_column:
    st.markdown(
        f"""
        <section class="info-card accent-mint">
            <div class="section-kicker">MY HOMETOWN</div>
            <h3>본가와 고향</h3>
            <p class="home-line">고향 · {safe(PROFILE['hometown'])}</p>
            <p class="home-line">본가 · {safe(PROFILE['family_home'])}</p>
            <p>{safe(PROFILE['home_detail'])}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
with ideal_column:
    render_card("MY IDEAL TYPE", PROFILE["ideal_type"], PROFILE["ideal_detail"], "accent-pink")

st.markdown(
    '<div class="section-title"><div class="section-kicker">POSTCARDS</div><h2>내가 여행한 곳</h2></div>',
    unsafe_allow_html=True,
)
for index, (trip_title, destination, memory) in enumerate(PROFILE["trips"], start=1):
    st.markdown(
        f"""
        <div class="trip-row">
            <div><div class="trip-index">TRIP {index:02d}</div><div class="trip-place">{safe(trip_title)}</div></div>
            <p class="trip-memory"><strong>{safe(destination)}</strong><br>{safe(memory)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer-note">만나서 반가워요! ✨ &nbsp; · &nbsp; 더 많은 이야기는 계속됩니다.</div>',
    unsafe_allow_html=True,
)
