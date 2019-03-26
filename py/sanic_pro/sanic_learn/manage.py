from main import app
import sys

# python manage.py runserver 0.0.0.0:8000
if sys.argv[1] == "runserver":
    host = "0.0.0.0"
    port = 8000
    try:
        if sys.argv[2]:
            if ":" in sys.argv[2]:
                host = sys.argv[2].split(":")[0]
                port = sys.argv[2].split(":")[1]
        else:
            host = str(sys.argv[2])
    except Exception as e:
        pass
    app.run(host=host, port=port)
