import subprocess

if __name__ == '__main__':
    while True:
        try:
            # subprocess.run(["/home/str/osnmaga/.venv/bin/python", "/home/str/osnmaga/start_all_bot.py"])
            subprocess.run(["/home/str/osnmaga/.venv/bin/python", r"/home/str/osnmaga/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
