import streamlit as st

st.title("Minimal Chat Test")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 過去のやり取りを表示
for role, text in st.session_state["messages"]:
    with st.chat_message(role):
        st.write(text)

# ユーザー入力 (1.26以降で使える)
user_input = st.chat_input("Type your message here...")
if user_input:
    # 履歴にユーザーのメッセージ追加
    st.session_state["messages"].append(("user", user_input))

    # ダミーでAI応答を返す
    reply_text = "これはダミー回答です。"
    st.session_state["messages"].append(("assistant", reply_text))

