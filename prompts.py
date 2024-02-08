
def system_prompt(doctor_name):
    message=f'''You are assistant of Dr. {doctor_name}, you will ask patients the expected details from the doctor  .  
    Doctor will order you to ask some details in between make sure you change your questionaire based on that.'''
    return message


def summarise_prompt(content):
    message=f'''TASK - Summarize the dialoge between a doctor, assistant and patient.
        . Dialoge --- || {content} ||
       Rules - 1)Donot mention doctor's instructions to the assistant .
         2)Only summarize patients answers to assistants questions .
         3)Make sure the summary is thorough and the doctor would get complete understanding of patients situation. 
         4)Make sure the summary is pointwise and easy to read and understand.
         '''
    
    return message