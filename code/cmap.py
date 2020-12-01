import gammalib
import ctools
import cscripts
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.utils.data import download_file
from matplotlib.colors import SymLogNorm


class cmap:
    
    def __init__(self,manageDir):
        self.manageDir = manageDir
    def createMap(self, xml, RA, DEC):
        RA = int(RA)
        DEC = int(DEC)
        fits = self.manageDir.get_fits_file()
        self.ctobssim(xml,RA,DEC)
        self.ctselect(RA,DEC)
        self.ctskymap(fits)
        self.manageDir.cleanCreate(fits)

    def ctobssim(self,xml,RA,DEC):
        sim = ctools.ctobssim()
        sim['inmodel'] = xml
        sim['outevents'] = 'events.fits'
        sim['caldb'] = 'prod2'
        sim['irf'] = 'South_0.5h'
        sim['ra'] = RA
        sim['dec'] = DEC
        sim['rad'] = 5.0
        sim['tmin'] = '2020-01-01T00:00:00'
        sim['tmax'] = '2020-01-01T01:00:00'
        sim['emin'] = 0.03
        sim['emax'] = 150.0
        sim.execute()
    
    def ctselect(self,RA,DEC):
        select = ctools.ctselect()
        select["inobs"]  = 'events.fits'
        select["outobs"] = 'selected_events.fits'
        select["ra"]     = RA
        select["dec"]    = DEC
        select["rad"]    = 5
        select["tmin"]   = '2020-01-01T00:00:00'
        select["tmax"]   = '2020-01-01T01:00:00'
        select["emin"]   = 0.3
        select["emax"]   = 150.0
        select.run()
        select.save()

    def ctskymap(self, fits):
        skymap = ctools.ctskymap()
        skymap['inobs']       = 'selected_events.fits'
        skymap['emin']        = 0.3
        skymap['emax']        = 150.0
        skymap['nxpix']       = 40
        skymap['nypix']       = 40
        skymap['binsz']       = 0.02
        skymap['proj']        = 'TAN'
        skymap['coordsys']    = 'CEL'
        skymap['xref']        = 87
        skymap['yref']        = 22.01
        skymap['bkgsubtract'] = 'IRF'
        skymap['caldb']       = 'prod2'
        skymap['irf']         = 'South_0.5h'
        skymap['outmap']      = fits
        skymap.run()
        skymap.save()


# Slightly smooth the map for display to suppress statistical fluctuations
#skymap.skymap().smooth('GAUSSIAN',0.02)

#from matplotlib.colors import SymLogNorm
# The SymLogNorm scale is a Log scale for both positive and negative values
# and is linear within a certain range around 0

#ax = plt.subplot()
#plt.imshow(skymap.skymap().array(),origin='lower',
#           extent=[83.63+0.02*20,83.63-0.02*20,22.01-0.02*20,22.01+0.02*20],
           # boundaries of the coord grid
#           norm=SymLogNorm(1)) # the scale will be linear within +-1 count
#ax.set_xlabel('R.A. (deg)')
#ax.set_ylabel('Dec (deg)')
#cbar = plt.colorbar()
#cbar.set_label('Counts')



#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
#hdu_list = fits.open(image_file)
#hdu_list.info()
#image_data = hdu_list[0].data

#hdu_list.close()

#file = fits.open(image_file)
#image_data = file[0].data
#image_data = fits.getdata(image_file)
#plt.imshow(image_data, cmap='gray')
#plt.colorbar()

