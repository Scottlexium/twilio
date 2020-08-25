from flask import Flask
from twilio.twiml.voice_receive import VoiceResponse


app = Flask(_name_)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
resp = VoiceResponse()

resp.say("Hello From Scott Lexium!")
return str(resp)

if _name_ == "_main_":
    app.run(debug=True)
