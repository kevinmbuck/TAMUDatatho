import tkinter as tk
import csv
import datetime

all_data = []
class justiceGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("An Unsafe America")
        self.frame = tk.Frame(self.root, width=800, height=800)
        self.frame.pack(expand=True, fill='both')
        self.canvas = tk.Canvas(self.frame, width=800, height=800, bg="lightgrey", scrollregion=(0, 0, 800, 1600))
        self.canvas.pack()
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side='right', fill='y')
        self.title = tk.Label(self.root, text="  An Unsafe America  ",
                              fg="white", bg="DodgerBlue4", font="system 55 italic")
        self.canvas.create_window(400, 100, window=self.title)
        
        self.home()
    def home(self):
        data1 = Data()
##        dataYearList = [data1.dateYear["2000"], data1.dateYear["2001"], data1.dateYear["2002"], data1.dateYear["2003"],
##                        data1.dateYear["2004"], data1.dateYear["2005"], data1.dateYear["2006"], data1.dateYear["2007"],
##                        data1.dateYear["2008"], data1.dateYear["2009"], data1.dateYear["2010"], data1.dateYear["2011"],
##                        data1.dateYear["2012"], data1.dateYear["2013"], data1.dateYear["2014"], data1.dateYear["2015"],
##                        data1.dateYear["2016"]]
##        self.canvas.create_rectangle(100, 250, 700, 600, fill = 'darkgrey')
##        self.labelGraphYear = tk.Label(self.canvas, text='Police Killings Per Year 2000-\'16', font = "Arial 16")
##        self.canvas.create_window(400, 265, window = self.labelGraphYear)
##        xGraphYear = 0
##        for num in dataYearList:
##            height = num%10
##            xpos0 = 160 + (xGraphYear * 5) +
##            xpos1 = 
##            ypos0 = (300 - height)+250
##            ypos1 = xpos0 + height
##            self.canvas.create_rectangle(xpos0, ypos0, xpos1, ypos1, fill = 'maroon')
##            xGraphYear += 1
        

class Data:
    def __init__(self):
        self.age = {"age0_10":0, "age11_20":0, "age21_30":0, "age31_40":0, "age41_50":0, "age51_60":0,
                    "age61_up":0, "Unknown":0}
        self.gender = {"Male": 0, "Female": 0, "Other": 0}
        self.race = {"Asian": 0, "Hispanic": 0, "Black": 0, "Native": 0, "Other": 0, "White": 0,
                     "Unknown": 0}
        self.dateYear = {"2000":0, "2001":0, "2002":0, "2003":0, "2004":0, "2005":0, "2006":0,
                         "2007":0, "2008":0, "2009":0, "2010":0, "2011":0, "2012":0, "2013":0, "2014":0,
                         "2015":0, "2016":0}
        self.dateSeason = {"Spring":0, "Summer":0, "Fall":0, "Winter":0}
        # spring = March, April, May
        # summer = June, July, August
        # fall = September, October, November
        # winter = December, January, February
        self.state = {"AL":0, "AK":0, "AZ":0, "AR":0, "CA":0, "CO":0, "CT":0, "DE":0, "FL":0,
                      "GA":0, "HI":0, "ID":0, "IL":0, "IN":0, "IA":0, "KS":0, "KY":0, "LA": 0,
                      "ME":0, "MD":0, "MA":0, "MI":0, "MN":0, "MS":0, "MO":0, "MT":0, "NE":0,
                      "NV":0, "NH":0, "NJ":0, "NM":0, "NY":0, "NC":0, "ND":0, "OH":0, "OK":0,
                      "OR":0, "PA":0, "RI":0, "SC":0, "SD":0, "TN":0, "TX":0, "UT":0, "VT":0,
                      "VA":0, "WA":0, "WV":0, "WI":0, "WY":0, "DC":0}
        self.deathWeapon = {"Shot and Tasered": 0, "Shot": 0, "Tasered": 0}
        self.armed ={"Blunt Object":0, "Blades":0, "Gun":0, "Explosives and Fire":0, "Toy Weapon":0,
                     "Unarmed":0, "Vehicle":0}
        self.bluntObjectList = ["Hammer", "Metal Hand Tool", "Metal Object", "Metal Pipe", "Metal Pole",
                                "Metal Rake", "Metal Stick", "Piece Of Wood", "Pipe", "Pole", "Rock",
                                "Shovel", "Blunt Object", "Brick", "Chain", "Carjack", "Contractor'S Level",
                                "Baton", "Beer Bottle", "Baseball Bat And Fireplace Poker", "Baseball Bat"]
        self.bladesList = ["Knife", "Axe", "Hatchet", "Lawn Mower Blade", "Machete", "Meat Cleaver", "Pick-Axe",
                          "Screwdriver", "Sharp Object", "Straight Edge Razor", "Sword", "Box Cutter",
                          "Bayonet"]
        self.explosivesList = ["Guns And Explosives", "Hand Torch"]
        self.mentalIllness = {"Healthy":0, "Precondition":0}
        self.fleeStatus = {"Flee":0, "Stay":0}
        self.elementsData()
    def elementsData(self):
        #with open("Police Fatalities copy.csv") as f:
        #   self.read_f = csv.reader(f)
        #   self.elementsData()
        f = open("Police Fatalities copy.csv", "r")
        read_f= csv.reader(f)
        for row in read_f:
            self.dateSimple = row[5].split("/")
            self.dateObject = datetime.date(int(self.dateSimple[2]), int(self.dateSimple[0]), int(self.dateSimple[1]))
            ##--------------------------##
            ## age start
            if row[2] != "":
                self.intAge = int(row[2])
                if self.intAge <= 10:
                    self.age["age0_10"] += 1
                elif self.intAge <= 20:
                    self.age["age11_20"] += 1
                elif self.intAge <= 30:
                    self.age["age21_30"] += 1
                elif self.intAge <= 40:
                    self.age["age31_40"] += 1
                elif self.intAge <= 50:
                    self.age["age41_50"] += 1
                elif self.intAge <= 60:
                    self.age["age51_60"] += 1
                elif self.intAge >= 61:
                    self.age["age61_up"] += 1
            else:
                self.age["Unknown"] += 1
            ## age done
            ##--------------------------##
            ## gender start
            if row[3] == "Male":
                self.gender["Male"] += 1
            elif row[3] == "Female":
                self.gender["Female"] += 1
            else:
                self.gender["Other"] += 1
            ## gender done
            ##--------------------------##
            ## race start
            if row[4] == "Asian":
                self.race["Asian"] += 1
            elif row[4] == "Hispanic":
                self.race["Hispanic"] += 1
            elif row[4] == "Black":
                self.race["Black"] += 1
            elif row[4] == "Native":
                self.race["Native"] += 1
            elif row[4] == "Other":
                self.race["Other"] += 1
            elif row[4] == "White":
                self.race["White"] += 1
            elif row[4] == "White":
                self.race["White"] += 1
            else:
                self.race["Unknown"] += 1
            ## race done
            ##--------------------------##
            ## year start
            if self.dateObject.year == 2000:
                self.dateYear["2000"] += 1
            elif self.dateObject.year == 2001:
                self.dateYear["2001"] += 1
            elif self.dateObject.year == 2002:
                self.dateYear["2002"] += 1
            elif self.dateObject.year == 2003:
                self.dateYear["2003"] += 1
            elif self.dateObject.year == 2004:
                self.dateYear["2004"] += 1
            elif self.dateObject.year == 2005:
                self.dateYear["2005"] += 1
            elif self.dateObject.year == 2006:
                self.dateYear["2006"] += 1
            elif self.dateObject.year == 2007:
                self.dateYear["2007"] += 1
            elif self.dateObject.year == 2008:
                self.dateYear["2008"] += 1
            elif self.dateObject.year == 2009:
                self.dateYear["2009"] += 1
            elif self.dateObject.year == 2010:
                self.dateYear["2010"] += 1
            elif self.dateObject.year == 2011:
                self.dateYear["2011"] += 1
            elif self.dateObject.year == 2012:
                self.dateYear["2012"] += 1
            elif self.dateObject.year == 2013:
                self.dateYear["2013"] += 1
            elif self.dateObject.year == 2014:
                self.dateYear["2014"] += 1
            elif self.dateObject.year == 2015:
                self.dateYear["2015"] += 1
            elif self.dateObject.year == 2016:
                self.dateYear["2016"] += 1
            ## year end
            ##--------------------------##
            ## season start
            if self.dateObject.month >= 3 and self.dateObject.month <= 5:
                self.dateSeason["Spring"] += 1
            elif self.dateObject.month >= 6 and self.dateObject.month <= 8:
                self.dateSeason["Summer"] += 1
            elif self.dateObject.month >= 9 and self.dateObject.month <= 11:
                self.dateSeason["Fall"] += 1
            elif self.dateObject.month >= 12 or self.dateObject.month <= 2:
                self.dateSeason["Winter"] += 1
            ## season end
            ##--------------------------##
            ## state start
            if row[7] == "AL":
                self.state["AL"] += 1
            elif row[7] == "AK":
                self.state["AK"] += 1
            elif row[7] == "AZ":
                self.state["AZ"] += 1
            elif row[7] == "AR":
                self.state["AR"] += 1
            elif row[7] == "CA":
                self.state["CA"] += 1
            elif row[7] == "CO":
                self.state["CO"] += 1
            elif row[7] == "CT":
                self.state["CT"] += 1
            elif row[7] == "DE":
                self.state["DE"] += 1
            elif row[7] == "FL":
                self.state["FL"] += 1
            elif row[7] == "GA":
                self.state["GA"] += 1
            elif row[7] == "HI":
                self.state["HI"] += 1
            elif row[7] == "ID":
                self.state["ID"] += 1
            elif row[7] == "IL":
                self.state["IL"] += 1
            elif row[7] == "IN":
                self.state["IN"] += 1
            elif row[7] == "IA":
                self.state["IA"] += 1
            elif row[7] == "KS":
                self.state["KS"] += 1
            elif row[7] == "KY":
                self.state["KY"] += 1
            elif row[7] == "LA":
                self.state["LA"] += 1
            elif row[7] == "ME":
                self.state["ME"] += 1
            elif row[7] == "MD":
                self.state["MD"] += 1
            elif row[7] == "MA":
                self.state["MA"] += 1
            elif row[7] == "MI":
                self.state["MI"] += 1
            elif row[7] == "MN":
                self.state["MN"] += 1
            elif row[7] == "MS":
                self.state["MS"] += 1
            elif row[7] == "MO":
                self.state["MO"] += 1
            elif row[7] == "MT":
                self.state["MT"] += 1
            elif row[7] == "NE":
                self.state["NE"] += 1
            elif row[7] == "NV":
                self.state["NV"] += 1
            elif row[7] == "NH":
                self.state["NH"] += 1
            elif row[7] == "NJ":
                self.state["NJ"] += 1
            elif row[7] == "NM":
                self.state["NM"] += 1
            elif row[7] == "NY":
                self.state["NY"] += 1
            elif row[7] == "NC":
                self.state["NC"] += 1
            elif row[7] == "ND":
                self.state["ND"] += 1
            elif row[7] == "OH":
                self.state["OH"] += 1
            elif row[7] == "OK":
                self.state["OK"] += 1
            elif row[7] == "OR":
                self.state["OR"] += 1
            elif row[7] == "PA":
                self.state["PA"] += 1
            elif row[7] == "RI":
                self.state["RI"] += 1
            elif row[7] == "SC":
                self.state["SC"] += 1
            elif row[7] == "SD":
                self.state["SD"] += 1
            elif row[7] == "TN":
                self.state["TN"] += 1
            elif row[7] == "TX":
                self.state["TX"] += 1
            elif row[7] == "UT":
                self.state["UT"] += 1
            elif row[7] == "VT":
                self.state["VT"] += 1
            elif row[7] == "VA":
                self.state["VA"] += 1
            elif row[7] == "WA":
                self.state["WA"] += 1
            elif row[7] == "WV":
                self.state["WV"] += 1
            elif row[7] == "WI":
                self.state["WI"] += 1
            elif row[7] == "WY":
                self.state["WY"] += 1
            elif row[7] == "DC":
                self.state["DC"] += 1
            ## state end
            ##--------------------------##
            ## start death by
            if row[8] == "Shot and Tasered":
                self.deathWeapon["Shot and Tasered"] += 1
            elif row[8] == "Shot":
                self.deathWeapon["Shot"] += 1
            elif row[8] == "Tasered":
                self.deathWeapon["Tasered"] += 1
            ## death by done
            ##--------------------------##
            ##  start armed
            if row[9] == "Gun":
                self.armed["Gun"] += 1
            elif row[9] == "Vehicle":
                self.armed["Vehicle"] += 1
            elif row[9] == "Unarmed" or row[9] == "":
                self.armed["Unarmed"] += 1
            elif row[9] == "Toy Weapon":
                self.armed["Toy Weapon"] += 1
            elif row[9] in self.explosivesList:
                self.armed["Explosives and Fire"] += 1
            elif row[9] in self.bluntObjectList:
                self.armed["Blunt Object"] += 1
            elif row[9] in self.bladesList:
                self.armed["Blades"] += 1
            ## weapon done
            ##--------------------------##
            ## mental illness start
            if row[10] == "TRUE":
                self.mentalIllness["Precondition"] += 1
            elif row[10] == "FALSE":
                self.mentalIllness["Healthy"] += 1
            ## mental illness done
            ##--------------------------##
            ## flee status start
            if row[11] == "TRUE":
                self.fleeStatus["Flee"] += 1
            elif row[11] == "FALSE":
                self.fleeStatus["Stay"] += 1
            ## flee status done
        f.close()
        print("age data is:")
        print(self.age)
        print("\n")
        print("gender data is:")
        print(self.gender)
        print("\n")
        print("race data is:")
        print(self.race)
        print("\n")
        print("year data is:")
        print(self.dateYear)
        print("\n")
        print("season data is:")
        print(self.dateSeason)
        print("\n")
        print("state data is:")
        print(self.state)
        print("\n")
        print("weapon killed by data is:")
        print(self.deathWeapon)
        print("\n")
        print("weapon armed with data is:")
        print(self.armed)
        print("\n")
        print("mental illness data is:")
        print(self.mentalIllness)
        print("\n")
        print("flee data is:")
        print(self.fleeStatus)
        print("\n")
        
justiceGUI()
tk.mainloop()

    
        
        

