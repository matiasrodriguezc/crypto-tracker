import time
import requests
from database import SessionLocal, engine
from models import Base, BitcoinPrice

Base.metadata.create_all(bind=engine)

def get_bitcoin_price():
    try:
        # API pública de CoinGecko
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"❌ Error obteniendo precio: {e}")
        return None

def save_price(price):
    session = SessionLocal()
    try:
        new_entry = BitcoinPrice(price=price)
        session.add(new_entry)
        session.commit()
        print(f"💾 Precio guardado en DB: ${price}")
    except Exception as e:
        print(f"❌ Error guardando en DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    print("👷 Worker Iniciado (Modo Real)...")
    while True:
        price = get_bitcoin_price()
        if price:
            save_price(price)
        else:
            print("⚠️ No se pudo obtener precio, reintentando...")
        
        # Esperar 1 minuto antes de la próxima búsqueda
        time.sleep(60)
