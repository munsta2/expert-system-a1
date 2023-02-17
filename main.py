import pandas as pd
import PySimpleGUI as sg


def main():

    knowledge_base = pd.read_csv("course knowledgebase.csv")
    last_layout = [
        [sg.Text("press Enter to submit questions")],
        [sg.Button("Enter")]
    ]

    layout = [[sg.Column(into_window(), key='-COL0-'), sg.Column(year_input_window(), visible=False, key='-COL1-'), sg.Column(fav_prof_window(), visible=False, key='-COL2-'), sg.Column(last_layout, visible=False, key='-COL3-')],
          [sg.Button("Back"),sg.Button('Next'), sg.Button('Exit')]]
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
            knowledge_base,explanation = infrence_engine(knowledge_base,values)



            sg.popup_non_blocking(' , '.join(knowledge_base),explanation)
            knowledge_base = pd.read_csv("course knowledgebase.csv")
            
        if layout == 0:
            window['Back'].update(disabled=True)
        else:
            window['Back'].update(disabled=False)

        if layout >= 3:
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

def fav_prof_window():
    prof_list = ["Amr","Passi","Chris","Mark","Gerwal","Czapor"]

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
    search_list = ["year","professor"]


    for i in range(len(search_list)):

        temp_df = knowledge_base.query("{} == '{}'".format(search_list[i],values[i]))
        
        if temp_df.empty:
            pass
        else:
            knowledge_base = temp_df
    return knowledge_base['course name'].tolist(), explanation_engine(values)

def explanation_engine(values):

    intro = "We choose this class for you for the following reasons: \n"
    year = "Your currently in {} year \n".format(values[0])
    prof = "Your favourite profssor is {} \n".format(values[1])

    return intro + year + prof



if __name__ == '__main__':
    main()


