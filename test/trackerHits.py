# first load the ROOT classes
# importing all is the safe way
from ROOT import *

# the CMS specific rootlogon.C part
gSystem.Load("libPhysicsToolsFWLite")
AutoLibraryLoader.enable()

# opening file and accessing branches
print "Opening SimHit file"
file = TFile("simevent.root")
events = file.Get("Events")
branch = events.GetBranch("PSimHit_r_TrackerHitsTIBLowTof.obj")
simHit = std.vector(PSimHit)()
branch.SetAddress(simHit)

histo = TH1F("nofhits", "Tof of hits", 100, -0.5, 50)

# looping over all events 
nOfEvents = events.GetEntries()
for ev in range(nOfEvents):
    branch.GetEntry(ev)
    size = simHit.size()
    for i in range(size):
        histo.Fill(simHit[i].timeOfFlight())

hFile = TFile("histo.root", "RECREATE")
histo.Write();

gROOT.SetBatch()
gROOT.SetStyle("Plain")

c = TCanvas()
histo.Draw()
c.SaveAs("tofhits.jpg")
