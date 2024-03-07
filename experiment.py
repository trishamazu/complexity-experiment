from psychopy import gui, data
import os

# Create a dialog box
info = {'Participant Name': ''}
dlg = gui.DlgFromDict(dictionary=info, title='Experiment')

# Check if the user pressed OK and the name field is not empty
if dlg.OK and info['Participant Name']:
    participant_name = info['Participant Name']
else:
    print("User cancelled or did not enter a name.")
    # Optionally, you can exit the experiment here if no name is provided
    # core.quit()

# Save the participant's name to a file
# Define the filename and path
filename = os.path.join('data', participant_name + '_data.csv')

# Using 'with' ensures the file is properly closed after writing
with open(filename, 'w') as file:
    file.write('Participant Name\n')
    file.write(f'{participant_name}\n')

print(f"Participant's name saved to {filename}")
