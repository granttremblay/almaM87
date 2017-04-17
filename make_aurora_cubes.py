import re
import os

##### Change this stuff ######################
velres = 20 #Velocity resolution / channel width in km/sec
weight = 'briggs' # if you use Briggs, you need to also specify a robust factor; can also use 'natural' or 'uniform'
robust_for_briggs = 0.0 # needed if using Briggs. 0.0 max angular resoluion, 2.0 "natural" at lower res, higher sensitivity
sigmacut =3.0 # Sigma level above RMS noise / threshold for CLEAN
taper = True # Tapering decreases resolution and increases sensitivity to extended structures
primary_beam_correction = True # PBcorr? 


run_name = '20kms_cube' # This will be added to the filenames of outputs
blue_edge =-500
symmetric = True
manual_nchannels = 0
pixelcut = -1 # Threshold value for excluding pixels in final maps. -1 = include all

##############################################

threshvalue = sigmacut * 0.2 #CO(2-1) RMS is 0.2 mJy/beam at 50 km/s
thresh = str(threshvalue) + 'mJy'


nchan_symmetric = 1 + (abs(2*blue_edge) / velres) 


## Make a useful filename for the maps
make_name_unique = '_' + run_name


if symmetric == True:
    nchannels = nchan_symmetric
else: 
    nchannels = manual_nchannels

### Clean the MS

os.system('rm -rf ../calibrated/calibrated.ms.contsub.clean.CO*')

clean(vis = '../calibrated/calibrated.ms.contsub',
  imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.clean',
  field = '0',
  spw = '0,3,6,9',
  mode = 'velocity',
  outframe='lsrk',
  veltype='optical',
  start = str(blue_edge) + 'km/s',
  width = str(velres) + 'km/s',
  nchan = nchannels, 
  restfreq = '229.537GHz', 
  interactive = F,
  imsize = [250, 250],
  cell = '0.2arcsec',
  weighting =  weight,
  robust = robust_for_briggs,
  uvtaper = taper,  
  outertaper = ['0.5arcsec'], # only used if you're tapering. 
  threshold = thresh,
  niter = 1000)



### Split out the moments

immoments(imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.clean' + '.image',
  moments = [0],
  outfile = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique  + '.mom0',
  includepix = [pixelcut, 100])

immoments(imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique  + '.clean' + '.image',
  moments = [1,2],
  outfile = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.mom',
  includepix = [pixelcut, 100])


### Make FITS images including the cube and the moment maps

exportfits( imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.clean' + '.image',
  fitsimage = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.fits',
  velocity = True)

exportfits( imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.mom0',
  fitsimage = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique  + '_IntensityMap.fits')

exportfits( imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.mom' + '.weighted_coord',
  fitsimage = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '_VelocityMap.fits')

exportfits( imagename = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.mom' + '.weighted_dispersion_coord',
  fitsimage = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique  +'_VelocityDispersion.fits')

final_cube_name = str(velres) + 'kms_' + weight + '_' + str(sigmacut) + 'sigma' + make_name_unique + '.fits'

print "Made the following maps:"
print final_cube_name + " (the full data cube)"
print final_cube_name[:-5] + "_IntensityMap.fits"
print final_cube_name[:-5] + "_VelocityMap.fits"
print final_cube_name[:-5] + "_VelocityDispersion.fits"
