import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv('DATABASE_URL'))

@st.cache_data
def load_data():
    query = """
        SELECT 
            w.workout_id,
            w.start_time::date as date,
            w.category,
            e.name,
            e.muscle_group,
            we.set_num,
            we.weight_kg,
            we.reps
        FROM workout_exercises we
        JOIN workouts w ON we.workout_id = w.workout_id
        JOIN exercises e ON we.exercise_id = e.exercise_id
        ORDER BY w.start_time
    """
    return pd.read_sql(query, con=engine)

df = load_data()
st.title('Gym Tracker')
st.dataframe(df)