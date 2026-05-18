def generar_regreso(pila_movimientos):

    print("" + "="*50)
    print(" SECUENCIA DE REGRESO AL PUNTO DE PARTIDA")
    print("="*50)
 
    if pila_vacia(pila_movimientos):
        print("  El robot no realizó ningún movimiento.")
        return
    paso_regreso = 1
 
    while not pila_vacia(pila_movimientos):
  
        movimiento = desapilar(pila_movimientos)
 
        direccion_regreso = OPUESTO[movimiento["direccion"]]
        pasos             = movimiento["pasos"]
 
        print(f"  Paso {paso_regreso}: {pasos} paso(s) hacia el {direccion_regreso}")
        paso_regreso += 1
    print("El robot llegó al punto de partida.")
 
def main():

    pila = registrar_movimientos()
 
    if pila_vacia(pila):
        print("No se registraron movimientos. Fin del programa.")
        return
    print("\n" + "="*50)
    print("RESUMEN DE MOVIMIENTOS REGISTRADOS")
    print("="*50)

    for i, mov in enumerate(pila, start=1):
        print(f"  {i}. {mov['pasos']} paso(s) hacia el {mov['direccion']}")
    generar_regreso(pila)
 
 
if __name__ == "__main__":
    main()