import wget
from tqdm import tqdm

def GetDataAEROET(station,start_date,end_date,
                  vars,temporal_type,inversion_type=None):
    '''
    station: Name of your station
    start_date: start date of type: YYYY-MM-DD
    end_date: start date of type: YYYY-MM-DD
    vars: name of vars type: AOD10 or AOD15
    temporal_type: True = Daily Mean, False = All data
    inversion_type: inv ex: ALM15 or HYB20
    '''
    if temporal_type == True: AVG = 10
    else: AVG = 20

    def PRINTEXCEPT(vars,valid_vars):
        print('#############################################################')
        print(f'{vars} is not valid variable')
        print(f'Are you sure this variable {vars} is a correct?')
        print(f'Try: {valid_vars}')

    try:
        start_date = start_date.split('-')
        end_date = end_date.split('-')
        YEAR_1,MONTH_1,DAY_1 = int(start_date[0]),int(start_date[1]),int(start_date[2])
        YEAR_2,MONTH_2,DAY_2 = int(end_date[0]),int(end_date[1]),int(end_date[2])

    except: print('Your data is not a valid time. Try YYYY-MM-DD.')
    
    inversion = ['SIZ', 'RIN',	'CAD', 'VOL', 'TAB', 'AOD',
              'SSA', 'ASY', 'FRC', 'LID', 'FLX', 'ALL',
              'PFN', 'U27']
    aod_retrieval = ['AOD10', 'AOD15', 'AOD20',
                    'SDA10', 'SDA15', 'SDA20',
                    'TOT10', 'TOT15', 'TOT20']
    zenith_radiance = ['ZEN00']

    normalize_water = ['LWN10','LWN10','LWN10']

    sky_scan_measurements = ['ALM00','HYB00','PPL00',
                             'PPP00','ALP00', 'HYP00']
    all_vars = inversion+aod_retrieval+zenith_radiance
    if vars in inversion:
        inversions_types = ['ALM15','ALM20','HYB15','HYB20']
        if inversion_type == None: 
            print(f'You need define type of inversion: \n{inversions_types}')
        else:
            try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
                'cgi-bin/print_web_data_inv_v3?'
                f'site={station}'
                f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
                f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
                f'&product={vars}&AVG={AVG}&{inversion_type}=1']
            except Exception as e: print(e)

    elif vars in aod_retrieval:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)

    elif vars in zenith_radiance:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_zenith_radiance_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)
    elif vars in normalize_water:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}&if_no_html=1']
        except Exception as e: print(e)
    elif vars in sky_scan_measurements:
        try:PATH_DOWNLOAD = ['https://aeronet.gsfc.nasa.gov/'
            'cgi-bin/print_web_data_raw_sky_v3?'
            f'site={station}'
            f'&year={YEAR_1}&month={MONTH_1}&day={DAY_1}&'
            f'year2={YEAR_2}&month2={MONTH_2}&day2={DAY_2}'
            f'&{vars}=1&AVG={AVG}']
        except Exception as e: print(e)
    
    else: PRINTEXCEPT(vars,all_vars)
        
    try:
        for _ in tqdm(PATH_DOWNLOAD,desc=f'Downloading - {station} Station'
                      ,ascii="●cC-"):
            try: wget.download(PATH_DOWNLOAD[0],out=f'{station}_{vars}.csv')
            except Exception as e: print(e)
    except: print('###################### Error in download ####################') 
