from random import choice
from databases import get_images
from simpleutilz.simpleColours import hex_to_colour
import pandas as pd

def generating_outfits_without_quizans(username, prompt):
    possible_combinations = ["T-shirt and Trousers", "T-shirt and Skirt", "T-shirt and Shorts", "Dress", "Jacket and Trousers", "Jacket and Skirt", "Jacket and Shorts", "Hoodie and Trousers", "Hoodie and Skirt", "Hoodie and Shorts"]
    actual_choice = choice(possible_combinations)
    possible_prompts = keyword_checker(prompt)
    colours = None
    if possible_prompts != None:
        colours = hex_to_colour(possible_prompts)
    if actual_choice == "T-shirt and Trousers":
        all_items = get_images(username)
        Trousers = []
        Tshirt = []
        return_Tshirt = ""
        for item in all_items:
            if item[2] =="T-shirt":
                Tshirt.append(item)
            elif item[2] == "Trousers":
                Trousers.append(item)
        if Trousers == [] or Tshirt == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Tshirt = choice(Tshirt)
        else:
            for item in Tshirt:
                if hex_to_colour(item[3]) == colours:
                    return_Tshirt = item
            if return_Tshirt == "":
                return_Tshirt = choice(Tshirt)

        return_Trousers = choice(Trousers)
        outfit = []
        outfit.append(return_Tshirt)
        outfit.append(return_Trousers)
        return outfit
    if actual_choice == "T-shirt and Skirt":
        all_items = get_images(username)
        Skirt = []
        Tshirt = []
        return_Tshirt = ""
        for item in all_items:
            if item[2] =="T-shirt":
                Tshirt.append(item)
            elif item[2] == "Skirt":
                Skirt.append(item)
        if Tshirt == [] or Skirt == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Tshirt = choice(Tshirt)
        else:
            for item in Tshirt:
                if hex_to_colour(item[3]) == colours:
                    return_Tshirt = item
            if return_Tshirt == "":
                return_Tshirt = choice(Tshirt)

        return_Tshirt = choice(Tshirt)
        return_Skirt = choice(Skirt)
        outfit = []
        outfit.append(return_Tshirt)
        outfit.append(return_Skirt)
        return outfit
    if actual_choice == "T-shirt and Shorts":
        all_items = get_images(username)
        Shorts = []
        Tshirt = []
        return_Tshirt = ""
        for item in all_items:
            if item[2] =="T-shirt":
                Tshirt.append(item)
            elif item[2] == "Shorts":
                Shorts.append(item)
        if Shorts == [] or Tshirt == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Tshirt = choice(Tshirt)
        else:
            for item in Tshirt:
                if hex_to_colour(item[3]) == colours:
                    return_Tshirt = item
            if return_Tshirt == "":
                return_Tshirt = choice(Tshirt)
        return_Tshirt = choice(Tshirt)
        return_Shorts = choice(Shorts)
        outfit = []
        outfit.append(return_Tshirt)
        outfit.append(return_Shorts)
        return outfit
    if actual_choice == "Dress":
        all_items = get_images(username)
        Dress = []
        return_Dress = ""
        for item in all_items:
            if item[2] =="Dress":
                Dress.append(item)
        if Dress == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Dress = choice(Dress)
        else:
            for item in Dress:
                if hex_to_colour(item[3]) == colours:
                    return_Dress = item
            if return_Dress == "":
                return_Dress = choice(Dress)
        return_Dress = choice(Dress)
        outfit = []
        outfit.append(return_Dress)
        return outfit
    if actual_choice == "Jacket and Trousers":
        all_items = get_images(username)
        Trousers = []
        Jacket= []
        return_Jacket = ""
        for item in all_items:
            if item[2] =="Jacket":
                Jacket.append(item)
            elif item[2] == "Trousers":
                Trousers.append(item)
        if Trousers == [] or Jacket == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Jacket = choice(Jacket)
        else:
            for item in Jacket:
                if hex_to_colour(item[3]) == colours:
                    return_Jacket = item
            if return_Jacket == "":
                return_Jacket = choice(Jacket)
        return_Jacket = choice(Jacket)
        return_Trousers = choice(Trousers)
        outfit = []
        outfit.append(return_Jacket)
        outfit.append(return_Trousers)
        return outfit
    if actual_choice == "Jacket and Skirt":
        all_items = get_images(username)
        Skirt = []
        Jacket = []
        return_Jacket = ""
        for item in all_items:
            if item[2] =="Jacket":
                Jacket.append(item)
            elif item[2] == "Skirt":
                Skirt.append(item)
        if Jacket == [] or Skirt == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Jacket = choice(Jacket)
        else:
            for item in Jacket:
                if hex_to_colour(item[3]) == colours:
                    return_Jacket = item
            if return_Jacket == "":
                return_Jacket = choice(Jacket)
        return_Jacket = choice(Jacket)
        return_Skirt = choice(Skirt)
        outfit = []
        outfit.append(return_Jacket)
        outfit.append(return_Skirt)
        return outfit
    if actual_choice == "Jacket and Shorts":
        all_items = get_images(username)
        Shorts = []
        Jacket = []
        return_Jacket = ""
        for item in all_items:
            if item[2] =="Jacket":
                Jacket.append(item)
            elif item[2] == "Shorts":
                Shorts.append(item)
        if Shorts == [] or Jacket == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Jacket = choice(Jacket)
        else:
            for item in Jacket:
                if hex_to_colour(item[3]) == colours:
                    return_Jacket = item
            if return_Jacket == "":
                return_Jacket = choice(Jacket)
        return_Jacket = choice(Jacket)
        return_Shorts = choice(Shorts)
        outfit = []
        outfit.append(return_Jacket)
        outfit.append(return_Shorts)
        return outfit
    if actual_choice == "Hoodie and Trousers":
        all_items = get_images(username)
        Trousers = []
        Hoodie= []
        return_Hoodie = ""
        for item in all_items:
            if item[2] =="Hoodie":
                Hoodie.append(item)
            elif item[2] == "Trousers":
                Trousers.append(item)
        if Trousers == [] or Hoodie == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Hoodie = choice(Hoodie)
        else:
            for item in Hoodie:
                if hex_to_colour(item[3]) == colours:
                    return_Hoodie = item
            if return_Hoodie == "":
                return_Hoodie = choice(Hoodie)
        return_Hoodie = choice(Hoodie)
        return_Trousers = choice(Trousers)
        outfit = []
        outfit.append(return_Hoodie)
        outfit.append(return_Trousers)
        return outfit
    if actual_choice == "Hoodie and Skirt":
        all_items = get_images(username)
        Skirt = []
        Hoodie= []
        return_Hoodie = ""
        for item in all_items:
            if item[2] =="Hoodie":
                Hoodie.append(item)
            elif item[2] == "Skirt":
                Skirt.append(item)
        if Skirt == [] or Hoodie == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Hoodie = choice(Hoodie)
        else:
            for item in Hoodie:
                if hex_to_colour(item[3]) == colours:
                    return_Hoodie = item
            if return_Hoodie == "":
                return_Hoodie = choice(Hoodie)
        return_Hoodie = choice(Hoodie)
        return_Skirt = choice(Skirt)
        outfit = []
        outfit.append(return_Hoodie)
        outfit.append(return_Skirt)
        return outfit
    if actual_choice == "Hoodie and Shorts":
        all_items = get_images(username)
        Shorts = []
        Hoodie= []
        return_Hoodie = ""
        for item in all_items:
            if item[2] =="Hoodie":
                Hoodie.append(item)
            elif item[2] == "Shorts":
                Shorts.append(item)
        if Shorts == [] or Hoodie == []:
            generating_outfits_without_quizans(username,prompt)
        if colours == None:
            return_Hoodie = choice(Hoodie)
        else:
            for item in Hoodie:
                if hex_to_colour(item[3]) == colours:
                    return_Hoodie = item
            if return_Hoodie == "":
                return_Hoodie = choice(Hoodie)
        return_Hoodie = choice(Hoodie)
        return_Shorts = choice(Shorts)
        outfit = []
        outfit.append(return_Hoodie)
        outfit.append(return_Shorts)
        return outfit


def generating_outfits_with_quizans(username, bodytype, colour, combination, style, prompt):
    all_items = get_images(username)
    possible_prompts = keyword_checker(prompt)
    colours = None
    if possible_prompts != None:
        colours = hex_to_colour(possible_prompts)
    print(combination)
    if combination == "T-shirt and trousers":
        top = []
        bottom = []
        return_top = ""
        for item in all_items:
            if item[2] =="T-shirt":
                top.append(item)
            elif item[2] == "Trousers":
                bottom.append(item)
            elif item[2] == "Hoodie":
                top.append(item)
        if top == [] or bottom == []:
            generating_outfits_without_quizans(username,prompt)
        for item in top:
            if hex_to_colour(item[3]) == colour:
                return_top = item
        if colours == None:
            return_top = choice(top)
        else:
            for item in top:
                if hex_to_colour(item[3]) == colours:
                    return_top = item
            if return_top == "":
                return_top = choice(top)
        if return_top == "":
            return_top = choice(top)
        return_bottom = choice(bottom)
        outfit = []
        outfit.append(return_top)
        outfit.append(return_bottom)
        return outfit
    elif combination == "Dress and Heels":
        print(colours)
        both_top_and_bottom = []
        return_both = ""
        for item in all_items:
            if item[2] =="Dress":
                both_top_and_bottom.append(item)
        if both_top_and_bottom == []:
            generating_outfits_without_quizans(username,prompt)
        for item in both_top_and_bottom:
            if hex_to_colour(item[3]) == colour:
                return_both = item
        if colours == None:
            return_both = choice(both_top_and_bottom)
        else:
            for item in both_top_and_bottom:
                print(hex_to_colour(item[3]))
                if hex_to_colour(item[3]) == colours:
                    return_both = item
            if return_both == "":
                return_both = choice(both_top_and_bottom)
        if return_both == "":
            return_both = choice(both_top_and_bottom)
        outfit = []
        outfit.append(return_both)
        return outfit
    if combination == "T-shirt and Skirt":
        top = []
        bottom = []
        return_top = ""
        for item in all_items:
            if item[2] =="T-shirt":
                top.append(item)
            elif item[2] == "Skirt":
                bottom.append(item)
            elif item[2] == "Hoodie":
                top.append(item)
            elif item[2] == "Shorts":
                bottom.append(item)
        if top == [] or bottom == []:
            generating_outfits_without_quizans(username,prompt)
        for item in top:
            if hex_to_colour(item[3]) == colour:
                return_top = item
        if colours == None:
            return_top = choice(top)
        else:
            for item in top:
                if hex_to_colour(item[3]) == colours:
                    return_top = item
            if return_top == "":
                return_top = choice(top)
        if return_top == "":
            return_top = choice(top)
        return_bottom = choice(bottom)
        outfit = []
        outfit.append(return_top)
        outfit.append(return_bottom)
        return outfit

def keyword_checker(keywords):
    data = pd.read_csv("./keywords.csv")
    for index, row in data.iterrows():
        for keyword in keywords.split():
            if keyword in row["Keywords"]:
                return row["Item"]

            
        

