from psychopy import core, visual, event, gui, data, clock
import random
import string
import pandas as pd
import numpy as np
import os

def countdown(win, event_text, action):
    countdown_text = visual.TextStim(win, text="", color="black", pos=(0, 0))
    for i in range(3, 0, -1):
        countdown_text.setText(f"{event_text} will {action} in: " + str(i))
        countdown_text.draw()
        win.flip()
        core.wait(1)
def generate_ID(length=6):
    ID = ""
    for _ in range(length):
        element = random.choice(random.choice([string.ascii_letters, string.digits]))
        ID += element
    return ID
def consent(win, ID):
    consent_message_1 = visual.TextStim(win, text="Your consent is needed to proceed.", color="black", pos=(0, 0.5), bold=True)
    consent_message_2 = visual.TextStim(win, text="Press 'Y' to accept the conditions or 'N' to deny approval.", color="black", pos=(0, 0))
    consent_message_3 = visual.TextStim(win, text="To see full condition form press 'C'.", color="black", pos=(0, -0.5))
    ID_msg = visual.TextStim(win, text=f"Your participant ID is {ID}", color="black", pos=(0.7, 0.85), height=0.05)
    consent_message_1.draw()
    consent_message_2.draw()
    consent_message_3.draw()
    ID_msg.draw()
    win.flip()
    consent_keys = event.waitKeys(keyList=["y", "n", "c"])
    
    if "y" in consent_keys:
        approved_consent = visual.TextStim(win, text="You have given your consent.", color="black", pos=(0, 0))
        approved_consent.draw()
        win.flip()
        core.wait(3)
    elif "n" in consent_keys:
        denied_consent = visual.TextStim(win, text="You have not given your consent. Therefore, you will exit this experiment.", color="black", pos=(0, 0))
        denied_consent.draw()
        win.flip()
        core.quit()
    elif "c" in consent_keys:
        consent_title_1 = visual.TextStim(win, text="Influence of Artificial Intelligence and Human Feedback on Decision Making: a Mouse Tracking Perspective.", color="black", italic=True, pos=(0, 0.65), height=0.06)
        consent_title_2 = visual.TextStim(win, text="CONSENT FORM", color="black", bold=True, pos=(0, 0.8))
        consent_information_1 = visual.TextStim(win, text="I hereby confirm that I have voluntarily signed up for this experiment and that I am fully aware of and agree with the purpose of the experiment and conditions that this entails, which are the following:1) The data collected from participants will always be anonimized and their personal identities will never be at risk.\n2) The data collected will be strictly used for scientific purposes and will never be shared for other purposes.\n3) Participants may withdraw their consent at any time as this experiment is completely voluntary.\n\nThis experiment will be carried out by Alex Presa Hughes (202409807@post.au.dk).", color="black", pos=(0, -0.3), height=0.05, wrapWidth=1.5)
        consent_information_2 = visual.TextStim(win, text="Press 'space' to return to consent screen.", color="black", bold=True, pos=(0, -0.75))
        consent_information_3 = visual.TextStim(win, text="The purpose of this experiment is to analyse the influence of AI (and differently programmed AI) when people are faced with moral decision-making- There are three conditions: a control condition where baseline performance (no recommendation is shown) and two versions of an AI condition. This experiment employs mouse-tracking capabilities. Participants' information (age and gender), reaction times and mouse-tracking data will be collected. There are not any known risks to this experiment. Participation is voluntary and consent may be withdrawn at any time.", color="black", height=0.05, pos=(0, 0.35), wrapWidth=1.5)
        consent_information_4 = visual.TextStim(win, text="In this experiment, there are 15 trials and three conditions. In each round, you will be shown two options on screen. You will have to choose one. Then, depending on the condition, there will be no feedback, AI feedback or human feedback. You will then see the same two options and choose one of the two again.", color="black", height=0.05, pos=(0, 0.1), wrapWidth=1.5)
        au_logo = visual.ImageStim(win, image="C:/Users/Alex Presa Hughes/Pictures/RandomPhotos/aarhus-university.png", pos=(-0.75, -0.75))
        consent_title_1.draw()
        consent_title_2.draw()
        consent_information_1.draw()
        consent_information_2.draw()
        consent_information_3.draw()
        consent_information_4.draw()
        au_logo.size = 0.3
        au_logo.draw()
        win.flip()
        event.waitKeys()
        consent_message_after_condition = visual.TextStim(win, text="Press 'Y' to accept the conditions or 'N' to deny approval.", color="black", pos=(0, 0))
        consent_message_after_condition.draw()
        win.flip()
        consent_keys = event.waitKeys(keyList=["y", "n"])
        if "y" in consent_keys:
            approved_consent = visual.TextStim(win, text="You have given your consent.", color="black", pos=(0, 0))
            approved_consent.draw()
            win.flip()
            core.wait(3)
        elif "n" in consent_keys:
            denied_consent = visual.TextStim(win, text="You have not given your consent. Therefore, you will exit this experiment.", color="black", pos=(0, 0))
            denied_consent.draw()
            win.flip()
            core.wait(3)
            core.quit()
def welcome(win):
    message = visual.TextStim(win, text="Welcome to this experiment!", color="black", pos=(0, 0.2))
    smiley_face = visual.ImageStim(win, image="C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cog_Sci_Projects/images/Screenshot 2025-11-12 135851.png", pos=(0, -0.2), size=(0.1, 0.175))
    message.draw()
    smiley_face.draw()
    win.flip()
    core.wait(5)
    message = visual.TextStim(win, text="What you need to know before starting:\n\nIn each round, you are hypothetically a solider in an army faced against different dilemmas. You will read war-themed dilemmas and then you will have two options (attack or no attack) on the screen. You will start at the fixation cross and use the mouse to choose one of them. You have 3 seconds for each choice.\nEach round has two choices:\nFirst choice: Move the mouse from the starting point and click the option you prefer.\nThere will then be a feedback round with 3 possibilities: 1) no advice, 2) advice from AI (type 1) or 3) advice from AI (type 2).\nYou then will choose one of the two options again.", color="black", pos=(0, 0), height=0.07)
    message_2 = visual.TextStim(win, text="Press any key to continue.", pos=(0, -0.8), bold=True, color="black")
    message.draw()
    message_2.draw()
    win.flip()
    event.waitKeys()
def collect_data(): 
    dialog = gui.Dlg(title="Basic information", pos=(0, 0), size=(800, 600)) 
    dialog.addField("Age", label="Age:") 
    dialog.addField("Gender", label="Gender:", choices=["Female", "Male", "Other"]) 
    ok_data = dialog.show() 
    if ok_data is None: 
        core.quit() 
    participant_info = {"Age": ok_data[0], "Gender": ok_data[1]} 
    return participant_info
def experiment(win, link, ID, participant_info):
    df = pd.read_csv(link)
    df_sample = df.sample(n = 15, random_state = None).reset_index(drop = True)
    
    mouse = event.Mouse(win)
    clock = core.Clock()
    start_pos = (0, -0.5)
    time_limit = 5
    mouse.setPos(start_pos)
    Trial = 0
    data = []

    message = visual.TextStim(win, text="Remember that you will only have 3 seconds to choose an option", 
                             bold=True, color="black", pos=(0, 0))
    message.draw()
    win.flip()
    core.wait(3)

    for index, row in df_sample.iterrows():
        # Assuming Option 1 is "Attack" and Option 2 is "No Attack"
        col1 = row["Option 1"]  # This should be "Attack" or attack-related action
        col2 = row["Option 2"]  # This should be "No Attack" or peaceful action
        situation = row["situation"]
        
        # Randomize side assignment for first choice
        if np.random.rand() < 0.5:
            pos1 = (0.5, 0.3)
            pos2 = (-0.5, 0.3)
            side_assignment_1 = "Option1_right"
        else:
            pos1 = (-0.5, 0.3)
            pos2 = (0.5, 0.3)
            side_assignment_1 = "Option1_left"

        # Random condition (1 = no AI, 2 = conservative AI, 3 = aggressive AI)
        condition = np.random.choice([1, 2, 3])
        
        # Get explanations based on condition
        if condition == 1:  # Control - no AI
            reco1 = None
            reco2 = None
        elif condition == 2:  # Conservative AI - recommends NO ATTACK
            reco1 = row["Explanation_conservative"]
            reco2 = row["Explanation_conservative"]
        else:  # condition == 3: Aggressive AI - recommends ATTACK
            reco1 = row["Explanation_aggressive"]
            reco2 = row["Explanation_aggressive"]

        # Create stimuli
        msg_1 = visual.TextStim(win, text=col1, pos=pos1, color="black", height=0.05, wrapWidth=0.4) 
        rect_1 = visual.Rect(win, width=0.5, height=0.5, pos=pos1, fillColor=None, lineColor="black")
        msg_2 = visual.TextStim(win, text=col2, pos=pos2, color="black", height=0.05, wrapWidth=0.4)
        rect_2 = visual.Rect(win, width=0.5, height=0.5, pos=pos2, fillColor=None, lineColor="black")
        starting_point = visual.TextStim(win, text="+", pos=start_pos, color="black")

        Trial += 1
        
        # Show trial number
        trial_number = visual.TextStim(win, text=f"Next round is round {Trial}", color="black", pos=(0, 0))
        trial_number.draw()
        win.flip()
        core.wait(4)
        
        countdown(win, "Round", "begin")
        
        # Show situation
        situation_text = visual.TextStim(win, text=situation, color="black", pos=(0, 0), wrapWidth=1.5)
        message = visual.TextStim(win, text="After reading, press any key to continue.", 
                                  color="black", bold=True, pos=(0, -0.8))
        situation_text.draw()
        message.draw()
        win.flip()
        event.waitKeys()
        
        countdown(win, "Dilemma choice selection", "appear")

        # ========== FIRST CHOICE ==========
        Trajectory_1 = []
        selected = False
        RT_1 = None
        Choice_1 = None
        num_clicks_1 = 0
        mouse.setPos(start_pos)
        clock.reset()

        while not selected:
            # Get mouse position and time FIRST
            pos = mouse.getPos()
            t = clock.getTime()
            Trajectory_1.append((float(t), float(pos[0]), float(pos[1])))
            
            # Draw everything
            rect_1.draw()
            rect_2.draw()
            msg_1.draw()
            msg_2.draw()
            starting_point.draw()
            win.flip()

            # Check for timeout
            if t >= time_limit:
                Choice_1 = "Timeout"
                RT_1 = time_limit
                message = visual.TextStim(win, text="You ran out of time.", color="red", bold=True, pos=(0, 0))
                message.draw()
                win.flip()
                core.wait(2)
                break

            # Check for mouse click
            if mouse.getPressed()[0]:
                num_clicks_1 += 1
                if rect_1.contains(mouse):
                    selected = True
                    RT_1 = t
                    Choice_1 = "Attack" if "Attack" in col1 else "Option 1"  # Label as Attack
                elif rect_2.contains(mouse):
                    selected = True
                    RT_1 = t
                    Choice_1 = "No Attack" if "No Attack" in col2 else "Option 2"  # Label as No Attack

        # ========== HANDLE FIRST CHOICE TIMEOUT ==========
        if Choice_1 == "Timeout":
            # Save timeout trial and move to next
            trial_data = {
                "ID": ID,
                "Trial": Trial,
                "Condition": condition,
                "Condition_Name": {1: "control", 2: "conservative_AI", 3: "aggressive_AI"}[condition],
                "Situation": situation,
                "Option_Attack": col1,  # This is the Attack option
                "Option_No_Attack": col2,  # This is the No Attack option
                "Side_Assignment_1": side_assignment_1,
                "Side_Assignment_2": None,
                "RT_1": RT_1,
                "Choice_1": Choice_1,
                "num_clicks_1": num_clicks_1,
                "Trajectory_1": Trajectory_1,
                "RT_2": None,
                "Choice_2": None,
                "num_clicks_2": None,
                "Trajectory_2": None,
                "start_pos": start_pos,
                "EndPos_1": Trajectory_1[-1][1:] if Trajectory_1 else None,
                "MaxDevX_1": max(abs(p[1]) for p in Trajectory_1) if Trajectory_1 else None,
                "MaxDevY_1": max(abs(p[2]) for p in Trajectory_1) if Trajectory_1 else None,
                "PathLength_1": sum(((Trajectory_1[i+1][1] - Trajectory_1[i][1])**2 + (Trajectory_1[i+1][2] - Trajectory_1[i][2])**2)**0.5 
                                  for i in range(len(Trajectory_1)-1)) if len(Trajectory_1) > 1 else None,
                "NumSamples_1": len(Trajectory_1),
                "EndPos_2": None,
                "MaxDevX_2": None,
                "MaxDevY_2": None,
                "PathLength_2": None,
                "NumSamples_2": None,
                "AI_Recommendation": None,
                "Changed_Mind": None,
                "Followed_AI": None
            }
            trial_data.update(participant_info)
            data.append(trial_data)
            continue

        # ========== SHOW FEEDBACK/CONDITION ==========
        if condition == 1:  # Control - no AI
            robot_img = visual.ImageStim(win, image="C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cog_Sci_Projects/images/Screenshot 2025-12-08 142651.png", pos=(0, -0.2), size=(0.2, 0.3))
            wait_text = visual.TextStim(win, text="...", color="gray", pos=(0, 0.4))
            wait_text.draw()
            robot_img.draw()
            win.flip()
            core.wait(1.5 + random.uniform(0, 1))
            fb_text = visual.TextStim(win, text="No ChatGPT recommendation available. Continue to final choice.", color="black", pos=(0, 0.4))
            message = visual.TextStim(win, text="Press any key to continue", bold=True, color="black", pos=(0, -0.8))
            fb_text.draw()
            robot_img.draw()
            message.draw()
            win.flip()
            event.waitKeys()
            ai_reco = None
        elif condition == 2:  # Conservative AI - ALWAYS recommends NO ATTACK
            ai_reco = col2  # Always recommend No Attack option
            explanation = reco2 if Choice_1 == "Attack" or Choice_1 == "Option 1" else reco1
            show_ai_recommendation(win, ai_reco, explanation)
            
        else:  # condition == 3: Aggressive AI - ALWAYS recommends ATTACK
            ai_reco = col1  # Always recommend Attack option
            explanation = reco1 if Choice_1 == "Attack" or Choice_1 == "Option 1" else reco2
            show_ai_recommendation(win, ai_reco, explanation)

        # ========== SECOND CHOICE ==========
        # Randomize side assignment for second choice
        if np.random.rand() < 0.5:
            pos1_2 = (0.5, 0.3)
            pos2_2 = (-0.5, 0.3)
            side_assignment_2 = "Option1_right"
        else:
            pos1_2 = (-0.5, 0.3)
            pos2_2 = (0.5, 0.3)
            side_assignment_2 = "Option1_left"

        # Create new stimuli for second choice
        msg_1_2 = visual.TextStim(win, text=col1, pos=pos1_2, color="black", height=0.05, wrapWidth=0.4) 
        rect_1_2 = visual.Rect(win, width=0.5, height=0.5, pos=pos1_2, fillColor=None, lineColor="black")
        msg_2_2 = visual.TextStim(win, text=col2, pos=pos2_2, color="black", height=0.05, wrapWidth=0.4)
        rect_2_2 = visual.Rect(win, width=0.5, height=0.5, pos=pos2_2, fillColor=None, lineColor="black")

        Trajectory_2 = []
        selected = False
        RT_2 = None
        Choice_2 = None
        num_clicks_2 = 0
        mouse.setPos(start_pos)
        clock.reset()

        while not selected:
            # Get mouse position and time FIRST
            pos = mouse.getPos()
            t = clock.getTime()
            Trajectory_2.append((float(t), float(pos[0]), float(pos[1])))
            
            # Draw everything
            rect_1_2.draw()
            rect_2_2.draw()
            msg_1_2.draw()
            msg_2_2.draw()
            starting_point.draw()
            win.flip()

            # Check for timeout
            if t >= time_limit:
                Choice_2 = "Timeout"
                RT_2 = time_limit
                message = visual.TextStim(win, text="You ran out of time.", color="red", bold=True, pos=(0, 0))
                message.draw()
                win.flip()
                core.wait(2)
                break

            # Check for mouse click
            if mouse.getPressed()[0]:
                num_clicks_2 += 1
                if rect_1_2.contains(mouse):
                    selected = True
                    RT_2 = t
                    Choice_2 = "Attack" if "Attack" in col1 else "Option 1"
                elif rect_2_2.contains(mouse):
                    selected = True
                    RT_2 = t
                    Choice_2 = "No Attack" if "No Attack" in col2 else "Option 2"

        # ========== SAVE TRIAL DATA ==========
        trial_data = {
            "ID": ID,
            "Trial": Trial,
            "Condition": condition,
            "Condition_Name": {1: "control", 2: "conservative_AI", 3: "aggressive_AI"}[condition],
            "Situation": situation,
            "Option_Attack": col1,
            "Option_No_Attack": col2,
            "Side_Assignment_1": side_assignment_1,
            "Side_Assignment_2": side_assignment_2,
            "RT_1": float(RT_1) if RT_1 else None,
            "Choice_1": Choice_1,
            "num_clicks_1": num_clicks_1,
            "Trajectory_1": Trajectory_1,
            "RT_2": float(RT_2) if RT_2 else None,
            "Choice_2": Choice_2,
            "num_clicks_2": num_clicks_2,
            "Trajectory_2": Trajectory_2,
            "start_pos": start_pos,
            "EndPos_1": Trajectory_1[-1][1:] if Trajectory_1 else None,
            "MaxDevX_1": max(abs(p[1]) for p in Trajectory_1) if Trajectory_1 else None,
            "MaxDevY_1": max(abs(p[2]) for p in Trajectory_1) if Trajectory_1 else None,
            "PathLength_1": sum(((Trajectory_1[i+1][1] - Trajectory_1[i][1])**2 + (Trajectory_1[i+1][2] - Trajectory_1[i][2])**2)**0.5 
                              for i in range(len(Trajectory_1)-1)) if len(Trajectory_1) > 1 else None,
            "NumSamples_1": len(Trajectory_1),
            "EndPos_2": Trajectory_2[-1][1:] if Trajectory_2 else None,
            "MaxDevX_2": max(abs(p[1]) for p in Trajectory_2) if Trajectory_2 else None,
            "MaxDevY_2": max(abs(p[2]) for p in Trajectory_2) if Trajectory_2 else None,
            "PathLength_2": sum(((Trajectory_2[i+1][1] - Trajectory_2[i][1])**2 + (Trajectory_2[i+1][2] - Trajectory_2[i][2])**2)**0.5 
                              for i in range(len(Trajectory_2)-1)) if len(Trajectory_2) > 1 else None,
            "NumSamples_2": len(Trajectory_2),
            # Track AI influence
            "AI_Recommendation": ai_reco,
            "AI_Type": {2: "conservative", 3: "aggressive"}.get(condition, None),
            "Changed_Mind": 1 if Choice_1 != Choice_2 else 0,
            "Followed_AI": 1 if condition != 1 and Choice_2 == ai_reco else 0 if condition != 1 else None,
            "First_Was_Attack": 1 if Choice_1 in ["Attack", "Option 1"] else 0,
            "Second_Was_Attack": 1 if Choice_2 in ["Attack", "Option 1"] else 0
        }
        
        trial_data.update(participant_info)
        data.append(trial_data)
        
        print(f"Trial {Trial}: Condition={condition}, Choice1={Choice_1}, Choice2={Choice_2}, AI={ai_reco[:20] if ai_reco else 'None'}")

    return data
def show_ai_recommendation(win, ai_reco, explanation):
    """Show AI recommendation with typing animation for entire message"""
    robot_img = visual.ImageStim(win, 
        image="C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cog_Sci_Projects/images/Screenshot 2025-12-08 142651.png", 
        pos=(0, -0.2), size=(0.2, 0.3))
    
    # Loading screen
    loading_text = visual.TextStim(win, text="ChatGPT is analyzing...", 
                                   color="gray", pos=(0, 0.4), wrapWidth=1.2)
    message = visual.TextStim(win, text="Please wait until the response has loaded, then press any key to continue.", bold=True, color="black", pos=(0, -0.8))
    loading_text.draw()
    robot_img.draw()
    message.draw()
    win.flip()
    core.wait(1.5 + random.uniform(0, 1))

    # Full message to type out
    full_message = f"ChatGPT recommends '{ai_reco}' because {explanation}"
    typed_message = ""
    
    # Type out the ENTIRE message character by character
    for i, char in enumerate(full_message):
        typed_message += char
        
        # Create text with what's been typed so far
        message_text = visual.TextStim(win, text=typed_message,
                                      color="black", pos=(0, 0.4), 
                                      wrapWidth=1.2)
        
        # Draw everything
        message_text.draw()
        robot_img.draw()
        message.draw()
        win.flip()
        
        # Adjust typing speed
        if char == ' ':
            core.wait(0.03)  # Short pause for spaces
        elif char in ',.:;!?':
            core.wait(0.1)   # Longer for punctuation
        elif char == '\n':
            core.wait(0.05)  # Short pause for line breaks
        else:
            core.wait(0.06 + random.uniform(-0.01, 0.01))  # Natural typing variation
    
    # Brief pause at the end
    core.wait(0.5)
    
    # Wait for key press to continue
    event.waitKeys()
def save_data(data, participant_info):
    """
    Save data to CSV file - ONE ROW PER DILEMMA
    """
    # Filter out None values and ensure all have trial data
    cleaned_data = []
    for trial in data:
        if isinstance(trial, dict) and "ID" in trial:
            # Already has participant info merged in experiment()
            cleaned_data.append(trial)
    
    if not cleaned_data:
        print("No data to save!")
        return
    
    dataframe = pd.DataFrame(cleaned_data)
    
    # Create data folder if it doesn't exist
    folder_path = "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cog_Sci_Projects/no_data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file = os.path.join(folder_path, "Perception_Action_Data_New.csv")
    
    # If file exists, append to it
    if os.path.isfile(file):
        existing_df = pd.read_csv(file)
        dataframe = pd.concat([existing_df, dataframe], ignore_index=True)
    
    # Save to CSV
    dataframe.to_csv(file, index=False)
    print(f"✓ Data saved to {file}")
    print(f"✓ Rows: {len(dataframe)} (One per dilemma)")
    print(f"✓ Columns: {list(dataframe.columns)}")
def farewell(win): 
    farewell_adress = visual.TextStim(win, text="Thank you for participating!\nYou have promoted the field of Cognitive Science.", 
                                     pos=(0, 0), color="black")
    farewell_adress.draw() 
    win.flip() 
    core.wait(3)
def run_experiment():
    # Step 1: Collect participant info
    participant_info = collect_data()
    
    # Step 2: Create window
    win = visual.Window(color="white", fullscr=True)
    
    # Step 3: Generate ID
    ID = generate_ID()
    
    # Step 4: Run experiment
    welcome(win)
    consent(win, ID)
    
    # Step 5: Run trials
    data = experiment(win, 
                     "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cog_Sci_Projects/dilemma_final_experiment_use.csv", 
                     ID, 
                     participant_info)
    
    # Step 6: Save data
    save_data(data, participant_info)
    
    # Step 7: Farewell
    farewell(win)
    core.quit()
if __name__ == "__main__":
    run_experiment()