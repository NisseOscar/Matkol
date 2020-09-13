# -*- coding: utf-8 -*-
import xlrd

#-------------------------------------------
class RecipeAnalyzer:
    def __init__(self):
        data = xlrd.open_workbook('Klimatavtryck.xlsx')
        sheet = data.sheet_by_index(0)
        self.Foodprint = {}
        self.weight = {}
        for i in range(1,sheet.nrows):
            row = sheet.row_values(i)
            self.Foodprint[row[0]] = row[1]
            self.weight[row[0]] = row[2]
        sheet = data.sheet_by_index(1)
        self.ingrediantDict = {}
        for i in range(0,sheet.nrows):
            row = sheet.row_values(i)
            self.ingrediantDict[" "+row[0]] = row[1]
        list = self.Foodprint.keys()
        measur = xlrd.open_workbook('matt.xlsx')
        sheet = measur.sheet_by_index(0)
        self.measurements = {}
        for i in range(0,sheet.nrows):
            row = sheet.row_values(i)
            self.measurements[row[0]] = row[1]
    #Functions-------------------------------------------------------

    def ingrediant(self,string):
        string = string.lower()
        keys =  self.ingrediantDict.keys()
        for key in keys:
            if key in string:
                try:
                    return float(self.Foodprint[self.ingrediantDict[key]])
                except KeyError:
                    return 0.0
        return 0
    def unit(self,string):
        string = string.lower()
        keys =  self.Foodprint.keys()
        for key in keys:
            if key in string:
                return float(self.weight[key])
        return 0.0

    def quantity(self,string):
        string = string.lower()
        keys =  self.measurements.keys()
        if not len(string.split())>=2:
            return 0.0
        values = string.split(' ',2)
        try:
            quantity = float(values[0])
        except ValueError:
            return 0.0
        measure = values[1]
        if measure in keys:
            return float(quantity*self.measurements[measure])
        else:
            return float(quantity*self.unit(string))

    def calculate(self,recipe):
        sum = 0.0
        ingrediants = recipe.splitlines()
        for line in ingrediants:
            s = self.quantity(line)*self.ingrediant(line)
            #print(line)
            #print("quantity is: " +str(self.quantity(line)) +", ingrediant has value:" +str(self.ingrediant(line)))
            sum = sum + s
        return round(sum,2)
