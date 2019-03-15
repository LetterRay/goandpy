from vibora import Vibora, Response

app = Vibora()

@app.route('/')
async def home():
    return Response(f'helloworld'.encode())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
