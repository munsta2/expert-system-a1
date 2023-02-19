import pandas as pd
import PySimpleGUI as sg


def main():

    knowledge_base = pd.read_csv("course knowledgebase.csv")
    last_layout = [
        [sg.Text("press Enter to submit questions")],
        [sg.Button("Enter")]
    ]

    layout = [
        
        [
        sg.Column(into_window(), key='-COL0-'),
        sg.Column(year_input_window(),visible=False, key='-COL1-'), 
        sg.Column(fav_prof_window(), visible=False, key='-COL2-'), 
        sg.Column(difculty_window(),visible=False,key='-COL3-'),
        sg.Column(workload_window(),visible=False,key='-COL4-'),
        sg.Column(last_layout, visible=False, key='-COL5-'),],
        [sg.Button("Back"),sg.Button('Next'), sg.Button('Exit')]
    ]
    window = sg.Window('ES for selecting Computer science course', layout,finalize=True,element_justification='c')
    window.TKroot.minsize(200,100)
    window['Back'].update(disabled=True)
    layout = 0
    while True:

        event, values = window.read()
        # print(event)
        if event in (None, 'Exit'):
            break
        elif event in 'Next':
            window[f'-COL{layout}-'].update(visible=False)
            layout+=1
            window[f'-COL{layout}-'].update(visible=True)
            # print(layout)
        elif event in "Back":
            window[f'-COL{layout}-'].update(visible=False)
            layout-=1
            window[f'-COL{layout}-'].update(visible=True)
        elif event in "Enter":

            print(values)
            knowledge_base,explanation = infrence_engine(knowledge_base,values)



            sg.popup_non_blocking(' , '.join(knowledge_base),explanation)
            knowledge_base = pd.read_csv("course knowledgebase.csv")
            
        if layout == 0:
            window['Back'].update(disabled=True)
        else:
            window['Back'].update(disabled=False)

        if layout >= 5:
            window['Next'].update(disabled=True)
        else:
            window['Next'].update(disabled=False)
    window.close()
   
def into_window():
    return [[sg.Text('Welcome to our Expert System to determine which course you should !')]]

def year_input_window():
    year = ["first","second","third","fourth"]
    text = [[sg.Text('What year are you in?')]]
    radio_buttons = [[sg.Radio(x,1,key=x, default=1) for x in year]]

    return text + radio_buttons

def difculty_window():
    difculty = ["easy","challenging","difficult"]
    text = [[sg.Text("What level of difficulty do you enjoy in your courses?")]]
    radio_buttons = [[sg.Radio(x,3,key=x,default=1) for x in difculty]]
    return text + radio_buttons

def workload_window():
    workload = ["low","medium","high"]
    text = [[sg.Text("What level of workload do you enjoy in your courses?")]]
    radio_buttons = [[sg.Radio(x,4,key=x,default=1) for x in workload]]
    return text + radio_buttons

def fav_prof_window():
    prof_list = ["Amr","Passi","Mangiardi","Mark","Gerwal","Czapor","Armstrong","Armstrong","Koczkodaj","Mayer"]

    layout = [[sg.Text('Who is your favourite Professor?')],
           *[[sg.Radio(x,2,key=x, default=2) for x in prof_list]]
    ]

    return layout

def infrence_engine(knowledge_base,values):

    target_key = False

    temp_dict = {}
    for k,v in values.items():
        if v != target_key:
            temp_dict[k] = v
    values = list(temp_dict.keys())
    print(values)
    search_list = ["year","professor","difficulty","workload"]
    used_values = []

    for i in range(len(search_list)):
        print("ahhhhhh", i)
        temp_df = knowledge_base.query("{} == '{}'".format(search_list[i],values[i]))
        print(temp_df)
        if temp_df.empty:
            used_values.append(None)
        else:
            used_values.append(values[i])
            knowledge_base = temp_df

        # print(knowledge_base)
    return knowledge_base['course name'].tolist(), explanation_engine(used_values)

def explanation_engine(values):
    print(values)
    intro = "We choose this class for you for the following reasons: \n"
    year = "Your currently in {} year \n".format(values[0])
    prof = "Your favourite profssor is {} \n".format(values[1]) if values[1] != None else ""
    difficulty = "you enjoy a course that is {}\n".format(values[2]) if values[2] != None else ""
    workload = "you enjoy a course with a {} amount of workload \n".format(values[3]) if values[3] != None else ""
    return intro + year + prof + difficulty + workload



if __name__ == '__main__':
    main()


