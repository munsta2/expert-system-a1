import pandas as pd


def main():

    knowledge_base = pd.read_csv("course knowledgebase.csv")

    print("welcome to our ES for selecting which computer science course you should take at laurentian!")
    user_input = input("Enter next to continue or exit to quit: ")

    



    while user_input != "next" and user_input != 'exit':
         user_input = input("Enter next to continue or exit to quit: ")


    if user_input.lower() == "next":
        
        knowledge_base = year_input(knowledge_base)
        print("---------------------")
        knowledge_base = fav_prof(knowledge_base)
        print("---------------------")

        # knowledge_base = knowledge_base.query("year == '{}'".format(year))
        print(knowledge_base)


def year_input(knowledge_base):
    years = ['first','second','third','fourth']

    year = input("What year are you in? (first,second,third,fourth): ")
    while year not in years:
        year = input(" Please enter a valid year \n What year are you in? (first,second,third,fourth): ")
    knowledge_base = knowledge_base.query("year == '{}'".format(year))
    return knowledge_base

def fav_prof(knowledge_base):
    prof_list = ["Amr","Passi","Chris","Mark","Gerwal","Czapor"]
    print("List of profs: ")
    for item in prof_list:
        print(item)
    user_input = input("Who's your favorite prof? :")

    while user_input not in prof_list:
        user_input = input("please enter valid prof name \n Who's your favorite prof? :")
    knowledge_base = knowledge_base.query("professor == '{}'".format(user_input))
    return knowledge_base



if __name__ == '__main__':
    main()
