# random_fun_facts.py
import streamlit as st
import random

st.title("🎉 Random Fun Facts Generator")

fun_facts = [
    "Honey never spoils 🍯",
    "Octopuses have three hearts 🐙",
    "Bananas are berries, but strawberries aren’t 🍓",
    "There are more stars in the universe than grains of sand on Earth ✨",
    "A group of flamingos is called a 'flamboyance' 🦩"
]

if st.button("Give me a fun fact!"):
    st.success(random.choice(fun_facts))
