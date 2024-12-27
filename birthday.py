import streamlit as st
from emoji import emojize
from datetime import date


# Function to play video
def playvideo(video_title):
    try:
        st.markdown(
            f"""
            <iframe width="700" height="394" src="{video_title}" frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
            """,
            unsafe_allow_html=True,
        )
    except Exception as e:
        st.error("Something went wrong. Please contact the developer.")

# Function to ask additional questions
def ask_questions():
    st.subheader("Additional Questions")

    additional_questions = [
        {"question": "Do you want to know how I introduce you to my MOM? CLICK ON YES (Play video)", "video": "https://www.youtube.com/embed/1-PTfDWk_u4"},
        {"question": "Do you want to know how I feel when you're not talking to me?", "video": "https://www.youtube.com/embed/vKbYFos88G0"},
        {"question": "Do you want to know how I feel every time I see you?", "video": "https://www.youtube.com/embed/EIcukYHB0iU"}
    ]

    for i, q in enumerate(additional_questions):
        st.write(f"Question {i + 1}: {q['question']}")
        user_choice = st.radio(
            f"Please select an option for Question {i + 1}:",
            ["No", "Yes"],
            key=f"video_choice_{i}"
        )

        if user_choice == "Yes":
            playvideo(q["video"])
        elif user_choice == "No":
            st.write("Thanks for your confirmation! 😊")
        st.write("---")

# Main function
def main():
    st.title("Romantic App")

    # Prompt user to select a date
    selected_date = st.date_input("Please select a date:", min_value=date(2024, 1, 1))

    # Define the target date
    target_date = date(2024, 12, 30)

    # Check the selected date and display appropriate message or play video
    if selected_date == target_date:
        st.success("The selected date is December 30! Suprise for you PLEASE CLICK THE BELOW LINK AND DOWNLOAD VIDEO")
      # Video file path
        video_file_path = "DR.mp4"  # Replace with the path to your video file


        st.markdown(
    "<h3 style='color: red;'>BE CAREFUL WHILE PLAYING THE VIDEO IF YOU ARE AT HOME</h3>",
    unsafe_allow_html=True,
     )
        # Create a download button for the video
        with open(video_file_path, "rb") as video_file:
            video_bytes = video_file.read()
            st.download_button(
                label="Download Video",
                data=video_bytes,
                file_name="shared_video.mp4",  # The name of the file when downloaded
                mime="video/mp4"
            )
    elif selected_date < target_date:
        st.info("Advance Happy Birthday Nana!")
    else:
        st.warning("The selected date is after December 30. You've missed the big day!")

    # Questions section
    questions = [
        {"question": "You want an item for every year (you wish to buy that every year:)", "answer": "Diary"},
        {"question": "What gift did I give you for the first time?", "answer": "Earrings"},
        {"question": "What do I like in you most?", "answer": "Eyes"},
        {"question": "On Day 1, which color shirt did I wear?", "answer": "Black"}
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0

    col1, col2 = st.columns(2)

    with col1:
        for index, q in enumerate(questions):
            st.subheader(f"Question {index + 1}")
            st.write(q["question"])
            user_answer = st.text_input(f"Your Answer for Question {index + 1}", key=f"answer_{index}")

            if st.button(f"Submit Answer for Question {index + 1}", key=f"submit_{index}"):
                if user_answer.strip().lower() == q["answer"].strip().lower():
                    st.balloons()
                    st.success("Congratulations! Your answer is correct.")
                    st.write("You won points!", emojize(":star-struck:"), emojize(":trophy::confetti_ball:"))
                    if f"answered_{index}" not in st.session_state:
                        st.session_state.score += 1
                        st.session_state[f"answered_{index}"] = True
                else:
                    st.error("Sorry, your answer is incorrect.")
                    st.write("Better luck next time!", emojize(":pensive_face:"))

    with col2:
        st.image("website.png")
    st.markdown(
    "<h3 style='color: blue;'>If your unable to answer any of these questions Try to reach to Developer  Mr.Dwaraka Reddy </h3>",
    unsafe_allow_html=True,
     )

    st.write("---")
    st.markdown(
        f"<h1 style='text-align: center; color: green;'>You won points are: {st.session_state.score}</h1>",
        unsafe_allow_html=True
    )

    st.write("----")
    ask_questions()

if __name__ == "__main__":
    main()
