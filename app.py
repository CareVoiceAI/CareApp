from flask import Flask, render_template, request
from response import *
from memory import *




app = Flask(__name__)


memory = Memory([])
memory.add_system_message(system_prompt("Dr. Patil"))
memory.add_doctor_message('''Introduction session and intial information . 
                          Ask patient as many questions you can to guage the intial situation and 
                          level of emergency on patients side .
                          End the conversation with thank you when enough 10-15 questions are asked.''')
memory.add_assistant_message('''Can you please state your name and age for the record?''' )
# Define the default route to return the index.html file



@app.route("/")
def home():
    return render_template("index.html",)



@app.route("/assistant")
def assistant():
    memory.print_chat()
    chats=memory.get_chats()
    return render_template("assistant.html",doctor_name="DR.Patil",chats=chats)


@app.route("/doctor")
def doctor():
    return render_template("doctor.html",doctor_name="DR.Patil")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    # print(message)
    
    chats=memory.add_patient_message(message)
    # memory.print_chat()
    resp=get_response(chats)
    # print(resp)
    chats=memory.add_assistant_message(resp['content'])
    return resp
    
@app.route("/summary", methods=["GET"])
def summary():
    chats=memory.get_chats()
    summary=get_summary(chats)

    return summary

if __name__=='__main__':
    app.run()

