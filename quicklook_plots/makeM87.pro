pro makeM87,eps=eps

	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	gal= 'M875kms'				    ;;; name of your object - for output files
	file= '10kms.fits'	    ;;; path to your observed datacube

	distance=16.1					;;; Distance to your object in Mpc - for scale bars
	bardist=1000					;;; Size of the scale bars, in PARSECS
	kpc=1							;;; Flag for units in the scale bar - kpc=1 --> kiloparsecs, kpc=0 --> parsecs

	vsys=0.0					;;; Systemic velocity of your object, in km/s
	posang=90.						;;; Position angle of the major axis, in degrees

	phasecen=[121.,113.]				;;; Phase Centre of your Cube in PIXELS. The place to call 0,0
	imageSize=150					;;; How big the area you wish to image is in PIXELS around your phasecentre
	chans2do=[23,44]					;;; Which channel range contains flux from your object? [startChan, endChan]
	chanmapsize=[6,4]				;;; How many plots you want in your channel maps in the X and Y directions. Needs to be large enough to fit them all in!


	specbox=[-10,10,-10,10]			;;; How big an area to include when creating your spectrum in ARCSECONDS [xmin,xmax,ymin,ymax]
	vrange=[[-400,400]]+vsys        ;;; Velocity range to plot in your spectrum

	maxsigma=0						;;; Clip the moment two display to some maximum value, to avoid noise peaks creating range issues.
	log=0							;;; Flag for plotting the moment zero with a logarithmic scale. True = log it, False =dont
	pvdthick=2.						;;; How thick a cut to make when creating the PVD in PIXELS. Usually pick at least one beam width.

	rmsfac=1.5						;;; RMS clip to apply in the SMOOTH MASK.

	outputfits=1					;;; Output FITS files of the produced moments? True=yes, False=no
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


	makeplots,gal,file,phasecen,imageSize,chans2do,distance,rmsfac,vsys,specbox,posang,eps=eps,bardist=bardist,chanmapsize=chanmapsize,vrange=vrange,maxsigma=maxsigma,log=log,kpc=kpc,pvdthick=pvdthick,outputfits=outputfits

end
