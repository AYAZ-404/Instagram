import random

class Spoofing:
    def __init__(self):
        self.android_versions = [
            '10.0', '11.0', '12.0', '13.0', '14.0', '15.0'
        ]
        self.device_models = [
            'SM-G991B', 'SM-G996B', 'SM-G998B',  # Samsung Galaxy S21 series
            'SM-F711B', 'SM-F926B',              # Samsung Fold series
            'Pixel 6', 'Pixel 7', 'Pixel 8',      # Google Pixel
            'Xiaomi 12', 'Xiaomi 13',            # Xiaomi
            'OnePlus 9', 'OnePlus 10',            # OnePlus
            'Moto G Stylus 5G',                  # Motorola
            'Redmi Note 11', 'Redmi Note 12'     # Redmi
        ]
        self.build_versions = [
            'QP1A.190711.020', 'RP1A.200720.011', 'SP1A.210812.016',
            'TP1A.220624.014', 'UP1A.231005.007'
        ]

    def generate_random_user_agent(self):
        """Generate a random Android user agent"""
        android_version = random.choice(self.android_versions)
        device_model = random.choice(self.device_models)
        build_version = random.choice(self.build_versions)

        user_agent = (
            f"Mozilla/5.0 (Linux; Android {android_version}; {device_model}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        )
        return user_agent

    def generate_random_viewport(self):
        """Generate random viewport dimensions for mobile devices"""
        viewports = [
            {'width': 360, 'height': 800},   # Standard mobile
            {'width': 390, 'height': 844},   # iPhone 12/13 Pro
            {'width': 412, 'height': 915},   # Pixel 7
            {'width': 428, 'height': 926},   # iPhone 12/13 Pro Max
            {'width': 393, 'height': 873},   # Pixel 8 Pro
        ]
        return random.choice(viewports)

    def generate_random_timezone(self):
        """Generate a random timezone offset"""
        timezone_offsets = [-720, -600, -480, -360, -300, -240, 0, 60, 600]  
        return random.choice(timezone_offsets)

    def generate_random_locale(self):
        """Generate random locale settings (English-speaking regions only)"""
        locales = [
            'en-US',  # United States
            'en-GB',  # United Kingdom
            'en-CA',  # Canada
            'en-AU',  # Australia
            'en-NZ',  # New Zealand
            'en-IE',  # Ireland
            'en-SG'   # Singapore
        ]
        return random.choice(locales)

    def generate_random_geolocation(self):
        """Generate random geolocation coordinates for Bangladesh"""
        locations = [
            {'latitude': 23.8103, 'longitude': 90.4125, 'accuracy': 50},  # Dhaka
            {'latitude': 22.3569, 'longitude': 91.7865, 'accuracy': 50},  # Chittagong
            {'latitude': 22.8456, 'longitude': 89.5403, 'accuracy': 50},  # Khulna
            {'latitude': 24.3745, 'longitude': 88.6042, 'accuracy': 50},  # Rajshahi
            {'latitude': 24.8949, 'longitude': 91.8687, 'accuracy': 50},  # Sylhet
            {'latitude': 24.7471, 'longitude': 90.4203, 'accuracy': 50},  # Mymensingh
            {'latitude': 23.4682, 'longitude': 91.1812, 'accuracy': 50},  # Comilla
            {'latitude': 25.7431, 'longitude': 89.2752, 'accuracy': 50},  # Rangpur
            {'latitude': 23.1670, 'longitude': 89.2081, 'accuracy': 50},  # Jessore
            {'latitude': 24.8467, 'longitude': 89.3734, 'accuracy': 50},  # Bogra
            {'latitude': 23.6306, 'longitude': 90.5019, 'accuracy': 50},  # Narayanganj
            {'latitude': 21.4271, 'longitude': 92.0058, 'accuracy': 50},  # Cox's Bazar
            {'latitude': 22.7010, 'longitude': 90.3535, 'accuracy': 50},  # Barisal
            {'latitude': 23.9961, 'longitude': 90.4072, 'accuracy': 50},  # Gazipur
            {'latitude': 23.8500, 'longitude': 90.2600, 'accuracy': 50},  # Savar
            {'latitude': 25.6267, 'longitude': 88.6385, 'accuracy': 50},  # Dinajpur
            {'latitude': 24.0041, 'longitude': 89.2474, 'accuracy': 50},  # Pabna
            {'latitude': 24.2505, 'longitude': 89.9248, 'accuracy': 50},  # Tangail
            {'latitude': 24.4140, 'longitude': 89.0004, 'accuracy': 50},  # Natore
            {'latitude': 24.4533, 'longitude': 89.7042, 'accuracy': 50},  # Sirajganj
            {'latitude': 23.0180, 'longitude': 91.3976, 'accuracy': 50},  # Feni
            {'latitude': 23.9056, 'longitude': 89.1219, 'accuracy': 50},  # Kushtia
            {'latitude': 23.9634, 'longitude': 91.1118, 'accuracy': 50},  # Brahmanbaria
            {'latitude': 24.9141, 'longitude': 89.9575, 'accuracy': 50},  # Jamalpur
            {'latitude': 23.6062, 'longitude': 89.8413, 'accuracy': 50},  # Faridpur
            {'latitude': 22.8943, 'longitude': 91.1018, 'accuracy': 50},  # Noakhali
            {'latitude': 22.5802, 'longitude': 89.9701, 'accuracy': 50},  # Pirojpur
            {'latitude': 25.9189, 'longitude': 89.2081, 'accuracy': 50},  # Lalmonirhat
            {'latitude': 23.5454, 'longitude': 89.1764, 'accuracy': 50},  # Jhenaidah
            {'latitude': 22.7196, 'longitude': 89.0718, 'accuracy': 50},  # Satkhira
            {'latitude': 23.4839, 'longitude': 89.4215, 'accuracy': 50},  # Magura
            {'latitude': 23.1766, 'longitude': 89.4795, 'accuracy': 50},  # Narail
            {'latitude': 23.7719, 'longitude': 88.6653, 'accuracy': 50},  # Meherpur
            {'latitude': 23.6393, 'longitude': 88.8354, 'accuracy': 50},  # Chuadanga
            {'latitude': 22.6625, 'longitude': 89.7891, 'accuracy': 50},  # Bagerhat
            {'latitude': 23.0076, 'longitude': 89.9922, 'accuracy': 50},  # Gopalganj
            {'latitude': 23.2185, 'longitude': 90.3664, 'accuracy': 50},  # Shariatpur
            {'latitude': 23.1633, 'longitude': 90.1874, 'accuracy': 50},  # Madaripur
            {'latitude': 23.7554, 'longitude': 89.6450, 'accuracy': 50},  # Rajbari
            {'latitude': 23.8569, 'longitude': 90.0076, 'accuracy': 50},  # Manikganj
            {'latitude': 23.5471, 'longitude': 90.4357, 'accuracy': 50},  # Munshiganj
            {'latitude': 23.9298, 'longitude': 90.7180, 'accuracy': 50},  # Narsingdi
            {'latitude': 24.4447, 'longitude': 90.7788, 'accuracy': 50},  # Kishoreganj
            {'latitude': 24.8787, 'longitude': 90.7371, 'accuracy': 50},  # Netrokona
            {'latitude': 25.0116, 'longitude': 90.0150, 'accuracy': 50},  # Sherpur
            {'latitude': 24.4759, 'longitude': 91.7709, 'accuracy': 50},  # Moulvibazar
            {'latitude': 25.0747, 'longitude': 91.3995, 'accuracy': 50},  # Sunamganj
            {'latitude': 24.3725, 'longitude': 91.4150, 'accuracy': 50},  # Habiganj
            {'latitude': 22.0945, 'longitude': 90.1121, 'accuracy': 50},  # Barguna
            {'latitude': 22.6843, 'longitude': 90.6433, 'accuracy': 50},  # Bhola
            {'latitude': 22.5855, 'longitude': 90.1987, 'accuracy': 50},  # Jhalokati
            {'latitude': 22.3551, 'longitude': 90.3297, 'accuracy': 50},  # Patuakhali
            {'latitude': 22.1969, 'longitude': 92.2223, 'accuracy': 50},  # Bandarban
            {'latitude': 23.1009, 'longitude': 91.9837, 'accuracy': 50},  # Khagrachari
            {'latitude': 22.6599, 'longitude': 92.1793, 'accuracy': 50},  # Rangamati
            {'latitude': 22.9573, 'longitude': 90.8354, 'accuracy': 50},  # Lakshmipur
            {'latitude': 25.0976, 'longitude': 89.1060, 'accuracy': 50},  # Joypurhat
            {'latitude': 24.8016, 'longitude': 88.9501, 'accuracy': 50},  # Naogaon
            {'latitude': 24.5950, 'longitude': 88.2917, 'accuracy': 50},  # Nawabganj
            {'latitude': 26.3458, 'longitude': 88.5529, 'accuracy': 50},  # Panchagarh
            {'latitude': 26.0357, 'longitude': 88.4485, 'accuracy': 50},  # Thakurgaon
            {'latitude': 25.3283, 'longitude': 89.5444, 'accuracy': 50},  # Gaibandha
            {'latitude': 25.8071, 'longitude': 89.6468, 'accuracy': 50},  # Kurigram
            {'latitude': 25.9329, 'longitude': 88.8524, 'accuracy': 50},  # Nilphamari
            {'latitude': 24.0487, 'longitude': 90.9996, 'accuracy': 50},  # Bhairab
            {'latitude': 24.4079, 'longitude': 90.4190, 'accuracy': 50},  # Gafargaon
            {'latitude': 24.0735, 'longitude': 90.2281, 'accuracy': 50},  # Kaliakair
            {'latitude': 24.1950, 'longitude': 90.4680, 'accuracy': 50},  # Sreepur
            {'latitude': 23.2307, 'longitude': 90.6436, 'accuracy': 50},  # Chandpur
            {'latitude': 22.4552, 'longitude': 92.0538, 'accuracy': 50},  # Rangunia
            {'latitude': 22.5000, 'longitude': 91.9500, 'accuracy': 50},  # Raozan
            {'latitude': 22.6500, 'longitude': 91.4500, 'accuracy': 50},  # Sandwip
            {'latitude': 20.8643, 'longitude': 92.3045, 'accuracy': 50},  # Teknaf
            {'latitude': 21.3280, 'longitude': 92.1158, 'accuracy': 50},  # Ukhia
            {'latitude': 22.5000, 'longitude': 91.8167, 'accuracy': 50},  # Hathazari
            {'latitude': 22.2858, 'longitude': 92.0306, 'accuracy': 50},  # Patiya
            {'latitude': 22.0252, 'longitude': 92.0620, 'accuracy': 50},  # Lohagara
            {'latitude': 22.3667, 'longitude': 91.9000, 'accuracy': 50},  # Boalkhali
            {'latitude': 23.0167, 'longitude': 91.7500, 'accuracy': 50},  # Ramgarh
            {'latitude': 22.7500, 'longitude': 91.8000, 'accuracy': 50},  # Fatikchhari
            {'latitude': 23.4000, 'longitude': 91.0333, 'accuracy': 50},  # Barura
            {'latitude': 23.2333, 'longitude': 91.1333, 'accuracy': 50},  # Laksam
            {'latitude': 23.6333, 'longitude': 90.9667, 'accuracy': 50},  # Muradnagar
            {'latitude': 23.5500, 'longitude': 90.6667, 'accuracy': 50},  # Daudkandi
            {'latitude': 23.6333, 'longitude': 90.7167, 'accuracy': 50},  # Titash
            {'latitude': 23.3667, 'longitude': 90.7333, 'accuracy': 50},  # Matlab
            {'latitude': 23.0667, 'longitude': 90.6667, 'accuracy': 50},  # Haimchar
            {'latitude': 23.3333, 'longitude': 90.8833, 'accuracy': 50},  # Kachua
            {'latitude': 23.1500, 'longitude': 90.7833, 'accuracy': 50},  # Faridganj
            {'latitude': 23.7371, 'longitude': 90.3900, 'accuracy': 50},  # Shahbagh
            {'latitude': 23.8757, 'longitude': 90.3976, 'accuracy': 50},  # Uttara
            {'latitude': 23.8062, 'longitude': 90.3666, 'accuracy': 50},  # Mirpur
            {'latitude': 23.7937, 'longitude': 90.4150, 'accuracy': 50},  # Gulshan
            {'latitude': 23.7461, 'longitude': 90.3776, 'accuracy': 50},  # Dhanmondi
            {'latitude': 23.7317, 'longitude': 90.4136, 'accuracy': 50},  # Motijheel
            {'latitude': 23.7667, 'longitude': 90.4000, 'accuracy': 50},  # Tejgaon
            {'latitude': 23.7500, 'longitude': 90.4167, 'accuracy': 50},  # Rampura
            {'latitude': 23.7981, 'longitude': 90.4132, 'accuracy': 50},  # Banani
            {'latitude': 23.8229, 'longitude': 90.4160, 'accuracy': 50},  # Khilkhet
            {'latitude': 23.7656, 'longitude': 90.3601, 'accuracy': 50},  # Mohammadpur
            {'latitude': 23.7259, 'longitude': 90.3846, 'accuracy': 50},  # Lalbagh
            {'latitude': 23.7788, 'longitude': 90.4262, 'accuracy': 50},  # Badda
            {'latitude': 23.7000, 'longitude': 90.4333, 'accuracy': 50},  # Jatrabari
            {'latitude': 23.7000, 'longitude': 90.4833, 'accuracy': 50},  # Demra
            {'latitude': 23.6934, 'longitude': 90.3340, 'accuracy': 50},  # Keraniganj
            {'latitude': 23.9000, 'longitude': 90.4100, 'accuracy': 50},  # Tongi
            {'latitude': 23.6063, 'longitude': 90.1581, 'accuracy': 50},  # Nawabganj
            {'latitude': 23.9213, 'longitude': 90.2223, 'accuracy': 50},  # Dhamrai
            {'latitude': 23.9317, 'longitude': 90.6272, 'accuracy': 50},  # Palash
            {'latitude': 24.1667, 'longitude': 90.7500, 'accuracy': 50},  # Belabo
            {'latitude': 23.9667, 'longitude': 90.8167, 'accuracy': 50},  # Raipura
            {'latitude': 24.0000, 'longitude': 89.2667, 'accuracy': 50},  # Pabna
            {'latitude': 24.2333, 'longitude': 90.0000, 'accuracy': 50},  # Basail
            {'latitude': 24.3667, 'longitude': 89.9833, 'accuracy': 50},  # Kalihati
            {'latitude': 24.1000, 'longitude': 90.1167, 'accuracy': 50},  # Mirzapur
            {'latitude': 24.4667, 'longitude': 90.1333, 'accuracy': 50},  # Ghatail
            {'latitude': 24.6167, 'longitude': 90.0333, 'accuracy': 50},  # Madhupur
            {'latitude': 24.5833, 'longitude': 89.8833, 'accuracy': 50},  # Gopalpur
            {'latitude': 24.7500, 'longitude': 89.8333, 'accuracy': 50},  # Sarishabari
            {'latitude': 24.9667, 'longitude': 90.6667, 'accuracy': 50},  # Durgapur
            {'latitude': 24.5333, 'longitude': 90.8833, 'accuracy': 50},  # Kendua
            {'latitude': 25.1000, 'longitude': 90.9167, 'accuracy': 50},  # Kalmakanda
            {'latitude': 24.6167, 'longitude': 90.8167, 'accuracy': 50},  # Atpara
            {'latitude': 24.5333, 'longitude': 90.9167, 'accuracy': 50},  # Madan
            {'latitude': 24.6000, 'longitude': 91.0167, 'accuracy': 50},  # Mohanganj
            {'latitude': 24.8167, 'longitude': 90.5833, 'accuracy': 50},  # Purbadhala
            {'latitude': 24.7833, 'longitude': 90.4167, 'accuracy': 50},  # Shambuganj
            {'latitude': 24.5833, 'longitude': 90.4167, 'accuracy': 50},  # Trishal
            {'latitude': 24.7500, 'longitude': 90.2667, 'accuracy': 50},  # Muktagachha
            {'latitude': 24.6833, 'longitude': 90.2667, 'accuracy': 50},  # Fulbaria
            {'latitude': 24.7667, 'longitude': 90.5833, 'accuracy': 50},  # Gauripur
            {'latitude': 24.2667, 'longitude': 90.3833, 'accuracy': 50},  # Bhaluka
        ]
        return random.choice(locations)

    def get_timezone_id(self, offset_minutes):
        """Convert offset in minutes to timezone ID (English-speaking regions)"""
        timezone_map = {
            -720: 'Pacific/Midway',
            -600: 'Pacific/Honolulu',
            -480: 'America/Los_Angeles',
            -360: 'America/Denver',
            -300: 'America/Chicago',
            -240: 'America/New_York',
            0:    'Europe/London',
            60:   'Europe/Dublin',
            600:  'Australia/Sydney',
        }
        return timezone_map.get(offset_minutes, 'UTC')

    def set_mobile_metrics(self, page):
        """Set mobile device metrics using JavaScript"""
        mobile_metrics_script = """
        Object.defineProperty(navigator, 'deviceMemory', {
            get: () => %d
        });
        Object.defineProperty(navigator, 'hardwareConcurrency', {
            get: () => %d
        });
        Object.defineProperty(navigator, 'platform', {
            get: () => 'Linux armv8l'
        });
        """ % (random.choice([2, 4, 6, 8]), random.choice([4, 6, 8]))

        page.add_init_script(mobile_metrics_script)