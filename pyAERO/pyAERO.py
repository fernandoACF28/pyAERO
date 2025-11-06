import os
import time
import random
import requests
from tqdm import tqdm

def GetDataAEROET(station,start_date,end_date,
                  vars,temporal_type,inversion_type=None,user_name=None):
    '''
    station: Name of your station
    start_date: start date of type: YYYY-MM-DD
    end_date: start date of type: YYYY-MM-DD
    vars: name of vars type: AOD10 or AOD15
    temporal_type: True = Daily Mean, False = All data
    inversion_type: inv ex: ALM15 or HYB20
    user_name: inser your e-mail to contact
    '''
    if temporal_type == True: AVG = 10
    else: AVG = 20

    def PRINTEXCEPT(vars,valid_vars):
        print('#############################################################')
        print(f'{vars} is not valid variable')
        print(f'Are you sure this variable {vars} is a correct?')
        print(f'Try: {valid_vars}')

    def Download(path,station,user_name):
        name_file = f'{station}_{vars}.csv'

        if os.path.exists(name_file): return 
        if user_name == None:headers = {'User-Agent': f'Python Script for Aerosol Research'}
        else:headers = {'User-Agent': f'Python Script for Aerosol Research (contact {user_name})'}
        progress_bar.set_description(f'Download for station: {station}...') # (Opcional) Atualiza o texto
        time.sleep(1)
        progress_bar.update(1)
        response = requests.get(path, headers=headers)
        response.raise_for_status() 
        with open(name_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        progress_bar.set_description(f'Download in: {name_file}')
        time.sleep(1)
        progress_bar.update(1)
        return response

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

    with tqdm(total=3, desc='downloading your data') as progress_bar:
        try: response = Download(PATH_DOWNLOAD[0],station,user_name)
        except requests.exceptions.HTTPError as errh:
            print(f"Erro de HTTP: {errh}")
            if response.status_code == 429:
                print(">> (Too Many Requests). icrease the sleep time <<<")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error: {errc}")
        except Exception as e: print(f'Error! : {e}')
            
        # time for not crash for 
        delay = random.uniform(4, 8)
        progress_bar.set_description(f'Wait for {delay:.1f} seconds...')
        time.sleep(delay)
        progress_bar.update(1) 
        progress_bar.set_description('Finish Download')
