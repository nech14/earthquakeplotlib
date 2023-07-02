# Vesninlib - library for drawing eq graphics

## Data availability:
Data of global GNSS network are available at https://simurg.space, ionosonde data availabel 
through https://giro.uml.edu. The data paper uses along with notebook (with outputs preserved) are available 
here https://cloud.iszf.irk.ru/index.php/s/3RcnGdohf38kmAO . Email artem_vesnin@iszf.irk.ru if you have any 
questions about data format or behaviour of particular piece of code.

## Preparing for using
Download conda (it is necessary to download a module via conda-forge)
```commandline
conda deactivate
conda create -n turkey_eq python=3.10
conda activate turkey_eq
conda install cartopy
```
## Installation:
```
pip install vesninlib
```

Examples:
1. Get data from data file:
```python
file_data = retrieve_data(file, type_d, times=times)
```
**file** - path to .h5 file with data  
**type_d** - description or title of your graphic  
**times** - array of datetime for getting needed data from the file

2. Draw graphic via plot_map:
```python
data = {'ROTI': retrieve_data(path, description)}
C_LIMITS ={
            'ROTI': [0,0.5*scale,'TECu/min']
        }
plot_map(times, data, 
         'ROTI', clims= C_LIMITS,
         savefig=f'{savefig}', ncols=ncols)
```
**times** - array of times for drawing it on the graphic
**data** - dictionary of data (ROTI (*description*) means description of file)
**savefig** - path to save the file. If value of 
savefig is None, function draw graphic, 
else it just saves as a file
**ncols** - number of columns in subplot
**clims, C_LIMITS** - range of colors
  
Another example:
```python
EPICENTERS = {'01:17': {'lat': 37.220, 
                        'lon': 37.019, 
                        'time': datetime(2023, 2, 6, 1, 17, 34)},
              '10:24': {'lat': 38.016, 
                        'lon': 37.206, 
                        'time': datetime(2023, 2, 6, 10, 24, 50)}
             }
plot_map(times, data, 'ROTI',
                 lat_limits=(25, 50),
                 lon_limits=(25, 50),
                 sort=True,
                 markers=[EPICENTERS['10:24']],
                 clims=C_LIMITS)
```
**EPICENTERS** - coordinates and time of earthquake epicenter  
**lat_limits, lon_limits** - coordinates to scale the graphic

## Authors
Vesnin, A., Yasyukevich, Y., Perevalova, N., 
& Şentürk, E. (2023). Ionospheric Response 
to the 6 February 2023 Turkey–Syria 
Earthquake. Remote Sensing, 15(9), 2336.
  
By [article](https://www.mdpi.com/2072-4292/15/9/2336)
