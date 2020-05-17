from flask import Blueprint, Response, jsonify, request

from flaskr.mutants.domain.human import Human
from flaskr.mutants.models.human import Mutant, NonMutant
from mongoengine.connection import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


# En este punto estamos haciendo decisiones de diseño de nuestra API HTTP pública.
# El ejercicio dice explícitamente que el endpoint tiene que aceptar una request
# POST con un json que tenga la llave `"dna"` en el body y el path tiene que ser `/mutant/`.
# Además, dice que el comportamiento tiene que ser:
#     1. Para los humanos que son mutantes, devolver una respuesta HTTP -no aclara
#     que sea vacía pero lo asumimos para poder tener un entregable– con status code 200 y
#     2. Para los humanos que no son mutantes, devolver una respuesta HTTP con status
#     code 403.
#
# Quizá estas no sean las mejores deciciones si queremos tener una API lo más RESTful posible
# Dado que `mutant` no es una entidad per-se pero una cualidad de la entidad `human` en nuestro
# dominio, tal vez lo más apropiado sería tener un endpoint `/humans/mutant/` que devuelva, ante
# un POST request con `"dna"` como llave en el cuerpo de la llamada, siempre status code 200
# si el `"dna"` para un humano existe –en este caso podemos asumir que si está bien formada
# la lista de strings, existe– y, en el cuerpo de la respuesta, devolver el objeto json del estilo:
#     ```
#     {
#         "is_mutant": true
#     }
#     ```
#
#     ó
#
#     ```
#     {
#         "is_mutant": false
#     }
#     ```
# según corresponda.
#
# De esa manera, podemos guardar el status code 403 para el caso de uso para el que fue creado:
# el cliente que está consultando el recurso no tiene permiso para hacerlo. Así, quizá hasta podemos
# salvar a Magneto de ser interferido por el Profesor X :).
#
# Por ahora, vamos a ir con el enfoque especificado en el ejercicio, de todas maneras tendremos la oportunidad
# de refactorizar luego, aunque será difícil si ya existen clientes usando nuestra API.


@bp.route("/mutant/", methods=["POST"])
def mutant() -> Response:
    """Expects a `"dna"` key in the body of the POST request and returns
    an empty response with status code 200 if the dna belongs to a mutant and
    403 if it doesn't.
    """
    dna = request.get_json().get("dna")

    if dna:
        if Human(dna).is_mutant():
            Mutant(dna=dna).save()
            return Response(None, status=200, mimetype="application/json")
        else:
            NonMutant(dna=dna).save()
            return Response(None, status=403, mimetype="application/json")
    return Response(None, status=400, mimetype="application/json")


# Otra vez pienso que este endpoint estaría mejor nombrado `/humans/stats/`
@bp.route("/stats/", methods=["GET"])
def stats() -> Response:
    db = get_db()

    mutant_count = db.mutant.estimated_document_count()
    human_count = mutant_count + db.non_mutant.estimated_document_count()
    mutant_ratio = mutant_count / human_count if human_count else 0.00

    return jsonify(
        {
            "count_mutant_dna": mutant_count,
            "count_human_dna": human_count,
            "ratio": round(mutant_ratio, 2),
        }
    )
