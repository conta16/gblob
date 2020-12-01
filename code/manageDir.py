import os

class manageDir:
        
    def __init__(self):
        self.skymap_folder = "../skymaps/"
        self.skymaps = []
        for name in os.listdir(self.skymap_folder):
            if name.startswith("skymap"):
                self.skymaps.append(name)

    def clean(self, skymaps):
        for name in skymaps:
            os.remove(self.skymap_folder+name)
        
    def get_fits_file(self):
        i = 0
        while os.path.exists("skymap"+str(i)+".fits"):
            self.skymaps.append("skymap"+str(i)+".fits")
            i += 1
        fits = "skymap"+str(i)+".fits"
        self.skymaps.append("skymap"+str(i)+".fits")
        return fits

    def cleanCreate(self,fits):
        os.remove("events.fits")
        os.remove("selected_events.fits")
        os.rename(fits,self.skymap_folder+fits)
