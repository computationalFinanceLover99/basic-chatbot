#libraries
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

####     BACKEND    ####

# llm initialization 
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key="AIzaSyD5_PsP5cbWOjKDHf0uBrNFn-txyXImlKY"
)

# memory 
memory = ConversationBufferMemory()

#conversation chain
chatbot = ConversationChain(llm=llm, memory=memory)

####    FRONTEND   ####

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["Post"])
def get_response():
    user_input = request.form["message"]
    reply = chatbot.predict(input=user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

#convo loop
""" print("chatbot. (type 'exit' to quit)\n")

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("exiting...")
        break
    
    response = chatbot.predict(input=user_input)
    print("bot: ", response) """
    

