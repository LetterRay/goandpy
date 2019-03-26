from sanic.response import json,text
from sanic import Blueprint

bp = Blueprint('test_blueprint')



@bp.route("/",methods=["POST","GET"])
async def test(request):
    return json({"hello": "world"})


@bp.get('/tt')
async def bar(request):
    return text(request.endpoint)
