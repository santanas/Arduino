import math
import string
import ROOT
import csv
import sys
from array import *
import re

## Inputs
f = open("temperature_multi.txt", "r")
title = "temperature_plot"

## Read data
list_steps = []
list_values = []

lines = f.readlines()
#print lines
counter = -1
for line in lines:
    line = line.rstrip('\n')
    line = line.rstrip('\r')
    print line
    splittedline = line.split(' ')
    if (len(splittedline) == 2):
        counter = counter+1        
        #Set start date
        if(counter == 0):
            startDateTime = splittedline[0]
            print "Start date time: " , startDateTime
        #Fill lists
        dateTimeElements = splittedline[0].split('-')
        #print splitteddate
        #print splittedtime
        currentyear = "20" + str(dateTimeElements[0])
        datetime = ROOT.TDatime(int(currentyear),int(dateTimeElements[1]),int(dateTimeElements[2]),int(dateTimeElements[3]),int(dateTimeElements[4]),int(dateTimeElements[5]))
        timevalue = datetime.Convert()
        #list_steps.append(float(counter))
        #print timevalue
        list_steps.append(float(timevalue))
        #splittedline[2] = re.sub('[+]', '', splittedline[2])
        #splittedline[2] = re.sub('[E]', 'e', splittedline[2])
        #print line
        #print counter
        #print float(splittedline[2])
        list_values.append(float(splittedline[1]))

Ntot = counter + 1
array_steps = array('f',list_steps)
array_values = array('f',list_values)

## Book Canvas
c1 = ROOT.TCanvas("test","test",600,600)
c1.SetGridx()
c1.SetGridy()

## Graph
g_P = ROOT.TGraph(Ntot,array_steps,array_values)
g_P.SetTitle(title)
g_P.SetLineColor(2)
g_P.SetMarkerColor(1)
g_P.SetMarkerStyle(20)

g_P.GetXaxis().SetTimeDisplay(1);
#g_P.GetXaxis().SetTimeFormat("%Y-%m-%d %H:%M")
g_P.GetXaxis().SetTimeFormat("%y-%m-%d %H:%M:%S")
g_P.GetXaxis().SetTimeOffset(0,"local")
#g_P.GetXaxis().LabelsOption("v")
g_P.GetXaxis().SetLabelSize(0.015)
g_P.GetXaxis().SetNdivisions(503)
g_P.GetXaxis().SetTitle("Time")
g_P.GetXaxis().SetTitleOffset(1.2)
#g_P.GetXaxis().SetLimits(1464375600,1464591600)

g_P.GetYaxis().SetTitle("Temperature (C)")
g_P.GetYaxis().SetTitleOffset(1.3)
#print array_values[0]
#print array_values[Ntot-1]
#g_P.GetYaxis().SetRangeUser(array_values[Ntot-1]*0.1,array_values[0]*10)
g_P.GetYaxis().SetRangeUser(10,30)

## Set time on xaxis
             
## Draw graph
c1.cd()
#c1.SetLogy()

g_P.Draw("ap")
#h_data_MATBASE.GetYaxis().SetRangeUser(0,ROOT.TMath.Max(h_exp_MATBASE.GetMaximum()*1.1,h_data_MATBASE.GetMaximum()*1.1))
ROOT.gPad.Update()

## Legend
#legend_MATBASE = ROOT.TLegend(0.441275,0.493892,0.876,0.663176)
#legend_MATBASE.SetTextFont(72)
#legend_MATBASE.SetTextSize(0.03)
#legend_MATBASE.AddEntry(h_data_MATBASE,"Data MATBASE","lpe")
#legend_MATBASE.AddEntry(h_exp_MATBASE,"#splitline{Random Choice}{(Binomial, N=25, p=0.25)}","l")
#legend_MATBASE.Draw()

## Save Plots
#c1.SaveAs(title+".pdf")
c1.SaveAs(title+".root")

