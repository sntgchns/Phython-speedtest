import speedtest

test = speedtest.Speedtest()

print("Buscando servidores...")
test.get_servers()
print("Eligiendo servidor...")
best = test.get_best_server()
    
print(f"Mejor servidor: {best['host']} ubicado en {best['country']}.")

print("Analizando velocidad de descarga...")
download_result = test.download()
print("Analizando velocidad de subida...")
upload_result = test.upload()
ping_result = test.results.ping

best_server = (f"Servidor: {best['host']}. Ubicación: {best['country']}.")
download_speed = (f"Descarga: {download_result / 1024 / 1024:.2f} Mbit/s")
upload_speed = (f"Subida: {upload_result / 1024 / 1024:.2f} Mbit/s")
ping_stats = (f"Ping: {ping_result} ms")

print(f"Descarga: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Subida: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result} ms")