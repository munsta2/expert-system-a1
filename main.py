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
        print(event)
        if event in (None, 'Exit'):
            break
        elif event in 'Next':
            print("I am happening")
            window[f'-COL{layout}-'].update(visible=False)
            layout+=1
            window[f'-COL{layout}-'].update(visible=True)
            print(layout)
        elif event in "Back":
            window[f'-COL{layout}-'].update(visible=False)
            layout-=1
            window[f'-COL{layout}-'].update(visible=True)
        elif event in "Enter":
            infrence_engine(knowledge_base,values)

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
    year = ["First","Second","Third","Fourth"]
    text = [[sg.Text('What year are you in?')]]
    radio_buttons = [[sg.Radio(x,1,key=x) for x in year]]

    return text + radio_buttons

def fav_prof_window():
    prof_list = ["Amr","Passi","Chris","Mark","Gerwal","Czapor"]

    layout = [[sg.Text('Who is your favourite Professor?')],
           *[[sg.Radio(x,2,key=x) for x in prof_list]]
    ]

    return layout

def infrence_engine(knowledge_base,values):
    print("lol get rekt")
if __name__ == '__main__':
    main()
