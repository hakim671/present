import streamlit as st
import datetime
import random

# 🎨 Настройки страницы
st.set_page_config(page_title="Для моей принцессы ❤️", page_icon="💌", layout="centered")

# 💖 Заголовок
st.title("💌 Привет, моя любименькая девочка!")
st.markdown("Ты очень дорога для меня. Вот маленький сюрприз только для тебя ❤️")

# 📅 Обратный отсчёт до важной даты
st.subheader("⏳ До нашей особенной даты осталось:")

# 👉 Введи здесь дату (год, месяц, день)
event_date = datetime.datetime(2026, 12, 1, 0, 0, 0)  
now = datetime.datetime.now()
delta = event_date - now

if delta.days >= 0:
    st.write(f"**{delta.days} дней, {delta.seconds // 3600} часов, {(delta.seconds // 60) % 60} минут**")
else:
    st.write("🎉 Наступил наш особенный день! 💖")

# 💬 Список комплиментов / причин
compliments = [
    "Ты делаешь мой мир ярче 🌟",
    "Твоя улыбка — лучшее лекарство 😍",
    "С тобой каждый день особенный 💕",
    "Ты — моя главная мотивация 💪",
    "Я счастлив, что встретил тебя 💖",
    "Ты самая прекрасная девушка во Вселенной ✨",
    "С тобой я чувствую себя живым 🌹"
]

st.subheader("🌸 Получи комплимент 🌸")
if st.button("💝 Нажми меня"):
    st.success(random.choice(compliments))

# 🌟 Немного атмосферы
st.markdown("---")
st.markdown("С любовью, твой ТИГР😁💕")
