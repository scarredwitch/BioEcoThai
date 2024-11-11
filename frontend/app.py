from flask import Flask, request, jsonify, render_template
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

# Update the SPARQL endpoint URL to match your Fuseki server
SPARQL_ENDPOINT = "http://localhost:3030/ds/query"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term')
    if not term:
        return jsonify({"results": []})

    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    # Basic SPARQL query format to search across all triples
    query = f"""
    PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
    PREFIX dwciri: <http://rs.tdwg.org/dwc/iri/>
    PREFIX dsw: <http://purl.org/dsw/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX bet: <http://www.semanticweb.org/SirikitJoshi/BioEcoThai/>

    SELECT ?s ?p ?o
    WHERE {{
        ?s ?p ?o .
        FILTER (CONTAINS(LCASE(STR(?o)), LCASE("{term}")) || 
                CONTAINS(LCASE(STR(?p)), LCASE("{term}")) ||
                CONTAINS(LCASE(STR(?s)), LCASE("{term}")))
    }}
    LIMIT 10
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    # Format the results to include subject, predicate, and object
    #print (results)
    formatted_results = [
        {
            "subject": result["s"]["value"] if "s" in result else None,
            "predicate": result["p"]["value"] if "p" in result else None,
            "object": result["o"]["value"] if "o" in result else None
        }
        for result in results["results"]["bindings"]
    ]

    return jsonify({"results": formatted_results})

if __name__ == '__main__':
    app.run(debug=True)
