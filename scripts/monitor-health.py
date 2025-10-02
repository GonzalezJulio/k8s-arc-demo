#!/usr/bin/env python3
import subprocess
import time
import os

NAMESPACE = "dev"
LABEL = "app=mi-app"
REFRESH = 10  # segundos

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error ejecutando comando: {e}"

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def main():
    print("🏥 Monitor de salud - Presiona Ctrl+C para parar")
    try:
        while True:
            clear_screen()
            
            # Estado de pods
            print("=== ESTADO DE PODS EN DEV ===")
            pods_output = run_command(f"kubectl get pods -n {NAMESPACE} -l {LABEL} -o wide")
            print(pods_output)

            # Health checks
            print("=== HEALTH CHECKS ===")
            health_output = run_command(f"kubectl describe pods -n {NAMESPACE} -l {LABEL} | grep -A 5 'Liveness\\|Readiness'")
            if health_output.strip():
                print(health_output)
            else:
                print("No health checks configurados")

            # Últimos eventos
            print("=== ÚLTIMOS EVENTOS ===")
            events_output = run_command(f"kubectl get events -n {NAMESPACE} --sort-by='.lastTimestamp' | tail -5")
            print(events_output)

            print(f"Actualizando en {REFRESH} segundos...")
            time.sleep(REFRESH)

    except KeyboardInterrupt:
        print("\n🛑 Monitor detenido por el usuario.")

if __name__ == "__main__":
    main()
