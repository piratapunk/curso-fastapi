from zoneinfo import ZoneInfo
from datetime import datetime
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola Lee!"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}/{fmt_str}")
async def time(iso_code: str, fmt_str: str = "12H"):
    fmt = "%H:%M" if fmt_str == "24H" else "%I:%M %p"
    iso = iso_code.upper()
    tz_str = country_timezones.get(iso)
    tz = ZoneInfo(tz_str)
    time = datetime.now(tz).strftime(fmt)
    return {"time": time}
