#!/usr/bin/env python3
import requests
import sys
import argparse

def run_tests(url: str):
    print("🧪 Ejecutando tests básicos...")

    # Test 1: Verificar que responde
    print("Test 1: Conectividad básica")
    try:
        response = requests.get(url, timeout=5)
        print("✅ App responde correctamente")
    except requests.exceptions.RequestException as e:
        print(f"❌ App no responde ({e})")
        sys.exit(1)

    # Test 2: Verificar código de respuesta
    print("Test 2: Código de respuesta")
    if response.status_code == 200:
        print("✅ Código HTTP correcto (200)")
    else:
        print(f"❌ Código HTTP incorrecto: {response.status_code}")
        sys.exit(1)

    # Test 3: Verificar contenido básico
    print("Test 3: Contenido básico")
    content = response.text.lower()
    if "nginx" in content or "welcome" in content:
        print("✅ Contenido esperado encontrado")
    else:
        print("❌ Contenido no encontrado")
        sys.exit(1)

    print("🎉 Todos los tests pasaron!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script de tests básicos para aplicaciones web")
    parser.add_argument("--url", type=str, default="http://localhost:80",
                        help="URL de la aplicación a testear (default: http://localhost:80)")
    args = parser.parse_args()

    run_tests(args.url)
